(function() {
  'use strict';

  var app = angular.module('kuulemmaApp', ['ngAnimate', 'ngSanitize']);

  app.config(function ($httpProvider, CSRF_TOKEN) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = CSRF_TOKEN;
    $httpProvider.defaults.headers.delete = { 'Content-Type': 'application/json' };
  });

}());
