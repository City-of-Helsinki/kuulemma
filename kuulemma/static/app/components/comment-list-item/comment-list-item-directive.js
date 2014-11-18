'use strict';
angular.module('kuulemmaApp')
  .directive('commentListItem', function () {
    return {
      templateUrl: '/static/dist/partials/components/comment-list-item/comment-list-item.html',
      restrict: 'A',
      scope: {
        comment: '&'
      },
      link: function postLink(scope) {
        scope.paragraphs = _.compact(scope.$parent.comment.body.split('\n'));
      }
    };
  });
