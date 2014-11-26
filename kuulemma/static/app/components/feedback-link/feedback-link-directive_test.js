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

    iit('should broadcast a correct event after clicking', inject(function($rootScope) {
      spyOn($rootScope, '$broadcast');
      element.click();
      expect($rootScope.$broadcast.callCount).toBe(1);
      expect($rootScope.$broadcast).toHaveBeenCalledWith('open-feedback-box');
    }));
  });
});
