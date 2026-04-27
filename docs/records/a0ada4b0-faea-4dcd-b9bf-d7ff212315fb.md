---
title: Stage-Discharge Time Series - Calvert Island - Archived Version 2.0
hide:
  - navigation
  - toc
---

# Stage-Discharge Time Series - Calvert Island - Archived Version 2.0

<a href='https://catalogue.hakai.org/dataset/ca-cioos_1347af6c-aedf-4ec6-bd37-ed508df6c40a' target='_blank'>View Record in Hakai Catalogue</a>

## Issues
| level   | message                                                                                                                                 |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Record isn't accesible via a standard data repository                                                                                   |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Korver, Maartje' contact.get('organisation-name')='Hakai Institute'                  |

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
            "name" : "Stage-Discharge Time Series - Calvert Island - Archived Version 2.0"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.1383514404297, 51.60223926037915], [-127.96669006347653, 51.60223926037915], [-127.96669006347653, 51.68660524501087], [-128.1383514404297, 51.68660524501087], [-128.1383514404297, 51.60223926037915]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>

<div id='map'></div>