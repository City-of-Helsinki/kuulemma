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
      return $http.put('/hearings/' + params.hearingId + '/links/comments/' + params.comment.id, {
        is_hidden: true,
        body: params.comment.body,
        title: params.comment.title,
        username: params.comment.username
      });
    }

    function unhideComment(params) {
      return $http.put('/hearings/' + params.hearingId + '/links/comments/' + params.comment.id, {
        is_hidden: false,
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
      unhideComment: unhideComment
    };
  });
