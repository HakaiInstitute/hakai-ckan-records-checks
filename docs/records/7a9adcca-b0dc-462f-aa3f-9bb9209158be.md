---
title: Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0
hide:
  - navigation
  - toc
---

# Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0

View Record in Hakai Catalogue: <a href="https://catalogue.hakai.org/dataset/ca-cioos_3f40326a-23f9-4e30-a16a-f332ace14e2f" target="_blank">https://catalogue.hakai.org/dataset/ca-cioos_3f40326a-23f9-4e30-a16a-f332ace14e2f</a>

## Issues
| level   | message                                                                                                                      |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------|
| INFO    | No version                                                                                                                   |
| INFO    | Contact missing ORCID: contact['individual-name']='Burt, J.' contact.get('organisation-name')=''                             |
| INFO    | Contact missing ORCID: contact['individual-name']='Okamoto, D.' contact.get('organisation-name')=''                          |
| INFO    | Record isn't accesible via a standard data repository                                                                        |
| WARNING | No funder                                                                                                                    |
| WARNING | No publisher                                                                                                                 |
| WARNING | Contact missing ORCID: contact['individual-name']='Pontier, Ondine' contact.get('organisation-name')='Hakai Institute'       |
| WARNING | Contact missing ORCID: contact['individual-name']='Hessing-Lewis, Margot' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Pontier, Ondine' contact.get('organisation-name')='Hakai Institute'       |


<a href="https://hakaiinstitute.github.io/hakai-metadata-entry-form#/en/hakai/df5J7W5Hk4e0p4yvlOAI0qcU9Gs2/-MtG8b48aDAEdJoqNT6N" target="_blank">Click here to resolve these issues in the Metadata Entry Form</a>


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
            "name" : "Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.6, 51.19], [-127.1, 51.19], [-127.1, 52.28], [-128.6, 52.28], [-128.6, 51.19]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>