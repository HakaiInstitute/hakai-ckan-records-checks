---
hide:
  - navigation
  - title
---
# Summary

This page present a summary of the differrent metadata records distributed at <{{ ckan_url }}>.

Please refer to the [issue](issues/index.md) page for a summary of the different issues encountered.

## Spatial Distribution

This map present the differet polygons and coordinates associated with all the metadata records.

<div id="map"></div>


## Record Submission Timeseries

This diagram present the cumulative timeseries of the different metadata records made available on the 
hakai catalogue.

``` plotly
{{pio.to_json(timeseries_figure)}}
```

## Citations over time

The citations are retrieved from [DataCite](https://commons.datacite.org) for
each records assoicated with a DOI.

``` plotly
{{ pio.to_json(citations_over_time_figure)}}
```

## Records Summary Table

Download:
[Excel](catalog_summary.xlsx){ .md-button }
[CSV](catalog_summary.csv){ .md-button }

{{
  catalog_summary[[
    'Title','Catalogue','sum','projects','licence','progress','state',
    'ressource-type','eov','metadata_publication','metadata_revision',
    'doi',
    'citation_count','citations_over_time',
  ]]
  .sort_values(['metadata_publication','Title'],ascending=[0,1])
  .rename(columns={
    "sum": "Issues",
    "metadata_publication":"publication",
    "metadata_revision":"revision",
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
