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

describe('Service: CommentListService', function () {

  var expectToBePromise = function(value) {
    expect(angular.isFunction(value.then)).toBe(true);
    expect(angular.isFunction(value.catch)).toBe(true);
    expect(angular.isFunction(value.finally)).toBe(true);
  };

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
      getHandler = $httpBackend.expectGET('/hearings/1/links/comments?order_by=created_at&page=1&per_page=20').respond(200);
      returnValue = service.get({hearingId: 1});
      $httpBackend.flush();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a get request to correct api endpoint', function() {
      expect($http.get.callCount).toBe(1);
      expect($http.get).toHaveBeenCalledWith(
        '/hearings/1/links/comments',
        {
          params: {
            order_by: 'created_at',
            page: 1,
            per_page: 20
          },
          method: 'get',
          url: '/hearings/1/links/comments'
        }
      );
    });

    it('should return promise', function() {
      expectToBePromise(returnValue);
    });
  });

  describe('Like function', function() {
    var likeHandler, returnValue;
    beforeEach(function() {
      spyOn($http, 'post').andCallThrough();
      likeHandler = $httpBackend.expectPOST('/users/1/links/likes').respond(201);
      returnValue = service.like({ userId: 1, commentId: 1 });
      $httpBackend.flush();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a post request to correct api endpoint', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/users/1/links/likes', { comment_id: 1 });
    });

    it('should return promise', function() {
      expectToBePromise(returnValue);
    });
  });

  describe('Unlike function', function() {
    var likeHandler, returnValue;
    beforeEach(function() {
      spyOn($http, 'delete').andCallThrough();
      likeHandler = $httpBackend.expectDELETE('/users/1/links/likes').respond(200);
      returnValue = service.unlike({ userId: 1, commentId: 1 });
      $httpBackend.flush();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a post request to correct api endpoint', function() {
      expect($http.delete.callCount).toBe(1);
      expect($http.delete).toHaveBeenCalledWith('/users/1/links/likes', { data: { comment_id: 1 }, method: 'delete', url: '/users/1/links/likes' });
    });

    it('should return promise', function() {
      expectToBePromise(returnValue);
    });
  });

  describe('Get user likes function', function() {
    var getHandler, returnValue;
    beforeEach(function() {
      spyOn($http, 'get').andCallThrough();
      getHandler = $httpBackend.expectGET('/users/1/links/likes').respond(200);
      returnValue = service.getUserLikes(1);
      $httpBackend.flush();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a post request to correct api endpoint', function() {
      expect($http.get.callCount).toBe(1);
      expect($http.get).toHaveBeenCalledWith('/users/1/links/likes');
    });

    it('should return promise', function() {
      expectToBePromise(returnValue);
    });
  });

  describe('Hiding comments', function() {
    var putHandler, returnValue, testData;
    beforeEach(function() {
      testData = {
        comment: {
          id: 2,
          body: 'Hello!',
          title: 'Title',
          username: 'tester',
          is_hidden: true
        },
        hearingId: 1
      };
      spyOn($http, 'put').andCallThrough();
      putHandler = $httpBackend.expectPUT('/hearings/1/links/comments/2').respond(200);
      returnValue = service.hideComment(testData);
      $httpBackend.flush();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a put request to correct api endpoint', function() {
      expect($http.put.callCount).toBe(1);
      expect($http.put).toHaveBeenCalledWith('/hearings/1/links/comments/2', {body: 'Hello!', title: 'Title', username: 'tester', is_hidden: true});
    });

    it('should return promise', function() {
      expectToBePromise(returnValue);
    });
  });

  describe('Unhiding comments', function() {
    var putHandler, returnValue, testData;
    beforeEach(function() {
      testData = {
        comment: {
          id: 2,
          body: 'Hello!',
          title: 'Title',
          username: 'tester',
          is_hidden: false
        },
        hearingId: 1
      };
      spyOn($http, 'put').andCallThrough();
      putHandler = $httpBackend.expectPUT('/hearings/1/links/comments/2').respond(200);
      returnValue = service.unhideComment(testData);
      $httpBackend.flush();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a put request to correct api endpoint', function() {
      expect($http.put.callCount).toBe(1);
      expect($http.put).toHaveBeenCalledWith('/hearings/1/links/comments/2', { is_hidden : false, body : 'Hello!', title : 'Title', username : 'tester' });
    });

    it('should return promise', function() {
      expectToBePromise(returnValue);
    });
  });

  describe('Editing comments', function() {
    var putHandler, returnValue, testData;
    beforeEach(function() {
      testData = {
        comment: {
          id: 2,
          body: 'Hello!',
          title: 'Title',
          username: 'tester',
          is_hidden: false
        },
        hearingId: 1
      };
      spyOn($http, 'put').andCallThrough();
      putHandler = $httpBackend.expectPUT('/hearings/1/links/comments/2').respond(200);
      returnValue = service.editComment(testData);
      $httpBackend.flush();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a put request to correct api endpoint', function() {
      expect($http.put.callCount).toBe(1);
      expect($http.put).toHaveBeenCalledWith('/hearings/1/links/comments/2', { is_hidden : false, body : 'Hello!', title : 'Title', username : 'tester' });
    });

    it('should return promise', function() {
      expectToBePromise(returnValue);
    });
  });
});
