---
title: Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada
hide:
  - navigation
  - toc
---

# Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada

<a href='https://catalogue.hakai.org/dataset/ca-cioos_0c8692f0-a103-4681-9247-9bb69c6e222e' target='_blank'>View Record in Hakai Catalogue</a>

## Issues
| level   | message    |
|:--------|:-----------|
| INFO    | No version |

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
            "name" : "Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.17543029785156, 51.63272286429384], [-128.10916900634766, 51.63272286429384], [-128.10916900634766, 51.68149662336026], [-128.17543029785156, 51.68149662336026], [-128.17543029785156, 51.63272286429384]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>