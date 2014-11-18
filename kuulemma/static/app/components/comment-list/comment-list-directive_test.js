'use strict';

describe('Directive: commentListDirective', function () {

  beforeEach(module('kuulemmaApp'));

  beforeEach(module('kuulemma/static/app/components/comment-list/comment-list.html', 'kuulemma/static/app/components/comment-list-item/comment-list-item.html'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope, $templateCache, $compile, $httpBackend) {
    var commentListTemplate = $templateCache.get('kuulemma/static/app/components/comment-list/comment-list.html');
    var commentListItemTemplate = $templateCache.get('kuulemma/static/app/components/comment-list-item/comment-list-item.html');

    $templateCache.put('/static/dist/partials/components/comment-list/comment-list.html', commentListTemplate);
    $templateCache.put('/static/dist/partials/components/comment-list-item/comment-list-item.html', commentListItemTemplate);

    $httpBackend.expectGET('/hearings/1/links/comments').respond({comments: [{
      id: '5', title: 'Comment title', username: 'test-user', body: 'Hello there!', created_at: '2014-12-12' }]});

    scope = $rootScope.$new();

    element = angular.element('<div hearing-id="1" comment-list></div>');
    element = $compile(element)(scope);
    scope.$digest();
    $httpBackend.flush();
  }));

  it('should pass hearing id to controller', function () {
    expect(scope.hearingId).toBe('1');
  });

  it('should render comments', function() {
    expect(angular.toJson(scope.comments))
      .toEqual(angular.toJson([ { id : '5', title : 'Comment title', username : 'test-user', body : 'Hello there!', created_at : '2014-12-12' } ]));
  });
});
