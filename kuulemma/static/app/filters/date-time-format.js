'use strict';

angular.module('kuulemmaApp')
  .filter('dateTimeFormat', function ($window) {
    return function (date) {
      var utcCreationTime = moment(date);
      var diffInDays = moment.utc($window.Date.now()).diff(utcCreationTime, 'days');

      if(diffInDays > 2) {
        return utcCreationTime.format('DD.MM.YYYY, HH:mm');
      } else {
        return utcCreationTime.locale('fi').fromNow();
      }
    };
  });
