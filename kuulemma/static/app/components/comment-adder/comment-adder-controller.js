(function() {
  'use strict';
  angular.module('kuulemmaApp').controller('AddCommentController', function AddCommentController($scope, CommentService) {
    $scope.openCommentBox = function() {
      $scope.commentBoxOpen = true;
    };

    $scope.closeCommentBox = function() {
      $scope.commentBoxOpen = false;
      $scope.form = angular.copy(emptyForm);
    };

    $scope.commentOptions = [
      { label: 'Yleisesti tähän kuulemiseen', id: 'SOME_ID' }
    ];

    var emptyForm = {
      title: '',
      username: '',
      commentsOn: $scope.commentOptions[0],
      body: '',
      follow: false,
      email: ''
    };

    $scope.form = angular.copy(emptyForm);

    $scope.saveComment = function() {
      var request = CommentService.save($scope.hearingId, $scope.form);
      request.success($scope.closeCommentBox);
    };
  });

})();
