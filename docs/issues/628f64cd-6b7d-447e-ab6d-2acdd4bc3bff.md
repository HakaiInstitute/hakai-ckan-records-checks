---
title: <a title='628f64cd-6b7d-447e-ab6d-2acdd4bc3bff' href='issues/628f64cd-6b7d-447e-ab6d-2acdd4bc3bff/' target='_blank'>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</a>
hide:
  - navigation
  - toc
---

# <a title='628f64cd-6b7d-447e-ab6d-2acdd4bc3bff' href='issues/628f64cd-6b7d-447e-ab6d-2acdd4bc3bff/' target='_blank'>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_12f951d4-4155-4c05-969d-a7158412f579 
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
    - **Vertical Extent**: [{'max': '1000.0', 'min': '0.0'}] 
    - **Eov**: other, marineTurtlesBirdsMammalsAbundanceAndDistribution 
    - **Metadata Created**: 2024-05-14T19:46:31.498653 
    - **Metadata Modified**: 2024-05-14T19:46:31.498660 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_12f951d4-4155-4c05-969d-a7158412f579' target='_blank'>link</a> 

### Issues

| level   | message                                                                                                                 |
|:--------|:------------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                     |
| INFO    | No version                                                                                                              |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute' |
| INFO    | Record isn't accesible via a standard data repository                                                                   |

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
            "name" : "<a title='628f64cd-6b7d-447e-ab6d-2acdd4bc3bff' href='issues/628f64cd-6b7d-447e-ab6d-2acdd4bc3bff/' target='_blank'>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</a>"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.60227432, 51.39074678], [-127.47434441, 51.39074678], [-127.47434441, 52.07117353], [-128.60227432, 52.07117353], [-128.60227432, 51.39074678]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>