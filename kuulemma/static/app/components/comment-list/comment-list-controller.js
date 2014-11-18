'use strict';

angular.module('kuulemmaApp')
  .controller('CommentListController', function ($scope, $rootScope, CommentListService, $attrs) {
    $scope.hearingId = $attrs.hearingId;
    CommentListService.get($scope.hearingId).then(function(response) {
      $scope.comments = response.data.comments || [];
      $scope.popularComments = getPopularComments();
    });

    function getPopularComments() {
      return _.sortBy($scope.comments, function(comment) {
        return comment.like_count * -1;
      });
    }

    $rootScope.$on('hearing-' + $attrs.hearingId + '-comment-added', function(event, comment) {
      $scope.comments.unshift(comment);
      $scope.popularComments.push(comment);
    });
  });
