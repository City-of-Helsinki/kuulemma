(function() {
  'use strict';
  angular.module('kuulemmaApp').directive('feedbackLink', function($rootScope) {
    return {
      restrict: 'A',
      link: function(scope, element){
        element.bind('click', function(event) {
          event.preventDefault();
          $rootScope.$broadcast('open-feedback-box');
        });
      }
    };
  });
})();
