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

describe('Service: CommentService', function () {

  beforeEach(module('kuulemmaApp'));

  var CommentService, $httpBackend, $http;
  beforeEach(inject(function (_CommentService_, _$httpBackend_, _$http_) {
    CommentService = _CommentService_;
    $httpBackend = _$httpBackend_;
    $http = _$http_;
    spyOn($http, 'post');
  }));

  afterEach(function() {
    $http.post.reset();
  });

  describe('Saving comment without email', function() {
    beforeEach(function() {
      CommentService.save(1, {
        title: 'test subject',
        body: 'Comment',
        follow: false,
        email: 'email@email.com',
        commentsOn: {
          key: 'hearing-1',
          label: 'Kuuleminen'
        }
      });
    });

    it('should make a post request without email', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        title : 'test subject',
        body : 'Comment',
        object_type: 'hearing',
        object_id: 1
      });
    });
  });

  describe('Saving comment with email', function() {
    beforeEach(function() {
      CommentService.save(1, {
        title: 'test subject',
        body: 'Comment',
        follow: true,
        email: 'email@email.com',
        commentsOn: {
          key: 'hearing-1',
          label: 'Kuuleminen'
        }
      });
    });

    it('should make a post request without email', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        title : 'test subject',
        body : 'Comment',
        email: 'email@email.com',
        object_type: 'hearing',
        object_id: 1
      });
    });
  });

  describe('Formatting commentsOn paramater name', function() {
    beforeEach(function() {
      CommentService.save(1, {
        commentsOn: {
          key: 'image-123',
          label: 'Kuvaan 123'
        }
      });
    });

    it('should change it from camelcase to dashed one before saving', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post).toHaveBeenCalledWith('/hearings/1/links/comments', {
        object_type: 'image',
        object_id: 123
      });
    });
  });
});
