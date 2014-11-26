'use strict';

angular.module('kuulemmaApp')
  .directive('commentList', function () {
    return {
      templateUrl: '/static/dist/partials/components/comment-list/comment-list.html',
      restrict: 'A',
      controller: 'CommentListController',
      scope: {
        userId: '@',
        hearingId: '@',
        isAdmin: '@',
        isOfficial: '@'
      },
      link: function postLink(scope) {
        scope.isAdmin = scope.isAdmin === 'True' ? true : false;
        scope.isOfficial = scope.isOfficial === 'True' ? true : false;
        scope.scrollToCommentsTop = function(params) {
          $('html, body').animate({
            scrollTop: $('#comment-list').offset().top
          }, params.duration);
        };
      }
    };
  });
