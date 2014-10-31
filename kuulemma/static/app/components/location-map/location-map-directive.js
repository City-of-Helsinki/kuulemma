(function() {
  'use strict';
  angular.module('kuulemmaApp').directive('locationMap', function($window) {
    return {
      restrict: 'A',
      scope: {
        latitude: '@',
        longitude: '@',
        polygon: '@'
      },
      link: function(scope, element) {
        var parsePolygon = function (polygon) {
          return _.map(polygon.split(' '), function(vertex){
            return _.map(vertex.split(','), function(coordenate) {
              return parseFloat(coordenate);
            });
          });
        };
        var L = $window.L;
        var map = L.map(element[0] ,{
          zoomControl:false,
          dragging:false,
          touchZoom:false,
          tap:false,
          doubleClickZoom:false,
        });
        var zoom = 14;
        var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
        var osmAttribution = 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
        var osm = new L.TileLayer(osmUrl, {
            minZoom: zoom,
            maxZoom: zoom,
            attribution: osmAttribution
        });

        map.setView(new L.LatLng(scope.latitude,scope.longitude), zoom);
        map.addLayer(osm);

        if (scope.polygon) {
          L.polygon(parsePolygon(scope.polygon)).addTo(map);
        }

      }
    };
  });
})();
