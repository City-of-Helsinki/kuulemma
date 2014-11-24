from datetime import date


# Main section
# ------------

title = 'Millainen on Hämeentien tulevaisuus?'

main_image = {
    'url': '/static/images/hameentie/main_image.jpg',
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

# Alternative 1
# -------------

alternative_1_title = 'Vaihtoehto 1'

alternative_1_main_image = {
    'url': '/static/images/hameentie/alternative_1/main_image.jpg',
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
    'url': '/static/images/hameentie/alternative_2/main_image.jpg',
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
    'url': '/static/images/hameentie/alternative_3/main_image.jpg',
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
    'title': title,
    'main_image': main_image,
    'lead': lead,
    'body': body,
    'opens_at': opens_at,
    'closes_at': closes_at,
    'published': published,
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
