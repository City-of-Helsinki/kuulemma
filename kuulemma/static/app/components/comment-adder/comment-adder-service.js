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
