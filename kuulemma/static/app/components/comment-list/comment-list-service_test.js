'use strict';

describe('Service: CommentListService', function () {

  beforeEach(module('kuulemmaApp'));

  var service, $http, $httpBackend;
  beforeEach(inject(function (_CommentListService_, _$httpBackend_, _$http_) {
    service = _CommentListService_;
    $http = _$http_;
    $httpBackend = _$httpBackend_;
  }));
  
  describe('Functions', function() {
    it('should have function get', function() {
      expect(angular.isFunction(service.get)).toBe(true);
    });
  });

  describe('Get function', function() {
    var getHandler, returnValue;
    beforeEach(function() {
      spyOn($http, 'get').andCallThrough();
      getHandler = $httpBackend.expectGET('/hearings/1/links/comments').respond(200);
      returnValue = service.get(1);
      $httpBackend.flush();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a get request to correct api endpoint', function() {
      expect($http.get.callCount).toBe(1);
      expect($http.get).toHaveBeenCalledWith('/hearings/1/links/comments');
    });

    it('should return promise', function() {
      expect(angular.isFunction(returnValue.then)).toBe(true);
      expect(angular.isFunction(returnValue.catch)).toBe(true);
      expect(angular.isFunction(returnValue.finally)).toBe(true);
    });
  });
});
