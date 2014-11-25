'use strict';
angular.module('kuulemmaApp')
  .directive('commentListItem', function () {
    return {
      templateUrl: '/static/dist/partials/components/comment-list-item/comment-list-item.html',
      restrict: 'A',
      scope: {
        comment: '&',
        hearingId: '@'
      },
      link: function postLink(scope, element) {
        scope.parsedComment = scope.$parent.comment.body.split('\n').join('<br>');
        scope.parsedParentPreview = scope.$parent.comment.parent_preview.split('\n').join('<br>');

        function makeContainerTruncatable(params) {
          _.defer(function () {
            var commentBodyContainer = element.find(params.selector);
            commentBodyContainer.dotdotdot({height: 150, after: '<button class="' + params.readmore.slice(1) + '">Lue lisää</button>'});

            commentBodyContainer.find(params.readmore).on('click', function() {
              commentBodyContainer.trigger('destroy.dot');
            });
          });
        }

        makeContainerTruncatable({ selector: '.body', readmore: '.readmore' });
        makeContainerTruncatable({ selector: '.parent-preview', readmore: '.readparent' });
      }
    };
  });
