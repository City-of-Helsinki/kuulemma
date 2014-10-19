'use strict';

var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync');
var filter = require('gulp-filter');
var gulp = require('gulp');
var gulpif = require('gulp-if');
var less = require('gulp-less');
var minifyCSS = require('gulp-minify-css');
var rename = require('gulp-rename');
var rev = require('gulp-rev');
var sourcemaps = require('gulp-sourcemaps');

var config = require('../config');

gulp.task('styles', function() {
  return gulp.src(config.less.src, {base: config.src})
    .pipe(sourcemaps.init())
    .pipe(less())
    .pipe(autoprefixer(['last 2 versions', 'ie >= 9']))
    .pipe(minifyCSS())
    .pipe(rename('all.css'))
    .pipe(gulpif(config.options.env === 'production', rev()))
    .pipe(sourcemaps.write('.', {includeContent: false, sourceRoot: '/static'}))
    .pipe(gulp.dest(config.less.dest))
    .pipe(filter('**/*.css'))
    .pipe(browserSync.reload({stream: true}))
    .pipe(rev.manifest())
    .pipe(gulp.dest(config.less.dest));
});
