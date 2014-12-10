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
