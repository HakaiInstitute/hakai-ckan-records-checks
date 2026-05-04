---
title: Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada
hide:
  - navigation
  - toc
---

# Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada

View Record in Hakai Catalogue: <https://catalogue.hakai.org/dataset/ca-cioos_5c13b300-e172-4010-a6d8-7586b68a3a96>

## Issues
| level   | message                                                                                                                 |
|:--------|:------------------------------------------------------------------------------------------------------------------------|
| ERROR   | Empty resource name                                                                                                     |
| INFO    | No version                                                                                                              |
| INFO    | Record isn't accesible via a standard data repository                                                                   |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute' |

[Click here to resolve these issues in the Metadata Entry Form](https://hakaiinstitute.github.io/hakai-metadata-entry-form#/en/hakai/qbqh6DF00XZq8MOpQ3kKkI9GUv43/-MTFIWmZWeEE0RkZrZVc)


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
            "name" : "Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.30122253, 51.7689035], [-128.05512885, 51.7689035], [-128.05512885, 51.98187882], [-128.30122253, 51.98187882], [-128.30122253, 51.7689035]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>