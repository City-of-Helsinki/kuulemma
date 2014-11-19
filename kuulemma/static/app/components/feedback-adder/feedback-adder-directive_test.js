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

describe('Directive: feedbackAdderDirective', function () {

  beforeEach(module('kuulemmaApp', 'test-templates'));

  var element, scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  describe('Big feedback adder', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<div feedback-adder size="big"></div>');
      element = $compile(element)(scope);
      scope.$digest();
    }));

    it('should add styling class to correct dom element', function() {
      expect(element.hasClass('big')).toBe(true);
    });
  });
});
