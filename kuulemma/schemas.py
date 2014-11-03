from marshmallow import fields, Schema


def data_required(value):
    return value != '' and value


class CommentSchema(Schema):
    id = fields.Integer()
    title = fields.String(validate=data_required, required=True)
    body = fields.String(validate=data_required, required=True)
    username = fields.String(validate=data_required, required=True)
    created_at = fields.DateTime()
    like_count = fields.Integer()
