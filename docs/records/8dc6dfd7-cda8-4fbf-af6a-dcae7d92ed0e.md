---
title: Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia
hide:
  - navigation
  - toc
---

# Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia

<a href='https://catalogue.hakai.org/dataset/ca-cioos_d7ffd737-5725-4a56-9134-a9ad91c2734d' target='_blank'>View Record in Hakai Catalogue</a>

## Issues
| level   | message                                                                                                                 |
|:--------|:------------------------------------------------------------------------------------------------------------------------|
| INFO    | Record isn't accesible via a standard data repository                                                                   |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute' |

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
            "name" : "Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-122.4, 50.62], [-122.0, 50.62], [-122.0, 50.75], [-122.4, 50.75], [-122.4, 50.62]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>