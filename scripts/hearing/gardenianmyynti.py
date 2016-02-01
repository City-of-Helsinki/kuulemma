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

title = 'Mihin käyttöön Gardenia tulisi myydä? - kaupunki järjestää tarjouskilpailun entisen talvipuutarhan rakennusten myynnistä'

slug = 'gardenianmyynti'

main_image = {
    'filename': 'images/gardenianmyynti/main_image.jpg',
    'caption': (
        'Viikin Gardenia talvella.'
    )
}

lead = '''

'''

body = '''

    <p>
    Helsingin kaupunki on käynnistämässä tarjouskilpailun Viikissä sijaitsevan Gardenian ja samalla tontilla sijaitsevien kahden toimistorakennuksen myymisestä. Tarjouskilpailun ensimmäisessä vaiheessa kartoitetaan rakennuksille uutta käyttöä.
    </p>
    <p>
    Viikin alueen asukkaat ja muut kuntalaiset voivat nyt kertoa mielipiteensä Gardenia-talvipuutarharakennuksen ja toimistorakennusten uudesta käyttötarkoituksesta. Helsingin kaupunki välittää mielipiteet ja ideat rakennusten ostamisesta kiinnostuneille tahoille.
    </p>
    <p class="lead">
    Millainen toiminta tai palvelu sinun mielestäsi sopisi hienoon lasirakennukseen, entiseen talvipuutarhaan ja tontilla oleviin toimistorakennuksiin?
    </p>
    <h3>Myynnin taustaa</h3>
    <p>
    Gardenia on valmistunut vuonna 2001. Lasirakenteisessa päärakennuksessa on toiminut trooppinen puutarha, viher- ja ympäristötietokeskus ja luontokoulu. Gardenian toiminta loppui marraskuussa 2015 kaupunginhallituksen päätökseen perustuen. Talvipuutarhan toimintaa ei saatu yrityksistä huolimatta taloudellisesti kannattavaksi.
    </p>
    <p>
    Myynnin taustalla on Helsingin kaupungin tavoite vähentää ylläpidettävien kiinteistöjen suurta määrää. Myynnistä päättää aikanaan kiinteistölautakunta. Gardenian rakennukset myydään vuokratontilla eli tontti säilyy Helsingin kaupungin omistuksessa.
    </p>
    <h3>Esittely- ja keskustelutilaisuus</h3>
    <p>
    Gardenian kehittämisestä järjestetään kaikille avoin keskustelutilaisuus keskiviikkona 10. helmikuuta klo 17.30
    <a href="http://palvelukartta.hel.fi/unit/9297">Gardeniassa (Koetilantie 1)</a>. Tiloihin on mahdollista tutustua ennen tilaisuuden alkua klo 16.30 alkaen. Tilaisuudessa esitellään talvipuutarhan ja toimistorakennusten myynnin periaatteet ja myyntihankkeen eteneminen. Tämän jälkeen kartoitetaan alueen asukkaiden ja muiden kiinnostuneiden ajatuksia ja toiveita Gardenian tulevaisuudesta mahdollisten ostajaehdokkaiden ja tulevien toimijoiden käyttöön. Tilaisuuteen ei tarvitse ilmoittautua.
    </p>
    <p class="lead">
    Kerro kantasi -palvelun kautta saadut mielipiteet ja ideat välitetään Gardenian ostamisesta kiinnostuneille tahoille. Palautetta voi antaa 10.2.2016 saakka. Kaupunki tekee palautteista yhteenvedon, joka julkaistaan verkossa helmikuussa.
    </p>
    <p>
    <a href="http://www.hel.fi/www/kv/fi/ajankohtaiset-hankkeet/talot-ja-tilat/gardenian_myynti">
    Lisätietoa Gardeniasta ja sen myynnistä</a>
    </p>
    <h4>Lisätietoja</h4>
    <p>Kiinteistövirasto, tilakeskus, myyntineuvottelija Heidi Autiosuo, puh. (09) 310 21014,
    <a href="mailto:etunimi.sukunimi@hel.fi">etunimi.sukunimi@hel.fi</a>
    </p>

'''  # noqa

opens_at = date(2016, 2, 1)

closes_at = date(2016, 2, 10)

published = True

area = {
    "type": "Polygon",
    "coordinates": [
          [
            [
              25.014919638633728,
              60.22299963743908
            ],
            [
              25.017237067222595,
              60.22409989526214
            ],
            [
              25.016695261001587,
              60.22457142302495
            ],
            [
              25.01639485359192,
              60.22460072678635
            ],
            [
              25.01510202884674,
              60.22433166399313
            ],
            [
              25.01478552818298,
              60.22429436798613
            ],
            [
              25.01440465450287,
              60.22427039195923
            ],
            [
              25.013819932937622,
              60.224262399946355
            ],
            [
              25.013980865478516,
              60.223553767060096
            ],
            [
              25.014919638633728,
              60.22299963743908
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
