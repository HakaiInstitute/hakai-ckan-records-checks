---
title: Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada
hide:
  - navigation
  - toc
---

# Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada

Records page: <a href='https://catalogue.hakai.org/dataset/ca-cioos_4fac74c8-f58c-46b0-87dc-ab70ce756880' target='_blank'>link</a>

???+ abstract "Metadata"

    - **Name**: ca-cioos_4fac74c8-f58c-46b0-87dc-ab70ce756880 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**: Geospatial 
    - **Progress**: underDevelopment 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 2 
    - **Vertical Extent**: [{'max': '500.0', 'min': '0.0'}] 
    - **Eov**: other 
    - **Doi**:  
    - **Metadata Publication**: 2022-03-11 
    - **Metadata Revision**: 2024-07-23 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_4fac74c8-f58c-46b0-87dc-ab70ce756880' target='_blank'>link</a> 

<div id='map'></div>




## Issues
| level   | message                                                                                                                                 |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------|
| INFO    | Title is greater than 60 characters                                                                                                     |
| INFO    | No version                                                                                                                              |
| INFO    | Record isn't accesible via a standard data repository                                                                                   |
| WARNING | Title contains acronyms potentially                                                                                                     |
| WARNING | No DOI defined                                                                                                                          |
| WARNING | No publisher                                                                                                                            |
| WARNING | Contact missing ORCID: contact['individual-name']='LiDAR Research Group, UNBC' contact.get('organisation-name')='Hakai Institute'       |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute' |


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
            "name" : "Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-125.3704833984375, 49.9229354544957], [-124.75524902343749, 49.9229354544957], [-124.75524902343749, 50.291094042311386], [-125.3704833984375, 50.291094042311386], [-125.3704833984375, 49.9229354544957]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>