'use strict';

describe('Controller: CommentListController', function () {

  beforeEach(module('kuulemmaApp'));

  var CommentListControllerCtrl,
    scope,
    $rootScope,
    CommentListService,
    $httpBackend,
    getHandler,
    createController;

  beforeEach(inject(function ($injector) {
    $rootScope = $injector.get('$rootScope');
    var $controller = $injector.get('$controller');

    CommentListService = $injector.get('CommentListService');
    spyOn(CommentListService, 'get').andCallThrough();

    $httpBackend = $injector.get('$httpBackend');
    getHandler = $httpBackend.expectGET('/hearings/1/links/comments').respond(200, { comments: [] });

    createController = function() {
      scope = $rootScope.$new();
      CommentListControllerCtrl = $controller('CommentListController', {
        $scope: scope,
        $attrs: { hearingId: 1 }
      });
      $httpBackend.flush();
    };

  }));

  afterEach(function() {
    CommentListService.get.reset();
    $httpBackend.verifyNoOutstandingExpectation();
    $httpBackend.verifyNoOutstandingRequest();
  });

  it('should load comments', function() {
    createController();
    expect(CommentListService.get.callCount).toBe(1);
    expect(CommentListService.get).toHaveBeenCalledWith(1);
  });

  describe('Loading comments successfully', function() {
    beforeEach(function() {
      getHandler.respond({comments: [ { text: 'mockComment' }, { text: 'Another mock comment' } ]});
      createController();
    });

    it('should put loaded comment into scope', function() {
      expect(scope.comments).toEqual([ { text : 'mockComment' }, { text : 'Another mock comment' } ]);
    });
  });

  describe('Loading comments unsuccessfully', function() {
    beforeEach(function() {
      getHandler.respond(404);
      createController();
    });

    it('should not put any comment to scope', function() {
      expect(scope.comments).toBeUndefined();
    });
  });

  describe('Sorting comments', function() {
    beforeEach(function() {
      getHandler.respond({
        comments: [
        {
          id: 1,
          like_count: 5,
          created_at: '2014-03-11T12:47:35+00:00'
        },
        {
          id: 2,
          like_count: 7,
          created_at: '2014-01-11T12:47:35+00:00'
        },
        {
          id: 3,
          like_count: 0,
          created_at: '2014-02-11T12:47:35+00:00'
        }
      ]});
      createController();
    });

    describe('Latest comments', function() {
      it('should sort comments by date automatically', function() {
        expect(_.pluck(scope.latestComments, 'id')).toEqual([1, 3, 2]);
      });

      it('should put the just added comment to be the latest', function() {
        $rootScope.$broadcast('hearing-1-comment-added', {id: 4});
        expect(_.pluck(scope.latestComments, 'id')).toEqual([4, 1, 3, 2]);
      });
    });

    describe('Popular comments', function() {
      it('should sort comments by popularity automatically', function() {
        expect(_.pluck(scope.popularComments, 'id')).toEqual([2, 1, 3]);
      });

      it('should put the just added comment to be the least popular', function() {
        $rootScope.$broadcast('hearing-1-comment-added', {id: 4});
        expect(_.pluck(scope.popularComments, 'id')).toEqual([2, 1, 3, 4]);
      });
    });
  });
});
