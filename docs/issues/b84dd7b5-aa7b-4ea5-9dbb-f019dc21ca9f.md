---
title: Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018
hide:
  - navigation
  - toc
---

# Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_a72c43e2-5b4d-4d56-89d4-464b4c513710' target='_blank'>link</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_a72c43e2-5b4d-4d56-89d4-464b4c513710 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Oceanography 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '0.0', 'min': '0.0'}] 
    - **Eov**: other, inorganicCarbon 
    - **Metadata Created**: 2024-05-14T20:02:32.893425 
    - **Metadata Modified**: 2024-05-14T20:02:32.893432 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_a72c43e2-5b4d-4d56-89d4-464b4c513710' target='_blank'>link</a> 

### Issues

| level   | message                                               |
|:--------|:------------------------------------------------------|
| INFO    | Title is greater than 60 characters                   |
| INFO    | No version                                            |
| INFO    | Record isn't accesible via a standard data repository |

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
            "name" : "Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-125.57747949, 49.70969514], [-124.52984083, 49.70969514], [-124.52984083, 50.11496976], [-125.57747949, 50.11496976], [-125.57747949, 49.70969514]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>