'use strict';

describe('Controller: AddFeedbackController', function () {

  beforeEach(module('kuulemmaApp'));

  var AddFeedbackControllerCtrl, scope, FeedbackService, $q, $httpBackend;

  beforeEach(inject(function ($controller, $rootScope, _FeedbackService_, _$q_, _$httpBackend_) {
    scope = $rootScope.$new();
    AddFeedbackControllerCtrl = $controller('AddFeedbackController', {
      $scope: scope
    });
    FeedbackService = _FeedbackService_;
    $q = _$q_;
    $httpBackend = _$httpBackend_;
  }));

  describe('Opening and closing feedback box', function() {
    it('should be initially closed', function() {
      expect(scope.feedbackBoxOpen).toBeUndefined();
    });

    it('should open feedback box', function() {
      scope.openFeedbackBox();
      expect(scope.feedbackBoxOpen).toBe(true);
    });

    it('should close feedback box', function() {
      scope.closeFeedbackBox();
      expect(scope.feedbackBoxOpen).toBe(false);
    });
  });

  describe('Form', function() {
    it('should be an object', function() {
      expect(angular.isObject(scope.form)).toBe(true);
    });

    it('should have content as empty initially', function() {
      expect(scope.form.content).toBe('');
    });
  });

  describe('Saving feedback', function() {
    var initialValues = {
      content : 'My Feedback!'
    };

    beforeEach(function() {
      scope.form = initialValues;
      $httpBackend.expectPOST('/feedback', {
        content: initialValues.content,
      }).respond(201, {
        feedbacks:
        {
          id: 1,
          content: initialValues.content,
        }
      });
      spyOn(FeedbackService, 'save').andCallThrough();
      scope.saveFeedback();
    });

    afterEach(function() {
      FeedbackService.save.reset();
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should call feedback service\'s save function', function() {
      expect(FeedbackService.save.callCount).toBe(1);
      expect(FeedbackService.save).toHaveBeenCalledWith(initialValues);
      $httpBackend.flush();
    });

    it('should broadcast a correct event after successfully added feedback', inject(function($rootScope) {
      spyOn($rootScope, '$broadcast');
      $httpBackend.flush();
      expect($rootScope.$broadcast.callCount).toBe(1);
      expect($rootScope.$broadcast).toHaveBeenCalledWith('feedback-added', {
        id: 1,
        content: initialValues.content,
      });
    }));
  });
});
