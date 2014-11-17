'use strict';

angular.module('kuulemmaApp').factory('CommentService', function($http) {

  function saveComment(hearingId, commentObj) {
    var omittedProperties = ['follow', 'commentsOn'];
    var commentsOn = commentObj.commentsOn.id;
    if(!commentObj.follow) {
      omittedProperties.push('email');
    }
    var formattedComment = _.omit(commentObj, omittedProperties);
    formattedComment.comments_on = commentsOn;
    // The following values are hardcoded to point to the current hearing for now.
    formattedComment.object_type = 'hearing';
    formattedComment.object_id = hearingId;
    return $http.post('/hearings/' + hearingId + '/links/comments', formattedComment);
  }

  return {
    save: saveComment
  };

});
