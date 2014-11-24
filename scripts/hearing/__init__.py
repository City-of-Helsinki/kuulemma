# -*coding: utf-8 -*-
from kuulemma.extensions import db
from kuulemma.models import Alternative, Hearing, Image


def _add_hearing(hearing_data):
    print('Start adding hearing: "{title}".'.format(
        title=hearing_data['title'].strip()
    ))

    hearing = Hearing(
        title=hearing_data['title'].strip(),
        lead=hearing_data['lead'].strip(),
        body=hearing_data['body'].strip(),
        opens_at=hearing_data['opens_at'],
        closes_at=hearing_data['closes_at'],
        published=hearing_data['published'],
    )

    hearing.main_image = Image(
        image_url=hearing_data['main_image']['url'],
        caption=hearing_data['main_image']['caption']
    )
    print('Main content added.')

    for alternative_data in hearing_data['alternatives']:
        alternative = Alternative(
            title=alternative_data['title'].strip(),
            lead=alternative_data['lead'].strip(),
            body=alternative_data['body'].strip(),
        )

        alternative.main_image = Image(
            image_url=alternative_data['main_image']['url'],
            caption=alternative_data['main_image']['caption']
        )

        hearing.alternatives.append(alternative)
        print('Alternative "{title}"" added.'.format(
            title=alternative_data['title'].strip()
        ))

    db.session.add(hearing)
    db.session.commit()
    print('Script completed! Hearing was successfully added.')
