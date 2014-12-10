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

describe('Directive: feedbackLinkDirective', function () {

  beforeEach(module('kuulemmaApp'));

  var element, scope, isolateScope;

  beforeEach(inject(function ($rootScope, $templateCache) {
    scope = $rootScope.$new();
  }));

  describe('Simple a element', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<a feedback-link href="#"></a>');
      element = $compile(element)(scope);
      scope.$digest();
    }));

    it('should broadcast a correct event after clicking', inject(function($rootScope) {
      spyOn($rootScope, '$broadcast');
      element.click();
      expect($rootScope.$broadcast.callCount).toBe(1);
      expect($rootScope.$broadcast).toHaveBeenCalledWith('open-feedback-box');
    }));
  });
});
