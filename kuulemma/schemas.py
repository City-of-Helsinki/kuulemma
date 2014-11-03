from marshmallow import fields, Schema


class CommentSchema(Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    body = fields.String(required=True)
    username = fields.String(required=True)
    created_at = fields.DateTime()
    like_count = fields.Integer()
