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

var config = require('./gulp/config');
var files = [].concat(
  config.js.src.vendorTest,
  config.html.src,
  config.js.src.app,
  config.js.src.mocks,
  config.js.src.test
);

module.exports = function(config) {
  config.set({
    autoWatch: true,
    browsers: ['Firefox', 'Chrome'],
    coverageReporter: {
      type: 'html',
      dir: 'tests/frontend/coverage'
    },
    files: files,
    frameworks: ['jasmine'],
    plugins: [
      'karma-jasmine',
      'karma-chrome-launcher',
      'karma-firefox-launcher',
      'karma-safari-launcher',
      'karma-ng-html2js-preprocessor',
      'karma-coverage'
    ],
    preprocessors: {
      'kuulemma/static/app/**/*.html': 'ng-html2js',
      'kuulemma/static/app/**/*.js': 'coverage'
    },

    ngHtml2JsPreprocessor: {
      stripPrefix: 'kuulemma/static/app/',
      moduleName: 'test-templates'
    }
  });
};
