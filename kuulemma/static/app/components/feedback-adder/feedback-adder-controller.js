/* Kuulemma
 * Copyright (C) 2014, Fast Monkeys Oy
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
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
      var request = FeedbackService.save($scope.form);
      request.success(function(response) {
        $rootScope.$broadcast('feedback-added', response.feedbacks);
        $scope.emptyForm();
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
