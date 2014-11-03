'use strict';

var config = require('./gulp/config');
var files = [].concat(
  config.js.src.vendorTest,
  config.js.src.app,
  config.js.src.mocks,
  config.js.src.test
);

module.exports = function(config) {
  config.set({
    autoWatch: true,
    browsers: ['Firefox', 'Chrome'],
    coverageReporter: {
      type: 'html',
      dir: 'tests/frontend/coverage'
    },
    files: files,
    frameworks: ['jasmine'],
    plugins: [
      'karma-jasmine',
      'karma-chrome-launcher',
      'karma-firefox-launcher',
      'karma-safari-launcher',
      'karma-ng-html2js-preprocessor',
      'karma-coverage'
    ],
    preprocessors: {
      'kuulemma/static/app/**/*.html': 'ng-html2js',
      'kuulemma/static/app/**/*.js': 'coverage'
    }
  });
};
