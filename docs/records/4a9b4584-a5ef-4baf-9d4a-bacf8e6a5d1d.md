---
title: Oceanographic Mooring Time Series, Rivers Inlet, BC, Canada (Research)
hide:
  - navigation
  - toc
---

# Oceanographic Mooring Time Series, Rivers Inlet, BC, Canada (Research)

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_41770c7d-27ea-4593-ba55-040bdc5b99f0' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_41770c7d-27ea-4593-ba55-040bdc5b99f0 
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
    - **Vertical Extent**: [{'max': '260.0', 'min': '90.0'}] 
    - **Eov**: oxygen, subSurfaceSalinity, subSurfaceTemperature 
    - **Doi**: 10.21966/yp9n-w389 
    - **Metadata Publication**: 2022-04-11 
    - **Metadata Revision**: 2026-02-20 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_41770c7d-27ea-4593-ba55-040bdc5b99f0' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                         |
|:--------|:----------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                             |
| WARNING | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Institute' |


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
            "name" : "Oceanographic Mooring Time Series, Rivers Inlet, BC, Canada (Research)"
        },
        "geometry": {'type': 'Point', 'coordinates': [-127.531247, 51.601505]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>