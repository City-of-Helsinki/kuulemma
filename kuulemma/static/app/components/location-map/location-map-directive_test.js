'use strict';

describe('Directive: locationMap', function () {

  beforeEach(module('kuulemmaApp'));

  var L, element, isolateScope, scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  describe('LocationMap with latitude and longitude', function() {
    beforeEach(inject(function($compile, $window) {
      L = $window.L;
      element = angular.element(
        '<div location-map latitude="0" longitude="0"></div>');
      spyOn(L, 'LatLng').andCallThrough();
      element = $compile(element)(scope);
      scope.$digest();
      isolateScope = element.isolateScope();
    }));

    it('should pass lat and long to scope', function () {
      expect(isolateScope.latitude).toBe('0');
      expect(isolateScope.longitude).toBe('0');
    });

    it('creates a LatLng object with correct lat and long', function () {
      expect(window.L.LatLng).toHaveBeenCalledWith('0','0');
    });

    it('creates a leaflet object', function () {
      expect($(element).hasClass('leaflet-container')).toBe(true);
    });
  });

  describe('LocationMap with lat, long, and polygon', function() {
    beforeEach(inject(function($compile, $window) {
      L = $window.L;
      element = angular.element(
        '<div location-map latitude="0" longitude="0" polygon=\'{"coordinates": [[[0.0, 0.0], [1.0, 2.0], [0.0, 0.0]]], "type": "Polygon"}\'></div>'
      );
      spyOn(document, 'getElementById').andReturn(element[0]);
      spyOn(L, 'geoJson').andCallThrough();
      element = $compile(element)(scope);
      scope.$digest();
      isolateScope = element.isolateScope();
    }));

    it('parses the polygon string into an array of vertex', function () {
      expect(L.geoJson).toHaveBeenCalledWith(
        JSON.parse('{"coordinates": [[[0.0, 0.0], [1.0, 2.0], [0.0, 0.0]]], "type": "Polygon"}')
      );
    });
  });
});
