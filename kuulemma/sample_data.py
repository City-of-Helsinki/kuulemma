# -*coding: utf-8 -*-
from datetime import date, datetime, timedelta
from random import randrange

from kuulemma.models import Alternative, Comment, Hearing, Image

alternative_body = '''
    <p>
    Rakennukset ovat suurimmaksi osaksi viisi–kuusikerroksisia, korkeimmat
    12-kerroksisia. Alueen keskeisin paikka on toriaukio, johon on suunniteltu
    kesiksi vesiallasta ja talviksi pientä luistelurataa. Toriaukion yhteyteen
    on suunniteltu sijoitettavaksi marketti ja muuta liiketilaa. Alueen halki
    kulkee maaston muotoja mukaileva kaareva katu, joka liittyy Kytösuotien
    pohjoispäähän. Pysäköinti on suunniteltu alueen keskeisessä
    markettikorttelissa pysäköintitaloon ja muissa kortteleissa pihakansien
    alle.
    </p>
    <p>
    Ehdotus perustuu neljään umpikortteliin ja Mannerheimintien tuntumassa
    olevaan liike ja pysäköintirakennukseen. Korttelit ovat toisiinsa nähden
    hieman vinossa, jolloin kortteleiden väliset katutilat ovat vaihtelevan
    levyisiä ja kortteleiden kulmiin syntyy aukiomaisia tiloja. Korkeimmat
    rakennukset ovat 14-kerroksisia, umpikortteleiden muut osat ovat 7–8
    kerroksisia. Kytösuontien varressa on suurempi aukio asukkaiden oleskelua
    varten. Ajoliikenne Mannerheimintieltä liittyy suoraan Kytösuontiehen, ja
    katu kiertää alueen keskeisimmän korttelin ympäri. Mannerheimintien
    varressa olevan pysäköintitalon lisäksi pysäköinti on suunniteltu
    kortteleiden pihakansien alle. Mannerheimintien ja Vihdintien kulmaukseen
    on tutkittu vaihtoehtoisesti myös liiketai urheilurakentamista.
    </p>

    '''

alternatives = [
    {
        'title': 'Verho (Arkkitehtitoimisto Ajak),',
        'lead': '''
            Ehdotus Verho perustuu kaareviin vaaleisiin rakennuksiin,
            jotka rajaavat aluetta Vihdintien ja Mannerheimintien suuntaan.
            Kaarevien rakennusten suojaamalla lounaispuolella korttelirakenne
            ja yksittäiset rakennukset ovat monimuotoisempia ja rakentaminen
            väljempää.

            ''',
        'body': alternative_body
    },
    {
        'title': 'Kotikulmat (Helsinki Zürich Office)',
        'lead': '''Ehdotus perustuu neljään umpikortteliin ja Mannerheimintien
            tuntumassa olevaan liikeja pysäköintirakennukseen. Korttelit ovat
            toisiinsa nähden hieman vinossa, jolloin kortteleiden väliset
            katutilat ovat vaihtelevan levyisiä ja kortteleiden kulmiin syntyy
            aukiomaisia tiloja.

            ''',
        'body': alternative_body
    },
    {
        'title': 'Koto (Serum Arkkitehdit)',
        'lead': '''Koto-ehdotus perustuu viisikulmaisiin kortteleihin ja
            niiden välissä kulkevaan polveilevaan katuun, joka yhtyy
            Kytösuontien pohjoispäähän. Rakennukset ovat vaihtelevan muotoisia
            ja korkuisia – aina yksikerroksisista osista 14-kerroksisiin.
            Pääosa taloista on 5–7-kerroksisia.

            ''',
        'body': alternative_body
    }
]

comments = [
    {
        'title': 'Liian matalaa',
        'username': 'Hessu K.',
        'body': '''Toki talot ovat korkeita ehdotuksissakin mutta huutavan
            asuntopulan aikana toivoisi vieläkin korkeampia taloja (20-25 krs)
            ja alueen vähän tiivimmin rakennettuna. Hieman tiivistettynä
            alueesta tulisi "oikea" kantakaupungin jatke. Asunnoista
            suurimman osan pitäisi olla yksiöitä ja kaksioita. Ehkä jopa YIT
            saisi rakennettua ja myytyä tällaiset asunnot vähemmässä kuin 10
            vuodessa. YIT:n, Skanskan ja SRV:n rakentamattomien tonttien
            jäljiltä Helsinki näyttää monin paikoin sodan uhrilta.

            '''
    },
    {
        'title': 'Verho on paras luonnos',
        'username': 'Timo Huhtinen, Kytösuonpolku 3:n asukas',
        'body': '''
            Yhtenäinen muurimainen rakenne Vihdintietä ja Mannerheimintietä
            vasten suojaa hyvin liikenteen melulta. Ratkaisu on kuitenkin
            mielenkiintoinen ja vaihteleva kaupunkiin Hämeenlinnan väylää
            pitkin pohjoisesta tulevan näkökulmasta.
            Muurimaisen rakenteen eteläja länsipuolelle pihoille syntyy...'

            '''
    },
    {
        'title': 'Kaupungin puolesta',
        'username': 'Patrick Jensen',
        'body': '''
            Ehdotuksia jatkosuunnitteluun:
            suunnitelmien pohjalta. Muut ehdotukset ovat muotokieleltään liian
            yksitoikkoisia tai mitoitukseltaan liian väljiä ollakseen
            varteenotettavia vaihtoehtoja.
            Onko mahdollista sijoittaa alueen pysäköintilaitos kallioon
            louhittavaan pysäköintiluolaan (en tunne alueen nykyisiä
            Olen hieman kummissani, ettei mikään suunnitelma ole sijoittanut
            koillisnurkkaan kunnon torahammasta merkiksi kaupungin
            alkamisesta. Korkeakin torni varjostaisi lähinnä risteysaluetta.
            Suunnitelmissa esitetyt palvelut eli ruokakauppa ja päiväkoti
            ovat hyvät. En keksi muita palvelutarpeita tälle alueelle.

            '''
    }
]

hearing_data = {
    'title': 'Kerro mielipiteesi Pikku-Huopalahden suunnitelmasta',
    'lead': '''
        Pikku huopalahden pohjoisosaan, Mannerheimintien ja vihdintien
        kulmaukseen, suunnitellaan uutta asuinaluetta. Asemakaavatyön
        pohjaksi on teetetty kolme maankäytön suunnitelmaa. suunnitelmista
        voi antaa palautetta ja keskustella tällä palstalla 6. kesäkuuta
        asti.'

        ''',
    'body': '''
        <p>Suunnitelmista saadun palautteen ja asiantuntija-arvioiden pohjalta
        valmistellaan asemakaavan muutosperiaatteet. Periaatteet tulevat
        keskusteluun syksyllä, jonka jälkeen ne viedään
        kaupunkisuunnittelulautakunnan käsittelyyn. Periaatteet ohjaavat
        jatkossa asemakaavatyötä.</p>
        <p>Millaiset asiat tai kohdat kussakin suunnitelmassa tuntuvat
        ratkaisuina hyviltä? Entä mikä herättää epäilyksiä? Millaisia
        palveluita alueella tarvittaisiin ruokakaupan ja päiväkodin
        lisäksi?</p>
        <p>Kaupunkisuunnitteluviraston teettämien suunnitelmien lisäksi kantaa
        voi ottaa myös Urban Helsinki -ryhmän tekemään suunnitelmaan. Sen
        lähtökohtana on ollut muita ehdotuksia tiiviimpi kaupunkirakenne ja
        suurempi asukasmäärä, ja siinä on otettu vapaus poiketa kaavoitusta
        ohjaavista normeista mm. valoisuusvaatimusten ja pysäköintipaikkojen
        määrän osalta.</p>

        '''
}


def get_random_future_date(range):
    return date.today() + timedelta(days=randrange(range))


def get_random_past_date(range):
    return date.today() - timedelta(days=randrange(range))


def get_image(caption='Asemapiirros lorem ipsum dolores ja niin edelleen.'):
    return Image(
        filename='images/ph1920.jpg',
        caption=caption
    )


def get_sample_hearing():
    hearing = Hearing(
        title=hearing_data['title'],
        lead=hearing_data['lead'],
        body=hearing_data['body'].strip(),
        opens_at=get_random_past_date(30),
        closes_at=get_random_future_date(30),
        published=True,
        main_image=get_image('Asemapiirros. Kuva: Arkkitehtitoimisto AJAK.'),
    )

    hearing.slug = str(datetime.utcnow())

    hearing.images.append(
        get_image('Arkkitehdin luonnos uudesta rakennuksesta.')
    )

    for alternative in alternatives:
        hearing.alternatives.append(
            Alternative(
                title=alternative['title'],
                lead=alternative['lead'].strip(),
                body=alternative['body'].strip(),
                main_image=get_image('Vaihtoehdon kuvan kuvateksti.'),
                images=[
                    get_image('Vaihtoehto voitaisiin toteuttaa myös näin.'),
                ]
            )
        )

    for i in range(randrange(15)):
        comment = comments[i % 3]
        hearing.comments.append(
            Comment(
                title=comment['title'],
                body=comment['body'].strip(),
                username=comment['username'],
                created_at=get_random_past_date(15)
            )
        )

    return hearing
