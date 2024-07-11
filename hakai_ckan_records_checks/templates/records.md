---
hide:
  - navigation
  - title
  - toc
---
# Records

Search your record here:

{{
  catalog_summary[[
    'Title','Catalogue','sum','projects','licence','progress','state',
    'ressource-type','eov','metadata_publication','metadata_revision',
    'doi',
    'citation_count','citations_over_time','INFO','WARNING','ERROR'
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
      index=False,
      render_links=True,
      table_id='records_table',
      escape=False,
      classes='table table-striped table-hover table-sm'
  )
}}
Download:
[Excel](./catalog_summary.xlsx){ .md-button }
[CSV](./catalog_summary.csv){ .md-button }

<script>
  document.addEventListener("DOMContentLoaded", function() {
      $(document).ready(function () {
        $("#records_table").DataTable({
          scrollX: true,
          columnDefs: [{
              width: '300px',
              targets: 0,
            },{
              className: 'max-width-100', // Assign a custom class
              targets: [2, 3] // Example columns to have max-width
            }
          ]
        });
      });
  });
</script>
