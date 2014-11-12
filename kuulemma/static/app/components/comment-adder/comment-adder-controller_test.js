'use strict';

describe('Controller: AddCommentController', function () {

  beforeEach(module('kuulemmaApp'));

  var AddCommentControllerCtrl, scope, CommentService, $q, $httpBackend;

  beforeEach(inject(function ($controller, $rootScope, _CommentService_, _$q_, _$httpBackend_) {
    scope = $rootScope.$new();
    AddCommentControllerCtrl = $controller('AddCommentController', {
      $scope: scope
    });
    CommentService = _CommentService_;
    $q = _$q_;
    $httpBackend = _$httpBackend_;
  }));

  describe('Opening and closing comment box', function() {
    it('should be initially closed', function() {
      expect(scope.commentBoxOpen).toBeUndefined();
    });

    it('should open comment box', function() {
      scope.openCommentBox();
      expect(scope.commentBoxOpen).toBe(true);
    });

    it('should close comment box', function() {
      scope.closeCommentBox();
      expect(scope.commentBoxOpen).toBe(false);
    });
  });

  describe('Form', function() {
    it('should be an object', function() {
      expect(angular.isObject(scope.form)).toBe(true);
    });

    it('should have title as empty initially', function() {
      expect(scope.form.title).toBe('');
    });
    
    it('should have username as empty initially', function() {
      expect(scope.form.username).toBe('');
    });

    it('should have the comment body as empty initially', function() {
      expect(scope.form.body).toBe('');
    });
    
    it('should should have context as empty initially', function() {
      expect(scope.form.commentsOn).toEqual({ label: 'Yleisesti tähän kuulemiseen', id: 'SOME_ID' });
    });

    it('should have follow options as false initially', function() {
      expect(scope.form.follow).toBe(false);
    });

    it('should have email as empty initially', function() {
      expect(scope.form.email).toBe('');
    });
  });

  describe('Saving comment', function() {
    var initialValues = {
      title : 'Title',
      username : 'user',
      commentsOn : { label: 'Yleisesti tähän kuulemiseen', id: 'SOME_ID' },
      body : 'Hello there!',
      follow : false,
      email : ''
    };

    beforeEach(function() {
      scope.form = initialValues;
      $httpBackend.expectPOST('/hearings/1/links/comments', {
        title: 'Title',
        username: 'user',
        comments_on: 'SOME_ID',
        body: 'Hello there!'
      }).respond(201, {
        comments:
        {
          title: 'Title',
          username: 'user',
          created_at: 'mock-date',
          id: '1',
          like_count: 0,
          body: 'Hello there!'
        }
      });
      spyOn(CommentService, 'save').andCallThrough();
      scope.hearingId = '1';
      scope.saveComment();
    });

    afterEach(function() {
      CommentService.save.reset();
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should call comment service\'s save function', function() {
      expect(CommentService.save.callCount).toBe(1);
      expect(CommentService.save).toHaveBeenCalledWith('1', initialValues);
      $httpBackend.flush();
    });

    it('should broadcast a correct event after successfully added comment', inject(function($rootScope) {
      spyOn($rootScope, '$broadcast');
      $httpBackend.flush();
      expect($rootScope.$broadcast.callCount).toBe(1);
      expect($rootScope.$broadcast).toHaveBeenCalledWith('hearing-1-comment-added', {
        title: 'Title',
        username: 'user',
        created_at: 'mock-date',
        id: '1',
        like_count: 0,
        body: 'Hello there!'
      });
    }));
  });
});