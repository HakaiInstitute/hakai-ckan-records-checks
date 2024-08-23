---
title: Data for the paper "Phylogenomic position of eupelagonemids, abundant, and diverse deep-ocean heterotrophs"
hide:
  - navigation
  - toc
---

# Data for the paper "Phylogenomic position of eupelagonemids, abundant, and diverse deep-ocean heterotrophs"

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_f67c0c58-3225-4dac-9264-1e76f07c9374' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_f67c0c58-3225-4dac-9264-1e76f07c9374 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Genomics 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: University of British Columbia 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '300.0', 'min': '300.0'}] 
    - **Eov**: other 
    - **Doi**: 10.21966/7t4p-s714 
    - **Metadata Publication**: 2024-08-02 
    - **Metadata Revision**: 2024-08-02 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_f67c0c58-3225-4dac-9264-1e76f07c9374' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                             |
|:--------|:--------------------------------------------------------------------------------------------------------------------|
| ERROR   | Invalid distributor organisation-name: organization_name='University of British Columbia' expects 'Hakai Institute' |
| INFO    | Title is greater than 60 characters                                                                                 |
| INFO    | Record isn't accesible via a standard data repository                                                               |


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
            "name" : "Data for the paper "Phylogenomic position of eupelagonemids, abundant, and diverse deep-ocean heterotrophs""
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-127.9661, 51.65001], [-127.966, 51.65001], [-127.966, 51.65], [-127.9661, 51.65], [-127.9661, 51.65001]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>