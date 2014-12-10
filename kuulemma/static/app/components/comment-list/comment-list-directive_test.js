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

describe('Directive: commentListDirective', function () {

  beforeEach(module('kuulemmaApp'));

  beforeEach(module(
    'kuulemma/static/app/components/comment-list/comment-list.html',
    'kuulemma/static/app/components/comment-list-item/comment-list-item.html',
    'kuulemma/static/app/components/comment-adder/comment-adder.html'
  ));

  var element,
    scope,
    createElement,
    createAdminElement,
    createOfficialElement;

  beforeEach(inject(function ($rootScope, $templateCache, $compile, $httpBackend) {
    var commentListTemplate = $templateCache.get('kuulemma/static/app/components/comment-list/comment-list.html');
    var commentListItemTemplate = $templateCache.get('kuulemma/static/app/components/comment-list-item/comment-list-item.html');
    var commentAdderTemplate = $templateCache.get('kuulemma/static/app/components/comment-adder/comment-adder.html');

    $templateCache.put('/static/dist/partials/components/comment-list/comment-list.html', commentListTemplate);
    $templateCache.put('/static/dist/partials/components/comment-list-item/comment-list-item.html', commentListItemTemplate);
    $templateCache.put('/static/dist/partials/components/comment-adder/comment-adder.html', commentAdderTemplate);

    $httpBackend.expectGET('/hearings/1/links/comments?order_by=created_at&page=1&per_page=20').respond({comments: [{
      id: '5', title: 'Comment title', username: 'test-user', body: 'Hello there!', parent_preview: '', created_at: '2014-12-12' }]});

    $httpBackend.expectGET('/users/2/links/likes').respond({ likes: [] });

    scope = $rootScope.$new();

    createElement = function createElement() {
      element = angular.element('<div hearing-id="1" user-id="2" comment-list></div>');
      element = $compile(element)(scope);
      scope.$digest();
      $httpBackend.flush();
    };

    createAdminElement = function createElement() {
      element = angular.element('<div hearing-id="1" user-id="2" comment-list is-admin="True"></div>');
      element = $compile(element)(scope);
      scope.$digest();
      $httpBackend.flush();
    };

    createOfficialElement = function createElement() {
      element = angular.element('<div hearing-id="1" user-id="2" comment-list is-official="True"></div>');
      element = $compile(element)(scope);
      scope.$digest();
      $httpBackend.flush();
    };
  }));

  describe('User comment list', function() {
    beforeEach(function() {
      createElement();
    });

    it('should have isAdmin and isOfficial as false', function() {
      expect(element.isolateScope().isAdmin).toBe(false);
      expect(element.isolateScope().isOfficial).toBe(false);
    });

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

  describe('Admin comment list', function() {
    beforeEach(function() {
      createAdminElement();
    });

    it('should add isAdmin to scope as truthy value', function() {
      expect(element.isolateScope().isAdmin).toBeTruthy();
    });
  });

  describe('Official comment list', function() {
    beforeEach(function() {
      createOfficialElement();
    });

    it('should add isOfficial to scope as truthy value', function() {
      expect(element.isolateScope().isOfficial).toBeTruthy();
    });
  });
});
