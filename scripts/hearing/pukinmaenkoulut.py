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

from datetime import date

# Main section
# ------------

title = 'Pukinmäen ja Malmin alueen koulujen oppilaaksiottoalueita tarkistetaan'

slug = 'pukinmaenkoulut'

main_image = {
    'filename': 'images/pukinmaenkoulut/main_image.jpg',
    'caption': (
        'Ehdotettu muutos Pukinmäen ja Malmin koulujen oppilaaksiottoalueisiin. '
        '(Opetusvirasto / Päivi El Mahboul)'
    )
}

lead = '''

    Opetusvirastossa valmistellaan esitystä Pukinmäen ja Malmin
    oppilaaksiottoalueiden tarkistamisesta. Samalla valmistellaan myös esitys
    1.8.2016 alkaen yhdistyvien Pukinmäen peruskoulun ja Soinisen koulun
    oppilaaksiottoalueesta.

'''

body = '''

    <p>
    Esityksen mukaan Ylä-Malmin peruskoulun oppilaaksiottoaluetta laajennetaan
    1.-9. luokkien osalta nykyisen Soinisen koulun alueelle siten, että uusi
    raja kulkee Kunnantieltä suoraan Pukinmäenkaarelle. Yhdistyvien Pukinmäen
    peruskoulun ja Soinisen koulun oppilaaksiottoalue muodostetaan Pukinmäen
    koulun oppilaaksiottoalueesta ja jäljellejäävästä osasta Soinisen koulun
    oppilaaksiottaoluetta. </p>
    <p class="lead">
    Mitä mieltä olet ehdotuksesta? Kommentoi suunnitelmaa 2.10.2015 saakka.
    </p>
    <p>
    Saatua palautetta hyödynnetään jatkosuunnittelussa ja siitä laaditaan
    yhteenveto, joka esitellään opetuslautakunnan suomenkieliselle jaostolle
    oppilaaksiottoaluetarkastelun käsittelyn yhteydessä 27.10. Varsinainen
    kuuleminen tehdään koulujen johtokuntien kautta. Johtokunnilta pyydetään
    lausunnot kouluverkon muutosehdotuksista 7.10. mennessä.
    </p>
    <p>
    Oppilaaksiottoalueiden tarkistuksista päättävät opetuslautakunnan jaostot
    opetusviraston esityksestä.
    </p>
    <p>
    Lisätietoa saa opetusviraston
    <a href="http://www.hel.fi/www/opev/palveluverkko-fi/peruskoulut/">
    palveluverkkosivuilta</a>.
    </p>
    <h4>Lisätietoja</h4>
    <p>
    aluepäällikkö Ulla-Maija Vähäsarja, puh. 09 310 71764,
    <a href="mailto:etunimi.sukunimi@hel.fi">etunimi.sukunimi@hel.fi</a>
    </p><p>
    rehtori Tomi Ojanen, Ylä-Malmin peruskoulu, puh. 09 310 82553,
    <a href="mailto:etunimi.sukunimi@hel.fi">etunimi.sukunimi@hel.fi</a>
    </p><p>
    rehtori Leena Hiillos, Pukinmäen peruskoulu ja Soinisen koulu, puh.
    09 310 80747,
    <a href="mailto:etunimi.sukunimi@hel.fi">etunimi.sukunimi@hel.fi</a>
    </p>

'''  # noqa

opens_at = date(2015, 9, 21)

closes_at = date(2015, 10, 2)

published = False

area = {
    'type': 'Polygon',
    'coordinates': [
        [
            [
                24.997200965881348,
                60.25612438328367
            ],
            [
                24.998574256896973,
                60.255655970908094
            ],
            [
                24.99801635742187,
                60.255081092014905
            ],
            [
                24.99986171722412,
                60.25446361825643
            ],
            [
                25.001320838928223,
                60.25261112710892
            ],
            [
                24.999990463256832,
                60.25233430908614
            ],
            [
                25.00041961669922,
                60.25156772388639
            ],
            [
                25.001020431518555,
                60.25143995794163
            ],
            [
                25.00462532043457,
                60.25216395837046
            ],
            [
                25.006299018859863,
                60.251099246318375
            ],
            [
                25.0068998336792,
                60.250226156602515
            ],
            [
                25.007457733154297,
                60.249970613745376
            ],
            [
                25.004324913024902,
                60.24833083296097
            ],
            [
                25.004582405090332,
                60.24824564730015
            ],
            [
                25.00192165374756,
                60.24703172755716
            ],
            [
                24.99788761138916,
                60.248778054045076
            ],
            [
                24.994883537292477,
                60.251248308089764
            ],
            [
                24.992523193359375,
                60.25178066601984
            ],
            [
                24.993810653686523,
                60.25342027406509
            ],
            [
                24.994196891784668,
                60.254165523308565
            ],
            [
                24.99612808227539,
                60.25529401130044
            ],
            [
                24.997200965881348,
                60.25612438328367
            ]
        ]
    ]
}


# Hearing
# -------

hearing = {
    'slug': slug,
    'title': title,
    'main_image': main_image,
    'lead': lead,
    'body': body,
    'opens_at': opens_at,
    'closes_at': closes_at,
    'published': published,
    'area': area,
    'alternatives': []
}
