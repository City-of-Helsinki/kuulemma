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

    $scope.saveComment = function(form) {
      if(form.$invalid) {
        return;
      }
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

      if($scope.newCommentForm) {
        $scope.newCommentForm.$setUntouched();
        $scope.newCommentForm.$setPristine();
      }
    };

    $scope.emptyForm();
  });

})();
