---
hide:
  - navigation
  - toc
  - title
---
#

This page present a summary of issues detected from <{{ ckan_url }}>.

<div id="map"></div>

``` plotly
{{ pio.to_json(figure) }}
```

## Records Summary

Download:
[Excel](catalog_summary.xlsx){ .md-button }
[CSV](catalog_summary.csv){ .md-button }

{{
  catalog_summary[['Title','Catalogue','sum','projects','licence','progress','state','ressource-type','eov','metadata_created','metadata_modified','INFO','WARNING','ERROR']]
  .rename(columns={"sum": "Issues"})
  .to_html(
      render_links=True,
      table_id='records_table',
      escape=False,
      classes='table table-striped table-hover table-sm'
  )
}}

## Issues Summary

Download:
[Excel](issues_list.xlsx){ .md-button }
[CSV](issues_list.csv){ .md-button }

{{
  issues_table[['title','level','message']]
  .to_html(
    index=False,
    render_links=True,
    table_id='issues_table',
    escape=False,
    classes='table table-striped table-hover table-sm'
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

    $(document).ready(function () {
      $("#records_table").DataTable({
        scrollX: true,
        columnDefs: [{
          width: '700px',
          targets: 1,
        }]
      });
    });
    $(document).ready(function () {
      $("#issues_table").DataTable();
    });
  })
</script>
