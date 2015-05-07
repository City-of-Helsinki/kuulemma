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

title = 'Myllypuron alueen kouluverkko'

slug = 'myllypuronkoulut'

main_image = {
    'filename': 'images/myllypuronkoulut/main_image.jpg',
    'caption': (
        'Myllypuron alueella on kaksi koulua, Myllypuron yläasteen koulu ja '
        'Myllypuron ala-asteen koulu Neulapadonrinteessä. Ala-asteen koululla '
        'on sivutoimipiste Neulapadontiellä.'
    )
}

lead = '''

    Myllypuron alueella tarkastellaan kouluverkkoa. Suunnitelmissa on, että
    Myllypuron ala-asteen ja yläasteen koulut voisi yhdistää yhtenäiseksi
    peruskouluksi.

'''

body = '''

    <p>
    Opetusviraston palveluverkkoa tarkastellaan säännöllisesti sen mukaan,
    miten väestömäärä eri alueilla kehittyy ja millaisia tiloja on
    käytettävissä. Palveluverkon tarkastelussa tavoitteena on yhtenäinen
    koulupolku lapselle omalla lähialueellaan. Yhtenäisten peruskoulujen määrää
    pyritään lisäämään. Palveluverkon kehittämistä linjaavat
    kaupunginhallituksen päättämät
    <a href="http://www.hel.fi/static/public/hela/Kaupunginhallitus/Suomi/Paatos/2015/Kanslia_2015-03-30_Khs_13_Pk/5A9C0AEB-D2FD-4026-B3E4-DC167594207A/Opetustoimen_palveluverkon_kehittamisen_tavoitteet.html" target="_blank">tavoitteet</a>.
    </p>
    <p>
    Opetuslautakunnan suomenkielinen jaosto päätti kokouksessaan 25.2.2014,
    että Myllypuro on yksi niistä alueista, joilla kouluverkkoa tarkastellaan.
    Alueella on kaksi koulua, Myllypuron ala-asteen koulu (luokat 1.-6.) ja
    Myllypuron yläasteen koulu (luokat 7.-9.). Koulut ovat vierekkäisillä
    tonteilla.
    </p>
    <p>
    Tavoitteena on löytää toimiva, koko aluetta palveleva tilaratkaisu
    Myllypuron alueen koulupalveluihin ja rakentaa yhtenäistä koulupolkua.
    Lapsimäärä alueella kasvaa, ja koulutilaa tarvitaan lisää.
    </p>
    <p>
    Kaupungin suunnitelmissa on, että Myllypuron yläasteen rakennusta
    laajennetaan vuosina 2018-2019 niin, että sinne tulee myös luokat 1.- 6.
    ja koulusta muodostuu yhtenäinen peruskoulu.
    </p>
    <p class="lead">
    Mitä mieltä olet kouluverkon kehittämisestä Myllypuron alueella? Voisiko
    Myllypuron ala-asteen koulun ja yläasteen koulun yhdistää yhtenäiseksi
    peruskouluksi? Mikä olisi vaihtoehtoinen ratkaisu? Kommentoi suunnitelmia
    2.6.2015 saakka.
    </p>
    <p>
    Saatua palautetta hyödynnetään jatkosuunnittelussa ja siitä laaditaan
    yhteenveto, joka esitellään opetuslautakunnan suomenkieliselle jaostolle
    kouluverkkotarkastelun käsittelyn yhteydessä kesäkuussa. Varsinainen
    kuuleminen tehdään koulujen johtokuntien ja oppilaskuntien kautta.
    Johtokunnilta pyydetään toukokuussa lausunnot kouluverkon
    muutosehdotuksista.
    </p>
    <p>
    Koulujen yhdistymisistä päättää kaupunginvaltuusto kaupunginhallituksen
    esittelystä.
    </p>
    <p>
    Lisätietoa saa opetusviraston
    <a href="http://www.hel.fi/www/opev/fi/palveluverkko/pol-palveluverkko/"
    target="_blank">verkkosivuilta</a>.
    </p>

'''  # noqa

opens_at = date(2015, 5, 13)

closes_at = date(2015, 6, 2)

published = False

area = {
    'type': 'Polygon',
    'coordinates': [
        [
            [
                25.060372352600098,
                60.22302095029002
            ],
            [
                25.06084442138672,
                60.21994109967191
            ],
            [
                25.07157325744629,
                60.22012227536435
            ],
            [
                25.07082223892212,
                60.22378820369548
            ],
            [
                25.060372352600098,
                60.223425891825066
            ],
            [
                25.060372352600098,
                60.22302095029002
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
