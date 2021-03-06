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
from kuulemma.models import Alternative, Hearing, Image, Section, Question


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

    if 'alternatives' in hearing_data:
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

    if 'sections' in hearing_data:
        for index, section_data in enumerate(hearing_data['sections']):
            section = Section(
                title=section_data['title'].strip(),
                lead=section_data['lead'].strip(),
                body=section_data['body'].strip(),
            )

            section.main_image = Image(
                filename=section_data['main_image']['filename'],
                caption=section_data['main_image']['caption']
            )

            hearing.sections.append(section)
            print('Section {index} added.'.format(index=index + 1))

    if 'questions' in hearing_data:
        for index, question_data in enumerate(hearing_data['questions']):
            question = Question(
                title=question_data['title'].strip(),
                lead=question_data['lead'].strip(),
                body=question_data['body'].strip(),
            )

            question.main_image = Image(
                filename=question_data['main_image']['filename'],
                caption=question_data['main_image']['caption']
            )

            hearing.questions.append(question)
            print('Question {index} added.'.format(index=index + 1))


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


def add_kalasatamankoulu():
    from .kalasatamankoulu import hearing
    _add_hearing(hearing)


def add_vesalankoulut():
    from .vesalankoulut import hearing
    _add_hearing(hearing)


def add_ylamalminkoulut():
    from .ylamalminkoulut import hearing
    _add_hearing(hearing)


def add_kannelmaenkoulut():
    from .kannelmaenkoulut import hearing
    _add_hearing(hearing)


def add_pukinmaenkoulut():
    from .pukinmaenkoulut import hearing
    _add_hearing(hearing)


def add_lauttasaarenkoulut():
    from .lauttasaarenkoulut import hearing
    _add_hearing(hearing)
