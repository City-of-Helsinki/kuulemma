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

title = 'Herttoniemen sairaalan alueelle asumista'

slug = 'herttoniemensairaala'

main_image = {
    'filename': 'images/herttoniemensairaala/main_image.jpg',
    'caption': (
        'Herttoniemen sairaala-alueen neljä alustavaa suunnitelmavaihtoehtoa keskustelussa.'
    )
}

lead = '''


'''

body = '''
    <p>
    Herttoniemen sairaala-alueen muuttamista asuinalueeksi suunnitellaan. Toimintansa lopettavien sairaalan ja terveysaseman tilalle ja niiden ympäristöön voisi tulla asuinrakentamista.
    </p>
    <p>
    Keskustelun pohjaksi on laadittu neljä alustavaa vaihtoehtoa sairaala-alueesta. Vaihtoehdot A "Hila" ja B "Vetoketju" ovat tiiviimpiä ja korkeampia versioita Länsi-Herttoniemelle ominaisesta avoimesta korttelirakenteesta. Vaihtoehdot C "Kampa" ja D "Umpikorttelit" ovat kantakaupunkimaisempia ja niissä on hieman enemmän uutta rakentamista. Kaikissa vaihtoehdoissa rakentamiseen käytetään likimain sama alue. Vaihtoehdoissa on 550–720 asukasta. Rakennusten korkeus on neljästä kahdeksaan kerrosta.
    </p>
    <p>
    Siilitien varteen ehdotetaan asuinrakennuksia ja uutta päiväkotia. Päiväkoti on vaihtoehdossa B sijoitettu Siilitien ja Kettutien kulmaan. Muissa vaihtoehdoissa se on alueen pohjoiskulmassa Siilitien varressa. Pysäköinti on kaikissa vaihtoehdoissa pihakansien alla ja maanpäällisissä pysäköintilaitoksissa. Liikuntapuiston pysäköintialuetta on pienennetty nykyisestä.
    </p>
    <p>
    Suunnitelmavaihtoehdot ja päivitetty osallistumis- ja arviointisuunnitelma ovat esillä 2.–23.11.2015 mm. Herttoniemen kirjastossa sekä verkkosivulla <a href="http://www.hel.fi/suunnitelmat">www.hel.fi/suunnitelmat</a>. Länsi-Hertsikan info- ja työpajailta järjestetään 10.11. klo 17 Herttoniemen yhteiskoululla, Kettutie 6.    </p>
    <p class="lead">
    Kerro näkemyksesi vaihtoehdoista! Miten vaihtoehdot sopivat Länsi-Herttoniemeen? Mitä hyviä ja huonoja puolia niissä on? Mitä mieltä olet kortteleista ja niiden piharatkaisuista? Kaavaratkaisua suunnitellaan saadun palautteen pohjalta.
    </p>
    <h4>Lisätietoja</h4>
    <ul>
    <li><a href="http://kartta.hel.fi/Applications/hanke/showplan.aspx?sour=haku&id=2015-002926&map=yes">
    Sairaala-alueen suunnitteluaineistot</a></li>
    <li><a href="http://helsinki.creamailer.fi/subscribe/553786e85ace1">
    Seuraa suunnittelua tilaamalla uutiskirje</a></li>
    <li><a href="http://www.facebook.com/events/537804663051994/">
    Länsi-Hertsikan ilta 10.11.2015</a></li>
    </ul>

'''  # noqa

opens_at = date(2015, 11, 2)

closes_at = date(2015, 11, 23)

published = False

area = {
    'type': 'Polygon',
    'coordinates': [
        [
            [
                25.03530979156494,
                60.207139035916406
            ],
            [
                25.036897659301754,
                60.206605952377515
            ],
            [
                25.037262439727783,
                60.207096389552085
            ],
            [
                25.037541389465332,
                60.208738234557096
            ],
            [
                25.038270950317383,
                60.20909004779543
            ],
            [
                25.036447048187256,
                60.210294713029356
            ],
            [
                25.035459995269775,
                60.20982564510067
            ],
            [
                25.036640167236328,
                60.20899409910464
            ],
            [
                25.035395622253418,
                60.20771475640846
            ],
            [
                25.03530979156494,
                60.207139035916406
            ]
        ]
    ]
}

# Alternative 1
# -------------

alternative_1_title = 'Vaihtoehto A'

alternative_1_main_image = {
    'filename': 'images/herttoniemensairaala/alternative_1/main_image.jpg',
    'caption': 'Vaihtoehto A:n esimerkkikuva.'
}

alternative_1_lead = '''

    Hila

'''

alternative_1_body = '''

<p>
Uudet asuinkerrostalot ovat 4–6-kerroksisia ja ulkomuodoltaan yksinkertaisia. Rakennuksissa on yksi tai kaksi porrashuonetta. Kahteen ja kolmeen riviin lomittuvien rakennusten väliin jää yhteispiha-aluetta. Päiväkoti sijoittuu alueen pohjoiskulmaan Siilitien varteen.
</p>
<p>
Pysäköintipaikat ovat rinteeseen sovitettujen pihakansien alla ja alueen keskellä olevassa kolmikerroksisessa maanpäällisessä pysäköintitalossa.
</p>
<p>
Vaihtoehdon laajuus on noin 22 000 k-m2 ja siinä syntyisi asuntoja noin 550 uudelle asukkaalle.
</p>

'''

# Alternative 2
# -------------

alternative_2_title = 'Vaihtoehto B'

alternative_2_main_image = {
    'filename': 'images/herttoniemensairaala/alternative_2/main_image.jpg',
    'caption': 'Vaihtoehto B:n esimerkkikuva.'
}

alternative_2_lead = '''

    Vetoketju

'''

alternative_2_body = '''

<p>
Kettukujan länsipuolelle tulee uusi seitsemänkerroksinen pistetalorivi, joka lomittuu vetoketjumaisesti rakenteilla olevien kirjaston korttelin uusien rakennusten kanssa. Liikuntapuiston reunaan tulee viisikerroksisia yhden tai kahden porrashuoneen taloja. Pihat aukeavat länteen liikuntapuistoon. Päiväkoti on sijoitettu Siilitien ja Kettukujan kulmaan.
</p>
<p>
Pysäköintipaikat ovat rinteeseen sovitettujen pihakansien alla ja alueen keskellä olevassa kolmikerroksisessa maanpäällisessä pysäköintitalossa.
</p>
<p>
Vaihtoehdon asuinkerrosala on noin 25 000 k-m2, mikä tarkoittaisi noin 630 uutta asukasta.
</p>

'''

# Alternative 3
# -------------

alternative_3_title = 'Vaihtoehto C'

alternative_3_main_image = {
    'filename': 'images/herttoniemensairaala/alternative_3/main_image.jpg',
    'caption': 'Vaihtoehto C:n esimerkkikuva.'
}

alternative_3_lead = '''

    Kampa

'''

alternative_3_body = '''

<p>
Vaihtoehto muodostuu korttelipihoja rajaavista, kadun puolelta umpinaisista ja puistoon aukeavista 4–7-kerroksista kortteleista sekä Siilitien varren yhdestä kahdeksankerroksisesta pistetalosta ja päiväkodista, joka sijoittuu alueen pohjoiskulmaan. Pihat avautuvat länteen liikuntapuistoon.
</p>
<p>
Pysäköintipaikat ovat rinteeseen sovitettujen pihakansien alla ja alueen keskellä olevassa kolmikerroksisessa maanpäällisessä pysäköintitalossa.
</p>
<p>
Asuinkerrosalaa vaihtoehdossa on noin 29 000 k-m2, mikä tarkoittaa asuntoja hieman yli 700 uudelle asukkaalle.
</p>

'''

# Alternative 4
# -------------

alternative_4_title = 'Vaihtoehto D'

alternative_4_main_image = {
    'filename': 'images/herttoniemensairaala/alternative_4/main_image.jpg',
    'caption': 'Vaihtoehto D:n esimerkkikuva.'
}

alternative_4_lead = '''

    Umpikorttelit

'''

alternative_4_body = '''

<p>
Vaihtoehto muodostuu isoja korttelipihoja rajaavista umpinaisista 4–7-kerroksista kortteleista ja Siilitien varren yhdestä kahdeksankerroksisesta pistetalosta ja päiväkodista alueen pohjoiskulmassa.
</p>
<p>
Pysäköintipaikat ovat rinteeseen sovitettujen pihakansien alla ja alueen keskellä olevassa kolmikerroksisessa maanpäällisessä pysäköintitalossa.
</p>
<p>
Vaihtoehdon asuinkerrosala on noin 28 000 k-m2 ja siinä syntyisi asuntoja hieman alle 700 uudelle asukkaalle.
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
        },
    ]
}
