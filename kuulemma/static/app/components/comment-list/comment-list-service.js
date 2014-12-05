/* Kuulemma
 * Copyright (C) 2014, Fast Monkeys Oy
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
'use strict';

angular.module('kuulemmaApp')
  .factory('CommentListService', function ($http) {

    function get(params) {
      return $http.get('/hearings/' + params.hearingId + '/links/comments', {
        params: {
          order_by: params.orderBy || 'created_at',
          page: params.page || 1,
          per_page: params.perPage || 20
        }
      });
    }

    function getUserLikes(userId) {
      return $http.get('/users/' + userId + '/links/likes');
    }

    function like(params) {
      return $http.post('/users/' + params.userId + '/links/likes', { comment_id: params.commentId });
    }

    function unlike(params) {
      return $http.delete('/users/' + params.userId + '/links/likes', {
        data: {
          comment_id: params.commentId
        }
      });
    }

    function hideComment(params) {
      var forcedParams = _.extend(params, {is_hidden: true});
      return editComment(forcedParams);
    }

    function unhideComment(params) {
      var forcedParams = _.extend(params, {is_hidden: false});
      return editComment(forcedParams);
    }

    function editComment(params) {
      return $http.put('/hearings/' + params.hearingId + '/links/comments/' + params.comment.id, {
        is_hidden: params.comment.is_hidden,
        body: params.comment.body,
        title: params.comment.title,
        username: params.comment.username
      });
    }

    return {
      get: get,
      like: like,
      unlike: unlike,
      getUserLikes: getUserLikes,
      hideComment: hideComment,
      unhideComment: unhideComment,
      editComment: editComment
    };
  });
