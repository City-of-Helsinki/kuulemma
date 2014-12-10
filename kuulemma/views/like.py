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

from flask import abort, Blueprint, jsonify, request
from flask.ext.login import current_user
from sqlalchemy.exc import IntegrityError

from kuulemma.extensions import db
from kuulemma.models import Comment, Like, User

like = Blueprint(
    name='like',
    import_name=__name__,
    url_prefix='/users/<int:user_id>/links/likes'
)


@like.route('')
def index(user_id):
    user = User.query.get_or_404(user_id)
    if user != current_user:
        abort(401)

    hearing = None
    if request.get_json():
        hearing_id = request.get_json().get('hearing_id', 0)
        hearing = Comment.query.get_or_404(hearing_id)

    comment_ids = user.get_liked_comment_ids(hearing)

    return jsonify({'comments': comment_ids})


@like.route('', methods=['POST'])
def create(user_id):
    user = User.query.get_or_404(user_id)
    if user != current_user:
        abort(401)

    comment_id = request.get_json().get('comment_id', 0)
    comment = Comment.query.get_or_404(comment_id)

    like = Like(
        user=user,
        comment=comment
    )
    db.session.add(like)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return (
            jsonify({'error': 'User has already liked the comment.'}),
            400
        )

    return jsonify({'like_count': comment.like_count}), 201


@like.route('', methods=['DELETE'])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    if user != current_user:
        abort(401)

    comment_id = request.get_json().get('comment_id', 0)

    like = (
        Like.query
        .filter(Like.user_id == user_id, Like.comment_id == comment_id)
        .first()
    )

    if not like:
        return (jsonify({'error': 'No comment was found.'}), 400)

    db.session.delete(like)
    db.session.commit()

    return '', 204
