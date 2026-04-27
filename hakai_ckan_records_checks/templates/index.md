---
hide:
  - navigation
  - title
---
# Summary

This page present a summary of the different metadata records distributed at <{{ ckan_url }}>. Please refer to the [issue](issues/index.md) page for a summary of the different issues encountered. To view issues specific to a record, click the corresponding number in the Records Summary Table. 

## Issue Distribution

``` plotly
{{ pio.to_json(figure_issues_distribution) }}
```

## Records Summary Table

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

Download:
[CSV](catalog_summary.csv){ .md-button }