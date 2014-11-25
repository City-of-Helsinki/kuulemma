'use strict';

angular.module('kuulemmaApp').factory('FeedbackService', function($http) {

  function saveFeedback(feedbackObject) {
    return $http.post('/feedback', feedbackObject);
  }

  return {
    save: saveFeedback
  };

});
