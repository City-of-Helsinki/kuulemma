'use strict';

var browserSync = require('browser-sync');
var gulp = require('gulp');

var config = require('../config');

gulp.task('watch', ['build'], function() {
  gulp.watch(config.img.src, ['images']);
  gulp.watch(config.js.src.app, ['scripts', browserSync.reload]);
  gulp.watch(config.src + '/app/**.less', ['styles']);
});
