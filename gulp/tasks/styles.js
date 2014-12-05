/* Kuulemma
 * Copyright (C) 2014, Fast Monkeys Oy
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
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
