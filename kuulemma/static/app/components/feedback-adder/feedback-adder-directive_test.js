'use strict';

describe('Directive: feedbackAdderDirective', function () {

  beforeEach(module('kuulemmaApp'));

  var element, scope, isolateScope;

  beforeEach(inject(function ($rootScope, $templateCache) {
    $templateCache.put('/static/dist/partials/components/feedback-adder/feedback-adder.html', '<div></div>');
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
