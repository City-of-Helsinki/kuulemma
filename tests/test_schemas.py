from kuulemma.schemas import CommentSchema
from tests.factories import CommentFactory, LikeFactory, UserFactory


def test_comment_serializer():
    comment = CommentFactory.build(
        id=123,
        title='Awesome title',
        body='So much content.'
    )
    user = UserFactory.build()
    LikeFactory.build(user=user, comment=comment)
    schema = CommentSchema()
    schema.contex = {'user': user}
    data, errors = schema.dump(comment)
    assert data == {
        'id': comment.id,
        'title': comment.title,
        'body': comment.body,
        'username': comment.username,
        'created_at': comment.created_at,
    }
