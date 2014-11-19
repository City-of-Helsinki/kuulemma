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

var gulp = require('gulp');
var rev = require('gulp-rev');
var gulpif = require('gulp-if');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var html2js = require('gulp-html2js');

var config = require('../config');

gulp.task('html', function() {
  return gulp.src(config.html.src)
    .pipe(html2js({
      outputModuleName: 'templates',
      useStrict: true,
      base: 'kuulemma/static/app/'
    }))
    .pipe(concat('templates.js'))
    .pipe(uglify())
    .pipe(gulpif(config.options.env === 'production', rev()))
    .pipe(gulp.dest(config.html.dest))
    .pipe(rev.manifest())
    .pipe(gulp.dest(config.html.dest));
});
