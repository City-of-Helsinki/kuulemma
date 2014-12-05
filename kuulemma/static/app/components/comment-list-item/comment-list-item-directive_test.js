'use strict';

describe('Directive: commentListItemDirective', function () {

  beforeEach(module('kuulemmaApp'));

  beforeEach(module(
    'kuulemma/static/app/components/comment-list-item/comment-list-item.html',
    'kuulemma/static/app/components/comment-adder/comment-adder.html'
  ));

  var element, scope, isolateScope, $httpBackend, CommentListService;

  beforeEach(inject(function ($rootScope, $templateCache, $compile, _$httpBackend_, _CommentListService_) {
    var commentListItemTemplate = $templateCache.get('kuulemma/static/app/components/comment-list-item/comment-list-item.html');
    var commentAdderTemplate = $templateCache.get('kuulemma/static/app/components/comment-adder/comment-adder.html');

    $templateCache.put('/static/dist/partials/components/comment-list-item/comment-list-item.html', commentListItemTemplate);
    $templateCache.put('/static/dist/partials/components/comment-adder/comment-adder.html', commentAdderTemplate);
    scope = $rootScope.$new();
    scope.$parent.comment = {body: 'comment', title: 'title', username: 'username', is_hidden: false, parent_preview: '', id: 1};
    $httpBackend = _$httpBackend_;
    CommentListService = _CommentListService_;

    element = angular.element('<div comment-list-item comment="comment" hearing-id="2"></div>');
    element = $compile(element)(scope);
    scope.$digest();
    isolateScope = element.isolateScope();
  }));

  it('should pass hearing id to controller', function () {
    expect(isolateScope.hearingId).toBe('2');
  });

  describe('Editing comments', function() {
    var requestHandler;
    beforeEach(function() {
      spyOn(CommentListService, 'editComment').andCallThrough();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    describe('Saving comments successfully', function() {
      beforeEach(function() {
        $httpBackend.expectPUT('/hearings/2/links/comments/1', {
          title: 'title',
          body: 'comment',
          username: 'username',
          is_hidden: false
        }).respond(201);
        isolateScope.saveChanges();
        $httpBackend.flush();
      });

      it('should make a put requests via CommentListService', function() {
        expect(CommentListService.editComment.callCount).toBe(1);
        expect(CommentListService.editComment).toHaveBeenCalledWith({
          hearingId: '2',
          comment: {
            body: 'comment',
            title: 'title',
            username: 'username',
            is_hidden: false,
            parent_preview: '',
            id: 1
          }
        });
      });
    });

    describe('Saving comments failing', function() {
      beforeEach(function() {
        $httpBackend.expectPUT('/hearings/2/links/comments/1', {title: 'title',
          body: 'edited comment',
          username: 'username',
          is_hidden: false
        }).respond(400);
        scope.$parent.comment.body = 'edited comment';
        isolateScope.saveChanges();
        $httpBackend.flush();
      });
      it('should revert changes if saving fails', function() {
        expect(scope.$parent.comment.body).toBe('comment');
      });
    });
  });
});
