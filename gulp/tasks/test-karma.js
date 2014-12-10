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
var karma = require('karma');

var config = require('../config');

gulp.task('test-karma', function(done) {
  karma.server.start({
    configFile: config.tests.karma,
    singleRun: true
  }, done);
});

gulp.task('tdd', function(done) {
  karma.server.start({
    configFile: config.tests.karma
  }, done);
});
