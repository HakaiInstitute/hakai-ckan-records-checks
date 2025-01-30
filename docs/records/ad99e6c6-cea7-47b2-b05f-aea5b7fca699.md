---
title: Botanical Beach Drone Mapping - July 2020
hide:
  - navigation
  - toc
---

# Botanical Beach Drone Mapping - July 2020

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_656ea307-fed0-48ca-b5d8-1bc017dc52d2' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_656ea307-fed0-48ca-b5d8-1bc017dc52d2 
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
    - **Vertical Extent**: [{'max': '20.0', 'min': '0.0'}] 
    - **Eov**: other 
    - **Doi**:  
    - **Metadata Publication**: 2022-03-15 
    - **Metadata Revision**: 2024-07-24 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_656ea307-fed0-48ca-b5d8-1bc017dc52d2' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                                              |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------|
| ERROR   | Invalid resources.url.status_code: 404 for resources[0].url=https://drive.google.com/drive/folders/1aSgvM2D1n9dlaRqAjeHP5PdqAw7SWS2h |
| INFO    | No version                                                                                                                           |
| INFO    | Record isn't accesible via a standard data repository                                                                                |
| WARNING | No DOI defined                                                                                                                       |
| WARNING | Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'                 |
| WARNING | Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'   |
| WARNING | Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'   |


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
            "name" : "Botanical Beach Drone Mapping - July 2020"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-124.45265489, 48.52152402], [-124.43377214, 48.52152402], [-124.43377214, 48.53061904], [-124.45265489, 48.53061904], [-124.45265489, 48.52152402]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>