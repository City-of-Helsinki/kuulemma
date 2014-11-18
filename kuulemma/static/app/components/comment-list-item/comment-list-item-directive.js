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
        scope.paragraphs = _.compact(scope.$parent.comment.body.split('\n'));
        scope.previewParagraphs = _.compact(scope.$parent.comment.parent_preview.split('\n'));

        function makeContainerTruncatable(params) {
          _.defer(function () {
            var commentBodyContainer = element.find(params.selector);
            commentBodyContainer.dotdotdot({height: 150, after: params.readmore});
            commentBodyContainer.trigger('isTruncated', function(isTruncated) {
              if(!isTruncated) {
                element.find(params.readmore).remove();
              }
            });

            element.find(params.readmore).on('click', function() {
              commentBodyContainer.trigger('destroy.dot');
              _.defer(function() {
                element.find(params.readmore).remove();
              });
            });
          });
        }

        makeContainerTruncatable({ selector: '.body', readmore: '.readmore' });
        makeContainerTruncatable({ selector: '.parent-preview', readmore: '.readparent' });
      }
    };
  });
