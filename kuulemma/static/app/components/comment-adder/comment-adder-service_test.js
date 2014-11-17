'use strict';

describe('Service: CommentService', function () {

  beforeEach(module('kuulemmaApp'));

  var CommentService, $httpBackend, $http;
  beforeEach(inject(function (_CommentService_, _$httpBackend_, _$http_) {
    CommentService = _CommentService_;
    $httpBackend = _$httpBackend_;
    $http = _$http_;
    spyOn($http, 'post');
  }));

  afterEach(function() {
    $http.post.reset();
  });

  describe('Saving comment without email', function() {
    beforeEach(function() {
      CommentService.save(1, {
        title: 'test subject',
        body: 'Comment',
        follow: false,
        email: 'email@email.com',
        commentsOn: {
          key: 'hearing-1',
          label: 'Kuuleminen'
        }
      });
    });

    it('should make a post request without email', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        title : 'test subject',
        body : 'Comment',
        object_type: 'hearing',
        object_id: 1
      });
    });
  });

  describe('Saving comment with email', function() {
    beforeEach(function() {
      CommentService.save(1, {
        title: 'test subject',
        body: 'Comment',
        follow: true,
        email: 'email@email.com',
        commentsOn: {
          key: 'hearing-1',
          label: 'Kuuleminen'
        }
      });
    });

    it('should make a post request without email', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        title : 'test subject',
        body : 'Comment',
        email: 'email@email.com',
        object_type: 'hearing',
        object_id: 1
      });
    });
  });

  describe('Formatting commentsOn paramater name', function() {
    beforeEach(function() {
      CommentService.save(1, {
        commentsOn: {
          key: 'image-123',
          label: 'Kuvaan 123'
        }
      });
    });

    it('should change it from camelcase to dashed one before saving', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        object_type: 'image',
        object_id: 123
      });
    });
  });
});
