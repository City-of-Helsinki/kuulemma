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

title = 'Millainen on Hämeentien tulevaisuus?'

slug = 'hameentie'

main_image = {
    'filename': 'images/hameentie/main_image.jpg',
    'caption': (
        'Liikenne nykyisin Hämeentiellä. '
        '(Helsingin kaupungin aineistopankki / Seppo Laakso)'
    )
}

lead = '''

    Hämeentien liikenne- ja katusuunnittelu on käynnistymässä ja nyt on
    saatekeskustelun aika. Miten Hämeentielle saataisiin mahtumaan
    jalankulkijat, pyöräilijät, autot ja joukkoliikenne? Millaisia
    vaihtoehtoisia lähestymistapoja tulisi tutkia? Millaisia vaikutuksia eri
    ratkaisuilla voisi olla, hyvässä tai pahassa? Mitä kaikkia seikkoja pitäisi
    tutkia ja huomioida suunnittelun yhteydessä?

'''

body = '''

    <p>
    Hämeentie olisi luonteva osa monen pyöräilijän reittiä kantakaupungissa ja
    Kalliossa, jos olosuhteet pyöräilylle olisivat siellä paremmat. Nykyisin
    pyörällä kuuluisi ajaa bussikaistalla, mutta monet pyöräilijät kokevat sen
    turvattomaksi ja siksi osa pyöräilijöistä ajaa jalkakäytävällä tai käyttää
    pitempiä reittejä.
    </p>
    <p>
    Autoliikenteen osalta Hämeentie toimii alueellisena kokoojakatuna, jonka
    tehtävänä on välittää kaupungin osa-alueen sisäistä liikennettä sekä toimia
    yhteytenä pääkatuverkkoon. Autoliikenteen kieltäminen Hämeentiellä ohjaisi
    liikenteen sekä Sörnäisten rantatielle että Kallion alempaan katuverkkoon.
    Henkilöautoja Hämeentiellä kulkee vuorokaudessa noin 15 000–20 000 ja
    linja-autoja aamun vilkkaimpana tuntina 260.
    </p>
    <p>
    Keskustelun pohjaksi Hämeentiestä on hahmoteltu kolme vaihtoehtoista
    lähestymistapaa. Suurin ero niiden välillä on se, miten Hämeentien
    henkilöautoliikenne ratkaistaan Kurvin ja Hakaniementorin välillä.
    </p>

'''

opens_at = date.today()

closes_at = date(2014, 12, 31)

published = False

area = {
    "type": "Polygon",
    "coordinates": [
        [
            [
                24.95057344436645,
                60.179876705755504
            ],
            [
                24.94990825653076,
                60.17988737619716
            ],
            [
                24.950037002563477,
                60.180010086027174
            ],
            [
                24.955852031707764,
                60.18216543610739
            ],
            [
                24.95819091796875,
                60.18331774346105
            ],
            [
                24.960615634918213,
                60.185200825382765
            ],
            [
                24.961034059524536,
                60.1860596455832
            ],
            [
                24.961313009262085,
                60.187206482249636
            ],
            [
                24.961570501327515,
                60.18755852639934
            ],
            [
                24.962042570114136,
                60.18754785845025
            ],
            [
                24.961785078048706,
                60.187345166759265
            ],
            [
                24.96165096759796,
                60.1872198173241
            ],
            [
                24.961302280426025,
                60.18569691681033
            ],
            [
                24.96121108531952,
                60.185472876448664
            ],
            [
                24.960771203041073,
                60.18493410646315
            ],
            [
                24.958491325378418,
                60.18320038067273
            ],
            [
                24.95771884918213,
                60.18280827922447
            ],
            [
                24.956393837928772,
                60.182120089852155
            ],
            [
                24.95548188686371,
                60.18178932703751
            ],
            [
                24.952579736709595,
                60.18074900291861
            ],
            [
                24.95068609714508,
                60.180063437984174
            ],
            [
                24.950605630874634,
                60.18001275362708
            ],
            [
                24.95057344436645,
                60.179876705755504
            ]
        ]
    ]
}

# Alternative 1
# -------------

alternative_1_title = 'Vaihtoehto 1'

alternative_1_main_image = {
    'filename': 'images/hameentie/alternative_1/main_image.jpg',
    'caption': 'Vaihtoehdon 1 esimerkkikuva.'
}

alternative_1_lead = '''

    Joukkoliikenne ja autoliikenne nykytilanteen mukaan, jonka lisäksi
    pyöräliikenteen kaistat.

'''

alternative_1_body = '''

    <p>
    Hämeentie säilytetään pitkälti nykyisellään. Nykyisten kaistojen lisäksi
    lisätään pyörille kaistat. Pyöräkaistoille otetaan tilaa autoliikenteen
    kaistoista, pysäköinnistä ja jalkakäytävistä.
    </p>
    <h4>
    Jatkossa keskeisiä selvitettäviä asioita vaihtoehto 1:n osalta:
    </h4>
    <ul>
        <li>
        kadun poikkileikkauksen leveyden riittävyys
        </li>
    </ul>

'''

# Alternative 2
# -------------

alternative_2_title = 'Vaihtoehto 2'

alternative_2_main_image = {
    'filename': 'images/hameentie/alternative_2/main_image.jpg',
    'caption': 'Vaihtoehdon 2 esimerkkikuva.'
}

alternative_2_lead = '''

    Helsinginkadun ja Haapaniemenkadun välillä joukkoliikenne ja autoliikenne
    nykytilanteen mukaan, jonka lisäksi pyöräliikenteelle omat kaistat.
    Haapaniemenkadun ja Hakaniementorin välillä joukkoliikennekatu ja
    pyöräliikenteen kaistat.

'''

alternative_2_body = '''

    <p>
    Helsinginkadun ja Haapaniemenkadun välillä Hämeentie säilytetään pitkälti
    nykyisellään. Nykyisten kaistojen lisäksi lisätään pyörille kaistat.
    Pyöräkaistoille otetaan tilaa pysäköinnistä ja jalkakäytävistä.
    Haapaniemenkadun ja Hakaniementorin välillä poistetaan autokaistat ja
    lisätään pyörille kaistat. Haapaniemenkadun eteläpuolisella
    joukkoliikennekadulla taksit ovat sallittu. Huoltoliikenne ja tontille ajo
    ovat sallittuja bussikaistoilla.
    </p>

    <h4>
    Jatkossa keskeisiä selvitettäviä asioita vaihtoehto 2:n osalta:
    </h4>
    <ul>
        <li>kadun poikkileikkauksen leveyden riittävyys</li>
        <li>joukkoliikennekatuosuuden vaikutukset autoliikenteen siirtymiseen
        muuhun katuverkkoon</li>
        <li>siirtyvän liikenteen vaikutukset pääkatuverkon kapasiteettiin</li>
        <li>siirtyvän liikenteen vaikutukset meluun ja päästöihin</li>
    </ul>

'''

# Alternative 3
# -------------

alternative_3_title = 'Vaihtoehto 3'

alternative_3_main_image = {
    'filename': 'images/hameentie/alternative_3/main_image.jpg',
    'caption': 'Vaihtoehdon 3 esimerkkikuva.'
}

alternative_3_lead = '''

    Läpiajava autoliikenne estetty, tonttiliikenne bussien kanssa samoilla
    kaistoilla ja pyöräliikenteellä omat kaistat.

'''

alternative_3_body = '''

    <p>
    Hämeentien läpiajava liikenne estetään Helsinginkadun ja Hakaniementorin
    välillä. Huolto- ja tonttiliikenne ohjataan muun katuverkon kautta
    Hämeentielle. Hämeentiellä huolto- ja tonttiliikenne käyttävät bussien
    kanssa samoja kaistoja. Pyörille lisätään kaistat.
    </p>

    <h4>
    Jatkossa keskeisiä selvitettäviä asioita vaihtoehto 3:n osalta:
    </h4>
    <ul>
        <li>liikenteen siirtyminen muuhun katuverkkoon</li>
        <li>siirtyvän liikenteen vaikutukset pääkatuverkon kapasiteettiin</li>
        <li>siirtyvän liikenteen vaikutukset meluun ja päästöihin</li>
        <li>huolto-, tontti- ja bussiliikenteen yhteisten kaistojen toimivuus
        </li>
    </ul>

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
        }
    ]
}
