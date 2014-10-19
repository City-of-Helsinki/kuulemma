'use strict';

var gulp = require('gulp');
var karma = require('karma');

var config = require('../config');

gulp.task('test-karma', function(done) {
  karma.server.start({
    configFile: config.tests.karma,
    singleRun: true
  }, done);
});

gulp.task('tdd', function(done) {
  karma.server.start({
    configFile: config.tests.karma
  }, done);
});
