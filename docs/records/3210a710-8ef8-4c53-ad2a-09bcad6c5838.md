---
title: Nearshore Macrophyte Stable Isotopes - BC Central Coast
hide:
  - navigation
  - toc
---

# Nearshore Macrophyte Stable Isotopes - BC Central Coast

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_288ea4b2-3706-4256-8146-02bd0265585b' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_288ea4b2-3706-4256-8146-02bd0265585b 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Nearshore 
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 1 
    - **Vertical Extent**: [{'max': '10.0', 'min': '0.0'}] 
    - **Eov**: stableCarbonIsotopes, macroalgalCanopyCoverAndComposition, seagrassCoverAndComposition 
    - **Doi**: 10.21966/q31x-qg72 
    - **Metadata Publication**: 2022-01-13 
    - **Metadata Revision**: 2024-08-02 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_288ea4b2-3706-4256-8146-02bd0265585b' target='_blank'>link</a> 

<div id='map'></div>


## Citations

**Total Citations**: 1

### Citations over time

|   2024 |
|-------:|
|      1 |

### Citations

| relationship   | id                 | type   |   status_code | url                                                                               |
|:---------------|:-------------------|:-------|--------------:|:----------------------------------------------------------------------------------|
| citations      | 10.21966/hpqq-0k76 | dois   |           200 | https://catalogue.hakai.org/dataset/ca-cioos_9201118a-b0c4-470f-a76f-396bacc5e93e |




## Issues
| level   | message                                                                                                                       |
|:--------|:------------------------------------------------------------------------------------------------------------------------------|
| ERROR   | Record DOI HTTPS link is failling: https://doi.org/10.21966/q31x-qg72 status_code=404                                         |
| INFO    | Record isn't accesible via a standard data repository                                                                         |
| WARNING | Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute' |


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
            "name" : "Nearshore Macrophyte Stable Isotopes - BC Central Coast"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.62224808, 51.28805197], [-127.44960574, 51.28805197], [-127.44960574, 52.00866824], [-128.62224808, 52.00866824], [-128.62224808, 51.28805197]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>