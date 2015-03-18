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

describe('Service: FeedbackService', function () {

  beforeEach(module('kuulemmaApp'));

  var FeedbackService, $httpBackend, $http;
  beforeEach(inject(function (_FeedbackService_, _$httpBackend_, _$http_) {
    FeedbackService = _FeedbackService_;
    $httpBackend = _$httpBackend_;
    $http = _$http_;
    spyOn($http, 'post');
  }));

  afterEach(function() {
    $http.post.reset();
  });

  describe('Saving feedback', function() {
    beforeEach(function() {
      FeedbackService.save({
        content: 'My Feedback!',
      });
    });

    it('should make a post request with content in data', function() {
      expect($http.post.callCount).toBe(1);
      expect($http.post.mostRecentCall.args[1].content).toContain('My Feedback!');
    });
  });
});
