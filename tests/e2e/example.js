'use strict';

describe('Example E2E test', function() {

  beforeEach(function() {
    browser.get('/');
  });

  it('it should have right title', function () {
    expect($('strong.lead').getText()).toContain('Kuulemispalvelu on lorem ipsum');
  });

});
