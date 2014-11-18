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

        _.defer(function () {
          var commentBodyContainer = element.find('.body');
          commentBodyContainer.dotdotdot({height: 150, after: '.readmore'});
          commentBodyContainer.trigger('isTruncated', function(isTruncated) {
            if(!isTruncated) {
              element.find('.readmore').remove();
            }
          });

          element.find('.readmore').on('click', function() {
            commentBodyContainer.trigger('destroy.dot');
            _.defer(function() {
              element.find('.readmore').remove();
            });
          });
        });
      }
    };
  });
