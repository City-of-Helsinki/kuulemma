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
  angular.module('kuulemmaApp').directive('commentCounter', function($rootScope) {
    return {
      restrict: 'A',
      scope: {
        hearingId: '@',
        count: '@'
      },
      link: function(scope, element){
        var count = parseInt(scope.count);
        var increase = function () {
          count += 1;
          element.text(count);
        };
        var decrease = function () {
          count -= 1;
          element.text(count);
        };
        element.text(count);
        $rootScope.$on('hearing-' + scope.hearingId + '-comment-added', increase);
        $rootScope.$on('hearing-' + scope.hearingId + '-comment-unhidden', increase);
        $rootScope.$on('hearing-' + scope.hearingId + '-comment-hidden', decrease);
      }
    };
  });
})();
