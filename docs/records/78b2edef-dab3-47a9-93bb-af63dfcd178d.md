---
title: Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)
hide:
  - navigation
  - toc
---

# Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_d049351d-b806-461f-85fb-451f100fd7d6' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_d049351d-b806-461f-85fb-451f100fd7d6 
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
    - **Vertical Extent**: [{'max': '1.0', 'min': '1.0'}] 
    - **Eov**: oxygen, inorganicCarbon, seaSurfaceTemperature, seaSurfaceSalinity 
    - **Doi**: 10.25921/9vnv-0g64 
    - **Metadata Publication**: 2022-12-01 
    - **Metadata Revision**: 2026-02-20 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_d049351d-b806-461f-85fb-451f100fd7d6' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                                                   |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                                       |
| INFO    | No version                                                                                                                                |
| INFO    | DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0247208      |
| INFO    | Contact missing ORCID: contact['individual-name']='Whitehead, Chris' contact.get('organisation-name')='Sitka Tribe of Alaska'             |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Whitehead, Chris' contact['organisation-name']='Sitka Tribe of Alaska'     |
| INFO    | Contact missing ORCID: contact['individual-name']='Lanphier, Karie' contact.get('organisation-name')='Sitka Tribe of Alaska'              |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Lanphier, Karie' contact['organisation-name']='Sitka Tribe of Alaska'      |
| INFO    | Contact missing ORCID: contact['individual-name']='Peterson, Willoughby' contact.get('organisation-name')='Sitka Tribe of Alaska'         |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Peterson, Willoughby' contact['organisation-name']='Sitka Tribe of Alaska' |
| INFO    | Contact missing ORCID: contact['individual-name']='Kennedy, Estjer' contact.get('organisation-name')='Sitka Tribe of Alaska'              |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Kennedy, Estjer' contact['organisation-name']='Sitka Tribe of Alaska'      |
| INFO    | Contact missing ORCID: contact['individual-name']='Hales, Burke' contact.get('organisation-name')='Oregon State University'               |
| WARNING | Title contains acronyms potentially                                                                                                       |


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
            "name" : "Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)"
        },
        "geometry": {'type': 'Point', 'coordinates': [-135.3456, 57.0526]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>