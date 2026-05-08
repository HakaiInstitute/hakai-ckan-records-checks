---
hide:
 - toc
---
# Hakai Metadata Records Issue Summary

This page present a summary of issues detected on the [Hakai Catalogue]({{ ckan_url }}).

## Issue Distribution

```plotly
{{ figure_issues_distribution_json }}
```

## Records Summary

{{
  catalog_summary.reindex(columns=[
    'Title','metadata_publication','metadata_revision',
    'INFO','WARNING','ERROR'
  ]).fillna("")
  .sort_values(['metadata_publication','Title'],ascending=[0,1])
  .rename(columns={
    "sum": "Issues",
    "metadata_publication":"publication",
    "metadata_revision":"revision",
    "INFO":'inf.',
    "WARNING":"war.",
    "ERROR":"err.",
  })
  .to_html(
      render_links=True,
      table_id='records_table',
      escape=False,
      classes='table table-striped table-hover table-sm'
  )
}}

## Issues

{{
  issues_table.reindex(columns=['metadata_revision','title','level','message']).fillna("")
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
  });
</script>
