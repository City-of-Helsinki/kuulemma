# -*- coding: utf-8 -*-
# Kuulemma
# Copyright (C) 2014, Fast Monkeys Oy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import csv
import io

import xlsxwriter
from flask import (
    abort,
    Blueprint,
    make_response,
    redirect,
    render_template,
    url_for
)
from flask.ext.login import current_user

from ..models import Hearing

hearing = Blueprint(
    name='hearing',
    import_name=__name__,
    url_prefix=''
)


# Redirects to the first hearing before the real index page is implemented.
@hearing.route('/kuulemiset')
def index():
    hearing = (
        Hearing.query
        .filter(Hearing.published)
        .first()
    )
    if not hearing:
        return redirect(url_for('frontpage.index'))

    return redirect(url_for('hearing.show', slug=hearing.slug))


@hearing.route('/<slug>')
def show(slug):
    hearing = (
        Hearing.query
        .filter(Hearing.slug == slug)
        .first()
    )

    if not hearing:
        return abort(404)

    if not (
        hearing.published or
        current_user.is_authenticated() and
        (current_user.is_official or current_user.is_admin)
    ):
        return abort(404)

    commentable_sections_string = hearing.get_commentable_sections_string()

    return render_template(
        'hearing/show.html',
        hearing=hearing,
        commentable_sections_string=commentable_sections_string,
        hearing_page_active=True
    )


@hearing.route('/<slug>/raportti.csv')
def report_as_csv(slug):
    hearing = (
        Hearing.query
        .filter(Hearing.slug == slug)
        .first()
    )

    if not (hearing and hearing.published):
        return abort(404)

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)

    writer.writerow(hearing.report_headers)
    for comment in hearing.comments_for_report:
        writer.writerow(comment.csv_value_array)

    csv_as_string = output.getvalue()
    response = make_response(csv_as_string)
    response.mimetype = 'text/csv'
    response.headers['Content-Disposition'] = (
        'attachment; filename={filename}.csv'.format(
            filename=hearing.report_filename
        )
    )
    return response


@hearing.route('/<slug>/raportti.xlsx')
def report_as_xlsx(slug):
    hearing = (
        Hearing.query
        .filter(Hearing.slug == slug)
        .first()
    )

    if not (hearing and hearing.published):
        return abort(404)

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    # Cell formatting.
    bolded = workbook.add_format({'bold': True})
    worksheet.set_column('A:A', 30)
    worksheet.set_column('B:D', 20)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 80)

    worksheet.write_row(0, 0, hearing.report_headers, bolded)
    for index, comment in enumerate(hearing.comments_for_report, start=1):
        worksheet.write_row(index, 0, comment.csv_value_array)

    workbook.close()

    xlsx_data = output.getvalue()
    response = make_response(xlsx_data)
    response.mimetype = (
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response.headers['Content-Disposition'] = (
        'attachment; filename={filename}.xlsx'.format(
            filename=hearing.report_filename
        )
    )
    return response
