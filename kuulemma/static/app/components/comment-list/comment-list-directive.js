'use strict';

angular.module('kuulemmaApp')
  .directive('commentList', function () {
    return {
      templateUrl: '/static/dist/partials/components/comment-list/comment-list.html',
      restrict: 'A',
      controller: 'CommentListController',
      scope: {
        userId: '@',
        hearingId: '@'
      },
      link: function postLink(scope) {
        scope.scrollToCommentsTop = function(params) {
          $('html, body').animate({
            scrollTop: $('#comment-list').offset().top
          }, params.duration);
        };
      }
    };
  });
