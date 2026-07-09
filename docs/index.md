---
hide:
  - navigation
  - toc
---

<style>.md-content__inner > h1 { display: none; }</style>

*Last updated: 2026-07-09*

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2.5rem;">

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">267</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Total Records</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-07-08</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">20</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Records with Issues</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-07-08</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">97.0%</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">% Records with DOI</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-07-08</div>
  
  
</div>

</div>

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {"data": [{"hovertemplate": "Number of Records with Issue=%{text}<br>message=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#AA2026", "pattern": {"shape": ""}}, "name": "", "orientation": "h", "showlegend": false, "text": [2.0, 2.0, 3.0, 4.0, 7.0, 8.0], "textposition": "outside", "x": [2, 2, 3, 4, 7, 8], "xaxis": "x", "y": ["No funder", "No DOI defined", "Tentative dataset should not have a version", "No version", "Metadata mismatch", "Invalid Resource URL"], "yaxis": "y", "type": "bar", "cliponaxis": false}], "layout": {"template": {"data": {"scatter": [{"type": "scatter"}]}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "Number of Records with Issue"}, "tickformat": "d"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {}, "tickfont": {"size": 10}, "linecolor": "black", "automargin": true}, "legend": {"tracegroupgap": 0}, "margin": {"t": 20, "l": 0, "r": 60, "b": 40}, "barmode": "relative", "plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)", "showlegend": false}};
    var el = document.getElementById('issue-distribution-chart');
    Plotly.newPlot(el, fig.data, fig.layout, {responsive: true}).then(function() {
      el.on('plotly_click', function(data) {
        var label = data.points[0].y;
        var slug = label.replace(/[.'"]/g, '').replace(/[^a-zA-Z0-9]/g, '-').toLowerCase().replace(/-+/g, '-');
        window.location.href = 'issues/' + slug + '/';
      });
    });
  } else {
    setTimeout(waitForPlotly, 50);
  }
})();
</script>

## Issues By Record

<table border="1" class="dataframe table table-striped table-hover table-sm" id="records_table">
  <thead>
    <tr style="text-align: right;">
      <th>Title</th>
      <th>Issues</th>
      <th>Project</th>
      <th>Last Revised</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_84820f31-b6db-479c-a47e-f22f2899b4d2'>Biogeochemical Sampling of 28 Streams on Vancouver Island</a></td>
      <td><a title='0e92249d-74e1-4253-a8a5-876d08a8ff65' href='records/0e92249d-74e1-4253-a8a5-876d08a8ff65'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_39a83551-ab8e-45be-a564-cece4b229371'>Zooplankton taxonomic abundance and biomass along the BC Coast</a></td>
      <td><a title='139df6dd-772b-424f-b830-30a5ba6abfc6' href='records/139df6dd-772b-424f-b830-30a5ba6abfc6'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1d142201-cbbe-4c58-b2c2-1feeac112c51'>iTrack Oysters September 2023 Experiment - Environmental and Oyster Health Data</a></td>
      <td><a title='bd461764-55b0-4c63-935a-5e9d1d5a6fed' href='records/bd461764-55b0-4c63-935a-5e9d1d5a6fed'>1</a></td>
      <td>Wet Lab</td>
      <td>2025-05-16</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_31ac855d-bf15-42d8-b20d-754638202c66'>Sea Stars 2024 Experiment - Environmental Data</a></td>
      <td><a title='da040f55-984d-490d-b917-a67856de4bac' href='records/da040f55-984d-490d-b917-a67856de4bac'>1</a></td>
      <td>Wet Lab</td>
      <td>2026-06-16</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_78818ed7-ec26-4004-afa1-137741ddda1e'>Calliarthron 2023 Experiment - Environmental Data</a></td>
      <td><a title='e4038a43-060b-474e-b6f2-ea68d0081053' href='records/e4038a43-060b-474e-b6f2-ea68d0081053'>1</a></td>
      <td>Wet Lab</td>
      <td>2025-05-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9fafb4c8-e61f-4372-ac71-c1ddbe57d80c'>Data record does not exist anymore: Geomorphology - Calvert Island</a></td>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='records/49967494-a7b6-4128-b336-671971d1e2c6'>2</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2026-06-09</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_33a367c1-2706-4301-af99-4455fbe189a0'>Cryosphere Snow Surveys Southwest British Columbia - Airborne Coastal Observatory</a></td>
      <td><a title='6a28454e-107a-4059-9b7d-e43bf8ee693b' href='records/6a28454e-107a-4059-9b7d-e43bf8ee693b'>3</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-05-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3efdccb0-08ef-4e90-ac91-72969f94a99a'>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='f1aee211-bfab-46fd-b650-c5cacb782f40' href='records/f1aee211-bfab-46fd-b650-c5cacb782f40'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-07-06</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1755dc37-8d33-4158-8041-c22536fd5771'>Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, BC, Canada (Provisional)</a></td>
      <td><a title='bf7c05e8-510d-4449-9e81-4c358ff3f440' href='records/bf7c05e8-510d-4449-9e81-4c358ff3f440'>1</a></td>
      <td>Oceanography</td>
      <td>2026-07-07</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d55021c3-a142-4e14-8208-36c9826c1893'>Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, BC, Canada (Research)</a></td>
      <td><a title='8882a149-fabd-4ecd-98d3-68a2a88aee38' href='records/8882a149-fabd-4ecd-98d3-68a2a88aee38'>1</a></td>
      <td>Oceanography</td>
      <td>2026-05-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2d693456-7e65-46be-95d7-6bb697320017'>Water Level and Weather Station Time Series, Pruth Bay, Kwakshua Channel, Central Coast, BC, Canada (Provisional)</a></td>
      <td><a title='11051c56-8d67-43fc-a13c-b706e851a5a4' href='records/11051c56-8d67-43fc-a13c-b706e851a5a4'>1</a></td>
      <td>Oceanography, Watersheds</td>
      <td>2026-07-07</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_86343dd1-28d0-4d02-8eaf-402d51a7fef7'>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program (Provisional)</a></td>
      <td><a title='acd6c43f-6cbd-43c8-9bff-7d9ae6630295' href='records/acd6c43f-6cbd-43c8-9bff-7d9ae6630295'>1</a></td>
      <td>Juvenile Salmon Program</td>
      <td>2026-07-07</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_532c06ad-0b55-4e86-9088-cec970a0a8e1'>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' href='records/ee2eec87-7a78-4a7f-87b7-54347a6c3b2f'>3</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2024-12-05</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c981d76-5fea-44af-904f-58b159838b0a'>Stream Event Sampling - Calvert Island</a></td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='records/def2a409-2319-4e8c-a584-9a467f044ada'>1</a></td>
      <td>Watersheds, Geospatial</td>
      <td>2026-06-09</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9201118a-b0c4-470f-a76f-396bacc5e93e'>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</a></td>
      <td><a title='55e7c337-02e8-4200-8ea9-88241d978f96' href='records/55e7c337-02e8-4200-8ea9-88241d978f96'>3</a></td>
      <td>Oceanography</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7de69ca8-b3f3-4761-b441-dfc9e63b1fbc'>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</a></td>
      <td><a title='70f29525-f17b-4bc7-ae7f-d1e7205ba16c' href='records/70f29525-f17b-4bc7-ae7f-d1e7205ba16c'>3</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_15caa6c8-be9b-4f19-81ae-bb82321eafd6'>Mean Tidal Current - Coastal British Columbia - Canada</a></td>
      <td><a title='646dd927-3248-4fc9-970c-abea15f7d304' href='records/646dd927-3248-4fc9-970c-abea15f7d304'>2</a></td>
      <td>Geospatial, Oceanography</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3732444b-7a97-4d9c-9f2e-2fc6f9618bae'>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</a></td>
      <td><a title='f409100d-95e4-4933-a927-fdf8d3b83204' href='records/f409100d-95e4-4933-a927-fdf8d3b83204'>1</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-05-25</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cf7a6149-b34a-404c-88e1-c556bf361408'>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</a></td>
      <td><a title='c83b5cbf-cc8c-4676-823c-77e28c0ec9da' href='records/c83b5cbf-cc8c-4676-823c-77e28c0ec9da'>2</a></td>
      <td>Nearshore, Geospatial</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fe76ef4c-254a-44fe-87bc-052cd3aa9663'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Research)</a></td>
      <td><a title='79433a1f-ec07-4cd5-a31a-8c2c53069085' href='records/79433a1f-ec07-4cd5-a31a-8c2c53069085'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-30</td>
    </tr>
  </tbody>
</table>


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