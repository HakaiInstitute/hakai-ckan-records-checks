---
title: Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia
hide:
  - navigation
  - toc
---

# Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_dd325fc4-033c-4696-b38d-0ac883ad67eb' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_dd325fc4-033c-4696-b38d-0ac883ad67eb 
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
    - **Vertical Extent**: [{'max': '2.0', 'min': '2.0'}] 
    - **Eov**: oxygen, seaSurfaceSalinity, seaSurfaceTemperature, inorganicCarbon 
    - **Doi**: 10.25921/jq11-2268 
    - **Metadata Publication**: 2021-06-11 
    - **Metadata Revision**: 2024-03-14 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_dd325fc4-033c-4696-b38d-0ac883ad67eb' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                                                                                                    |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                                                                                        |
| INFO    | DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0209049                                                       |
| INFO    | Contact missing ORCID: contact['individual-name']='Lebon, Geoffrey T.' contact.get('organisation-name')='University of Washington Joint Institute for the Study of the Atmosphere'         |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Lebon, Geoffrey T.' contact['organisation-name']='University of Washington Joint Institute for the Study of the Atmosphere' |
| INFO    | Contact missing ORCID: contact['individual-name']='Harrington, Christen D.' contact.get('organisation-name')='Alaska Department of Transportation'                                         |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Harrington, Christen D.' contact['organisation-name']='Alaska Department of Transportation'                                 |
| INFO    | Contact missing ORCID: contact['individual-name']='Bidlack, Allison' contact.get('organisation-name')='University of Alaska Southeast, Alaska Coastal Rainforest Center'                   |
| INFO    | Contact missing organization ROR:  contact['individual-name']='Bidlack, Allison' contact['organisation-name']='University of Alaska Southeast, Alaska Coastal Rainforest Center'           |
| WARNING | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Institute'                                                                            |


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
            "name" : "Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-135.7, 48.6], [-122.5, 48.6], [-122.5, 59.5], [-135.7, 59.5], [-135.7, 48.6]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>