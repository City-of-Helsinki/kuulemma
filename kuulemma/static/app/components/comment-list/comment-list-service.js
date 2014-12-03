'use strict';

angular.module('kuulemmaApp')
  .factory('CommentListService', function ($http) {

    function get(id) {
      return $http.get('/hearings/' + id + '/links/comments');
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
