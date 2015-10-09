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

title = 'Vuosaaren alueella tarkastellaan kouluverkkoa'

slug = 'vuosaarenkoulut'

main_image = {
    'filename': 'images/vuosaarenkoulut/main_image.jpg',
    'caption': (
        'Vuosaaren kouluverkko lukuvuonna 2015-2016. (Opetusvirasto/Päivi El Mahboul)'
    )
}

lead = ''

body = '''
<p>
Vuosaaressa tarkastellaan syksyn aikana kouluverkkoa. Koulujen määrää ja tilojen
tarvetta selvitetään. Tarkastelu perustuu opetuslautakunnan päätökseen ja
kaupunginhallituksen <a href="http://www.hel.fi/static/public/hela/Kaupunginhallitus/Suomi/Paatos/2015/Kanslia_2015-03-30_Khs_13_Pk/5A9C0AEB-D2FD-4026-B3E4-DC167594207A/Opetustoimen_palveluverkon_kehittamisen_tavoitteet.html">
palveluverkkolinjauksiin.</a>
</p>
<p>
Elokuussa 2016 peruskouluissa otetaan käyttöön uudet opetussuunnitelmat. Niissä
korostuu uudenlainen tapa oppia ja opettaa. Koulujen tiloja käytetään joustavammin
ja monipuolisemmin. Uusien opetussuunnitelmien myötä opetettavien aineiden määrät
ja valinnaisuudet muuttuvat, mikä vaikuttaa koulujen toimintaan.
Kouluverkkotarkastelulla ennakoidaan tulevia muutoksia. Kaikilla alueilla pyritään
tarjoamaan laadukkaat ja monipuoliset opetuspalvelut.
</p>
<p>
Vuosaaressa on yksi laajennettu oppilaaksiottoalue, johon kuuluu kahdeksan
peruskoulua (3 yhtenäistä peruskoulua, 4 ala-asteen koulua ja 1 yläasteen koulu).
Koulujen koot vaihtelevat. Heteniityn ala-asteen koulu on pienin ja Aurinkolahden
peruskoulu suurin. Maahanmuuttajataustaiset oppilaat jakautuvat epätasaisesti alueen
kouluihin. Tehtaanpuiston yläasteen koulu ja Vuosaaren lukio toimivat samassa
rakennuksessa, joka kaipaa peruskorjausta.
</p>
<p>
 Vuosaareen rakennetaan uusia asuntoja. Vuodelle 2025 tehdyn väestöennusteen pohjalta
peruskoululaisten kokonaismäärä Vuosaaren alueella ei kuitenkaan kasva, sillä osassa
aluetta peruskouluikäiset vähenevät ja osassa kasvavat.
</p>
<p>
Vuosaaren kouluverkkotarkastelun ehdotukset on tuotettu ideariihessä, jossa olivat
mukana koulujen johtokunnat, henkilöstön edustus ja alueella asuvat
kaupunginvaltuutetut. Ideariihen jälkeen koulut ovat kommentoineet ehdotuksia ja
täydentäneet niitä omilla näkemyksillään.
</p>
<p>
Koulupalvelujen kehittämisessä mietitään nyt eri vaihtoehtoja. Ehdotuksessa
tarkastellaan sitä, miten nykyiset koulurakennukset muodostaisivat yhtenäiset
peruskoulut. Väestöennusteen mukaan alueella tarvitaan noin 3 500 oppilaspaikkaa.
Koulurakennuksen laajennuksen tai uudisrakentamisen tekeminen kestää vähintään 4-5
vuotta.
</p>
<p>
Alueella asuvien oppilaiden lähikoulut (koulujen oppilaaksiottoalueet) määritellään
palvelutarkastelun jälkeen. Oppilaaksiottorajojen tarkastuksilla pystytään
huomioimaan alueelliset väestömuutokset.
</p>
<p class="lead">
<a href="http://www.hel.fi/static/liitteet/opev/palveluverkko/vuosaari-ehdotukset-kartat-tekstit.pdf">
Vaihtoehdot pdf-muodossa</a></p>
<p class="lead">
Kysymys:
Mikä vaihtoehdoista 1-4 olisi sinusta paras kouluverkkoratkaisu Vuosaaren alueella? Voit myös esittää muuta ratkaisua.
</p>
<p>
Kommentoi ehdotuksia 22.10. saakka. Saatua palautetta hyödynnetään jatkosuunnittelussa.
</p>
<p>
Vuosaaren alueen kouluverkosta järjestetään kaikille avoin asukastilaisuus maanantaina 26.10.2015 kello 18-20 Kallahden peruskoulussa os. Kallvikinniementie 1, Helsinki 99. Asukastilaisuuden jälkeen valmistuneita kouluverkon muutosesityksiä voi kommentoida 2.11.- 17.11.2015. Tästä tiedotetaan vielä tarkemmin. 
</p>
<p>
 Lisätietoa opetusviraston
<a href="http://www.hel.fi/www/opev/palveluverkko-fi/peruskoulut/">palveluverkkosivuilta</a>.   
</p>
<h4>Lisätietoja:</h4>
<p>aluepäällikkö Taina Tervonen, puh. 09 310 83013,
<a href="mailto:etunimi.sukunimi@hel.fi">etunimi.sukunimi@hel.fi</a></p>
'''  # noqa

opens_at = date(2015, 10, 12)

closes_at = date(2015, 10, 22)

published = True

area = {
    'type': 'Polygon',
    'coordinates': [
        [
            [
                25.086593627929688,
                60.18689710700169
            ],
            [
                25.086679458618164,
                60.18911600976546
            ],
            [
                25.08856773376465,
                60.19188942732679
            ],
            [
                25.095691680908203,
                60.19568649593106
            ],
            [
                25.10298728942871,
                60.20178648404814
            ],
            [
                25.113201141357422,
                60.20788533831751
            ],
            [
                25.113201141357422,
                60.208567657083265
            ],
            [
                25.122556686401364,
                60.21764967363427
            ],
            [
                25.122385025024414,
                60.21956808774096
            ],
            [
                25.124874114990234,
                60.22250943804349
            ],
            [
                25.128135681152344,
                60.22340457923737
            ],
            [
                25.13234138488769,
                60.22532265663597
            ],
            [
                25.13500213623047,
                60.228007776453296
            ],
            [
                25.13749122619629,
                60.232013736780395
            ],
            [
                25.137319564819336,
                60.23469830848293
            ],
            [
                25.135860443115234,
                60.23601920747618
            ],
            [
                25.136289596557614,
                60.236956587361625
            ],
            [
                25.138263702392575,
                60.236402684307066
            ],
            [
                25.139036178588867,
                60.235720944615956
            ],
            [
                25.149593353271484,
                60.23222680606138
            ],
            [
                25.14985084533691,
                60.23618964217734
            ],
            [
                25.151567459106445,
                60.236530508920005
            ],
            [
                25.15491485595703,
                60.23256771402948
            ],
            [
                25.157747268676754,
                60.233249519326534
            ],
            [
                25.160751342773438,
                60.233164294440144
            ],
            [
                25.18092155456543,
                60.229030621384
            ],
            [
                25.182037353515625,
                60.22907323923007
            ],
            [
                25.18993377685547,
                60.226729175401395
            ],
            [
                25.20392417907715,
                60.23030913266004
            ],
            [
                25.2011775970459,
                60.218630210423306
            ],
            [
                25.219802856445312,
                60.19969640603265
            ],
            [
                25.218944549560547,
                60.19841670072346
            ],
            [
                25.20092010498047,
                60.20080544359962
            ],
            [
                25.1601505279541,
                60.16465712803696
            ],
            [
                25.157661437988278,
                60.16534034577624
            ],
            [
                25.12375831604004,
                60.16581004973186
            ],
            [
                25.10427474975586,
                60.168329256366505
            ],
            [
                25.1107120513916,
                60.172043666306266
            ],
            [
                25.111312866210938,
                60.17597109124899
            ],
            [
                25.086593627929688,
                60.18689710700169
            ]
        ]
    ]
}

# Alternative 1
# -------------

alternative_1_title = 'Vaihtoehto 1'

alternative_1_main_image = {
    'filename': 'images/vuosaarenkoulut/alternative_1/main_image.jpg',
    'caption': 'Vaihtoehdon 1 esimerkkikuva.'
}

alternative_1_lead = '''

    Vuosaaressa on 4 yhtenäistä peruskoulua. Ne muodostetaan seuraavasti:

'''

alternative_1_body = '''

<p><ul>
<li>Vuosaaren peruskoulun Koukkusaarentien toimipiste, Vuosaaren ala-asteen koulu ja Heteniityn ala-asteen koulu yhdistyvät yhdeksi peruskouluksi. Koulussa on noin 1 200 oppilaspaikkaa.</li>
<li>Tehtaanpuiston yläasteen koulu ja Mustakiven ala-asteen koulu yhdistyvät yhtenäiseksi peruskouluksi. Koulutiloja tarvitaan noin 550 oppilaalle. Nykyisessä Mustakiven ala-asteen koulun rakennuksessa on 370 oppilaspaikkaa. Lisätilaa tarvitaan noin 200 oppilaspaikan verran.</li>
<li>Kallahden peruskoulu, Meri-Rastilan ala-asteen koulu ja Vuosaaren peruskoulun Venemestarintien toimipiste yhdistyvät yhtenäiseksi peruskouluksi. Koulussa on yhteensä noin 1 100 oppilaspaikkaa.</li>
<li>Aurinkolahden peruskoulu säilyy nykyisellään. Koulussa on noin 790 oppilaspaikkaa.</li>
</ul></p>
<p>
Jokaisessa koulussa on useampi toimipiste. Ehdotukseen sisältyy lisärakentamista. Tehtaanpuiston yläasteen rakennuksesta luovutaan. Kouluverkkopäätöksen jälkeen selvitetään, millaisia painotuksia koulujen opetuksessa on.
</p>

'''

# Alternative 2
# -------------

alternative_2_title = 'Vaihtoehto 2'

alternative_2_main_image = {
    'filename': 'images/vuosaarenkoulut/alternative_2/main_image.jpg',
    'caption': 'Vaihtoehdon 2 esimerkkikuva.'
}

alternative_2_lead = '''

    Vuosaaressa on 4 yhtenäistä peruskoulua. Ne muodostetaan seuraavasti:

'''

alternative_2_body = '''

<p><ul>
<li>Heteniityn ala-asteen koulu yhdistyy Vuosaaren peruskouluun. Koulussa on noin 890 oppilaspaikkaa.</li>
<li>Vuosaaren ala-asteen koulu, Mustakiven ala-asteen koulu ja Tehtaanpuiston yläasteen koulu yhdistyvät. Koulurakennuksissa on 840 oppilaspaikkaa. Lisätilaa tarvitaan noin 150 oppilaspaikan verran.</li>
<li>Kallahden peruskoulu ja Meri-Rastilan ala-asteen koulu yhdistyvät yhtenäiseksi peruskouluksi. Koulussa on 910 oppilaspaikkaa. Koulun oppilaaksiottoaluetta määriteltäessä otetaan huomioon Meri-Rastilan kaavoituksen kautta tuleva väestökasvu.</li>
<li>Aurinkolahden peruskoulu säilyy nykyisellään. Koulussa on noin 790 oppilaspaikkaa.</li>
</ul></p>
<p>
Koulut ovat lähes samankokoisia. Jokaisessa koulussa on useampi toimipiste. Ehdotukseen sisältyy lisärakentamista. Tehtaanpuiston yläasteen rakennuksesta luovutaan. Kouluverkkopäätöksen jälkeen selvitetään, millaisia painotuksia koulujen opetuksessa on.
</p>

'''

# Alternative 3
# -------------

alternative_3_title = 'Vaihtoehto 3'

alternative_3_main_image = {
    'filename': 'images/vuosaarenkoulut/alternative_3/main_image.jpg',
    'caption': 'Vaihtoehdon 3 esimerkkikuva.'
}

alternative_3_lead = '''

    Vuosaaressa on 5 yhtenäistä peruskoulua. Ne muodostetaan seuraavasti:

'''

alternative_3_body = '''

<p><ul>
<li>Heteniityn ala-asteen koulu yhdistyy Vuosaaren peruskouluun. Koulussa on noin 890 oppilaspaikkaa.</li>
<li>Vuosaaren ala-asteen koulu, Mustakiven ala-asteen koulu ja Tehtaanpuiston yläasteen koulu yhdistyvät. Koulussa on noin 840 oppilaspaikkaa. Joko Mustakiven tai Vuosaaren ala-asteen koulun tiloja muokataan. Kouluun rakennetaan aineluokkia lähinnä 7.-9. luokkien opetukseen.</li>
<li>Meri-Rastilan ala-asteen koulua laajennetaan yhtenäiseksi peruskouluksi. Koululle tulee lisää tilaa, jonka jälkeen koulussa on noin 500 oppilaspaikkaa.</li>
<li>Kallahden peruskoulu säilyy nykyisellään. Koulussa on noin 670 oppilaspaikkaa.</li>
<li>Aurinkolahden peruskoulu säilyy nykyisellään. Koulussa on noin 790 oppilaspaikkaa.
</ul></p>
<p>
Alueelliset väestömuutokset pystytään ottamaan huomioon tarkistamalla koulujen oppilaaksiottoalueita. Ehdotukseen sisältyy lisärakentamista. Tehtaanpuiston yläasteen rakennuksesta luovutaan. Kallahden peruskouluun ja Aurinkolahden peruskouluun ei ehdoteta muutoksia. Kallahden peruskoulu ja Meri-Rastilan ala-asteen koulu toimivat yhdessä rakennuksessa. Muissa kouluissa on useampi toimipiste. Kouluverkkopäätöksen jälkeen selvitetään, millaisia painotuksia koulujen opetuksessa on.
</p>

'''


# Alternative 4
# -------------

alternative_4_title = 'Vaihtoehto 4'

alternative_4_main_image = {
    'filename': 'images/vuosaarenkoulut/alternative_4/main_image.jpg',
    'caption': 'Vaihtoehdon 4 esimerkkikuva.'
}

alternative_4_lead = '''

    Vuosaaressa on 5 yhtenäistä peruskoulua. Ne muodostetaan seuraavasti:

'''

alternative_4_body = '''

<p><ul>
<li>Vuosaaren peruskoulu ja Heteniityn ala-asteen koulu yhdistyvät yhdeksi peruskouluksi. Koulussa on yhteensä noin 890 oppilaspaikkaa.</li>
<li>Meri-Rastilan ala-asteen koulua laajennetaan yhtenäiseksi peruskouluksi. Koululle tulee lisää tilaa, jonka jälkeen koulussa on noin 500 oppilaspaikkaa.</li>
<li>Vuosaaren ala-asteen koulu ja Tehtaanpuiston yläasteen koulu yhdistyvät yhtenäiseksi peruskouluksi. Koulurakennuksissa on noin 470 oppilaspaikkaa. Lisätilaa tarvitaan noin 100 oppilaspaikan verran.</li>
<li>Kallahden peruskoulu säilyy nykyisellään. Koulussa on noin 670 oppilaspaikkaa.</li>
<li>Aurinkolahden peruskoulu ja Mustakiven ala-asteen koulu yhdistyvät yhdeksi peruskouluksi. Koulussa on noin 1 000 oppilaspaikkaa.</li>
</ul></p>
<p>
Alueelliset väestömuutokset pystytään ottamaan huomioon tarkistamalla koulujen oppilaaksiottoalueita. Ehdotukseen sisältyy lisärakentamista. Tehtaanpuiston yläasteen rakennuksesta luovutaan. Kallahden peruskouluun ei ehdoteta muutoksia. Kallahden peruskoulu toimii yhdessä rakennuksessa. Muut koulut toimivat useammassa toimipisteessä. Kouluverkkopäätöksen jälkeen selvitetään, millaisia painotuksia koulujen opetuksessa on.
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
        {
            'title': alternative_4_title,
            'main_image': alternative_4_main_image,
            'lead': alternative_4_lead,
            'body': alternative_4_body,
        }
    ]
}
