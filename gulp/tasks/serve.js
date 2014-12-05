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
var gutil = require('gulp-util');
var childProcess = require('child_process');
var http = require('http');
var retry = require('retry');

var config = require('../config');
var child;

function log(data) {
  data.slice(0, -1).split('\n').forEach(function(line) {
    gutil.log('[' + gutil.colors.gray('flask') + ']', line);
  });
}

function stopServer() {
  if (child) {
    child.kill();
  }
}

gulp.task('serve', [], function(done) {
  child = childProcess.spawn(
    'python',
    ['manage.py', 'runserver'],
    {cwd: config.root}
  );

  child.stdout.setEncoding('utf8');
  child.stdout.on('data', log);

  child.stderr.setEncoding('utf8');
  child.stderr.on('data', log);

  var operation = retry.operation({
    minTimeout: 100,
    maxTimeout: 2000
  });

  operation.attempt(function() {
    var url = 'http://' + config.server.host + ':' + config.server.port + '/';
    http.get(url, function() {
      done();
    }).on('error', function(e) {
      if (operation.retry(e)) {
        return;
      }
      if (e) {
        child.kill();
        done(operation.mainError());
      }
    });
  });

});


module.exports = {
  stopServer: stopServer
};
