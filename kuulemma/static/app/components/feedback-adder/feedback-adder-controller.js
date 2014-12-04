(function() {
  'use strict';
  angular.module('kuulemmaApp').controller('AddFeedbackController', function AddFeedbackController($scope, $rootScope, FeedbackService) {
    $scope.openFeedbackBox = function() {
      $scope.feedbackBoxOpen = true;
    };

    $scope.closeFeedbackBox = function() {
      $scope.feedbackBoxOpen = false;
      $scope.emptyForm();
    };

    $scope.toggleFeedbackBox = function() {
      $scope.buttonText = '';
      if ($scope.feedbackBoxOpen) {
        $scope.closeFeedbackBox();
      } else {
        $scope.openFeedbackBox();
      }
    };

    $scope.saveFeedback = function() {
      $scope.sendingFeedback = true;
      var request = FeedbackService.save($scope.form);
      request.success(function(response) {
        $rootScope.$broadcast('feedback-added', response.feedbacks);
        $scope.emptyForm();
        $scope.sendingFeedback = false;
        $scope.thankUser();
      });
    };

    $scope.emptyForm = function() {
      var emptyFields = {
        content: ''
      };
      $scope.form = angular.copy(emptyFields);
    };

    $scope.thankUser = function() {
      $scope.closeFeedbackBox();
      $scope.buttonText = 'Kiitoksia palautteesta!';
    };

    $rootScope.$on('open-feedback-box', function() {
      $scope.openFeedbackBox();
      $scope.$apply();
    });

    $scope.emptyForm();
  });

})();
