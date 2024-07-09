---
title: {{ record['title']}}
hide:
  - navigation
  - toc
---

# {{ record['title'] }}

Records page: {{ record['Catalogue'] }}

???+ abstract "Metadata"
{% for key,value in record.to_dict().items() if key not in ('ERROR','WARNING','INFO','sum','title','spatial','Title','citation_count','citations_over_time','relationships') %}
    - **{{ key.replace(('-'),' ').replace('_',' ').title() }}**: {{value}} {% endfor %}

<div id='map'></div>

{% if record['citation_count'] and record['citation_count'] > 0 %}
!!! info "Citations"

    **Total Citations**: {{ record['citation_count']}}

    **Citations over time**:
    {% for line in pd.DataFrame(record['citations_over_time']).set_index('year').T.to_markdown(index=False).split('\n') %}
    {{ line }}{% endfor %}

    **Citations**:
    {% for line in pd.DataFrame(record['relationships']).to_markdown(index=False).split('\n') %}
    {{ line }}{% endfor %}
    
{% endif %}

{% if not issues.empty %}
!!! warning "Issues"
    {% for line in issues.sort_values('level').drop(columns=['record_id']).to_markdown(index=false).split('\n') %}
    {{ line }}{% endfor %}
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