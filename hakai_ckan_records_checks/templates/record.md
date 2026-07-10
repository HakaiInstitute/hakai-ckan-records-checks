---
title: {{ record['title']}}
hide:
  - navigation
  - toc
---

# {{ record['title'] }}

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2rem;">
  <a href="https://catalogue.hakai.org/dataset/{{ record['name'] }}" style="flex:1;min-width:200px;padding:1rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-decoration:none;border-left:4px solid var(--md-primary-fg-color);box-shadow:0 1px 4px rgba(0,0,0,.08);display:flex;align-items:center;">
    <span style="font-weight:600;color:var(--md-typeset-color);">View Record in Hakai Catalogue</span>
  </a>
  {% if form_url %}
  <a href="{{ form_url }}" style="flex:1;min-width:200px;padding:1rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-decoration:none;border-left:4px solid var(--md-primary-fg-color);box-shadow:0 1px 4px rgba(0,0,0,.08);display:flex;align-items:center;">
    <span style="font-weight:600;color:var(--md-typeset-color);">Resolve Issues in Metadata Entry Form</span>
  </a>
  {% endif %}
</div>

{{ issues.drop(columns=['record_id']).rename(columns={'message': 'Issue'}).to_markdown(index=False) }}

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