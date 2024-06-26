---
title: {{ record['title']}}
hide:
  - navigation
  - toc
---

# {{ record['title'] }}

<div id='map'></div>

!!! info "Metadata"
    {% for key,value in record.to_dict().items() if key not in ('ERROR','WARNING','INFO','sum','title','spatial') %}
    - **{{ key.replace(('-'),' ').replace('_',' ').title() }}**: {{value}} {% endfor %}

### Issues

{{
    issues
    .drop(columns=['record_id'])
    .to_markdown(index=false)
}}

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