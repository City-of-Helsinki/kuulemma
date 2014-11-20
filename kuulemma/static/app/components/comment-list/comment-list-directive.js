'use strict';

angular.module('kuulemmaApp')
  .directive('commentList', function () {
    return {
      templateUrl: '/static/dist/partials/components/comment-list/comment-list.html',
      restrict: 'A',
      controller: 'CommentListController',
      link: function postLink(scope, element, attrs) {
        scope.hearingId = attrs.hearingId;

        scope.scrollToCommentsTop = function(params) {
          $('html, body').animate({
            scrollTop: $('#latest-comments').offset().top
          }, params.duration);
        };
      }
    };
  });
