---
title: McMullin Group Kelp Extent - Based on UAS Imagery - 2017
hide:
  - navigation
  - toc
---

# McMullin Group Kelp Extent - Based on UAS Imagery - 2017

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_d61f51c3-7614-465f-bf27-c78986ca07c3' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_d61f51c3-7614-465f-bf27-c78986ca07c3 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Geospatial 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 4 
    - **Vertical Extent**: [{'max': '0.0', 'min': '0.0'}] 
    - **Eov**: other 
    - **Doi**:  
    - **Metadata Publication**: 2022-03-03 
    - **Metadata Revision**: 2024-07-23 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_d61f51c3-7614-465f-bf27-c78986ca07c3' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                                            |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------------|
| ERROR   | Invalid resources.url.status_code: 404 for resources[1].url=https://drive.google.com/open?id=1jukkkqR46AAO14Q80XMWzwojRotSkuYS     |
| ERROR   | Empty resource name                                                                                                                |
| ERROR   | Invalid resources.url.status_code: 500 for resources[2].url=https://drive.google.com/open?id=1sBR_cDxyR5SiYtdVeRgJwqnhaGrTOYIB     |
| INFO    | No version                                                                                                                         |
| WARNING | Title contains acronyms potentially                                                                                                |
| WARNING | No DOI defined                                                                                                                     |
| WARNING | No funder                                                                                                                          |
| WARNING | Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'               |
| WARNING | Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'             |
| WARNING | Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute' |


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
            "name" : "McMullin Group Kelp Extent - Based on UAS Imagery - 2017"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.44315751, 52.02620636], [-128.37559157, 52.02620636], [-128.37559157, 52.07215005], [-128.44315751, 52.07215005], [-128.44315751, 52.02620636]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>