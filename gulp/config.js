'use strict';

var wiredep = require('wiredep');
var yargs = require('yargs');

var root = __dirname + '/..';
var src = root + '/kuulemma/static';
var dest = root + '/kuulemma/static/dist';

module.exports = {
  options: yargs.argv,
  root: root,
  src: src,
  dest: dest,
  js: {
    src: {
      vendor: wiredep().js,
      app: [src + '/app/**/*.js'],
      test: [src + '/app/**_test.js'],
      e2e: [root + '/tests/e2e/**/*.js']
    },
    dest: dest + '/js'
  },
  less: {
    src: [src + '/app/app.less'],
    dest: dest + '/css'
  },
  img: {
    src: [src + '/img/**'],
    dest: dest + '/img'
  },
  server: {
    host: 'localhost',
    port: 5000
  },
  tests: {
    karma: root + '/karma.conf.js',
    protractor: root + '/protractor.conf.js'
  }
};
