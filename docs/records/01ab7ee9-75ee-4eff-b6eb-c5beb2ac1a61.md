---
title: High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA
hide:
  - navigation
  - toc
---

# High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_4a09d56b-b120-46c8-9263-ae3c42a02e9b' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_4a09d56b-b120-46c8-9263-ae3c42a02e9b 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Oceanography 
    - **Progress**: onGoing 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 2 
    - **Vertical Extent**: [{'max': '4.3', 'min': '4.3'}] 
    - **Eov**: inorganicCarbon, seaSurfaceTemperature, seaSurfaceSalinity 
    - **Doi**: 10.25921/kmam-ct93 
    - **Metadata Publication**: 2023-01-24 
    - **Metadata Revision**: 2025-04-23 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_4a09d56b-b120-46c8-9263-ae3c42a02e9b' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                                              |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                                  |
| INFO    | DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0246099 |
| INFO    | Contact missing ORCID: contact['individual-name']='Hales, Burke' contact.get('organisation-name')='Oregon State University'          |
| WARNING | Title contains acronyms potentially                                                                                                  |


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
            "name" : "High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA"
        },
        "geometry": {'type': 'Point', 'coordinates': [-131.5954, 55.315]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>