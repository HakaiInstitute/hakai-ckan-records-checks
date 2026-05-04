---
title: Trails - Calvert Island - British Columbia - Canada
hide:
  - navigation
  - toc
---

# Trails - Calvert Island - British Columbia - Canada

View Record in Hakai Catalogue: <https://catalogue.hakai.org/dataset/ca-cioos_ea4e84d5-c89c-4611-9594-449e468bd76c>

## Issues
| level   | message                                                                                                                            |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------------|
| INFO    | No version                                                                                                                         |
| WARNING | No DOI defined                                                                                                                     |
| WARNING | Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute' |

[Click here to resolve these issues in the Metadata Entry Form](https://hakaiinstitute.github.io/hakai-metadata-entry-form#/en/hakai/qbqh6DF00XZq8MOpQ3kKkI9GUv43/-MUpVU2tGOVdZMk85OHU)


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
            "name" : "Trails - Calvert Island - British Columbia - Canada"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.1603240966797, 51.63805006307942], [-128.08685302734375, 51.63805006307942], [-128.08685302734375, 51.66914840783798], [-128.1603240966797, 51.66914840783798], [-128.1603240966797, 51.63805006307942]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>