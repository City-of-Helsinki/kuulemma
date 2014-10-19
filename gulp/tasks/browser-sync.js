'use strict';

var browserSync = require('browser-sync');
var gulp = require('gulp');

var config = require('../config');

gulp.task('browser-sync', ['watch', 'serve'], function() {
  browserSync({
    proxy: config.server.host + ':' + config.server.port
  });
});
