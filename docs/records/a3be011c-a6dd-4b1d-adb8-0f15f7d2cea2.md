---
title: Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory
hide:
  - navigation
  - toc
---

# Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_0507a738-cd65-4ba4-943e-42b9d022b637' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_0507a738-cd65-4ba4-943e-42b9d022b637 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Airborne Coastal Observatory, Geospatial 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Geospatial 
    - **Resources Count**: 2 
    - **Vertical Extent**: [{'max': '1500.0', 'min': '185.0'}] 
    - **Eov**: other 
    - **Doi**: 10.21966/ytgc-6g46 
    - **Metadata Publication**: 2024-10-09 
    - **Metadata Revision**: 2024-10-09 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_0507a738-cd65-4ba4-943e-42b9d022b637' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                          |
|:--------|:-----------------------------------------------------------------------------------------------------------------|
| ERROR   | Record DOI HTTPS link is failling: https://doi.org/10.21966/ytgc-6g46 status_code=404                            |
| ERROR   | Invalid distributor organisation-name: organization_name='Hakai Geospatial' expects 'Hakai Institute'            |
| ERROR   | Failed to retrieve DOI from dataCite [404] The resource you are looking for doesn't exist.: 10.21966/ytgc-6g46   |
| INFO    | Title is greater than 60 characters                                                                              |
| INFO    | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Geospatial' |
| INFO    | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Geospatial' |


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
            "name" : "Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-122.1, 50.5], [-121.7, 50.5], [-121.7, 51.12], [-122.1, 51.12], [-122.1, 50.5]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>