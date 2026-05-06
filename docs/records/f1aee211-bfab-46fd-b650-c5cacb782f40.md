---
title: Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory
hide:
  - navigation
  - toc
---

# Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory

View Record in Hakai Catalogue: <a href="https://catalogue.hakai.org/dataset/ca-cioos_3efdccb0-08ef-4e90-ac91-72969f94a99a" target="_blank">https://catalogue.hakai.org/dataset/ca-cioos_3efdccb0-08ef-4e90-ac91-72969f94a99a</a>

## Issues
| level   | message                                                                                                                  |
|:--------|:-------------------------------------------------------------------------------------------------------------------------|
| INFO    | Record isn't accesible via a standard data repository                                                                    |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'  |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'  |
| WARNING | Contact missing ORCID: contact['individual-name']='Giesbrecht, Ian' contact.get('organisation-name')='Hakai Institute'   |
| WARNING | Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute' |


<a href="https://hakaiinstitute.github.io/hakai-metadata-entry-form#/en/hakai/RvRPlFMSsIaBwoGdQIq5BVYfBBa2/-NpRG7xQ84LQrgS4jhie" target="_blank">Click here to resolve these issues in the Metadata Entry Form</a>


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
            "name" : "Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-124.9, 50.53], [-124.2, 50.53], [-124.2, 50.99], [-124.9, 50.99], [-124.9, 50.53]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>