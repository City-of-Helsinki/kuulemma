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

from shapely.geometry import shape

from kuulemma.extensions import db
from kuulemma.models import Alternative, Hearing, Image


def _add_hearing(hearing_data):
    print('Start adding hearing.')

    hearing = Hearing(
        slug=hearing_data['slug'],
        title=hearing_data['title'].strip(),
        lead=hearing_data['lead'].strip(),
        body=hearing_data['body'].strip(),
        opens_at=hearing_data['opens_at'],
        closes_at=hearing_data['closes_at'],
        published=hearing_data['published'],
    )

    hearing.main_image = Image(
        filename=hearing_data['main_image']['filename'],
        caption=hearing_data['main_image']['caption']
    )

    if hearing_data['area']:
        hearing.area = shape(hearing_data['area'])

    print('Main content added.')

    for index, alternative_data in enumerate(hearing_data['alternatives']):
        alternative = Alternative(
            title=alternative_data['title'].strip(),
            lead=alternative_data['lead'].strip(),
            body=alternative_data['body'].strip(),
        )

        alternative.main_image = Image(
            filename=alternative_data['main_image']['filename'],
            caption=alternative_data['main_image']['caption']
        )

        hearing.alternatives.append(alternative)
        print('Alternative {index} added.'.format(index=index + 1))

    db.session.add(hearing)
    db.session.commit()
    print('Script completed! Hearing was successfully added.')


def add_hameentie():
    from .hameentie import hearing
    _add_hearing(hearing)


def add_sturenkatu():
    from .sturenkatu import hearing
    _add_hearing(hearing)


def add_maria():
    from .maria import hearing
    _add_hearing(hearing)


def add_latokartanontie():
    from .latokartanontie import hearing
    _add_hearing(hearing)


def add_myllypuronkoulut():
    from .myllypuronkoulut import hearing
    _add_hearing(hearing)


def add_pikkuhuopalahti():
    from .pikkuhuopalahti import hearing
    _add_hearing(hearing)


def add_pakilankoulut():
    from .pakilankoulut import hearing
    _add_hearing(hearing)


def add_servicenatsodra():
    from .servicenatsodra import hearing
    _add_hearing(hearing)
