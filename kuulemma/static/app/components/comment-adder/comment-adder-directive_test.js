'use strict';

describe('Directive: commentAdderDirective', function () {

  beforeEach(module('kuulemmaApp'));

  var element, scope, isolateScope;

  beforeEach(inject(function ($rootScope, $templateCache) {
    $templateCache.put('/static/dist/partials/components/comment-adder/comment-adder.html', '<div></div>');
    scope = $rootScope.$new();
  }));
  
  describe('Element with only button text', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<div comment-adder button-text="Click me!"></div>');
      element = $compile(element)(scope);
      scope.$digest();
      isolateScope = element.isolateScope();
    }));

    it('should put button text to scope', function () {
      expect(isolateScope.buttonText).toBe('Click me!');
    });
  });

  describe('Element with initial context', function() {
    beforeEach(inject(function($compile) {
      element = angular.element(
        '<div comment-adder button-text="Click me!" initial-context="test context"></div>');
      element = $compile(element)(scope);
      scope.$digest();
      isolateScope = element.isolateScope();
    }));
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
});
