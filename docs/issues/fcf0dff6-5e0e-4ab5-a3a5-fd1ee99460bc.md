---
title: Geology - Calvert Island
hide:
  - navigation
  - toc
---

# Geology - Calvert Island

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_6ae1b131-d903-44ca-92a9-64cf6487ddc2' target='_blank'>link</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_6ae1b131-d903-44ca-92a9-64cf6487ddc2 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Geospatial 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 2 
    - **Vertical Extent**: [{'max': '0.0', 'min': '0.0'}] 
    - **Eov**: other 
    - **Doi**: 10.21966/f6bn-9773 
    - **Metadata Publication**: 2022-03-02 
    - **Metadata Revision**: 2024-03-15 
    - **Citation Count**: 0 
    - **Citations Over Time**: [] 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_6ae1b131-d903-44ca-92a9-64cf6487ddc2' target='_blank'>link</a> 

### Issues

| level   | message                                                                                                                 |
|:--------|:------------------------------------------------------------------------------------------------------------------------|
| INFO    | No version                                                                                                              |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute' |

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
            "name" : "Geology - Calvert Island"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.2489013671875, 51.402632657661314], [-127.8204345703125, 51.402632657661314], [-127.8204345703125, 51.7644403180351], [-128.2489013671875, 51.7644403180351], [-128.2489013671875, 51.402632657661314]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>