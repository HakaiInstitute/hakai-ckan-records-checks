---
title: {{ record['title']}}
hide:
  - navigation
  - toc
---

# {{ record['title'] }}

<a href='https://catalogue.hakai.org/dataset/{{ record['name'] }}' target='_blank'>View Record in Hakai Catalogue</a>

## Issues
{{ issues.sort_values('level').drop(columns=['record_id']).to_markdown(index=False) }}

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
            "name" : "{{ record['title'] }}"
        },
        "geometry": {{ record['spatial']}}
    }
    L.geoJSON(geojsonFeature).addTo(map);
   })
</script>