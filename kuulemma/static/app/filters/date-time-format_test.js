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

    // TODO: Fix this test.
    xit('should show "2 päivää sitten"', function() {
      expect(filter(utcDate(testDate))).toBe('kaksi päivää sitten');
    });
  });
});
