---
title: <a title='fcf0dff6-5e0e-4ab5-a3a5-fd1ee99460bc' href='/issues/fcf0dff6-5e0e-4ab5-a3a5-fd1ee99460bc/' target='_blank'>Geology - Calvert Island</a>
hide:
  - navigation
  - toc
---

# <a title='fcf0dff6-5e0e-4ab5-a3a5-fd1ee99460bc' href='/issues/fcf0dff6-5e0e-4ab5-a3a5-fd1ee99460bc/' target='_blank'>Geology - Calvert Island</a>

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
    - **Metadata Created**: 2024-05-14T19:46:48.983989 
    - **Metadata Modified**: 2024-05-14T19:46:48.983995 
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
            "name" : "<a title='fcf0dff6-5e0e-4ab5-a3a5-fd1ee99460bc' href='/issues/fcf0dff6-5e0e-4ab5-a3a5-fd1ee99460bc/' target='_blank'>Geology - Calvert Island</a>"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.2489013671875, 51.402632657661314], [-127.8204345703125, 51.402632657661314], [-127.8204345703125, 51.7644403180351], [-128.2489013671875, 51.7644403180351], [-128.2489013671875, 51.402632657661314]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>