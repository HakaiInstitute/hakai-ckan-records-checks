---
title: <a title='1ceb46a4-fe5b-43f0-a7b9-ff0ff1a1febe' href='/issues/1ceb46a4-fe5b-43f0-a7b9-ff0ff1a1febe/' target='_blank'>Kelp Canopy Extent 2006 - NW Calvert Island</a>
hide:
  - navigation
  - toc
---

# <a title='1ceb46a4-fe5b-43f0-a7b9-ff0ff1a1febe' href='/issues/1ceb46a4-fe5b-43f0-a7b9-ff0ff1a1febe/' target='_blank'>Kelp Canopy Extent 2006 - NW Calvert Island</a>

<div id='map'></div>

!!! info "Metadata"
    
    - **Name**: ca-cioos_4034f474-4d52-4a9e-9650-f3c6bd5011e0 
    - **Organization**: Hakai Institute 
    - **Ressource Type**: dataset 
    - **Licence**: CC-BY-4.0 
    - **Private**: False 
    - **Projects**:  
    - **Progress**: completed 
    - **State**: active 
    - **Type**: dataset 
    - **Distributor**: Hakai Institute 
    - **Resources Count**: 2 
    - **Vertical Extent**: [{'max': '50.0', 'min': '0.0'}] 
    - **Eov**: other 
    - **Metadata Created**: 2024-05-14T19:58:48.002041 
    - **Metadata Modified**: 2024-05-14T19:58:48.002049 
    - **Catalogue**: <a href='https://catalogue.hakai.org/dataset/ca-cioos_4034f474-4d52-4a9e-9650-f3c6bd5011e0' target='_blank'>link</a> 

### Issues

| level   | message                                                                                                                                         |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR   | No projects associated                                                                                                                          |
| INFO    | No version                                                                                                                                      |
| WARNING | No DOI defined                                                                                                                                  |
| WARNING | No funder                                                                                                                                       |
| WARNING | No publisher                                                                                                                                    |
| WARNING | Contact missing ORCID: contact['individual-name']='Keith Holmes, Jenn Burt' contact.get('organisation-name')='Hakai Institute'                  |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Keith Holmes, Jenn Burt' contact['organisation-name']='Hakai Institute'          |
| WARNING | Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Institute'                                 |
| WARNING | Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'         |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Hakai Geospatial Technology Team' contact['organisation-name']='Hakai Institute' |
| WARNING | Contact missing ORCID: contact['individual-name']='Keith Holmes, Jenn Burt' contact.get('organisation-name')='Hakai Institute'                  |
| WARNING | Contact missing organization ROR:  contact['individual-name']='Keith Holmes, Jenn Burt' contact['organisation-name']='Hakai Institute'          |

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
            "name" : "<a title='1ceb46a4-fe5b-43f0-a7b9-ff0ff1a1febe' href='/issues/1ceb46a4-fe5b-43f0-a7b9-ff0ff1a1febe/' target='_blank'>Kelp Canopy Extent 2006 - NW Calvert Island</a>"
        },
        "geometry": {'type': 'Polygon', 'coordinates': [[[-128.1719970703125, 51.63229666135982], [-128.10985565185547, 51.63229666135982], [-128.10985565185547, 51.68362528576685], [-128.1719970703125, 51.68362528576685], [-128.1719970703125, 51.63229666135982]]]}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>