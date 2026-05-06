---
title: Herring Survey Data - 2016 - BC Central Coast
hide:
  - navigation
  - toc
---

# Herring Survey Data - 2016 - BC Central Coast

View Record in Hakai Catalogue: <a href="https://catalogue.hakai.org/dataset/ca-cioos_d342e016-1e9a-448a-bc1a-af53fe8d5dfd" target="_blank">https://catalogue.hakai.org/dataset/ca-cioos_d342e016-1e9a-448a-bc1a-af53fe8d5dfd</a>

## Issues
| level   | message                                                                                                                                 |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | No version                                                                                                                              |
| WARNING | No DOI defined                                                                                                                          |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'                    |


<a href="https://hakaiinstitute.github.io/hakai-metadata-entry-form#/en/hakai/qbqh6DF00XZq8MOpQ3kKkI9GUv43/-MXhzYmdPTzl2elpwWFM" target="_blank">Click here to resolve these issues in the Metadata Entry Form</a>


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
            "name" : "Herring Survey Data - 2016 - BC Central Coast"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.54187017306685, 51.58844754923095], [-127.72888189181685, 51.58844754923095], [-127.72888189181685, 52.26927804083806], [-128.54187017306685, 52.26927804083806], [-128.54187017306685, 51.58844754923095]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>