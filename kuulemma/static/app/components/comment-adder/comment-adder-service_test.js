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
        commentsOn: { id: 'some_id' }
      });
    });

    it('should make a post request without email', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        title : 'test subject',
        body : 'Comment',
        comments_on: 'some_id'
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
        commentsOn: { id: 'some_id' }
      });
    });

    it('should make a post request without email', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        title : 'test subject',
        body : 'Comment',
        email: 'email@email.com',
        comments_on: 'some_id'
      });
    });
  });

  describe('Formatting commentsOn paramater name', function() {
    beforeEach(function() {
      CommentService.save(1, {
        commentsOn: { label: 'Yleisesti tähän kommenttiin', id: '1' }
      });
    });

    it('should change it from camelcase to dashed one before saving', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        comments_on : '1'
      });
    });
  });
});
