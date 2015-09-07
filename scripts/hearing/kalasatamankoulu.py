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

title = 'Uusi peruskoulu Kalasatamaan'

slug = 'kalasatamankoulu'

main_image = {
    'filename': 'images/kalasatamankoulu/main_image.jpg',
    'caption': (
        'Kalasataman koulut ja päiväkodit. '
        '(Opetusvirasto / Päivi El Mahboul)'
    )
}

lead = '''

    Kalasataman alueelle rakennetaan uusi peruskoulu. Se aloittaa toimintansa
    elokuussa 2016. Aluksi koulussa on peruskoulun ensimmäisten vuosiluokkien
    oppilaita sekä erityisoppilaita.

'''

body = '''

    <p>
    Koulurakennus valmistuu vaiheittain niin, että vuonna 2020 rakennuksessa
    toimii yli 700 oppilaan koulu. Koulun opetustarjonnasta ja siitä, mikä on
    koulun oppilaaksiottoalue, päätetään tämän syksyn aikana.
    </p>
    <p>
    Suunnitelmien mukaan Brahenpuiston koulu siirtyy samaan rakennukseen
    vaiheittain. Koulua esitetään yhdistettäväksi Kalasataman uuteen
    peruskouluun. Brahenpuiston koulussa on noin 90 oppilasta. Koulu on
    erityiskoulu oppilaille, joilla on kielellisiä erityisvaikeuksia. Koulu
    toimii nyt samassa rakennuksessa Aleksis Kiven koulun kanssa. Oppilaat
    kouluun tulevat koko kaupungin alueelta.
    </p>
    <p>
    Uudessa koulussa tulee myös toimimaan päiväkoti. Koulurakennukseen tulee
    esiopetuksen tiloja. Koulu ja päiväkoti tulevat toimimaan kiinteässä
    yhteistyössä.
    </p>
    <p>
    Kalasatamaan rakennetaan uudenlainen peruskoulu, jossa kaikkia koulun
    tiloja voi käyttää oppimiseen. Kouluympäristö tukee yhdessä oppimista ja
    tiedon jakamista. Digitalisaatio on luonteva osa koulun toimintaa.
    </p>
    <p class="lead">
    Millaisen koulun haluaisit Kalasatamaan? Mikä on tärkeää koulun fyysisessä
    ympäristössä? Millaisena näet vanhempien roolin uuden koulun toiminnassa?
    Miten koulu voisi parhaiten toimia Kalasataman alueen asukkaiden eduksi?
    Palautetta voi antaa 17.9.2015 saakka.
    </p>
    <p>
    Saatua palautetta hyödynnetään jatkosuunnittelussa. Opetusvirasto
    järjestää Kalasataman uudesta koulusta <strong>kaikille avoimen
    asukastilaisuuden torstaina, 17. syyskuuta kello 18.00-19.30
    opetusviraston juhlasalissa, os. Kaikukatu 2, 6. kerros.</strong>
    Tilaisuudessa on paikalla opetusviraston, kiinteistöviraston
    tilakeskuksen, varhaiskasvatusviraston ja kaupunkisuunnitteluviraston
    edustajia. Paikalla on myös kaupungin liikennesuunnittelija.
    </p>
    <p>
    Asukastilaisuuden jälkeen <strong>18.-25.9.2015</strong> asukkailta
    kerätään lisää palautetta.
    </p>
    <h4>Lisätietoja</h4>
    <p>
    aluepäällikkö Kirsi Myllymäki, puh. 09 310 83012,
    <a href="mailto:etunimi.sukunimi@hel.fi"</a>
    </p><p>
    opetuspäällikkö Marjo Kyllönen, puh. 09 310 86208,
    <a href="mailto:etunimi.sukunimi@hel.fi"</a>
    </p><p>
    tilapalvelupäällikkö Mauno Kemppi, puh. 09 310 86860,
    <a href="mailto:etunimi.sukunimi@hel.fi"</a>
    </p>

'''  # noqa

opens_at = date(2015, 9, 7)

closes_at = date(2015, 9, 17)

published = False

area = {
    'type': 'Polygon',
    'coordinates': [
        [
            [
                24.96166706085205,
                60.1820427343311
            ],
            [
                24.963769912719727,
                60.1812745040928
            ],
            [
                24.966344833374023,
                60.17648332944924
            ],
            [
                24.976730346679688,
                60.175245406790246
            ],
            [
                24.978017807006836,
                60.178468177021195
            ],
            [
                24.98707294464111,
                60.18604364292773
            ],
            [
                24.972481727600098,
                60.187899898939335
            ],
            [
                24.97162342071533,
                60.187835891858484
            ],
            [
                24.97042179107666,
                60.187771884652825
            ],
            [
                24.96956348419189,
                60.18747318270969
            ],
            [
                24.966301918029785,
                60.18495544405647
            ],
            [
                24.96166706085205,
                60.1820427343311
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
