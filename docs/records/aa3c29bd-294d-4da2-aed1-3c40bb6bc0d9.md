---
title: Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 Analyzer located at Bamfield Marine Sciences Centre, Bamfield, BC, Canada (Provisional)
hide:
  - navigation
  - toc
---

# Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 Analyzer located at Bamfield Marine Sciences Centre, Bamfield, BC, Canada (Provisional)

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_fb5c9e1e-a911-46b7-8c1d-e34215a105ed' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_fb5c9e1e-a911-46b7-8c1d-e34215a105ed 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Oceanography 
    - **Progress**: onGoing 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '20.0', 'min': '20.0'}] 
    - **Eov**: seaSurfaceTemperature, inorganicCarbon, subSurfaceSalinity, subSurfaceTemperature 
    - **Doi**:  
    - **Metadata Publication**: 2023-10-20 
    - **Metadata Revision**: 2026-02-05 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_fb5c9e1e-a911-46b7-8c1d-e34215a105ed' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                             |
|:--------|:------------------------------------|
| INFO    | Title is greater than 60 characters |
| INFO    | No version                          |
| WARNING | Title contains acronyms potentially |
| WARNING | No DOI defined                      |


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
            "name" : "Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 Analyzer located at Bamfield Marine Sciences Centre, Bamfield, BC, Canada (Provisional)"
        },
        "geometry": {'type': 'Point', 'coordinates': [-125.13535, 48.83515]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>