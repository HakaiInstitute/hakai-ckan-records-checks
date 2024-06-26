---
title: Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017
hide:
  - navigation
  - toc
---

# Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_1769a04e-b77b-409b-8e48-bc2098bbad3e' target='_blank'>link</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_1769a04e-b77b-409b-8e48-bc2098bbad3e 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Juvenile Salmon Program 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 2 
    - **Vertical Extent**: [{'max': '9.0', 'min': '0.0'}] 
    - **Eov**: other 
    - **Metadata Created**: 2024-05-14T19:56:36.379055 
    - **Metadata Modified**: 2024-05-14T19:56:36.379062 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_1769a04e-b77b-409b-8e48-bc2098bbad3e' target='_blank'>link</a> 

### Issues

| level   | message                                                                                                                |
|:--------|:-----------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                    |
| INFO    | No version                                                                                                             |
| WARNING | Contact missing ORCID: contact['individual-name']='Janusson, Carly' contact.get('organisation-name')='Hakai Institute' |
| INFO    | Record isn't accesible via a standard data repository                                                                  |

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
            "name" : "Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-127.11545814, 49.78433133], [-124.85227454, 49.78433133], [-124.85227454, 50.81587848], [-127.11545814, 50.81587848], [-127.11545814, 49.78433133]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>