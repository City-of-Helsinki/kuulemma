(function() {
  'use strict';
  angular.module('kuulemmaApp').directive('feedbackAdder', function() {
    return {
      restrict: 'A',
      templateUrl: '/static/dist/partials/components/feedback-adder/feedback-adder.html',
    };
  });
})();
