import pytest

from kuulemma.schemas import CommentSchema
from tests.factories import (
    CommentFactory,
    HearingFactory,
    LikeFactory,
    UserFactory
)


@pytest.mark.usefixtures('database')
def test_comment_serializer():
    hearing = HearingFactory(id=1)
    comment = CommentFactory(
        id=123,
        hearing=hearing,
        title='Awesome title',
        body='So much content.'
    )
    user = UserFactory()
    LikeFactory(user=user, comment=comment)
    schema = CommentSchema()
    schema.contex = {'user': user}
    data, errors = schema.dump(comment)
    assert data == {
        'id': comment.id,
        'title': comment.title,
        'body': comment.body,
        'username': comment.username,
        'created_at': comment.created_at.isoformat() + '+00:00',
        'like_count': comment.like_count,
        'tag': comment.tag,
        'parent_preview': comment.parent_preview,
        'is_hidden': comment.is_hidden,
        'object_type': 'hearing',
        'object_id': hearing.id
    }
