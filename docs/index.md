---
hide:
  - navigation
  - toc
---

<style>.md-content__inner > h1 { display: none; }</style>

*Last updated: 2026-06-24*

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2.5rem;">

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">266</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Total Records</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">+2 since 2026-06-23</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid green;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">82</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Records with Issues</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:green;margin-top:0.5rem;">-1 since 2026-06-23</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">96.6%</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">% Records with DOI</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-06-23</div>
  
  
</div>

</div>

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {"data": [{"hovertemplate": "Number of Records with Issue=%{text}<br>message=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#AA2026", "pattern": {"shape": ""}}, "name": "", "orientation": "h", "showlegend": false, "text": [1.0, 2.0, 3.0, 3.0, 8.0, 40.0, 49.0], "textposition": "outside", "x": [1, 2, 3, 3, 8, 40, 49], "xaxis": "x", "y": ["Primary DOI does not have a Hakai prefix (10.21966/)", "Duplicate DOI shared with another record", "No funder", "No DOI defined", "Invalid Resource URL", "No version", "Metadata mismatch"], "yaxis": "y", "type": "bar", "cliponaxis": false}], "layout": {"template": {"data": {"scatter": [{"type": "scatter"}]}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "Number of Records with Issue"}, "tickformat": "d"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {}, "tickfont": {"size": 10}, "linecolor": "black", "automargin": true}, "legend": {"tracegroupgap": 0}, "margin": {"t": 20, "l": 0, "r": 60, "b": 40}, "barmode": "relative", "plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)", "showlegend": false}};
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7e49967a-b5ab-443d-860b-e3c0eb0f709c'>Horne Lake Bathymetry Mapping</a></td>
      <td><a title='ed22dc0f-f2cc-41e5-ac1c-893e1b65c6d0' href='records/ed22dc0f-f2cc-41e5-ac1c-893e1b65c6d0'>3</a></td>
      <td>Geospatial</td>
      <td>2026-05-27</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1efbadd2-e735-48cc-9498-e3a5a88e48a6'>Seawater Carbon Dioxide (CO2) Content from the SuperCO2 System in the Pacific Ecosystem Autonomous Research Laboratory, Bamfield Marine Sciences Centre, BC, Canada (Provisional)</a></td>
      <td><a title='c5dafa6e-f2df-4f02-a94e-8f82b29dfb66' href='records/c5dafa6e-f2df-4f02-a94e-8f82b29dfb66'>1</a></td>
      <td>Oceanography</td>
      <td>2026-04-13</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_84820f31-b6db-479c-a47e-f22f2899b4d2'>Biogeochemical Sampling of 28 Streams on Vancouver Island</a></td>
      <td><a title='0e92249d-74e1-4253-a8a5-876d08a8ff65' href='records/0e92249d-74e1-4253-a8a5-876d08a8ff65'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7cafde4f-bdd5-4b95-a41d-7939ddcf08c6'>Time series of quarterly kelp canopy extent from Landsat 5, 7, 8, and 9 since 1985</a></td>
      <td><a title='a48161da-c603-43d6-9dc6-44b861984b49' href='records/a48161da-c603-43d6-9dc6-44b861984b49'>1</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-01-30</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5b4cbe9f-8f2e-414c-80ff-741372891fe9'>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</a></td>
      <td><a title='b9671efe-5980-452b-90f8-f30e4f1bc194' href='records/b9671efe-5980-452b-90f8-f30e4f1bc194'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-02-27</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9a018fe0-8bd1-41d1-af8d-079960b71473'>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</a></td>
      <td><a title='6be4c552-469a-4558-b63d-7a2c52566fe2' href='records/6be4c552-469a-4558-b63d-7a2c52566fe2'>1</a></td>
      <td>Genomics, Nearshore</td>
      <td>2026-05-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f7a867ce-0f18-43f6-8148-775235d800b6'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2023), Central Coast, British Columbia, Canada</a></td>
      <td><a title='e67a81ba-0ac5-49bd-a1fe-02b98f79d8a7' href='records/e67a81ba-0ac5-49bd-a1fe-02b98f79d8a7'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial, Nearshore</td>
      <td>2025-11-18</td>
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
      <td>2025-11-05</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_53730b70-be6f-4e24-8b9d-4a5e2c491121'>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</a></td>
      <td><a title='83f387d2-f77e-4921-af15-e064d87ad01a' href='records/83f387d2-f77e-4921-af15-e064d87ad01a'>1</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2025-04-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_35beb32e-8dc9-42ab-9630-2ae23e414026'>Rocky Subtidal Fish and Invertebrate Community Surveys from the Central Coast of BC</a></td>
      <td><a title='4a949e26-fe94-4f63-a3c6-a62e19301102' href='records/4a949e26-fe94-4f63-a3c6-a62e19301102'>1</a></td>
      <td>Nearshore</td>
      <td>2026-01-27</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d7ffd737-5725-4a56-9134-a9ad91c2734d'>Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia</a></td>
      <td><a title='8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e' href='records/8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e'>1</a></td>
      <td>Geospatial</td>
      <td>2026-05-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9fafb4c8-e61f-4372-ac71-c1ddbe57d80c'>Data record does not exist anymore: Geomorphology - Calvert Island</a></td>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='records/49967494-a7b6-4128-b336-671971d1e2c6'>2</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2026-06-09</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7fd3ec6c-083a-4942-84b4-215e69492072'>Phytoplankton Pigment Timeseries from High-Performance Liquid Chromatography for the Northern Salish Sea and Central Coast, BC, Canada (Research)</a></td>
      <td><a title='cb0f4710-d78a-4073-959c-95f874f88711' href='records/cb0f4710-d78a-4073-959c-95f874f88711'>1</a></td>
      <td>Oceanography</td>
      <td>2026-02-05</td>
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
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_43422dc8-2573-4f60-bf87-df447d57ab7a'>USGS Glacier Mapping - 2023 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='78efda1b-9688-4bcf-b16e-7167c17c0bcb' href='records/78efda1b-9688-4bcf-b16e-7167c17c0bcb'>1</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-03-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6652a7a9-d27f-4cbe-ac04-435c238e991d'>Water Level Time Series, Choke Pass, Central Coast, BC, Canada (Provisional)</a></td>
      <td><a title='7607322d-6dea-4758-a257-de8353c899c1' href='records/7607322d-6dea-4758-a257-de8353c899c1'>2</a></td>
      <td>Oceanography</td>
      <td>2026-02-20</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6143028b-028d-46c7-a67d-f3a513435e63'>Water Property Measurements from Conductivity-Temperature-Depth Profiles, BC, Canada (Provisional)</a></td>
      <td><a title='13dc3c6c-9dd4-47a4-92ad-681c653d3565' href='records/13dc3c6c-9dd4-47a4-92ad-681c653d3565'>1</a></td>
      <td>Juvenile Salmon Program, Oceanography, Nearshore</td>
      <td>2026-04-14</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_59b33373-ae4a-4719-a3df-0e36a08187d8'>Seagrass Site-Level Production on BC Central Coast</a></td>
      <td><a title='9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' href='records/9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f'>1</a></td>
      <td>Nearshore</td>
      <td>2024-12-30</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b8483c9e-81e6-4e1a-b09f-2d66f8fee9a2'>Spatial extent of surface canopy kelp (Nereocystis luetkeana) derived from fixed-wing surveys (2023), Denman Island to south Quadra Island, British Columbia, Canada</a></td>
      <td><a title='abb0b617-3a3e-43ec-b62e-e2918bfc10aa' href='records/abb0b617-3a3e-43ec-b62e-e2918bfc10aa'>1</a></td>
      <td>Airborne Coastal Observatory, Nearshore, Geospatial</td>
      <td>2024-07-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c24f23f0-8d16-4bfd-835a-5475f1ecd8e8'>Extent of Canopy-Forming Kelps, Derived from World View-2, Central Coast, Central Coast, British Columbia</a></td>
      <td><a title='b0e815da-1b17-404d-8bf6-0bdb4a22d170' href='records/b0e815da-1b17-404d-8bf6-0bdb4a22d170'>1</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_16ae186b-9d99-42cf-b18d-09f9bb0501d7'>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</a></td>
      <td><a title='b1c4c93b-6324-4b84-b341-76be046cbf28' href='records/b1c4c93b-6324-4b84-b341-76be046cbf28'>1</a></td>
      <td>Juvenile Salmon Program</td>
      <td>2026-05-27</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_60f653ae-a3fd-484d-807c-3d7e4a0712cb'>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</a></td>
      <td><a title='5c2aac2c-0dd8-49d8-87b2-5c52b3d42946' href='records/5c2aac2c-0dd8-49d8-87b2-5c52b3d42946'>1</a></td>
      <td>Nearshore, Genomics</td>
      <td>2025-04-21</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_12f951d4-4155-4c05-969d-a7158412f579'>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</a></td>
      <td><a title='79ace68f-f5a9-4224-8615-20fa255cb6d4' href='records/79ace68f-f5a9-4224-8615-20fa255cb6d4'>2</a></td>
      <td>Geospatial, 100 Islands</td>
      <td>2025-04-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_251aef08-4017-4493-b9d8-c4583913b511'>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</a></td>
      <td><a title='3a8b11a2-5deb-469e-824b-32ab0eb5c2ca' href='records/3a8b11a2-5deb-469e-824b-32ab0eb5c2ca'>2</a></td>
      <td>Geospatial</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_160803d3-8019-4a73-9191-5f75f0ec21be'>Mount Robson BC Parks Survey - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='550e7acb-0e3f-461f-bd47-8b6ced16bf43' href='records/550e7acb-0e3f-461f-bd47-8b6ced16bf43'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e2baa28d-c063-4354-ae1f-2abdb8397d8f'>Gordon River Archaeology - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='a4e3915d-207e-493d-97ff-c1e6ad6f0ce7' href='records/a4e3915d-207e-493d-97ff-c1e6ad6f0ce7'>2</a></td>
      <td>Geospatial, Airborne Coastal Observatory</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_532c06ad-0b55-4e86-9088-cec970a0a8e1'>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' href='records/ee2eec87-7a78-4a7f-87b7-54347a6c3b2f'>3</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2024-12-05</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c39138f-8f01-4948-a3de-864044686c55'>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</a></td>
      <td><a title='f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff' href='records/f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff'>3</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bdb9229b-f594-40df-994e-e52e8a678165'>Broken Group Imagery and LiDAR - 2018 - Airborne Coastal Observatory</a></td>
      <td><a title='eb02906a-9645-4486-ba14-46d71c581352' href='records/eb02906a-9645-4486-ba14-46d71c581352'>2</a></td>
      <td>Geospatial</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6dc431f0-3ca4-4c48-992c-df82d6f8521c'>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</a></td>
      <td><a title='b276330c-4ee9-476a-979a-cebe52d51db6' href='records/b276330c-4ee9-476a-979a-cebe52d51db6'>3</a></td>
      <td>Geospatial, Airborne Coastal Observatory</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8d36f54-4955-463c-94e5-f0030c3230f3'>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</a></td>
      <td><a title='50037e63-bfac-4b7a-8547-56337fe40026' href='records/50037e63-bfac-4b7a-8547-56337fe40026'>1</a></td>
      <td>Geospatial</td>
      <td>2026-06-11</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d049351d-b806-461f-85fb-451f100fd7d6'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)</a></td>
      <td><a title='78b2edef-dab3-47a9-93bb-af63dfcd178d' href='records/78b2edef-dab3-47a9-93bb-af63dfcd178d'>2</a></td>
      <td>Oceanography</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8e99157a-8daf-4e68-92ae-9d22cfd46ce7'>Elliot Creek – Homathko Estuary Mapping - 2021 - Airborne Coastal Observatory</a></td>
      <td><a title='36e9e6ae-a407-456e-8fe2-a3a78b246bf7' href='records/36e9e6ae-a407-456e-8fe2-a3a78b246bf7'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f952a904-f9f7-4876-b518-c98b1fd96f7e'>Snow Mapping Coastal British Columbia - 2021 - Airborne Coastal Observatory</a></td>
      <td><a title='2168fd41-96d4-4b72-b5ec-0a5c342aad2a' href='records/2168fd41-96d4-4b72-b5ec-0a5c342aad2a'>2</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c1b9801b-742b-41b6-a69b-5e7ae6f09bce'>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</a></td>
      <td><a title='d3c4dde5-38b2-480d-a4e7-228bde9eb537' href='records/d3c4dde5-38b2-480d-a4e7-228bde9eb537'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5eda02a9-36b6-4875-91c9-989e9e06c5ad'>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</a></td>
      <td><a title='b47e53cd-74dd-4580-80d0-260860064f4b' href='records/b47e53cd-74dd-4580-80d0-260860064f4b'>1</a></td>
      <td>100 Islands</td>
      <td>2026-05-14</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_41770c7d-27ea-4593-ba55-040bdc5b99f0'>Oceanographic Mooring Time Series, Rivers Inlet, BC, Canada (Research)</a></td>
      <td><a title='4a9b4584-a5ef-4baf-9d4a-bacf8e6a5d1d' href='records/4a9b4584-a5ef-4baf-9d4a-bacf8e6a5d1d'>1</a></td>
      <td>Oceanography</td>
      <td>2026-05-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c981d76-5fea-44af-904f-58b159838b0a'>Stream Event Sampling - Calvert Island</a></td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='records/def2a409-2319-4e8c-a584-9a467f044ada'>1</a></td>
      <td>Watersheds, Geospatial</td>
      <td>2026-06-09</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_26443ab2-964f-4031-a53b-f132434573e8'>Ecosystem Comparison Plots - Calvert Island</a></td>
      <td><a title='d8754c99-a540-4085-8c66-d9447da5f6e9' href='records/d8754c99-a540-4085-8c66-d9447da5f6e9'>2</a></td>
      <td>Geospatial, Watersheds</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_395aa495-de81-4947-b1c5-2c98172a6def'>High-resolution hydrometeorological data from seven small coastal watersheds, British Columbia, Canada, 2013-2019</a></td>
      <td><a title='2b33a5f0-1172-41e4-8330-b4c77d1665c7' href='records/2b33a5f0-1172-41e4-8330-b4c77d1665c7'>1</a></td>
      <td>Watersheds</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6844547c-708e-437b-aef7-157b4d9d9bcb'>Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada</a></td>
      <td><a title='3c4cc294-1e9a-410e-81b0-0d9461e4b1c9' href='records/3c4cc294-1e9a-410e-81b0-0d9461e4b1c9'>1</a></td>
      <td>Watersheds, Oceanography</td>
      <td>2026-06-09</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9201118a-b0c4-470f-a76f-396bacc5e93e'>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</a></td>
      <td><a title='55e7c337-02e8-4200-8ea9-88241d978f96' href='records/55e7c337-02e8-4200-8ea9-88241d978f96'>3</a></td>
      <td>Oceanography</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9e61819e-8385-41d2-a5c5-0e2f37c522ef'>LiDAR-based Ecosystem Classification for Calvert Island</a></td>
      <td><a title='18911dee-9ca0-408b-8999-28da3e3dde7a' href='records/18911dee-9ca0-408b-8999-28da3e3dde7a'>1</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b52d5602-f81d-4565-9574-e448e99bc997'>Bathymetry for Six Lakes on Calvert and Hecate Islands - 2016 - British Columbia - Canada</a></td>
      <td><a title='f0cae885-2124-41c1-8523-2c6725c40dd6' href='records/f0cae885-2124-41c1-8523-2c6725c40dd6'>1</a></td>
      <td>Watersheds, Geospatial</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d05df775-4295-4b9f-b3b3-29fe891d9ed9'>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</a></td>
      <td><a title='b36a7c12-cb56-46b7-8241-9b52ac30c766' href='records/b36a7c12-cb56-46b7-8241-9b52ac30c766'>3</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d94882f8-c069-454d-a0ea-96c2b17d789d'>LiDAR Derived Watersheds with Metrics - Calvert Island</a></td>
      <td><a title='79e98468-af9a-4b52-aa9c-71129fa9cb03' href='records/79e98468-af9a-4b52-aa9c-71129fa9cb03'>2</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0c8692f0-a103-4681-9247-9bb69c6e222e'>Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada</a></td>
      <td><a title='ee09830d-dd5e-41eb-8aee-0fe9cef5fe79' href='records/ee09830d-dd5e-41eb-8aee-0fe9cef5fe79'>2</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_14bf37c7-5eb6-4194-a992-c039fd7fb38b'>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</a></td>
      <td><a title='69268e35-08ac-4e6d-b489-4bb72ac117b1' href='records/69268e35-08ac-4e6d-b489-4bb72ac117b1'>3</a></td>
      <td>Geospatial</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7de69ca8-b3f3-4761-b441-dfc9e63b1fbc'>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</a></td>
      <td><a title='70f29525-f17b-4bc7-ae7f-d1e7205ba16c' href='records/70f29525-f17b-4bc7-ae7f-d1e7205ba16c'>3</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bef293d6-8721-4214-b8f5-03b5ffb28e1c'>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</a></td>
      <td><a title='f9ff815c-c57a-4750-8f80-25f5e145c8c0' href='records/f9ff815c-c57a-4750-8f80-25f5e145c8c0'>3</a></td>
      <td>Geospatial</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1b517e6f-4f0a-4577-b7c2-c37f95d5b413'>Field Station Structures - Calvert Island</a></td>
      <td><a title='7ed2118f-ecaa-41e4-aa81-911ffa47bf34' href='records/7ed2118f-ecaa-41e4-aa81-911ffa47bf34'>2</a></td>
      <td>Geospatial</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d61f51c3-7614-465f-bf27-c78986ca07c3'>McMullin Group Kelp Extent - Based on UAS Imagery - 2017</a></td>
      <td><a title='22951dd4-a9f7-4f2a-b11d-d50e184dc223' href='records/22951dd4-a9f7-4f2a-b11d-d50e184dc223'>1</a></td>
      <td>Geospatial</td>
      <td>2026-05-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_27ba6c11-2421-4e85-bc11-1c1083514ed9'>Owikeno Lake Bathymetric Survey</a></td>
      <td><a title='2fe3bd2a-973e-48db-a599-6d44ca1ef0ad' href='records/2fe3bd2a-973e-48db-a599-6d44ca1ef0ad'>1</a></td>
      <td>Geospatial</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5c13b300-e172-4010-a6d8-7586b68a3a96'>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</a></td>
      <td><a title='c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' href='records/c8f6fd7c-7c63-440b-b69a-bd0df3abfd26'>2</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94cdfcba-bbd4-4053-8976-75de69460c14'>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</a></td>
      <td><a title='52048599-9a0c-4d33-861f-26eaedc86bd5' href='records/52048599-9a0c-4d33-861f-26eaedc86bd5'>2</a></td>
      <td>Nearshore, Geospatial</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_62de21ed-90fb-422a-9c55-29c513a00f95'>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td><a title='e3205958-52b4-4c42-a02d-34d713a20a53' href='records/e3205958-52b4-4c42-a02d-34d713a20a53'>1</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7c47472a-b16c-446c-89d5-eefa23e07922'>High-resolution record of surface seawater CO2 content from November 2017 to June 2018 collected in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td><a title='f31f38bf-16bc-4136-8982-a2df5fefb3a0' href='records/f31f38bf-16bc-4136-8982-a2df5fefb3a0'>1</a></td>
      <td>Oceanography</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a72c43e2-5b4d-4d56-89d4-464b4c513710'>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</a></td>
      <td><a title='45983472-7627-4227-b312-079c2aeda7ef' href='records/45983472-7627-4227-b312-079c2aeda7ef'>1</a></td>
      <td>Oceanography</td>
      <td>2026-02-20</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4b5c0c20-2115-4986-bf56-237e360240bd'>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</a></td>
      <td><a title='1a9a5aae-41ee-4272-a52e-6c37abedfbff' href='records/1a9a5aae-41ee-4272-a52e-6c37abedfbff'>3</a></td>
      <td>Oceanography, Watersheds</td>
      <td>2025-01-30</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a0ca5d26-b457-4726-97d4-ed0c8dd6cd99'>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</a></td>
      <td><a title='dd30b32a-2099-4909-838d-6ade9804381a' href='records/dd30b32a-2099-4909-838d-6ade9804381a'>1</a></td>
      <td>Nearshore</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1c9b7bcd-d3cc-4856-9428-df7abb2149f0'>Mobile Invertebrate Rocky Intertidal Surveys - BC Central Coast - 2016-2018</a></td>
      <td><a title='f8f299be-a37e-43bf-9416-5ff59e664f65' href='records/f8f299be-a37e-43bf-9416-5ff59e664f65'>1</a></td>
      <td>Nearshore</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2738ef2b-0c74-422d-a140-082e5f7b3793'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</a></td>
      <td><a title='f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a' href='records/f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a'>1</a></td>
      <td>Nearshore</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d200376b-7dd8-4778-b3f5-379243bf93b8'>High-resolution record of surface water pH at Sentry Shoal in the Northern Strait of Georgia</a></td>
      <td><a title='1f798a06-9c01-4025-93c6-b1a9f8ce6832' href='records/1f798a06-9c01-4025-93c6-b1a9f8ce6832'>1</a></td>
      <td>Oceanography</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f462be7f-ab53-409e-8f8c-9b9fecc5e16e'>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</a></td>
      <td><a title='c2b05382-684f-4349-a64b-b20521223574' href='records/c2b05382-684f-4349-a64b-b20521223574'>3</a></td>
      <td>Geospatial</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_15caa6c8-be9b-4f19-81ae-bb82321eafd6'>Mean Tidal Current - Coastal British Columbia - Canada</a></td>
      <td><a title='646dd927-3248-4fc9-970c-abea15f7d304' href='records/646dd927-3248-4fc9-970c-abea15f7d304'>2</a></td>
      <td>Geospatial, Oceanography</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8c8ed7d-51fa-45e0-b4eb-d21ddc55526a'>Clam Garden Geospatial Data - Quadra Island - 2016</a></td>
      <td><a title='693c7ca7-a244-4375-9460-ff7c27187af2' href='records/693c7ca7-a244-4375-9460-ff7c27187af2'>2</a></td>
      <td>Geospatial</td>
      <td>2026-06-01</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1347af6c-aedf-4ec6-bd37-ed508df6c40a'>Stage-Discharge Time Series - Calvert Island - Archived</a></td>
      <td><a title='a0ada4b0-faea-4dcd-b9bf-d7ff212315fb' href='records/a0ada4b0-faea-4dcd-b9bf-d7ff212315fb'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_62336906-31e6-4c32-968c-2312e703e08f'>Underwater Video Transects - Calvert Island - 2016</a></td>
      <td><a title='d64fd03b-46d4-4662-a123-c11bc42199b6' href='records/d64fd03b-46d4-4662-a123-c11bc42199b6'>3</a></td>
      <td>Geospatial</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94b4992f-19e2-46d4-875e-f0c952ea62f7'>Kelp Field Data for Remote Sensing - BC Central Coast</a></td>
      <td><a title='cd3ca52d-dc83-4501-9e53-7b00c8ab9090' href='records/cd3ca52d-dc83-4501-9e53-7b00c8ab9090'>1</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-05-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ea6c0e20-9b99-48f7-adfb-6c1b70f6bd2a'>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</a></td>
      <td><a title='35dd16d8-20b1-49d5-8c59-9cdc02475cd0' href='records/35dd16d8-20b1-49d5-8c59-9cdc02475cd0'>1</a></td>
      <td>Nearshore</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3732444b-7a97-4d9c-9f2e-2fc6f9618bae'>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</a></td>
      <td><a title='f409100d-95e4-4933-a927-fdf8d3b83204' href='records/f409100d-95e4-4933-a927-fdf8d3b83204'>2</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-05-25</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_55daf524-146e-4b06-8c6c-3255c7e3c77a'>Vegetated Islands Polygons - 100 Islands Research</a></td>
      <td><a title='0c08a4f0-b28c-40fe-aaa8-a03113a7c735' href='records/0c08a4f0-b28c-40fe-aaa8-a03113a7c735'>1</a></td>
      <td>100 Islands</td>
      <td>2026-05-25</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_82c07005-9313-436c-9239-7be3f5907be2'>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</a></td>
      <td><a title='dc84cb4c-ba14-4632-a595-eed526bf9db1' href='records/dc84cb4c-ba14-4632-a595-eed526bf9db1'>1</a></td>
      <td>100 Islands</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_af65bf72-27af-4747-8911-ab05591762ac'>Kelp forest communities along an otter gradient</a></td>
      <td><a title='f5d51d99-ce24-4713-a317-7927dd283f1a' href='records/f5d51d99-ce24-4713-a317-7927dd283f1a'>1</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cf7a6149-b34a-404c-88e1-c556bf361408'>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</a></td>
      <td><a title='c83b5cbf-cc8c-4676-823c-77e28c0ec9da' href='records/c83b5cbf-cc8c-4676-823c-77e28c0ec9da'>1</a></td>
      <td>Nearshore, Geospatial</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8b069feb-57fc-4d57-bf5c-761fd7cf0b45'>Surface Seawater and Marine Boundary Layer CO2 Observations from the Kwakshua Channel (KC) Buoy on the Central Coast of British Columbia (Research)</a></td>
      <td><a title='3f883dc6-56ac-42f5-a1d4-6de554a9e63d' href='records/3f883dc6-56ac-42f5-a1d4-6de554a9e63d'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fe76ef4c-254a-44fe-87bc-052cd3aa9663'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Research)</a></td>
      <td><a title='79433a1f-ec07-4cd5-a31a-8c2c53069085' href='records/79433a1f-ec07-4cd5-a31a-8c2c53069085'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-15</td>
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