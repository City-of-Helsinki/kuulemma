'use strict';

var changed = require('gulp-changed');
var gulp = require('gulp');
var imagemin = require('gulp-imagemin');

var config = require('../config');

gulp.task('images', function() {
  return gulp.src(config.img.src)
    .pipe(changed(config.img.dest))
    .pipe(imagemin({
      progressive: true,
      interlaced: true
    }))
    .pipe(gulp.dest(config.img.dest));
});
