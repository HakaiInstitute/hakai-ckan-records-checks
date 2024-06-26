---
title: Underwater Video Transects - Calvert Island - 2016
hide:
  - navigation
  - toc
---

# Underwater Video Transects - Calvert Island - 2016

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_62336906-31e6-4c32-968c-2312e703e08f' target='_blank'>link</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_62336906-31e6-4c32-968c-2312e703e08f 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Geospatial 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '100.0', 'min': '0.0'}] 
    - **Eov**: other 
    - **Metadata Created**: 2024-05-14T19:51:35.080964 
    - **Metadata Modified**: 2024-05-14T19:51:35.080970 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_62336906-31e6-4c32-968c-2312e703e08f' target='_blank'>link</a> 

### Issues

| level   | message                                                                                                                                 |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | No version                                                                                                                              |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Institute'                         |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute' |
| INFO    | Record isn't accesible via a standard data repository                                                                                   |

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
            "name" : "Underwater Video Transects - Calvert Island - 2016"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.13217163085938, 51.64870258356993], [-128.06350708007812, 51.64870258356993], [-128.06350708007812, 51.69958706405643], [-128.13217163085938, 51.69958706405643], [-128.13217163085938, 51.64870258356993]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>