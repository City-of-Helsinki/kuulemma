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
      app: [src + '/app/app.js', src + '/app/**/*.js', '!' + src + '/app/**/*_test.js'],
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
