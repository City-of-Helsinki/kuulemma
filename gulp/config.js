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
      vendor: wiredep().js.concat([src + '/bower_components/moment/locale/fi.js']),
      vendorTest: wiredep({ devDependencies: true }).js.concat([src + '/bower_components/moment/locale/fi.js']),
      app: [src + '/app/**/*.js', '!' + src + '/app/**/*_test.js'],
      mocks: [src + '/mocks/**/*.js'],
      test: [src + '/app/**/*_test.js'],
      e2e: [root + '/tests/e2e/**/*.js']
    },
    dest: dest + '/js'
  },
  html: {
    src: [src + '/app/**/*.html'],
    dest: dest + '/partials'
  },
  less: {
    src: [src + '/app/app.less'],
    watch: [src + '/app/**/*.less', '!' + src + '/app/app.less'],
    dest: dest + '/css'
  },
  img: {
    src: [src + '/images/**'],
    dest: dest + '/images'
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
