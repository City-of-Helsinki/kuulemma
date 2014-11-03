'use strict';

var concat = require('gulp-concat');
var gulp = require('gulp');
var gulpif = require('gulp-if');
var ngAnnotate = require('gulp-ng-annotate');
var rev = require('gulp-rev');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');

var config = require('../config');

gulp.task('scripts', function() {
  var paths = [].concat(
    config.js.src.vendor,
    config.js.src.app
  );
  return gulp.src(paths, {base: config.src})
    .pipe(sourcemaps.init())
    .pipe(ngAnnotate())
    .pipe(concat('all.js'))
    .pipe(uglify())
    .pipe(gulpif(config.options.env === 'production', rev()))
    .pipe(sourcemaps.write('.', {includeContent: false, sourceRoot: '/static'}))
    .pipe(gulp.dest(config.js.dest))
    .pipe(rev.manifest())
    .pipe(gulp.dest(config.js.dest));
});
