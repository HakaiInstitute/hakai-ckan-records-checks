---
title: Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia
hide:
  - navigation
  - toc
---

# Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_291b98a4-d868-462c-852a-d6cf79ecf6ce' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_291b98a4-d868-462c-852a-d6cf79ecf6ce 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Nearshore, Geospatial 
    - **Progress**: onGoing 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Tula Foundation 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '0', 'min': '0'}] 
    - **Eov**: macroalgalCanopyCoverAndComposition 
    - **Doi**: 10.21966/9cbv-ra30 
    - **Metadata Publication**: 2025-10-14 
    - **Metadata Revision**: 2025-10-14 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_291b98a4-d868-462c-852a-d6cf79ecf6ce' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                              |
|:--------|:-----------------------------------------------------------------------------------------------------|
| ERROR   | Invalid distributor organisation-name: organization_name='Tula Foundation' expects 'Hakai Institute' |
| INFO    | Title is greater than 60 characters                                                                  |
| INFO    | Record isn't accesible via a standard data repository                                                |
| WARNING | Title contains acronyms potentially                                                                  |


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
            "name" : "Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.4, 51.65], [-128.1, 51.65], [-128.1, 52.09], [-128.4, 52.09], [-128.4, 51.65]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>