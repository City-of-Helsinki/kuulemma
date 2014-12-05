'use strict';

angular.module('kuulemmaApp')
  .filter('commentBodyFilter', function () {
    return function (commentBody) {
      return commentBody.split('\n').join('<br>');
    };
  });
