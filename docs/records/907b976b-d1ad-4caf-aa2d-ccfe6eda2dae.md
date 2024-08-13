---
title: Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0
hide:
  - navigation
  - toc
---

# Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_2a92ca16-f5c6-4362-acea-6bb5117b8d65' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_2a92ca16-f5c6-4362-acea-6bb5117b8d65 
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
    - **Doi**:  
    - **Metadata Publication**: 2022-03-02 
    - **Metadata Revision**: 2024-07-23 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_2a92ca16-f5c6-4362-acea-6bb5117b8d65' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                                                    |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                                        |
| INFO    | No version                                                                                                                                 |
| INFO    | Record isn't accesible via a standard data repository                                                                                      |
| WARNING | No DOI defined                                                                                                                             |
| WARNING | No funder                                                                                                                                  |
| WARNING | Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'                     |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Reshitnyk, Luba' contact['organisation-name']='Hakai Institute'             |
| WARNING | Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'         |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Technology Team, Geospatial' contact['organisation-name']='Hakai Institute' |
| WARNING | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Institute'                            |
| WARNING | Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'         |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Technology Team, Geospatial' contact['organisation-name']='Hakai Institute' |


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
            "name" : "Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-130.35642493, 50.22213452], [-126.18162025, 50.22213452], [-126.18162025, 52.9911972], [-130.35642493, 52.9911972], [-130.35642493, 50.22213452]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>