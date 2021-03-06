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

describe('Directive: commentAdderDirective', function () {

  beforeEach(module('kuulemmaApp', 'test-templates'));

  var element, scope, isolateScope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  describe('Element with only button text', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<div comment-adder button-text="Click me!" context-list="ctx-1:"></div>');
      element = $compile(element)(scope);
      scope.$digest();
      isolateScope = element.isolateScope();
    }));

    it('should put button text to scope', function () {
      expect(isolateScope.buttonText).toBe('Click me!');
    });
  });

  describe('Element without button text', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<div comment-adder context-list="ctx-1:"></div>');
      element = $compile(element)(scope);
      scope.$digest();
      isolateScope = element.isolateScope();
    }));

    it('should not fail, just set it to be undefined', function () {
      expect(isolateScope.buttonText).toBeUndefined();
    });
  });

  describe('Element with hearing id', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<div comment-adder hearing-id="1" context-list="ctx-1:"></div>');
      element = $compile(element)(scope);
      scope.$digest();
      isolateScope = element.isolateScope();
    }));

    it('should put hearing id to scope', function() {
      expect(isolateScope.hearingId).toBe('1');
    });
  });

  describe('Element with context-list', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<div comment-adder button-text="Click me!" context-list="ctx-1:This is context 1;ctx-2:This is context 2"></div>');
      element = $compile(element)(scope);
      scope.$digest();
      isolateScope = element.isolateScope();
    }));

    it('should put context list to scope', function () {
      expect(isolateScope.contextList).toBe('ctx-1:This is context 1;ctx-2:This is context 2');
    });
  });

  describe('Small comment adder', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<div comment-adder button-text="Click me!" size="small" context-list="ctx-1:This is context 1;ctx-2:This is context 2"></div>');
      element = $compile(element)(scope);
      scope.$digest();
    }));

    it('should add styling class to correct dom element', function() {
      expect(angular.element(element.children()[0]).hasClass('narrow')).toBe(true);
    });
  });
});
