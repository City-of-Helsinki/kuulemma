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
'use strict';
angular.module('kuulemmaApp')
  .directive('commentListItem', function ($rootScope, CommentListService) {
    return {
      templateUrl: '/static/dist/partials/components/comment-list-item/comment-list-item.html',
      restrict: 'A',
      scope: {
        comment: '=',
        hideComment: '&',
        unhideComment: '&',
        hearingId: '@'
      },
      link: function postLink(scope, element) {
        var editableEntries = ['username', 'body', 'title'];
        var editableEntriesBeforeChanges = _.pick(scope.$parent.comment, editableEntries);

        scope.saveChanges = function() {
          var editableEntriesBackup = angular.copy(editableEntriesBeforeChanges);
          editableEntriesBeforeChanges = _.pick(scope.$parent.comment, editableEntries);
          scope.commentUnderEdit = false;
          CommentListService.editComment({hearingId: scope.hearingId, comment: scope.$parent.comment})
            .success(function() {
              $rootScope.$broadcast('edited-comment-' + scope.$parent.comment.id);
            })
            .error(function() {
              scope.$parent.comment = _.extend(scope.$parent.comment, editableEntriesBackup);
            });
        };

        scope.cancelChanges = function() {
          scope.$parent.comment = _.extend(scope.$parent.comment, editableEntriesBeforeChanges);
          scope.commentUnderEdit = false;
        };

        var eventListenerRemover = $rootScope.$on('edited-comment-' + scope.$parent.comment.id, function() {
          eventListenerRemover();
          postLink(scope, element);
        });

        scope.$on('$destroy', eventListenerRemover);

        function makeContainerTruncatable(params) {
          _.defer(function () {
            var commentBodyContainer = element.find(params.selector);
            commentBodyContainer.dotdotdot({height: 150, after: '<button class="' + params.readmore.slice(1) + '">Lue lisää</button>'});

            commentBodyContainer.find(params.readmore).on('click', function() {
              commentBodyContainer.trigger('destroy.dot');
            });
          });
        }

        makeContainerTruncatable({ selector: '.comment-body', readmore: '.readmore' });
        makeContainerTruncatable({ selector: '.parent-preview', readmore: '.readparent' });
      }
    };
  });
