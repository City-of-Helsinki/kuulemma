'use strict';

describe('Filter: dateTimeFormat', function () {

  beforeEach(module('kuulemmaApp'));

  function utcDate(testDate) {
    return testDate.format('YYYY-MM-DDTHH:mm:ssZ');
  }

  var filter, now, testDate;
  beforeEach(inject(function($filter, $window) {
    filter = $filter('dateTimeFormat');
    spyOn($window.Date, 'now').andReturn(1416210879629);
    now = moment($window.Date.now());
    testDate = null;
  }));

  describe('Time exactly two days ago', function() {
    beforeEach(function() {
      testDate = now.subtract(2, 'days');
    });

    it('should show "2 päivää sitten"', function() {
      expect(filter(utcDate(testDate))).toBe('kaksi päivää sitten');
    });
  });
});
