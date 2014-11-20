(function() {
  'use strict';
  angular.module('kuulemmaApp').controller('AddCommentController', function AddCommentController($scope, $rootScope, CommentService) {
    $scope.openCommentBox = function() {
      $scope.commentBoxOpen = true;
    };

    $scope.closeCommentBox = function() {
      $scope.commentBoxOpen = false;
      $scope.emptyForm();
    };

    $scope.commentOptions = _.map($scope.contextList.split(';'), function(context) {
      var keyValuePair = context.split(':');
      return {
        key: keyValuePair[0],
        label: keyValuePair[1]
      };
    });

    $scope.saveComment = function() {
      var request = CommentService.save($scope.hearingId, $scope.form);
      request.success(function(response) {
        $rootScope.$broadcast('hearing-' + $scope.hearingId + '-comment-added', response.comments);
        if($scope.commentingOnComment()) {
          $scope.closeCommentBox();
          return;
        }
        $scope.emptyForm();
      });
    };

    $scope.commentingOnComment = function() {
      return $scope.commentOptions.length === 1 &&
        $scope.commentOptions[0].key.split('-')[0] === 'comment';
    };

    $scope.emptyForm = function() {
      var emptyFields = {
        title: '',
        username: '',
        commentsOn: $scope.commentOptions[0],
        body: '',
        follow: false,
        email: ''
      };
      $scope.form = angular.copy(emptyFields);
    };

    $scope.emptyForm();
  });

})();
