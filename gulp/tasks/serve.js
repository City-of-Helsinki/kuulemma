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
