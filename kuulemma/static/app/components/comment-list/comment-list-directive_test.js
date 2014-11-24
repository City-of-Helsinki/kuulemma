'use strict';

describe('Directive: commentListDirective', function () {

  beforeEach(module('kuulemmaApp'));

  beforeEach(module(
    'kuulemma/static/app/components/comment-list/comment-list.html',
    'kuulemma/static/app/components/comment-list-item/comment-list-item.html',
    'kuulemma/static/app/components/comment-adder/comment-adder.html'
  ));

  var element,
    scope;

  beforeEach(inject(function ($rootScope, $templateCache, $compile, $httpBackend) {
    var commentListTemplate = $templateCache.get('kuulemma/static/app/components/comment-list/comment-list.html');
    var commentListItemTemplate = $templateCache.get('kuulemma/static/app/components/comment-list-item/comment-list-item.html');
    var commentAdderTemplate = $templateCache.get('kuulemma/static/app/components/comment-adder/comment-adder.html');

    $templateCache.put('/static/dist/partials/components/comment-list/comment-list.html', commentListTemplate);
    $templateCache.put('/static/dist/partials/components/comment-list-item/comment-list-item.html', commentListItemTemplate);
    $templateCache.put('/static/dist/partials/components/comment-adder/comment-adder.html', commentAdderTemplate);

    $httpBackend.expectGET('/hearings/1/links/comments').respond({comments: [{
      id: '5', title: 'Comment title', username: 'test-user', body: 'Hello there!', parent_preview: '', created_at: '2014-12-12' }]});

    $httpBackend.expectGET('/users/2/links/likes').respond({ likes: [] });

    scope = $rootScope.$new();

    element = angular.element('<div hearing-id="1" user-id="2" comment-list></div>');
    element = $compile(element)(scope);
    scope.$digest();
    $httpBackend.flush();
  }));

  it('should pass hearing id to controller', function () {
    expect(element.isolateScope().hearingId).toBe('1');
  });

  it('should pass user id to controller', function() {
    expect(element.isolateScope().userId).toBe('2');
  });

  it('should render comments', function() {
    expect(angular.toJson(element.isolateScope().comments))
      .toEqual(angular.toJson([ { id : '5', title : 'Comment title', username : 'test-user', body : 'Hello there!', parent_preview: '', created_at : '2014-12-12' } ]));
  });
});
