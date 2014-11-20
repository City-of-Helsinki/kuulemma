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
      },
      link: function(scope, element, attrs) {
        if(attrs.size && attrs.size === 'small') {
          var container = element.children()[0];
          angular.element(container).addClass('narrow');
        }
      }
    };
  });
})();
