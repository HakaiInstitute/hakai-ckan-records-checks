---
title: Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5
hide:
  - navigation
  - toc
---

# Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5

View Record in Hakai Catalogue: <a href="https://catalogue.hakai.org/dataset/ca-cioos_5033d8e4-7b58-45b5-86e6-e98e14d1d6b9" target="_blank">https://catalogue.hakai.org/dataset/ca-cioos_5033d8e4-7b58-45b5-86e6-e98e14d1d6b9</a>

## Issues
| level   | message                                                                                                                                                |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR   | Invalid distributor organisation-name: organization_name='Vancouver Island University' expects 'Hakai Institute'                                       |
| INFO    | No version                                                                                                                                             |
| INFO    | Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Vancouver Island University'                   |
| INFO    | Record isn't accesible via a standard data repository                                                                                                  |
| WARNING | No funder                                                                                                                                              |
| WARNING | Contact missing ORCID: contact['individual-name']='Korver, Maartje C.' contact.get('organisation-name')='Hakai Institute -  McGill University'         |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Korver, Maartje C.' contact['organisation-name']='Hakai Institute -  McGill University' |
| WARNING | Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'                                 |
| WARNING | Contact missing ORCID: contact['individual-name']='Brunsting, Ray' contact.get('organisation-name')='Hakai Institute'                                  |
| WARNING | Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'                                 |

<a href="https://hakaiinstitute.github.io/hakai-metadata-entry-form#/en/hakai/qbqh6DF00XZq8MOpQ3kKkI9GUv43/-MVhmY1RwNHlma250bWg" target="_blank">Click here to resolve these issues in the Metadata Entry Form</a>


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
            "name" : "Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.13265424, 51.60936247], [-127.95907025, 51.60936247], [-127.95907025, 51.69558793], [-128.13265424, 51.69558793], [-128.13265424, 51.60936247]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>