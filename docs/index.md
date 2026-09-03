---
hide:
  - navigation
  - toc
---

<style>.md-content__inner > h1 { display: none; }</style>

*Last updated: 2026-09-03*

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2.5rem;">

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">278</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Total Records</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">-1 since 2026-09-02</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid red;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">33</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Records with Issues</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:red;margin-top:0.5rem;">+1 since 2026-09-02</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">96.8%</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">% Records with DOI</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-09-02</div>
  
  
</div>

</div>

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {"data": [{"hovertemplate": "Number of Records with Issue=%{text}<br>message=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#AA2026", "pattern": {"shape": ""}}, "name": "", "orientation": "h", "showlegend": false, "text": [1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 7.0, 8.0, 9.0], "textposition": "outside", "x": [1, 1, 1, 2, 2, 2, 3, 7, 8, 9], "xaxis": "x", "y": ["Contact missing affiliation", "Organization missing ROR", "Record DOI HTTPS link is failling", "No DOI defined", "Resource GitHub repository is not under the HakaiInstitute organization", "No funder", "Broken link (202)", "Broken link (404)", "Invalid Resource URL", "Metadata mismatch"], "yaxis": "y", "type": "bar", "cliponaxis": false}], "layout": {"template": {"data": {"scatter": [{"type": "scatter"}]}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "Number of Records with Issue"}, "tickformat": "d"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {}, "tickfont": {"size": 10}, "linecolor": "black", "automargin": true}, "legend": {"tracegroupgap": 0}, "margin": {"t": 20, "l": 0, "r": 60, "b": 40}, "barmode": "relative", "plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)", "showlegend": false}};
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_52e97374-bee5-4b1a-9b85-7170a5df8d6b'>Biomass and density of Pycnopodia helianthoides from the central coast of BC</a></td>
      <td><a title='f7433c1a-3aad-4761-81c4-c191a5e6ac92' href='records/f7433c1a-3aad-4761-81c4-c191a5e6ac92'>2</a></td>
      <td>Oceanography, Nearshore</td>
      <td>2026-09-01</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_73abfecf-d35c-4f9c-a991-eee5cece08ea'>Kelp Canopy Extent 2012 - NW Calvert Island</a></td>
      <td><a title='33bb67af-4d61-4b15-93a9-f3ab2498430b' href='records/33bb67af-4d61-4b15-93a9-f3ab2498430b'>1</a></td>
      <td>Geospatial</td>
      <td>2026-08-31</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_940218ef-d7f8-4f3f-9e69-52150ecdbec5'>North Vancouver Island Aerial Survey - 2024 - Airborne Coastal Observatory</a></td>
      <td><a title='bc1133da-5601-4f92-bc53-41be547c936b' href='records/bc1133da-5601-4f92-bc53-41be547c936b'>3</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-08-31</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c7466354-bacc-4781-acdc-543dd03d1eab'>Nanwakolas LiDAR Surveys - Airborne Coastal Observatory</a></td>
      <td><a title='39818579-9692-4256-9810-d8b80e9821aa' href='records/39818579-9692-4256-9810-d8b80e9821aa'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-08-31</td>
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ba41d935-f293-447f-be3d-7098e569b431'>Water Property Measurements from Conductivity-Temperature-Depth Profiles, BC, Canada (Research)</a></td>
      <td><a title='613ba2f9-b21d-445f-8eaa-f42950c9350b' href='records/613ba2f9-b21d-445f-8eaa-f42950c9350b'>1</a></td>
      <td>Oceanography, Nearshore, Watersheds, Juvenile Salmon Program</td>
      <td>2026-08-27</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b2b18171-35b6-4345-b81b-497a90c2e7c5'>Seagrass fish and macroinvertebrate swaths BC Central Coast</a></td>
      <td><a title='7b1120bc-4a2c-432c-9e54-879d66751a59' href='records/7b1120bc-4a2c-432c-9e54-879d66751a59'>1</a></td>
      <td>Nearshore</td>
      <td>2026-03-27</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f815a700-c943-4d6f-afeb-a4854ad10cfc'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Vancouver Island, British Columbia, Canada</a></td>
      <td><a title='b01f58f7-1518-4829-aff6-ac4a8f2c0616' href='records/b01f58f7-1518-4829-aff6-ac4a8f2c0616'>1</a></td>
      <td>Airborne Coastal Observatory, Geospatial, Nearshore</td>
      <td>2026-07-28</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7e9c97a3-4bf1-4852-81b6-d74cedf2c94c'>Environmental DNA survey of Calvert Island, British Columbia, 2021</a></td>
      <td><a title='c5e60545-c6f2-4945-af0a-21812ba5f0d9' href='records/c5e60545-c6f2-4945-af0a-21812ba5f0d9'>1</a></td>
      <td>Genomics</td>
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_012164c6-28dd-4078-b702-f0c2ce63d548'>Biodiversity and Oceanographic data from the False Creek Bioblitz, 2022</a></td>
      <td><a title='44bdc298-1329-400a-bc02-4d35d251865d' href='records/44bdc298-1329-400a-bc02-4d35d251865d'>1</a></td>
      <td>Genomics, Nearshore, Oceanography</td>
      <td>2026-08-10</td>
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6143028b-028d-46c7-a67d-f3a513435e63'>Water Property Measurements from Conductivity-Temperature-Depth Profiles, BC, Canada (Provisional)</a></td>
      <td><a title='13dc3c6c-9dd4-47a4-92ad-681c653d3565' href='records/13dc3c6c-9dd4-47a4-92ad-681c653d3565'>1</a></td>
      <td>Juvenile Salmon Program, Oceanography, Nearshore</td>
      <td>2026-06-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d55021c3-a142-4e14-8208-36c9826c1893'>Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, BC, Canada (Research)</a></td>
      <td><a title='8882a149-fabd-4ecd-98d3-68a2a88aee38' href='records/8882a149-fabd-4ecd-98d3-68a2a88aee38'>1</a></td>
      <td>Oceanography</td>
      <td>2026-05-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_59b33373-ae4a-4719-a3df-0e36a08187d8'>Seagrass Site-Level Production on BC Central Coast</a></td>
      <td><a title='9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' href='records/9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f'>1</a></td>
      <td>Nearshore</td>
      <td>2026-06-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_86343dd1-28d0-4d02-8eaf-402d51a7fef7'>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program (Provisional)</a></td>
      <td><a title='acd6c43f-6cbd-43c8-9bff-7d9ae6630295' href='records/acd6c43f-6cbd-43c8-9bff-7d9ae6630295'>1</a></td>
      <td>Juvenile Salmon Program</td>
      <td>2026-07-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_12f951d4-4155-4c05-969d-a7158412f579'>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</a></td>
      <td><a title='79ace68f-f5a9-4224-8615-20fa255cb6d4' href='records/79ace68f-f5a9-4224-8615-20fa255cb6d4'>2</a></td>
      <td>Geospatial, 100 Islands</td>
      <td>2026-07-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5eda02a9-36b6-4875-91c9-989e9e06c5ad'>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</a></td>
      <td><a title='b47e53cd-74dd-4580-80d0-260860064f4b' href='records/b47e53cd-74dd-4580-80d0-260860064f4b'>1</a></td>
      <td>100 Islands</td>
      <td>2026-06-26</td>
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7de69ca8-b3f3-4761-b441-dfc9e63b1fbc'>Rocky Intertidal RPAS Mapping Project - BC Central Coast - Canada</a></td>
      <td><a title='70f29525-f17b-4bc7-ae7f-d1e7205ba16c' href='records/70f29525-f17b-4bc7-ae7f-d1e7205ba16c'>3</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-08-31</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c3eff62f-bcee-4faa-a7e1-7b9380d94e74'>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</a></td>
      <td><a title='a8d40002-d393-40da-882c-73c0ad8ca7e6' href='records/a8d40002-d393-40da-882c-73c0ad8ca7e6'>1</a></td>
      <td>Geospatial, Airborne Coastal Observatory</td>
      <td>2026-06-10</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_87a845e3-e71a-43cc-a75f-ec6a3b812a0e'>Acoustic Doppler Current Profiler Time Series from Fixed Platform on the British Columbia Central Coast (Provisional)</a></td>
      <td><a title='9c581481-f2ee-4353-b1ab-c5bf242945fe' href='records/9c581481-f2ee-4353-b1ab-c5bf242945fe'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3f40326a-23f9-4e30-a16a-f332ace14e2f'>Nereocystis kelp canopy productivity data from BC Central Coast</a></td>
      <td><a title='4b04cbfe-71f4-47b4-b028-3fcd24e7cff2' href='records/4b04cbfe-71f4-47b4-b028-3fcd24e7cff2'>3</a></td>
      <td>Nearshore</td>
      <td>2026-08-04</td>
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