---
hide:
  - navigation
  - toc
---

<style>.md-content__inner > h1 { display: none; }</style>

*Last updated: 2026-09-25*

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2.5rem;">

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">298</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Total Records</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">-3 since 2026-09-24</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid red;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">31</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Records with Issues</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:red;margin-top:0.5rem;">+4 since 2026-09-24</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid red;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">96.6%</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">% Records with DOI</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:red;margin-top:0.5rem;">-0.1% since 2026-09-24</div>
  
  
</div>

</div>

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {"data": [{"hovertemplate": "Number of Records with Issue=%{text}<br>message=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#AA2026", "pattern": {"shape": ""}}, "name": "", "orientation": "h", "showlegend": false, "text": [1.0, 2.0, 3.0, 4.0, 7.0, 7.0, 10.0], "textposition": "outside", "x": [1, 2, 3, 4, 7, 7, 10], "xaxis": "x", "y": ["No version", "No funder", "No DOI defined", "Broken link (202)", "Broken link (404)", "Metadata mismatch", "Invalid Resource URL"], "yaxis": "y", "type": "bar", "cliponaxis": false}], "layout": {"template": {"data": {"scatter": [{"type": "scatter"}]}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "Number of Records with Issue"}, "tickformat": "d"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {}, "tickfont": {"size": 10}, "linecolor": "black", "automargin": true}, "legend": {"tracegroupgap": 0}, "margin": {"t": 20, "l": 0, "r": 60, "b": 40}, "barmode": "relative", "plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)", "showlegend": false}};
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1f1774ff-7398-4099-b89f-59df7ef0749e'>Surface underway seawater and marine boundary layer observations of partial pressure of carbon dioxide (pCO2), water temperature, salinity and other parameters made during the M/V Seaspan Royal cruises in the coastal waters of British Columbia, Canada from 2022-07-01 to 2022-12-20</a></td>
      <td><a title='58d56d16-6350-4b01-a062-6bdb2d9f89b4' href='records/58d56d16-6350-4b01-a062-6bdb2d9f89b4'>1</a></td>
      <td>Oceanography</td>
      <td>2026-09-10</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a787372d-e6f0-4128-bd08-7e9f5e667e1d'>Discrete water chemistry measurements of the carbon dioxide system, nutrients, and organic carbon in fresh and marine waters of the Northeast Pacific coast of North America</a></td>
      <td><a title='c1e0447b-a06c-44c8-abd0-3108b2f00b7a' href='records/c1e0447b-a06c-44c8-abd0-3108b2f00b7a'>2</a></td>
      <td>Oceanography</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b4844ae2-d9c1-42f2-ae4d-a8f994c395a0'>Putting fjord biodiversity on the map for Britsh Columbia conservation planning</a></td>
      <td><a title='c7a168e8-f15e-446f-a49d-0b4a1f043ac2' href='records/c7a168e8-f15e-446f-a49d-0b4a1f043ac2'>1</a></td>
      <td>Genomics, Oceanography</td>
      <td>2026-09-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_73abfecf-d35c-4f9c-a991-eee5cece08ea'>Kelp Canopy Extent 2012 - NW Calvert Island</a></td>
      <td><a title='33bb67af-4d61-4b15-93a9-f3ab2498430b' href='records/33bb67af-4d61-4b15-93a9-f3ab2498430b'>1</a></td>
      <td>Geospatial</td>
      <td>2026-08-31</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c7466354-bacc-4781-acdc-543dd03d1eab'>Nanwakolas LiDAR Surveys - Airborne Coastal Observatory</a></td>
      <td><a title='39818579-9692-4256-9810-d8b80e9821aa' href='records/39818579-9692-4256-9810-d8b80e9821aa'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_53189107-9df5-426b-acb4-f903468554fe'>Comparing invertebrate and seaweed diversity in kelp forests and urchin barrens in Owen Bay, British Columbia, using Autonomous Reef Monitoring Structures (ARMS)</a></td>
      <td><a title='c4932b55-1dd8-4f2f-89da-5822056ecc37' href='records/c4932b55-1dd8-4f2f-89da-5822056ecc37'>1</a></td>
      <td>Sentinels of Change, Genomics</td>
      <td>2026-08-25</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_91107fce-93a4-4bc9-bce4-e7d9e1cf02a0'>Sentinel 3A and 3B Chlorophyll and Suspended Matter Concentrations for Coastal British Columbia and Southeast Alaska, 8-Day Average (Research)</a></td>
      <td><a title='185462b6-5d10-43d8-91b2-b92010e80ff4' href='records/185462b6-5d10-43d8-91b2-b92010e80ff4'>2</a></td>
      <td>Oceanography</td>
      <td>2026-05-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d1bef0b7-4d15-4bc1-bf34-faca6352891f'>Daily satellite (Sentinel 3A and 3B) chlorophyll and suspended matter concentrations for coastal British Columbia and southeast Alaska</a></td>
      <td><a title='caf810f0-228a-4827-856c-f9b07a2377af' href='records/caf810f0-228a-4827-856c-f9b07a2377af'>2</a></td>
      <td>Oceanography</td>
      <td>2026-05-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ba41d935-f293-447f-be3d-7098e569b431'>Water Property Measurements from Conductivity-Temperature-Depth Profilers, BC, Canada (Research)</a></td>
      <td><a title='613ba2f9-b21d-445f-8eaa-f42950c9350b' href='records/613ba2f9-b21d-445f-8eaa-f42950c9350b'>1</a></td>
      <td>Oceanography, Nearshore, Watersheds, Juvenile Salmon Program</td>
      <td>2026-09-14</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_84820f31-b6db-479c-a47e-f22f2899b4d2'>Biogeochemical Sampling of 28 Streams on Vancouver Island</a></td>
      <td><a title='0e92249d-74e1-4253-a8a5-876d08a8ff65' href='records/0e92249d-74e1-4253-a8a5-876d08a8ff65'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_43bad5e5-0484-4c11-80a5-c844245f940e'>Farwell Canyon Airborne Surveys - 2024 - Airborne Coastal Observatory</a></td>
      <td><a title='37440dfd-53f8-462b-a544-b6c8d39c44cd' href='records/37440dfd-53f8-462b-a544-b6c8d39c44cd'>2</a></td>
      <td>Geospatial, Airborne Coastal Observatory</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c544ef5b-967d-46b2-bbcf-395116b50e7d'>Mystery Creek Aerial Photo and LiDAR Survey - 2025 - Airborne Coastal Observatory</a></td>
      <td><a title='9eda1bfc-0d13-4e1d-9542-b9a7cce16991' href='records/9eda1bfc-0d13-4e1d-9542-b9a7cce16991'>2</a></td>
      <td>Geospatial, Airborne Coastal Observatory</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_35900174-c64a-493e-9a7e-390ac7e997e4'>Bowhead Whale Drone Data Collection - Cumberland Sound - Nunavut</a></td>
      <td><a title='5fc21b4d-2dfa-4908-8aaf-90a82509324a' href='records/5fc21b4d-2dfa-4908-8aaf-90a82509324a'>2</a></td>
      <td>Geospatial</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b5f0f854-efe1-4132-808d-074244d813e1'>Gitga'at Territory Coastal Mapping Project</a></td>
      <td><a title='0074861a-39f2-42c1-ae71-abef4f78fd78' href='records/0074861a-39f2-42c1-ae71-abef4f78fd78'>2</a></td>
      <td>Geospatial</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f815a700-c943-4d6f-afeb-a4854ad10cfc'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Vancouver Island, British Columbia, Canada</a></td>
      <td><a title='b01f58f7-1518-4829-aff6-ac4a8f2c0616' href='records/b01f58f7-1518-4829-aff6-ac4a8f2c0616'>1</a></td>
      <td>Airborne Coastal Observatory, Geospatial, Nearshore</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7e9c97a3-4bf1-4852-81b6-d74cedf2c94c'>Environmental DNA survey of Calvert Island, British Columbia, 2021</a></td>
      <td><a title='c5e60545-c6f2-4945-af0a-21812ba5f0d9' href='records/c5e60545-c6f2-4945-af0a-21812ba5f0d9'>1</a></td>
      <td>Genomics</td>
      <td>2026-06-15</td>
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_87341cb3-f906-4fa5-973c-b6742aa0fbb5'>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='2916abf5-419e-4cd7-8e25-f45f07a21313' href='records/2916abf5-419e-4cd7-8e25-f45f07a21313'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_96e3dd9c-7863-44d5-95cd-a3d0a8653d83'>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='6c99bd67-3be1-4818-bf01-dfa56e910db3' href='records/6c99bd67-3be1-4818-bf01-dfa56e910db3'>2</a></td>
      <td>Geospatial, Airborne Coastal Observatory</td>
      <td>2026-09-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9fafb4c8-e61f-4372-ac71-c1ddbe57d80c'>Data record does not exist anymore: Geomorphology - Calvert Island</a></td>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='records/49967494-a7b6-4128-b336-671971d1e2c6'>2</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2026-06-09</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6143028b-028d-46c7-a67d-f3a513435e63'>Water Property Measurements from Conductivity-Temperature-Depth Profilers, BC, Canada (Provisional)</a></td>
      <td><a title='13dc3c6c-9dd4-47a4-92ad-681c653d3565' href='records/13dc3c6c-9dd4-47a4-92ad-681c653d3565'>1</a></td>
      <td>Juvenile Salmon Program, Oceanography, Nearshore</td>
      <td>2026-09-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_86343dd1-28d0-4d02-8eaf-402d51a7fef7'>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program (Provisional)</a></td>
      <td><a title='acd6c43f-6cbd-43c8-9bff-7d9ae6630295' href='records/acd6c43f-6cbd-43c8-9bff-7d9ae6630295'>1</a></td>
      <td>Juvenile Salmon Program</td>
      <td>2026-07-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c981d76-5fea-44af-904f-58b159838b0a'>Stream Event Sampling - Calvert Island</a></td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='records/def2a409-2319-4e8c-a584-9a467f044ada'>1</a></td>
      <td>Watersheds, Geospatial</td>
      <td>2026-07-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4034f474-4d52-4a9e-9650-f3c6bd5011e0'>Kelp Canopy Extent 2006 - NW Calvert Island</a></td>
      <td><a title='0f19ac6e-dc86-445b-b2da-7b61a389222e' href='records/0f19ac6e-dc86-445b-b2da-7b61a389222e'>1</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-05-25</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0a8ff4c9-158a-4a46-9bb0-9d480ff40466'>Hakai Place Names Service - Coastal British Columbia - Canada</a></td>
      <td><a title='b6621a3c-1700-4015-a359-56b6c7155835' href='records/b6621a3c-1700-4015-a359-56b6c7155835'>1</a></td>
      <td>Geospatial, Airborne Coastal Observatory</td>
      <td>2026-06-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_15caa6c8-be9b-4f19-81ae-bb82321eafd6'>Mean Tidal Current - Coastal British Columbia - Canada</a></td>
      <td><a title='646dd927-3248-4fc9-970c-abea15f7d304' href='records/646dd927-3248-4fc9-970c-abea15f7d304'>2</a></td>
      <td>Geospatial, Oceanography</td>
      <td>2026-08-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7ddae37a-e706-45d2-8060-8306300a98c8'>Oceanographic Mooring Time Series, Hyacinthe Bay, BC, Canada (Provisional)</a></td>
      <td><a title='7c2b8668-75a3-4fc8-bff3-bdae5d95f52d' href='records/7c2b8668-75a3-4fc8-bff3-bdae5d95f52d'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3732444b-7a97-4d9c-9f2e-2fc6f9618bae'>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</a></td>
      <td><a title='f409100d-95e4-4933-a927-fdf8d3b83204' href='records/f409100d-95e4-4933-a927-fdf8d3b83204'>1</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-05-25</td>
    </tr>
  </tbody>
</table>


<script>
  document.addEventListener("DOMContentLoaded", function() {
    $(document).ready(function () {
      $("#records_table").DataTable({
        scrollX: true,
        autoWidth: false,
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