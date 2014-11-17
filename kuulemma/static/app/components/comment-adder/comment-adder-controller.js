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

    $scope.commentOptions = [
      { label: 'Yleisesti tähän kuulemiseen', id: 'SOME_ID' }
    ];

    $scope.saveComment = function() {
      var request = CommentService.save($scope.hearingId, $scope.form);
      request.success(function(response) {
        $rootScope.$broadcast('hearing-' + $scope.hearingId + '-comment-added', response.comments);
        $scope.emptyForm();
      });
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
