from marshmallow import fields, Schema

from kuulemma.models.comment import COMMENTABLE_TYPES


def data_required(value):
    return value != '' and value


def object_type_validator(value):
    return value in COMMENTABLE_TYPES


class CommentSchema(Schema):
    id = fields.Integer()
    title = fields.String(validate=data_required, required=True)
    body = fields.String(validate=data_required, required=True)
    username = fields.String(validate=data_required, required=True)
    created_at = fields.DateTime()
    like_count = fields.Integer()
    object_type = fields.String(validate=object_type_validator)
    object_id = fields.Integer()
    tag = fields.String()
    parent_preview = fields.String()
