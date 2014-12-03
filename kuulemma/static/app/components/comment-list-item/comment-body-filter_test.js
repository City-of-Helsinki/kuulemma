'use strict';

describe('Filter: commentBodyFilter', function () {

  beforeEach(module('kuulemmaApp'));

  var commentBodyFilter;
  beforeEach(inject(function ($filter) {
    commentBodyFilter = $filter('commentBodyFilter');
  }));

  it('replace line breaks with <br> tags', function () {
    var text = 'line1\nline2\n\nline3';
    expect(commentBodyFilter(text)).toBe('line1<br>line2<br><br>line3');
  });

  it('should do nothing if no line breaks', function() {
    var text = 'line1';
    expect(commentBodyFilter(text)).toBe('line1');
  });

});
