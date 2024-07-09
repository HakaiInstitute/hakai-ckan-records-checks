---
title: Real-Time Provisional High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected from Kodiak, Alaska, USA
hide:
  - navigation
  - toc
---

# Real-Time Provisional High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected from Kodiak, Alaska, USA

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_82fccfae-965f-4e4e-b510-0000ae044824' target='_blank'>link</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_82fccfae-965f-4e4e-b510-0000ae044824 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**:  
    - **Progress**: onGoing 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '0.0', 'min': '0.0'}] 
    - **Eov**: seaSurfaceTemperature, inorganicCarbon, seaSurfaceSalinity 
    - **Doi**:  
    - **Metadata Publication**: 2022-11-08 
    - **Metadata Revision**: 2022-11-08 
    - **Citation Count**:  
    - **Citations Over Time**:  
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_82fccfae-965f-4e4e-b510-0000ae044824' target='_blank'>link</a> 

### Issues

| level   | message                                                                                                                                                            |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR   | No projects associated                                                                                                                                             |
| WARNING | Title contains acronyms potentially                                                                                                                                |
| INFO    | Title is greater than 60 characters                                                                                                                                |
| INFO    | No version                                                                                                                                                         |
| WARNING | No DOI defined                                                                                                                                                     |
| WARNING | No funder                                                                                                                                                          |
| WARNING | No publisher                                                                                                                                                       |
| WARNING | Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'                                                |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Evans, Wiley' contact['organisation-name']='Hakai Institute'                                        |
| WARNING | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Institute'                                                    |
| INFO    | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='NOAA'                                                               |
| INFO    | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='University of Alaska Fairbanks Ocean Acidification Research Center' |
| INFO    | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Dakunalytics'                                                       |
| WARNING | Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'                                                |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Evans, Wiley' contact['organisation-name']='Hakai Institute'                                        |
| ERROR   | Invalid resources.url.status_code: 404 for resources[0].url=https://catalogue.hakai.org/erddap/tabledap/KodiakBoL5min.html                                         |

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
            "name" : "Real-Time Provisional High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected from Kodiak, Alaska, USA"
        },
        "geometry": {'type': 'Point', 'coordinates': [-152.41, 57.79]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>