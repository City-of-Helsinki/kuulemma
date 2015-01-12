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

describe('Directive: commentCounter', function () {

  beforeEach(module('kuulemmaApp'));

  var element, scope, isolateScope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  beforeEach(inject(function($compile) {
    element = angular.element(
      '<span comment-counter hearing-id="1" count="12"></span>');
    element = $compile(element)(scope);
    scope.$digest();
    isolateScope = element.isolateScope();
  }));

  it('should put hearing id to scope', function () {
    expect(isolateScope.hearingId).toBe('1');
  });

  it('should put count to scope', function () {
    expect(isolateScope.count).toBe('12');
  });

  it('should set the element text to count', function () {
    expect($(element).text()).toBe('12');
  });

  describe('adding a comment', function () {
    beforeEach(inject(function ($rootScope) {
      $rootScope.$broadcast('hearing-1-comment-added');
    }));

    it('should increase the element count with one', function () {
      expect($(element).text()).toBe('13');
    });
  });

  describe('hiding a comment', function () {
    beforeEach(inject(function ($rootScope) {
      $rootScope.$broadcast('hearing-1-comment-hidden');
    }));

    it('should decrease the element count with one', function () {
      expect($(element).text()).toBe('11');
    });
  });

  describe('unhiding a comment', function () {
    beforeEach(inject(function ($rootScope) {
      $rootScope.$broadcast('hearing-1-comment-unhidden');
    }));

    it('should increase the element count with one', function () {
      expect($(element).text()).toBe('13');
    });
  });

});
