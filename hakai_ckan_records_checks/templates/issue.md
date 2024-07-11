---
hide:
  - toc
---
# {{ title }}

This page present the list of all the records associated with the issue: **{{ title }}**.

{{
  issues_table[['metadata_revision','title','level','message']]
  .sort_values(['metadata_revision','message'],ascending=[0,1])
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
    $(document).ready(function () {$("#issues_table").DataTable()});
  });
</script>
