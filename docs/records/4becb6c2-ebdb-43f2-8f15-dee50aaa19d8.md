---
title: Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0
hide:
  - navigation
  - toc
---

# Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0

View Record in Hakai Catalogue: <a href="https://catalogue.hakai.org/dataset/ca-cioos_fd5ada9a-5719-4ca1-89d2-17adb48d1493" target="_blank">https://catalogue.hakai.org/dataset/ca-cioos_fd5ada9a-5719-4ca1-89d2-17adb48d1493</a>

## Issues
| level   | message                                                                                                                                    |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Contact missing ORCID: contact['individual-name']='Rockwell, Lisa' contact.get('organisation-name')='Gulf Islands National Park Reserve'   |
| INFO    | Contact missing ORCID: contact['individual-name']='Collyer, M. J. P.' contact.get('organisation-name')='Pacific Rim National Park Reserve' |
| INFO    | Contact missing ORCID: contact['individual-name']='Helms, Sibylla' contact.get('organisation-name')='Gulf Islands National Park Reserve'   |
| INFO    | Record isn't accesible via a standard data repository                                                                                      |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'    |


<a href="https://hakaiinstitute.github.io/hakai-metadata-entry-form#/en/hakai/qbqh6DF00XZq8MOpQ3kKkI9GUv43/-MXBNZnZGekFJcFFDcm8" target="_blank">Click here to resolve these issues in the Metadata Entry Form</a>


<script>
   document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map').setView([51.505, -125.09], 5);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    var geojsonFeature = {
        "type": "Feature",
        "properties": {
            "name" : "Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-123.81789453, 48.48393505], [-122.96096027, 48.48393505], [-122.96096027, 49.05595865], [-123.81789453, 49.05595865], [-123.81789453, 48.48393505]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>