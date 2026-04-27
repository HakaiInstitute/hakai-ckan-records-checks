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
[CSV](catalog_summary.csv){ .md-button }

{{
  catalog_summary
  .sort_values(['metadata_publication','Title'],ascending=[0,1])
  [['Title','sum','projects','Last Revised']]
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
    $(document).ready(function () {
      $("#records_table").DataTable({
        scrollX: true,
        pageLength: 10,
      });
    });
  });
</script>
