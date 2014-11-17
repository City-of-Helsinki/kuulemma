(function() {
  'use strict';
  angular.module('kuulemmaApp').directive('commentAdder', function() {
    return {
      restrict: 'A',
      templateUrl: '/static/dist/partials/components/comment-adder/comment-adder.html',
      scope: {
        buttonText: '@',
        hearingId: '@',
        contextList: '@'
      }
    };
  });
})();
