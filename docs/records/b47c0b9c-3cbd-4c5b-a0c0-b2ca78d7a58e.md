---
title: Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada. Version 1.0.
hide:
  - navigation
  - toc
---

# Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada. Version 1.0.

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_6844547c-708e-437b-aef7-157b4d9d9bcb' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_6844547c-708e-437b-aef7-157b4d9d9bcb 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Watersheds, Oceanography 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '5.0', 'min': '0.0'}] 
    - **Eov**: nutrients, dissolvedOrganicCarbon, other 
    - **Doi**: 10.21966/n0h9-cq15 
    - **Metadata Publication**: 2022-03-29 
    - **Metadata Revision**: 2024-07-24 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_6844547c-708e-437b-aef7-157b4d9d9bcb' target='_blank'>link</a> 

<div id='map'></div>


## Citations

**Total Citations**: 1

### Citations over time

|   2022 |
|-------:|
|      1 |

### Citations

| relationship   | id                      | type   |   status_code | url                                                                             |
|:---------------|:------------------------|:-------|--------------:|:--------------------------------------------------------------------------------|
| citations      | 10.5194/bg-18-3029-2021 | dois   |           200 | https://bg.copernicus.org/articles/18/3029/2021/                                |
| parts          | 10.5194/bg-2020-350     | dois   |           200 | https://bg.copernicus.org/articles/18/3029/2021/bg-18-3029-2021-discussion.html |




## Issues
| level   | message                                                                                                    |
|:--------|:-----------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                        |
| INFO    | Contact missing ORCID: contact['individual-name']='Oliver, Allison A.' contact.get('organisation-name')='' |
| INFO    | Record isn't accesible via a standard data repository                                                      |


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
            "name" : "Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada. Version 1.0."
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.15445681, 51.61731613], [-127.95404703, 51.61731613], [-127.95404703, 51.71899959], [-128.15445681, 51.71899959], [-128.15445681, 51.61731613]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>