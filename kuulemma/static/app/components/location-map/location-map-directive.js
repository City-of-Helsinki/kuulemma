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
