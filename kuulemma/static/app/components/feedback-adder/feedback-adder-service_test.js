'use strict';

describe('Service: FeedbackService', function () {

  beforeEach(module('kuulemmaApp'));

  var FeedbackService, $httpBackend, $http;
  beforeEach(inject(function (_FeedbackService_, _$httpBackend_, _$http_) {
    FeedbackService = _FeedbackService_;
    $httpBackend = _$httpBackend_;
    $http = _$http_;
    spyOn($http, 'post');
  }));

  afterEach(function() {
    $http.post.reset();
  });

  describe('Saving feedback', function() {
    beforeEach(function() {
      FeedbackService.save({
        content: 'My Feedback!',
      });
    });

    it('should make a post request with content in data', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/feedback', {
        content : 'My Feedback!',
      });
    });
  });
});
