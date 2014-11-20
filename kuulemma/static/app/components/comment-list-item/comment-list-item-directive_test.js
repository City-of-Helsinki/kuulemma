'use strict';

describe('Directive: commentListItemDirective', function () {

  beforeEach(module('kuulemmaApp'));

  beforeEach(module(
    'kuulemma/static/app/components/comment-list-item/comment-list-item.html',
    'kuulemma/static/app/components/comment-adder/comment-adder.html'
  ));

  var element, scope, isolateScope;

  beforeEach(inject(function ($rootScope, $templateCache, $compile, $httpBackend) {
    var commentListItemTemplate = $templateCache.get('kuulemma/static/app/components/comment-list-item/comment-list-item.html');
    var commentAdderTemplate = $templateCache.get('kuulemma/static/app/components/comment-adder/comment-adder.html');

    $templateCache.put('/static/dist/partials/components/comment-list-item/comment-list-item.html', commentListItemTemplate);
    $templateCache.put('/static/dist/partials/components/comment-adder/comment-adder.html', commentAdderTemplate);
    scope = $rootScope.$new();
    scope.$parent.comment = {body: 'comment', parent_preview: ''};

    element = angular.element('<div comment-list-item comment="comment" hearing-id="2"></div>');
    element = $compile(element)(scope);
    scope.$digest();
    isolateScope = element.isolateScope();
  }));

  it('should pass hearing id to controller', function () {
    expect(isolateScope.hearingId).toBe('2');
  });

  describe('Comment paragraphs', function() {
    var updateElement;
    beforeEach(inject(function($compile) {
      updateElement = function() {
        element = $compile(element)(scope);
        scope.$digest();
        isolateScope = element.isolateScope();
      };
    }));

    describe('One line comment', function() {
      it('should create paragraphs array with only one item', function() {
        expect(isolateScope.paragraphs).toEqual(['comment']);
        expect(isolateScope.previewParagraphs).toEqual([]);
        expect(element.find('.body p').length).toBe(1);
        expect(element.find('.parent-preview p').length).toBe(0);
      });
    });

    describe('Two line simple comment', function() {
      beforeEach(function() {
        var comment = 'line 1\nline 2';
        scope.$parent.comment = {body: comment, parent_preview: comment};
        updateElement();
      });

      it('should create paragraphs array with two items', function() {
        expect(isolateScope.paragraphs).toEqual(['line 1', 'line 2']);
        expect(isolateScope.previewParagraphs).toEqual(['line 1', 'line 2']);
        expect(element.find('.body p').length).toBe(2);
        expect(element.find('.parent-preview p').length).toBe(2);
      });
    });

    describe('Multiline random structure comment', function() {
      beforeEach(function() {
        var comment = 'line 1\n\nline 3\nline 4\n\n\n\n\nline 5';
        scope.$parent.comment = {body: comment, parent_preview: comment};
        updateElement();
      });

      it('should create four lines in comment box', function() {
        expect(isolateScope.paragraphs).toEqual(['line 1', 'line 3', 'line 4', 'line 5']);
        expect(isolateScope.previewParagraphs).toEqual(['line 1', 'line 3', 'line 4', 'line 5']);
        expect(element.find('.body p').length).toBe(4);
        expect(element.find('.parent-preview p').length).toBe(4);
      });
    });
  });
});
