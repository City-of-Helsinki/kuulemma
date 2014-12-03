'use strict';

angular.module('kuulemmaApp')
  .controller('CommentListController', function ($scope, $q, $rootScope, CommentListService, $timeout, $window) {
    var hearingComments = CommentListService.get({
      hearingId: $scope.hearingId,
      orderBy: $scope.orderBy
    });
    var userLikes = $scope.userId ? CommentListService.getUserLikes($scope.userId) : {data: {}};

    $q.all([hearingComments, userLikes]).then(function(response) {
      $scope.comments = response[0].data.comments || [];
      $scope.page = response[0].data.page || 1;
      $scope.per_page = response[0].data.per_page || 20;
      if (response[0].data.comments.length >= $scope.per_page) {
        $scope.commentsStillLeft = true;
      }
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

    $scope.fetchMore = function() {
      CommentListService.get({
        hearingId: $scope.hearingId,
        orderBy: $scope.orderBy,
        page: $scope.page + 1
      }).
        success(function(response) {
          $scope.comments.push.apply($scope.comments, response.comments);
          $scope.page = response.page;
          if (response.comments.length < $scope.per_page) {
            $scope.commentsStillLeft = false;
          }
        }).
        error(function() {
          $scope.commentsStillLeft = false;
        });
    };

    $rootScope.$on('hearing-' + $scope.hearingId + '-comment-added', function(event, comment) {
      if ($scope.orderBy === 'created_at') {
        var scrollDuration = 200;
        $scope.scrollToCommentsTop({ duration: scrollDuration });
        $timeout(function() {
          $scope.comments.unshift(comment);
        }, scrollDuration);
      }
    });
  });
