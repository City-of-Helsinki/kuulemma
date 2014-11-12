'use strict';

angular.module('kuulemmaApp')
  .controller('CommentListController', function ($scope, $rootScope, CommentListService, $attrs) {
    $scope.hearingId = $attrs.hearingId;
    CommentListService.get($scope.hearingId).then(function(response) {
      $scope.comments = response.data.comments || [];
      $scope.latestComments = getLatestComments();
      $scope.popularComments = getPopularComments();
    });

    function getLatestComments() {
      return _.sortBy($scope.comments, function(comment) {
        return new Date(comment.created_at).getTime() * -1;
      });
    }

    function getPopularComments() {
      return _.sortBy($scope.comments, function(comment) {
        return comment.like_count * -1;
      });
    }

    $rootScope.$on('hearing-' + $attrs.hearingId + '-comment-added', function(event, comment) {
      $scope.comments.push(comment);
      $scope.latestComments.unshift(comment);
      $scope.popularComments.push(comment);
    });
  });
