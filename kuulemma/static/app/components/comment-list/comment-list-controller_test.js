/* Kuulemma
 * Copyright (C) 2014, Fast Monkeys Oy
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
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

    describe('Fetching more successfully', function() {
      beforeEach(function() {
        createController();
        var newComments = [{id: 90}, {id: 91}, {id: 92}];
        $httpBackend.expectGET('/hearings/1/links/comments?order_by=created_at&page=2&per_page=20').respond(200, { comments: newComments });
      });

      it('should add the fetched comments to the end of the comments list', function() {
        scope.comments = [{id: 1}, {id: 2}];
        scope.fetchMore();
        $httpBackend.flush();
        expect(_.pluck(scope.comments, 'id')).toEqual([1, 2, 90, 91, 92]);
      });

      it('should set commentsStillLeft to false if less comments were returned than was asked', function() {
        scope.commentsStillLeft = true;
        scope.fetchMore();
        $httpBackend.flush();
        expect(scope.commentsStillLeft).toBeFalsy();
      });

      it('should not set commentsStillLeft to false if returned the asked amount of comments', function() {
        scope.commentsStillLeft = true;
        scope.per_page = 3;
        scope.fetchMore();
        $httpBackend.flush();
        expect(scope.commentsStillLeft).toBeTruthy();
      });
    });

    describe('Fetching more unsuccessfully', function() {
      beforeEach(function() {
        createController();
        $httpBackend.expectGET('/hearings/1/links/comments?order_by=created_at&page=2&per_page=20').respond(404);
      });

      it('should set commentsStillLeft to false', function() {
        scope.commentsStillLeft = true;
        scope.fetchMore();
        $httpBackend.flush();
        expect(scope.commentsStillLeft).toBeFalsy();
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
