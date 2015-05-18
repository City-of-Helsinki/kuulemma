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

title = 'Pakilan ja Torpparinmäen alueen koulujen oppilaaksiottoalueet'

slug = 'pakilankoulut'

main_image = {
    'filename': 'images/pakilankoulut/main_image.jpg',
    'caption': (
        'Tarkastelussa on mukana kolme koulua, Torpparinmäen peruskoulu, '
        'Pakilan yläasteen koulu ja Paloheinän ala-asteen koulu. Tarkoitus on '
        'siirtää osaa Torpparinmäen peruskoulun oppilaaksiottoaluetta '
        'etelämmäksi.'
    )
}

lead = '''

    Pakilan ja Torpparinmäen alueen koulujen koulujen oppilaaksiottoalueita
    tarkistetaan. Paloheinän ala-asteen koulussa on tilanahtautta kun taas
    Torpparinmäen peruskoulussa on tilaa.

'''

body = '''

    <p>
    Koulujen oppilaaksiottoalueita tarkistetaan aika ajoin sen mukaan, miten
    väestömäärä eri alueilla kehittyy ja millaisia tiloja on käytettävissä.
    Tavoitteena on löytää mahdollisimman toimiva ratkaisu koulupalveluihin ja
    tilankäyttöön. </p>
    <p>
    Opetusvirasto valmistelee Pakilan ja Torpparinmäen alueen koulujen
    oppilaaksiottoalueiden tarkistamista kahden eri vaihtoehdon pohjalta.
    </p>
    <p>
    Vaihtoehto 1: Torpparinmäen peruskoulun oppilaaksiottoaluetta laajennetaan
    Paloheinän ala-asteen ja Pakilan yläasteen koulujen oppilaaksiottoalueelle.
    Uusi raja kulkee Kuusimiehentieltä Sysimiehentietä ja kääntyy
    Sysimiehenkujan jälkeen kävelytietä pitkin kohti Tuusulantietä.
    </p>
    <p>
    Vaihtoehto 2: Torpparinmäen peruskoulun oppilaaksiottoaluetta laajennetaan
    Paloheinän ala-asteen ja Pakilan yläasteen koulujen oppilaaksiottoalueelle.
    Uusi raja kulkee Kuusimiehentieltä Sysimiehentietä Raiviontielle ja siitä
    kohti Tuusulantietä.
    </p>
    <p class="lead">
    Mitä mieltä olet vaihtoehdoista? Kommentoi suunnitelmia 26.5.2015 saakka.
    </p>
    <p>
    Saatua palautetta hyödynnetään jatkosuunnittelussa ja siitä laaditaan
    yhteenveto, joka esitellään opetuslautakunnan suomenkieliselle jaostolle
    oppilaaksiottoaluetarkastelun käsittelyn yhteydessä kesäkuussa. Varsinainen
    kuuleminen tehdään koulujen johtokuntien kautta. Johtokunnilta pyydetään
    lausunnot kouluverkon muutosehdotuksista 26. toukokuuta mennessä.
    </p>
    <p>
    Oppilaaksiottoalueiden tarkistuksista päättävät opetuslautakunnan jaostot
    opetusviraston esityksestä.
    </p>
    <p>
    Lisätietoa saa opetusviraston
    <a href="http://www.hel.fi/www/opev/fi/palveluverkko/pol-palveluverkko/"
    target="_blank">verkkosivuilta</a>.
    </p>

'''  # noqa

opens_at = date(2015, 5, 19)

closes_at = date(2015, 5, 26)

published = False

area = {
    'type': 'Polygon',
    'coordinates': [
        [
            [
                24.951109886169434,
                60.25548563747356
            ],
            [
                24.948191642761227,
                60.25599663511859
            ],
            [
                24.94716167449951,
                60.25608180061736
            ],
            [
                24.943256378173825,
                60.2572102225611
            ],
            [
                24.941024780273438,
                60.25714635065936
            ],
            [
                24.93746280670166,
                60.25627342217957
            ],
            [
                24.938621520996094,
                60.25388871842684
            ],
            [
                24.939866065979004,
                60.25303699642047
            ],
            [
                24.94123935699463,
                60.25248336523535
            ],
            [
                24.94166851043701,
                60.25197231275598
            ],
            [
                24.941411018371582,
                60.250886299753624
            ],
            [
                24.941883087158203,
                60.24973636437459
            ],
            [
                24.947633743286133,
                60.25035392728328
            ],
            [
                24.948577880859375,
                60.253249928999125
            ],
            [
                24.951109886169434,
                60.25548563747356
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
