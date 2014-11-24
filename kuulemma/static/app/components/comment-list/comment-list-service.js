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

    return {
      get: get,
      like: like,
      unlike: unlike,
      getUserLikes: getUserLikes
    };
  });
