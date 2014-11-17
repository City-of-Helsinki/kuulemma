'use strict';

angular.module('kuulemmaApp')
  .factory('CommentListService', function ($http) {

    function get(id) {
      return $http.get('/hearings/' + id + '/links/comments');
    }

    return {
      get: get
    };
  });
