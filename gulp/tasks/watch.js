'use strict';

var browserSync = require('browser-sync');
var gulp = require('gulp');

var config = require('../config');

gulp.task('watch', ['build'], function() {
  gulp.watch(config.img.src, ['images']);
  gulp.watch(config.js.src.app, ['jshint', 'scripts', browserSync.reload]);
  gulp.watch(config.src + '/app/**.less', ['styles', browserSync.reload]);
  gulp.watch(config.html.src, ['html', browserSync.reload]);
  gulp.watch(config.less.watch, ['styles', browserSync.reload]);
});
