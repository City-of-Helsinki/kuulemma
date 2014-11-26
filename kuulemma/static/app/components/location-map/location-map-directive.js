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
        var L = $window.L;
        var map = L.map(element[0] ,{
          zoomControl:false,
          scrollWheelZoom: false,
          dragging:false,
          touchZoom:false,
          tap:false,
          doubleClickZoom:false,
        });
        var zoom = 14;
        var osmUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
        var osmAttribution = 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
        var osm = new L.TileLayer(osmUrl, {
            minzoom: 1,
            maxzoom: 15,
            attribution: osmAttribution
        });

        map.setView(new L.LatLng(scope.latitude, scope.longitude), zoom);
        map.addLayer(osm);
        if (scope.polygon) {
          var poly = L.geoJson(JSON.parse(scope.polygon));
          poly.addTo(map);
          // Center and zoom map
          map.fitBounds(poly.getBounds());
        }
      }
    };
  });
})();
