(function() {
  'use strict';
  angular.module('kuulemmaApp').directive('commentAdder', function() {
    return {
      restrict: 'A',
      templateUrl: '/static/dist/partials/components/comment-adder/comment-adder.html',
      scope: {
        buttonText: '@',
        initialContext: '@',
        hearingId: '@',
        hearingAlternatives: '@'
      },
      link: function(scope, element, attrs) {
        if(attrs.contextList) {
          scope.contextList = _.map(attrs.contextList.split(';'), function(context) {
            var keyValuePair = context.split(':');
            return _.object([keyValuePair[0]], [keyValuePair[1]]);
          });
        }
      }
    };
  });
})();
