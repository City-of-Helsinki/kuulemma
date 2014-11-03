'use strict';

describe('Controller: AddCommentController', function () {

  beforeEach(module('kuulemmaApp'));

  var AddCommentControllerCtrl, scope, CommentService, $q;

  beforeEach(inject(function ($controller, $rootScope, _CommentService_, _$q_) {
    scope = $rootScope.$new();
    AddCommentControllerCtrl = $controller('AddCommentController', {
      $scope: scope
    });
    CommentService = _CommentService_;
    $q = _$q_;
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
    var successSpy = jasmine.createSpy('success spy');
    beforeEach(function() {
      spyOn(CommentService, 'save').andReturn({ success: successSpy });
      scope.hearingId = '1';
      scope.saveComment();
    });

    afterEach(function() {
      successSpy.reset();
      CommentService.save.reset();
    });

    it('should call comment service\'s save function', function() {
      expect(CommentService.save.callCount).toBe(1);

      var initialValues =   { title : '', username : '', commentsOn : { label: 'Yleisesti tähän kuulemiseen', id: 'SOME_ID' }, body : '', follow : false, email : '' };
      expect(CommentService.save).toHaveBeenCalledWith('1', initialValues);
    });
  });
});