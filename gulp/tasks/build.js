'use strict';

var gulp = require('gulp');

gulp.task('build', ['jshint', 'scripts', 'html', 'styles', 'images']);
