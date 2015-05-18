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

title = 'Pikku Huopalahden pohjoisosaan uutta asumista'

slug = 'pikkuhuopalahti'

main_image = {
    'filename': 'images/pikkuhuopalahti/pipo_kerrokantasi_paakuva.jpg',
    'caption': (
        'Ideoita Pikku Huopalahden pohjoisosan suunnitteluun keskustelun '
        'pohjaksi. Kuva: Serum Arkkitehdit'
    )
}

lead = '''

    Pikku Huopalahden pohjoisosaan suunnitellaan uutta asuinaluetta noin
    kahdelle tuhannelle asukkaalle.

'''

body = '''

    <p>
    Mannerheimintien ja Vihdintien kulmauksessa sijaitsevan alueen nykyiset
    rakennukset on tarkoitus purkaa ja rakentaa tilalle asuinkerrostaloja.
    Talojen kivijalkoihin tulisi tiloja palveluille ja liiketoiminnalle.
    </p>
    <p>
    Alueella nykyisin sijaitseva oikeuslääketieteellinen ja
    hammaslääketieteellinen yliopistotoiminta on siirtymässä muualle.
    Rakennuksille ei ole löytynyt muita käyttäjiä, ja niiden muuttaminen
    asunnoiksi olisi hankalaa.
    </p>
    <p>
    Alueesta on valmistunut kaavaluonnos, josta toivotaan mielipiteitä ja
    kehittämisehdotuksia. Luonnosta työstetään eteenpäin saadun palautteen,
    lisäselvitysten ja vaikutusten arvioinnin perusteella. Tavoitteena on
    esitellä kaavaluonnos kaupunkisuunnittelulautakunnalle ensi syksynä.
    Hankkeen etenemistä voi seurata kaupungin karttapalvelussa.
    </p>
    <p>
    Kaavamuutoksen pohjaksi teetettiin kolme maankäyttösuunnitelmaa kolmella
    eri arkkitehtitoimistolla. Lisäksi tarkasteluun otettiin mukaan Urban
    Helsinki -ryhmän itsenäisesti tuottama ehdotus. Luonnos on kehitetty
    pääosin Serum Arkkitehtien ehdotuksen pohjalta. Sen kantakaupunkimaisen
    ratkaisun katsottiin muun muassa sopivan hyvin nykyisen Pikku Huopalahden
    täydentäjäksi.
    </p>
    <p class="lead">
    Kerro ajatuksesi suunnitelmaluonnoksesta 11. kesäkuuta mennessä!
    </p>
    <p>
    Mikä suunnitelmassa on hyvää ja mikä kaipaa vielä kehittämistä? Millaisia
    palveluja keskustakorttelissa olisi hyvä olla? Entä millaisia
    aktiviteetteja kaipaisit alueen puistoihin ja aukioille?
    </p>
    <h4>Tutustu suunnitelmaluonnokseen:</h4>
    <ul>
      <li><a href="static/images/pikkuhuopalahti/pipo_kerrokantasi_havainnekuva.jpg"
      target="_blank">Havainnekuva</a></li>
      <li><a href="static/images/pikkuhuopalahti/pdfs/pipo_kerrokantasi_viitesuunnitelma.pdf"
      target="_blank">Viitesuunnitelma-raportti</a></li>
      <li><a href="http://kartta.hel.fi/applications/Hanke/showplan.aspx?map=yes&ID=2013-013706"
      target="_blank">Hankkeen suunnitteluaineisto karttapalvelussa</a></li>
      <li><a href="http://helsinki.creamailer.fi/subscribe/5268fea2835dd"
      target="_blank">Tilaa uutiskirje</a></li>
    </ul>

'''  # noqa

opens_at = date(2015, 5, 19)

closes_at = date(2015, 6, 11)

published = False

area = {
    "type": "Polygon",
    "coordinates": [
        [
            [
                24.899214506149292,
                60.20793864498217
            ],
            [
                24.8990535736084,
                60.20548644874818
            ],
            [
                24.89923596382141,
                60.20335395519314
            ],
            [
                24.89901065826416,
                60.20335928659983
            ],
            [
                24.898914098739624,
                60.204276275666366
            ],
            [
                24.89801287651062,
                60.20430826319444
            ],
            [
                24.896811246871944,
                60.20464946155332
            ],
            [
                24.89677906036377,
                60.20512926574193
            ],
            [
                24.89577054977417,
                60.20512393462281
            ],
            [
                24.89574909210205,
                60.2066859154606
            ],
            [
                24.89373207092285,
                60.20679786344945
            ],
            [
                24.894504547119137,
                60.208269144369595
            ],
            [
                24.899214506149292,
                60.20793864498217
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
