---
hide:
  - navigation
  - title
---
# Summary

This page present a summary of the different metadata records distributed at <{{ ckan_url }}>. Please refer to the [issue](issues/index.md) page for a summary of the different issues encountered. To view issues specific to a record, click the corresponding number in the Records Summary Table. 

## Overview

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2.5rem;">
{% for m in metrics %}
<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid {{ m['color'] }};box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">{{ m['value'] }}</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">{{ m['label'] }}</div>
  {% if m['delta'] %}
  <div style="font-size:0.8rem;font-weight:600;color:{{ m['color'] }};margin-top:0.5rem;">{{ m['delta'] }} since {{ m['previous_date'] }}</div>
  {% endif %}
</div>
{% endfor %}
</div>

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {{ figure_issues_distribution_json }};
    Plotly.newPlot('issue-distribution-chart', fig.data, fig.layout, {responsive: true});
  } else {
    setTimeout(waitForPlotly, 50);
  }
})();
</script>

## Records Summary Table

{{
  catalog_summary[catalog_summary['sum'] != '']
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
        order: [[1, 'desc']],
        columnDefs: [{
          targets: 1,
          render: function(data, type, row) {
            if (type !== 'display') {
              return parseInt(String(data).replace(/<[^>]*>/g, ''), 10) || 0;
            }
            return data;
          }
        }],
      });
    });
  });
</script>

Download:
[CSV](catalog_summary.csv){ .md-button }