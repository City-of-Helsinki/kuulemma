'use strict';

angular.module('kuulemmaApp')
  .controller('CommentListController', function ($scope, $q, $rootScope, CommentListService, $timeout, $window) {
    var hearingComments = CommentListService.get($scope.hearingId);
    var userLikes = $scope.userId ? CommentListService.getUserLikes($scope.userId) : {data: {}};

    $q.all([hearingComments, userLikes]).then(function(response) {
      $scope.comments = response[0].data.comments || [];
      $scope.popularComments = getPopularComments();
      $scope.userLikes = response[1].data.comments || [];
    });

    $scope.toggleLike = function(commentId) {
      if(!$scope.userId) {
        return;
      }
      var comment = _.findWhere($scope.comments, { id: commentId });
      if($scope.alreadyLiked(commentId)) {
        $scope.userLikes = _.without($scope.userLikes, commentId);
        comment.like_count--;
        CommentListService.unlike({ userId: $scope.userId, commentId: commentId })
          .error(function() {
            $scope.userLikes.push(commentId);
            comment.like_count++;
        });
      } else {
        $scope.userLikes.push(commentId);
        comment.like_count++;
        CommentListService.like({ userId: $scope.userId, commentId: commentId })
          .error(function() {
            $scope.userLikes = _.without($scope.userLikes, commentId);
            comment.like_count--;
        });
      }
    };

    $scope.hideComment = function(comment) {
      var confirm = $window.confirm('Haluatko varmasti piilottaa kommentin? Kommentin voi myöhemmin palauttaa takaisin näkyviin.');
      if(!confirm) {
        return;
      }

      CommentListService.hideComment({
        hearingId: $scope.hearingId,
        comment: comment
      })
        .success(function() {
          comment.is_hidden = true;
        });
    };

    $scope.unhideComment = function(comment) {
      CommentListService.unhideComment({
        hearingId: $scope.hearingId,
        comment: comment
      })
        .success(function() {
          comment.is_hidden = false;
        });
    };

    $scope.alreadyLiked = function(commentId) {
      return _.contains($scope.userLikes, commentId);
    };

    function getPopularComments() {
      var likedComments = _.filter($scope.comments, function(comment) {
        return comment.like_count > 0;
      });

      return _.sortBy(likedComments, function(comment) {
        return comment.like_count * -1;
      });
    }

    $rootScope.$on('hearing-' + $scope.hearingId + '-comment-added', function(event, comment) {
      var scrollDuration = 200;
      $scope.scrollToCommentsTop({ duration: scrollDuration });
      $timeout(function() {
        $scope.comments.unshift(comment);
      }, scrollDuration);
    });
  });
