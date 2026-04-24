---
hide:
  - navigation
  - title
---
# Summary

This page present a summary of the differrent metadata records distributed at <{{ ckan_url }}>.

Please refer to the [issue](issues/index.md) page for a summary of the different issues encountered.

## Records Summary Table

Download:
[Excel](catalog_summary.xlsx){ .md-button }
[CSV](catalog_summary.csv){ .md-button }

{{
  catalog_summary
  .assign(**{'Last Revised': lambda df: df['metadata_revision'].fillna(df['metadata_publication'])})
  .sort_values(['metadata_publication','Title'],ascending=[0,1])
  [['Title','Catalogue','sum','projects','Last Revised']]
  .rename(columns={
    "sum": "Issues",
    "projects": "Project"
  })
  .to_html(
      render_links=True,
      table_id='records_table',
      escape=False,
      index=False,
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
      var table = $("#records_table").DataTable({
        scrollX: true,
        dom: 'lfrtip',
        pageLength: 10,
        columnDefs: [{
          width: '300px',
          targets: 0,
        }]
      });

      table.columns().every(function () {
        var column = this;
        var input = $('<br><input type="text" placeholder="Filter..." style="width:90%;font-size:0.8em">')
          .on('keyup change clear', function () {
            column.search(this.value).draw();
          });
        $(column.header()).append(input);
      });
    });
    $(document).ready(function () {
      $("#issues_table").DataTable();
    });
  })
</script>
