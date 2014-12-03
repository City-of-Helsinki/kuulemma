'use strict';

describe('Controller: CommentListController', function () {

  beforeEach(module('kuulemmaApp'));

  var CommentListControllerCtrl,
    scope,
    $rootScope,
    CommentListService,
    $httpBackend,
    commentGetHandler,
    likeGetHandler,
    $controller,
    createController;

  beforeEach(inject(function ($injector) {
    $rootScope = $injector.get('$rootScope');
    $controller = $injector.get('$controller');

    CommentListService = $injector.get('CommentListService');
    spyOn(CommentListService, 'get').andCallThrough();

    $httpBackend = $injector.get('$httpBackend');
  }));

  describe('Logged in user', function() {
    beforeEach(function() {
      commentGetHandler = $httpBackend.expectGET('/hearings/1/links/comments?order_by=created_at&page=1&per_page=20').respond(200, { comments: [] });
      likeGetHandler = $httpBackend.expectGET('/users/2/links/likes').respond(200, { comments: [] });

      createController = function() {
        scope = $rootScope.$new();
        scope.userId = '2';
        scope.hearingId = '1';
        scope.scrollToCommentsTop = jasmine.createSpy();
        CommentListControllerCtrl = $controller('CommentListController', {
          $scope: scope
        });
        $httpBackend.flush();
      };
    });

    afterEach(function() {
      CommentListService.get.reset();
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should load comments', function() {
      createController();
      expect(CommentListService.get.callCount).toBe(1);
      expect(CommentListService.get).toHaveBeenCalledWith({hearingId: '1'});
    });

    describe('Loading likes successfully', function() {
      beforeEach(function() {
        likeGetHandler.respond({comments: [1, 2, 3]});
        createController();
      });

      it('should put loaded likes into scope', function() {
        expect(scope.userLikes).toEqual([ 1, 2, 3 ]);
      });
    });

    describe('Loading comments successfully', function() {
      beforeEach(function() {
        commentGetHandler.respond({comments: [ { text: 'mockComment' }, { text: 'Another mock comment' } ]});
        createController();
      });

      it('should put loaded comment into scope', function() {
        expect(scope.comments).toEqual([ { text : 'mockComment' }, { text : 'Another mock comment' } ]);
      });
    });

    describe('Loading comments unsuccessfully', function() {
      beforeEach(function() {
        commentGetHandler.respond(404);
        createController();
      });

      it('should not put any comment to scope', function() {
        expect(scope.comments).toBeUndefined();
      });
    });

    describe('Toggle like', function() {
      beforeEach(function() {
        spyOn(CommentListService, 'like').andCallThrough();
        spyOn(CommentListService, 'unlike').andCallThrough();
        commentGetHandler.respond(200, { comments: [{id: 1, like_count: 1}, {id: 5, like_count: 0}] });
        likeGetHandler.respond(200, { comments: [1, 2, 3] });
        createController();
      });

      afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
        CommentListService.like.reset();
        CommentListService.unlike.reset();
      });

      describe('Successful liking', function() {
        beforeEach(function() {
          $httpBackend.expectPOST('/users/2/links/likes', { comment_id: 5 }).respond(201);
        });

        it('should like the comment if not yet liked', function() {
          scope.toggleLike(5);
          expect(CommentListService.like.callCount).toBe(1);
          expect(CommentListService.unlike).not.toHaveBeenCalled();
          $httpBackend.flush();
        });

        it('should add the liking without waiting the server response', function() {
          scope.toggleLike(5);
          expect(scope.userLikes).toEqual([1, 2, 3, 5]);
          $httpBackend.flush();
        });

        it('should increase the like count', function() {
          scope.toggleLike(5);
          $httpBackend.flush();
          expect(_.findWhere(scope.comments, {id: 5}).like_count).toBe(1);
        });
      });

      describe('Failed liking', function() {
        beforeEach(function() {
          $httpBackend.expectPOST('/users/2/links/likes', { comment_id: 5 }).respond(400);
        });

        it('should remove the liking if server call fails', function() {
          scope.toggleLike(5);
          $httpBackend.flush();
          expect(scope.userLikes).toEqual([1, 2, 3]);
        });

        it('should not increase the like count', function() {
          scope.toggleLike(5);
          $httpBackend.flush();
          expect(_.findWhere(scope.comments, {id: 5}).like_count).toBe(0);
        });
      });

      describe('Successful unliking', function() {
        beforeEach(function() {
          $httpBackend.expectDELETE('/users/2/links/likes').respond(204);
        });

        it('should unlike the comment if already liked', function() {
          scope.toggleLike(1);
          expect(CommentListService.unlike.callCount).toBe(1);
          expect(CommentListService.like).not.toHaveBeenCalled();
          $httpBackend.flush();
        });

        it('should remove the liking without waiting the server response', function() {
          scope.toggleLike(1);
          expect(scope.userLikes).toEqual([2, 3]);
          $httpBackend.flush();
        });

        it('should decrease the like count', function() {
          scope.toggleLike(1);
          $httpBackend.flush();
          expect(_.findWhere(scope.comments, {id: 1}).like_count).toBe(0);
        });
      });

      describe('Failed unlinking', function() {
        beforeEach(function() {
          $httpBackend.expectDELETE('/users/2/links/likes').respond(400);
        });

        it('should put the liking back if server call fails', function() {
          scope.toggleLike(1);
          $httpBackend.flush();
          expect(scope.userLikes).toEqual([2, 3, 1]);
        });

        it('should not decrease the like count', function() {
          scope.toggleLike(1);
          $httpBackend.flush();
          expect(_.findWhere(scope.comments, {id: 1}).like_count).toBe(1);
        });
      });
    });
  });

  describe('User without login', function() {
    beforeEach(function() {
      commentGetHandler = $httpBackend.expectGET('/hearings/1/links/comments?order_by=created_at&page=1&per_page=20').respond(200, { comments: [] });

      createController = function() {
        scope = $rootScope.$new();
        scope.userId = undefined;
        scope.hearingId = '1';
        scope.scrollToCommentsTop = jasmine.createSpy();
        CommentListControllerCtrl = $controller('CommentListController', {
          $scope: scope
        });
        $httpBackend.flush();
      };
      createController();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should set an empty array as userLikes', function() {
      expect(scope.userLikes).toEqual([]);
    });

    it('should do nothing when like button is clicked', function() {
      spyOn(_, 'findWhere');
      scope.toggleLike(1);
      expect(_.findWhere).not.toHaveBeenCalled();
    });
  });

  describe('New comment added', function() {
    beforeEach(function() {
      commentGetHandler = $httpBackend.expectGET('/hearings/1/links/comments?order_by=created_at&page=1&per_page=20').respond(200, { comments: [] });

      createController = function() {
        scope = $rootScope.$new();
        scope.userId = undefined;
        scope.hearingId = '1';
        scope.scrollToCommentsTop = jasmine.createSpy();
        CommentListControllerCtrl = $controller('CommentListController', {
          $scope: scope
        });
        $httpBackend.flush();
      };
      createController();
    });

    afterEach(function() {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should add the new comment to comments ordered by created_at', inject(function($timeout) {
      var newComment = {id: 20};
      scope.orderBy = 'created_at'
      $rootScope.$broadcast('hearing-' + scope.hearingId + '-comment-added', newComment);
      $timeout.flush()
      expect(_.pluck(scope.comments, 'id')).toContain(newComment.id);
    }));

    it('should not add the new comment to comments ordered by like_count', inject(function($timeout) {
      var newComment = {id: 20};
      scope.orderBy = 'like_count'
      $rootScope.$broadcast('hearing-' + scope.hearingId + '-comment-added', newComment);
      $timeout.flush()
      expect(_.pluck(scope.comments, 'id')).not.toContain(newComment.id);
    }));
  });
});
