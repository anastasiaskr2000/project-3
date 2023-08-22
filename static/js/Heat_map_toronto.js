function Heatmap() {
    console.log('heat')
    const myMap = L.map('map-id').setView([43.7032, -79.3832], 11);
    // Add a tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(myMap);

    // Load GeoJSON data
    let heatFilePath = "http://127.0.0.1:5000/crime_geojson_data"
    d3.json(heatFilePath).then(data => {

        const filteredData = data.features.filter(feature => {
            const occDate = new Date(feature.properties.OCC_DATE);
            return occDate.getFullYear() === 2022;
        });

        // Create separate heat map layers for each crime category
        const crimeCategories = ['Assault', 'Auto Theft', 'Break and Enter', 'Robbery', 'Theft Over'];
        const heatLayers = {};

        // Loop through each crime category
        crimeCategories.forEach(category => {
            const categoryFeatures = filteredData.filter(feature =>
                feature.properties.MCI_CATEGORY === category
            );

            const heatData = categoryFeatures.map(feature =>
                feature.geometry.coordinates.reverse()
            );

            heatLayers[category] = L.heatLayer(heatData, { radius: 20, blur: 10 });
        });

        // Create layer control to switch between heat map layers
        L.control.layers(null, heatLayers, {
            collapsed: false
        }).addTo(myMap);

        // Add the default layer (Assault) to the map
        heatLayers['Assault'].addTo(myMap);
    });

    myMap.on('resize', function () {
        myMap.invalidateSize();
    })
}
Heatmap();