---
title: {{ record['title']}}
hide:
  - navigation
  - toc
---

# {{ record['title'] }}

View Record in Hakai Catalogue: <a href="https://catalogue.hakai.org/dataset/{{ record['name'] }}" target="_blank">https://catalogue.hakai.org/dataset/{{ record['name'] }}</a>

{{ issues.drop(columns=['record_id']).rename(columns={'message': 'Issue'}).to_markdown(index=False) }}
{% if form_url %}

<a href="{{ form_url }}" target="_blank">Click here to resolve these issues in the Metadata Entry Form</a>
{% endif %}

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