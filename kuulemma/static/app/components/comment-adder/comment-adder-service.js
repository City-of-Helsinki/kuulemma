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

angular.module('kuulemmaApp').factory('CommentService', function($http) {

  function saveComment(hearingId, commentObj) {
    var omittedProperties = commentObj.follow ? ['follow', 'commentsOn'] : ['follow', 'commentsOn', 'email'];
    var formattedComment = _.omit(commentObj, omittedProperties);

    var splittedContext = commentObj.commentsOn.key.split('-');
    formattedComment.object_type = splittedContext[0];
    formattedComment.object_id = +splittedContext[1];

    return $http.post('/hearings/' + hearingId + '/links/comments', formattedComment);
  }

  return {
    save: saveComment
  };

});
