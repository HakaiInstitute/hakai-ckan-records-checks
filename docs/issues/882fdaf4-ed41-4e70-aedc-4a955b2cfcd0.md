---
title: <a title='882fdaf4-ed41-4e70-aedc-4a955b2cfcd0' href='/issues/882fdaf4-ed41-4e70-aedc-4a955b2cfcd0/' target='_blank'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</a>
hide:
  - navigation
  - toc
---

# <a title='882fdaf4-ed41-4e70-aedc-4a955b2cfcd0' href='/issues/882fdaf4-ed41-4e70-aedc-4a955b2cfcd0/' target='_blank'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_2738ef2b-0c74-422d-a140-082e5f7b3793 
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
    - **Vertical Extent**: [{'max': '0.0', 'min': '0.0'}] 
    - **Eov**: other, invertebrateAbundanceAndDistribution 
    - **Metadata Created**: 2024-05-14T19:48:19.996896 
    - **Metadata Modified**: 2024-05-14T19:48:19.996903 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_2738ef2b-0c74-422d-a140-082e5f7b3793' target='_blank'>link</a> 

### Issues

| level   | message                                                                                                                       |
|:--------|:------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                           |
| INFO    | No version                                                                                                                    |
| WARNING | Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute' |
| INFO    | Record isn't accesible via a standard data repository                                                                         |

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
            "name" : "<a title='882fdaf4-ed41-4e70-aedc-4a955b2cfcd0' href='/issues/882fdaf4-ed41-4e70-aedc-4a955b2cfcd0/' target='_blank'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</a>"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.17701209, 51.62693395], [-128.1138407, 51.62693395], [-128.1138407, 51.67805576], [-128.17701209, 51.67805576], [-128.17701209, 51.62693395]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>