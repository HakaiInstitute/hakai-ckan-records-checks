---
title: Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016
hide:
  - navigation
  - toc
---

# Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_804b5b42-5550-4620-b789-7c2fe9572c03' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_804b5b42-5550-4620-b789-7c2fe9572c03 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Oceanography 
    - **Progress**: underDevelopment 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '0.0', 'min': '0.0'}] 
    - **Eov**: other, zooplanktonBiomassAndDiversity 
    - **Doi**: 10.21966/bhqd-9361 
    - **Metadata Publication**: 2022-02-04 
    - **Metadata Revision**: 2024-07-23 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_804b5b42-5550-4620-b789-7c2fe9572c03' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                                                       |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR   | Record DOI HTTPS link is failling: https://doi.org/10.21966/bhqd-9361 status_code=502                                                         |
| INFO    | Title is greater than 60 characters                                                                                                           |
| INFO    | No version                                                                                                                                    |
| INFO    | Contact missing ORCID: contact['individual-name']='Mahara, Natalie' contact.get('organisation-name')='University of British Columbia'         |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Mahara, Natalie' contact['organisation-name']='University of British Columbia' |
| INFO    | Contact missing ORCID: contact['individual-name']='Hunt, Brian' contact.get('organisation-name')='University of British Columbia'             |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Hunt, Brian' contact['organisation-name']='University of British Columbia'     |
| INFO    | Record isn't accesible via a standard data repository                                                                                         |
| WARNING | No funder                                                                                                                                     |
| WARNING | No publisher                                                                                                                                  |


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
            "name" : "Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-126.93452704, 49.56730131], [-124.18481219, 49.56730131], [-124.18481219, 50.90762515], [-126.93452704, 50.90762515], [-126.93452704, 49.56730131]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>