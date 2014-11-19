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
  .directive('commentList', function () {
    return {
      templateUrl: 'components/comment-list/comment-list.html',
      restrict: 'A',
      controller: 'CommentListController',
      scope: {
        userId: '@',
        hearingId: '@',
        isAdmin: '@',
        isOfficial: '@',
        orderBy: '@'
      },
      link: function postLink(scope) {
        scope.isAdmin = scope.isAdmin === 'True' ? true : false;
        scope.isOfficial = scope.isOfficial === 'True' ? true : false;
        scope.scrollToCommentsTop = function(params) {
          $('html, body').animate({
            scrollTop: $('.comment-lists').offset().top
          }, params.duration);
        };
      }
    };
  });
