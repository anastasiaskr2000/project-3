var map;
var heatMapLayer;
var homicideMapLayer;

// Initialize the map
function initializeMap() {
    map = L.map('map-id').setView([43.68108112399995, -79.39119482699992], 13);

    // Add a tile layer (e.g., OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
}

// Function to load the Homicide map
function loadHomicideMap() {
  if (heatMapLayer) {
      map.removeLayer(heatMapLayer);
  }
  if (!homicideMapLayer) {
      homicideMapLayer = L.layerGroup();

      // Example: Load GeoJSON data for Homicide map
      var geojson = 'http://127.0.0.1:5000/homicide_geojson';
      d3.json(geojson).then(function (data) {
          // Create a GeoJSON layer for Homicide map
          var geojsonLayer = L.geoJson(data, {
              onEachFeature: function (feature, layer) {
                  if (feature.properties && feature.properties.AREA_NAME) {
                      // Display the AREA_NAME on mouseover
                      layer.bindTooltip(feature.properties.AREA_NAME, {
                          sticky: true // Keep the tooltip open until explicitly closed
                      });
                  }

                  layer.on('mouseover', function () {
                      // Highlight the polygon on mouseover (optional)
                      layer.setStyle({
                          weight: 3,
                          color: '#666',
                          fillOpacity: 0.7
                      });
                  });

                  layer.on('mouseout', function () {
                      // Reset the style on mouseout (optional)
                      geojsonLayer.resetStyle(layer);
                  });
              }
          }).addTo(homicideMapLayer);
      });

      // Add the Homicide map layer to the map
      homicideMapLayer.addTo(map);
  } else {
      map.addLayer(homicideMapLayer);
  }
}

// Function to load the Heatmap
function loadHeatmap() {
  if (homicideMapLayer) {
      map.removeLayer(homicideMapLayer);
  }
  if (!heatMapLayer) {
      heatMapLayer = L.layerGroup();

      // Example: Load GeoJSON data for Heatmap
      var heatFilePath = "http://127.0.0.1:5000/crime_geojson_data";
      d3.json(heatFilePath).then(function (data) {
          const filteredData = data.features.filter(feature => {
              const occDate = new Date(feature.properties.OCC_DATE);
              return occDate.getFullYear() === 2022;
          });

          // Extract coordinates for the heatmap
          const heatData = filteredData.map(feature => {
              const coordinates = feature.geometry.coordinates;
              return [coordinates[1], coordinates[0]]; // Reverse the coordinates for Leaflet
          });

          // Create a heatmap layer
          heatMapLayer = L.heatLayer(heatData, { radius: 20, blur: 10 });

          // Add the heatmap layer to the map
          heatMapLayer.addTo(map);
      });
  } else {
      map.addLayer(heatMapLayer);
  }
}
