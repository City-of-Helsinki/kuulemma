'use strict';

describe('Example E2E test', function() {

  beforeEach(function() {
    browser.get('/');
  });

  it('it should have right title', function () {
    expect($('p').getText()).toBe('Hello world! This is HTML5 Boilerplate.');
  });

});
