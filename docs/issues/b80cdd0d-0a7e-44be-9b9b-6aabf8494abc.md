---
title: Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory
hide:
  - navigation
  - toc
---

# Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_c3958106-fc49-44bd-8227-bfc3e8bcb58c' target='_blank'>link</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_c3958106-fc49-44bd-8227-bfc3e8bcb58c 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Airborne Coastal Observatory 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 2 
    - **Vertical Extent**: [{'max': '150.0', 'min': '0.0'}] 
    - **Eov**: other 
    - **Doi**: 10.21966/wfcv-n753 
    - **Metadata Publication**: 2022-03-01 
    - **Metadata Revision**: 2024-03-20 
    - **Citation Count**: 0 
    - **Citations Over Time**: [] 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_c3958106-fc49-44bd-8227-bfc3e8bcb58c' target='_blank'>link</a> 

### Issues

| level   | message                                                                                                                             |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                                 |
| INFO    | No version                                                                                                                          |
| WARNING | Contact missing ORCID: contact['individual-name']='Airborne Coastal Observatory' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'   |
| WARNING | Contact missing ORCID: contact['individual-name']='Airborne Coastal Observatory' contact.get('organisation-name')='Hakai Institute' |

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
            "name" : "Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-129.5, 52.65], [-129.4, 52.65], [-129.4, 52.7], [-129.5, 52.7], [-129.5, 52.65]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>