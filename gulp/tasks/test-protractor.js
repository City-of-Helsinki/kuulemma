'use strict';

var gulp = require('gulp');
var protractor = require('gulp-protractor').protractor;

var config = require('../config');
var serve = require('./serve');

gulp.task('test-protractor', ['build', 'serve'], function() {
  return gulp.src(config.js.src.e2e)
    .pipe(protractor({
      configFile: config.tests.protractor,
      args: ['--baseUrl', 'http://' + config.server.host + ':' + config.server.port]
    }))
    .on('error', function(e) {
      throw e;
    })
    .on('end', function() {
      serve.stopServer();
    });
});
