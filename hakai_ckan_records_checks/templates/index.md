---
hide:
  - navigation
---
# Summary

This page present a summary of issues detected from <{{ ckan_url }}>.

<div id="map"></div>


## Record Submission Timeseries

``` plotly
{{pio.to_json(timeseries_figure)}}
```

## Citations over time

``` plotly
{{ pio.to_json(citations_over_time_figure)}}
```

## Issue Distribution

``` plotly
{{ pio.to_json(figure) }}
```

## Record Table

Download:
[Excel](catalog_summary.xlsx){ .md-button }
[CSV](catalog_summary.csv){ .md-button }

{{
  catalog_summary[[
    'Title','Catalogue','sum','projects','licence','progress','state',
    'ressource-type','eov','metadata_publication','metadata_revision',
    'doi',
    'citation_count','citations_over_time',
    'INFO','WARNING','ERROR'
  ]]
  .sort_values(['metadata_publication','Title'],ascending=[0,1])
  .rename(columns={
    "sum": "Issues",
    "metadata_publication":"publication",
    "metadata_revision":"revision",
    "INFO":'inf.',
    "WARNING":"war.",
    "ERROR":"err.",
    "ressource-type":"ressour type",
    "citation_count": "Citations",
    "citation_over_time": "Citation Distribution"
  })
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
  issues_table[['metadata_revision','title','level','message']]
  .sort_values(['metadata_revision','level','message'],ascending=[0,0,1])
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
          width: '300px',
          targets: 1,
        },{
          className: 'max-width-100', // Assign a custom class
          targets: [2, 3] // Example columns to have max-width
        }
        ]
      });
    });
    $(document).ready(function () {
      $("#issues_table").DataTable();
    });
  })
</script>
