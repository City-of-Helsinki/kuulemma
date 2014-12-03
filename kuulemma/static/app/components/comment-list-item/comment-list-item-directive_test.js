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
});
