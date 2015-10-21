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

title = 'Kulosaaren ostari uudistuu'

slug = 'kulosaarenostari'

main_image = {
    'filename': 'images/kulosaarenostari/main_image.jpg',
    'caption': (
        'Miten Kulosaaren ostoskeskusta pitäisi uudistaa?'
    )
}

lead = '''


'''

body = '''
    <p>
    Kulosaaren ostoskeskus on rakennettu vuonna 1960 yhtiön omalle tontille. Se on tärkeä osa Kulosaarta ja tarjoaa asukkaille päivittäiset palvelut. Palvelut on tarkoitus turvata edelleenkin.
    </p>
    <p>
    Ostoskeskusyhtiö haluaa uudistaa ostoskeskusta. Osa tiloista on tyhjillään ja sopii huonosti nykypäivän liiketoimintaan ja huoltoon. Suhteessa vuokratuottoon on rakennuksen ylläpito kallista. Toisaalta ostoskeskus on arvioitu arkkitehtonisesti merkittäväksi, korkeimpaan luokkaan Helsingin kaupunginmuseon raportissa 2004.
    </p>
    <p>
    Alkuvaiheessa olevan suunnittelun ja asemakaavatyön pohjaksi keskustellaan juuri nyt siitä, purettaisiinko nykyinen ostoskeskus kokonaan, osittain vai tulisiko sen säilyä nykyisellään. Keskustelun pohjaksi on hahmoteltu kolme vaihtoehtoa:
    </p>
    <ol type="A">
    <li>Ostoskeskus säilyy nykyisellään</li>
    <li>Korjataan Svinhufvudintien puoleinen osa ja rakennetaan takaosan tilalle asuinrakennus</li>
    <li>Puretaan koko ostari ja rakennetaan uusi asuin- ja liikekortteli</li>
    </ol>
    <p>
    Suunnittelusta ja vaihtoehdoista voi antaa palautetta 16. marraskuuta saakka. Saatua palautetta hyödynnetään jatkosuunnittelussa ja siitä laaditaan yhteenveto, joka esitellään kaupunkisuunnittelulautakunnalle suunnitelman käsittelyn yhteydessä.
    </p>
    <p>
    Palautetta toivotaan muun muassa seuraaviin kysymyksiin:
    </p>
    <ul>
    <li>Mikä perusvaihtoehto palvelisi parhaiten kulosaarelaisia pitkälläkin tähtäimellä?</li>
    <li>Mitä hyvää tai huonoa, mahdollisuuksia tai riskejä kussakin vaihtoehdossa on?</li>
    </ul>

    <h4>Lisätietoja</h4>
    <ul>
    <li><a href="http://www.hel.fi/hel2/ksv/liitteet/2015_kaava/0785_18_havainnemateriaali.pdf">
    Lue lisää ja katso lisäkuvia vaihtoehdoista</a></li>
    <li><a href="http://kartta.hel.fi/Applications/hanke/showplan.aspx?sour=haku&id=2015-008157&map=yes">
    Hankkeen suunnitteluaineistot</a></li>
    <li><a href="http://www.facebook.com/events/1499917820300740">
    Esittely- ja keskustelutilaisuus 2.11. klo 17.30 Kulosaaren ala-asteella. Tervetuloa!</a></li>
    </ul>

'''  # noqa

opens_at = date(2015, 10, 26)

closes_at = date(2015, 11, 16)

published = False

area = {
    'type': 'Polygon',
    'coordinates': [
        [
            [
                25.006454586982727,
                60.18605431136558
            ],
            [
                25.006577968597412,
                60.18595029394863
            ],
            [
                25.00691056251526,
                60.186006303367925
            ],
            [
                25.00713050365448,
                60.186016971817914
            ],
            [
                25.00989854335785,
                60.186030307375546
            ],
            [
                25.00990927219391,
                60.186190333644355
            ],
            [
                25.007382631301876,
                60.18703312578877
            ],
            [
                25.006717443466187,
                60.18619300074222
            ],
            [
                25.00660479068756,
                60.18609965218779
            ],
            [
                25.006470680236816,
                60.18606764690802
            ]
        ]
    ]
}

# Alternative 1
# -------------

alternative_1_title = 'Vaihtoehto 1'

alternative_1_main_image = {
    'filename': 'images/kulosaarenostari/alternative_1/main_image.jpg',
    'caption': 'Vaihtoehto A säilyttää ostoskeskuksen nykyisellään.'
}

alternative_1_lead = '''

    Ostoskeskus säilyy nykyisellään

'''

alternative_1_body = '''

<p>
Tässä vaihtoehdossa nykyinen ostoskeskus säilyy. Tontilla ei ole tilaa lisärakentamiselle. On epävarmaa, pystyykö ostoskeskusyhtiö tekemään tarvittavan peruskorjauksen ja pitämään liikehuoneistot vuokrattuina. Toisaalta rakennushistorialliset ja arkkitehtoniset arvot säilyvät.
</p>

'''

# Alternative 2
# -------------

alternative_2_title = 'Vaihtoehto 2'

alternative_2_main_image = {
    'filename': 'images/kulosaarenostari/alternative_2/main_image.jpg',
    'caption': 'Vaihtoehto B:ssä osa ostarista säilytetään ja osa korvataan uudella rakennuksella.'
}

alternative_2_lead = '''

    Korjattu Svinhufvudintien puoleinen osa ja uusi asuinrakennus

'''

alternative_2_body = '''

<p>
Tässä vaihtoehdossa Svinhufvudintien puoleinen osa ostoskeskuksesta säilyy ja peruskorjataan. Tärkeä osa ostarin historiallisia ja arkkitehtonisia arvoja säilyy. Tämän arvokkaimman osan suojelemista asemakaavalla selvitetään. Ostoskeskuksen itäinen osa puretaan ja tilalle rakennetaan uudisrakennus, jolla katetaan toisen puolen peruskorjauksen kustannukset. Valtaosa korkeammasta uudisrakennuksesta olisi asumista. Päivittäistavarakauppa voisi jatkaa uusissa tiloissa uudisrakennuksen maantasokerroksessa tai säilytettävän ostoskeskuksen tiloissa. Liiketilaa on lähes saman verran kuin nykyisellä ostarilla. Ostarin nykyistä kellaria laajennetaan ja autopaikat sijoitetaan sinne.
</p>

'''

# Alternative 3
# -------------

alternative_3_title = 'Vaihtoehto 3'

alternative_3_main_image = {
    'filename': 'images/kulosaarenostari/alternative_3/main_image.jpg',
    'caption': 'Vaihtoehto C:ssä ostoskeskus puretaan ja tilalle rakennetaan uusi asuin- ja liikekortteli.'
}

alternative_3_lead = '''

    Uusi asuin- ja liikekortteli

'''

alternative_3_body = '''

<p>
Tässä vaihtoehdossa koko nykyinen ostoskeskus puretaan ja tilalle tulee uudiskortteli. Korttelia on alustavasti tutkittu samalla määrällä uudisrakentamista kuin vaihtoehdossa B. Kadunvarren kivijalassa on liiketilaa ja pihakannen päällä ylemmissä kerroksissa asumista. Liiketilan määrää tutkitaan vielä. Autopaikat järjestetään pihakannen alle. Uudiskorttelin suunnittelu voidaan ratkaista usealla eri tavalla, mutta rakennusten korkeus voisi jäädä matalammaksi kuin vaihtoehdossa B.
</p>

'''

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
    'alternatives': [
        {
            'title': alternative_1_title,
            'main_image': alternative_1_main_image,
            'lead': alternative_1_lead,
            'body': alternative_1_body,
        },
        {
            'title': alternative_2_title,
            'main_image': alternative_2_main_image,
            'lead': alternative_2_lead,
            'body': alternative_2_body,
        },
        {
            'title': alternative_3_title,
            'main_image': alternative_3_main_image,
            'lead': alternative_3_lead,
            'body': alternative_3_body,
        },
    ]
}
