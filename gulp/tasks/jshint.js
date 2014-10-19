'use strict';

var gulp = require('gulp');
var jshint = require('gulp-jshint');

var config = require('../config');

gulp.task('jshint', function() {
  var paths = [].concat(
    config.js.src.app,
    config.js.src.test,
    config.js.src.e2e
  );
  return gulp.src(paths, {base: config.src})
    .pipe(jshint())
    .pipe(jshint.reporter('jshint-stylish'))
    .pipe(jshint.reporter('fail'));
});
