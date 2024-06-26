---
hide:
  - navigation
  - toc
---

# [Summary]({{ckan_url}})

This page present a summary of:

- [Summary](#summary)
  - [Records Summary](#records-summary)
  - [Issues Summary](#issues-summary)

<div id="map"></div>

``` plotly
{{ pio.to_json(figure) }}
```

## Records Summary

Download:
[Excel](catalog_summary.xlsx){ .md-button }
[CSV](catalog_summary.csv){ .md-button }

{{
    catalog_summary
    .drop(columns=['id','name','spatial','vertical-extent','organization','private'])
    .to_markdown()
}}

## Issues Summary

Download:
[Excel](issues_list.xlsx){ .md-button }
[CSV](issues_list.csv){ .md-button }

{{
    issues_table[['title','level','message']]
    .to_markdown(
        index=False
    )
}}

<script>
  document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map').setView([51.505, -125.09],3);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    var geojsonFeatures = [
        {% for id,row in catalog_summary.dropna(subset=['name','spatial'], how='any').iterrows() %}
        {
            "type":"Feature",
            "properties": {
                "name": "{{row['name']}}",
                "row_id": "{{id}}"
            },
            "geometry": {{row['spatial']}}
        },
        {% endfor %}
    ];
    L.geoJSON(geojsonFeatures).addTo(map);
  })
</script>
