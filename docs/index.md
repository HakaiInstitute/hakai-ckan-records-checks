---
hide:
  - navigation
  - toc
---

<style>.md-content__inner > h1 { display: none; }</style>

*Last updated: 2026-11-20*

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2.5rem;">

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">312</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Total Records</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">-1 since 2026-11-19</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid red;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">38</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Records with Issues</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:red;margin-top:0.5rem;">+19 since 2026-11-19</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">96.2%</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">% Records with DOI</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-11-19</div>
  
  
</div>

</div>

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {"data": [{"hovertemplate": "Number of Records with Issue=%{text}<br>message=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#AA2026", "pattern": {"shape": ""}}, "name": "", "orientation": "h", "showlegend": false, "text": [1.0, 1.0, 2.0, 3.0, 4.0, 29.0], "textposition": "outside", "x": [1, 1, 2, 3, 4, 29], "xaxis": "x", "y": ["Broken link (410)", "No funder", "Metadata mismatch", "Broken link (202)", "Broken link (404)", "Invalid Resource URL"], "yaxis": "y", "type": "bar", "cliponaxis": false}], "layout": {"template": {"data": {"scatter": [{"type": "scatter"}]}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "Number of Records with Issue"}, "tickformat": "d"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {}, "tickfont": {"size": 10}, "linecolor": "black", "automargin": true}, "legend": {"tracegroupgap": 0}, "margin": {"t": 20, "l": 0, "r": 60, "b": 40}, "barmode": "relative", "plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)", "showlegend": false}};
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d1bde732-9401-4cd9-9e4a-2e5b02a69ad2'>Parasitism of an intertidal foundation species: Allometric scaling and environmental constraints on trematode distribution in barnacles across biological scales</a></td>
      <td><a title='a3b64e3a-3315-4d64-81d8-6e772e44951d' href='records/a3b64e3a-3315-4d64-81d8-6e772e44951d'>1</a></td>
      <td>Sentinels of Change</td>
      <td>2026-10-29</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f622773a-3ac2-4d91-bc4d-7286c7324434'>Genetic evidence for the presence of Maritrema gratiosum in the Northeast Pacific</a></td>
      <td><a title='9cdf1117-a07a-4fc1-ba03-e69f3e2963fb' href='records/9cdf1117-a07a-4fc1-ba03-e69f3e2963fb'>1</a></td>
      <td>Sentinels of Change, Genomics</td>
      <td>2026-10-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_741bd412-6387-4dcd-8d61-7046b949f406'>Global Eutrophication Monitoring Dataset of Trinidad and Tobago</a></td>
      <td><a title='1e13d2ee-580f-4785-838b-908a449781a3' href='records/1e13d2ee-580f-4785-838b-908a449781a3'>2</a></td>
      <td>Oceanography</td>
      <td>2026-10-06</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b922699f-69b6-4d63-b538-7c290086a408'>BC Estuary Water Quality Monitoring Data - Quw'utsun/Xwulqw'selu River Estuary (Provisional)</a></td>
      <td><a title='d320d90e-96bf-4993-81c5-f1f57886b0e6' href='records/d320d90e-96bf-4993-81c5-f1f57886b0e6'>1</a></td>
      <td>Estuary Resilience</td>
      <td>2026-09-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_83a949b4-99be-4a36-a910-0c81946a9bf6'>BC Estuary Water Quality Monitoring Data - Muuyaḥi River Estuary (Provisional)</a></td>
      <td><a title='5216f7f5-a569-4f76-9cab-171f1e847498' href='records/5216f7f5-a569-4f76-9cab-171f1e847498'>1</a></td>
      <td>Estuary Resilience</td>
      <td>2026-09-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ae7e017c-9211-4f98-b56e-90a4bbac161c'>BC Estuary Water Quality Monitoring Data - Snuneymuxw River Estuary (Provisional)</a></td>
      <td><a title='1af6a43a-e73b-4774-8e10-b9f2928ab133' href='records/1af6a43a-e73b-4774-8e10-b9f2928ab133'>1</a></td>
      <td>Estuary Resilience</td>
      <td>2026-09-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bea3da72-dafe-4e25-b5b2-0176e0ffba44'>BC Estuary Water Quality Monitoring Data - Chemainus River Estuary (Provisional)</a></td>
      <td><a title='b7638e0b-e734-4a96-97af-9e7729b61831' href='records/b7638e0b-e734-4a96-97af-9e7729b61831'>1</a></td>
      <td>Estuary Resilience</td>
      <td>2026-09-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dce15b7b-3772-4106-ab20-c3979c4c3f57'>BC Estuary Water Quality Monitoring Data - Fulmore River - Shoal Creek Estuary Complex (Provisional)</a></td>
      <td><a title='4c7b7347-767d-45e4-b3ad-7e0133b31e1c' href='records/4c7b7347-767d-45e4-b3ad-7e0133b31e1c'>1</a></td>
      <td>Estuary Resilience</td>
      <td>2026-09-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dfb93c87-300e-4843-91f9-7c51bc59422e'>BC Estuary Water Quality Monitoring Data - Little Qualicum River Estuary (Provisional)</a></td>
      <td><a title='8dadb6a8-8eb2-44ea-9d2d-c4332e4c544b' href='records/8dadb6a8-8eb2-44ea-9d2d-c4332e4c544b'>1</a></td>
      <td>Estuary Resilience</td>
      <td>2026-09-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e9b72149-8cf1-4000-ae3e-6b29ad60b078'>BC Estuary Water Quality Monitoring Data - Malksope River Estuary (Provisional)</a></td>
      <td><a title='35245eae-e508-47da-bcf7-54346cda086a' href='records/35245eae-e508-47da-bcf7-54346cda086a'>1</a></td>
      <td>Estuary Resilience</td>
      <td>2026-09-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ed84df74-5a2d-4a7d-87c8-a7b93f11088e'>BC Estuary Water Quality Monitoring Data - Nalaxdlala River Estuary (Provisional)</a></td>
      <td><a title='5177d019-598e-4415-b778-9688403652c8' href='records/5177d019-598e-4415-b778-9688403652c8'>1</a></td>
      <td>Estuary Resilience</td>
      <td>2026-09-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b4844ae2-d9c1-42f2-ae4d-a8f994c395a0'>Putting fjord biodiversity on the map for British Columbia conservation planning</a></td>
      <td><a title='c7a168e8-f15e-446f-a49d-0b4a1f043ac2' href='records/c7a168e8-f15e-446f-a49d-0b4a1f043ac2'>1</a></td>
      <td>Genomics, Oceanography</td>
      <td>2026-09-28</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_53189107-9df5-426b-acb4-f903468554fe'>Comparing invertebrate and seaweed diversity in kelp forests and urchin barrens in Owen Bay, British Columbia, using Autonomous Reef Monitoring Structures (ARMS)</a></td>
      <td><a title='c4932b55-1dd8-4f2f-89da-5822056ecc37' href='records/c4932b55-1dd8-4f2f-89da-5822056ecc37'>1</a></td>
      <td>Sentinels of Change, Genomics</td>
      <td>2026-08-25</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d986aade-6bf1-4dfa-97c2-686975f944d5'>Watersheds Stream Stations Timeseries, Calvert and Hecate Islands, BC, Canada (Research)</a></td>
      <td><a title='ff456916-01f7-4eb0-961f-3658f0b4f39b' href='records/ff456916-01f7-4eb0-961f-3658f0b4f39b'>1</a></td>
      <td>Watersheds</td>
      <td>2026-07-13</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a8671db6-81cc-4c92-b681-58595fe66182'>Water Property Measurements from the Bute Inlet Ocean Observing Station (BIOOS) Wirewalker, Bute Inlet, BC, Canada (Provisional)</a></td>
      <td><a title='2510cc69-bd46-4534-a62f-dae1903b388d' href='records/2510cc69-bd46-4534-a62f-dae1903b388d'>2</a></td>
      <td>Oceanography</td>
      <td>2026-08-14</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_33c8ce77-0674-4933-a305-01a25d253f70'>Sea star microbiome data from 16S amplicon sequencing associated with rocky intertidal sites on Calvert and Quadra Islands</a></td>
      <td><a title='e14d0456-297e-4636-8e7c-c615791b165e' href='records/e14d0456-297e-4636-8e7c-c615791b165e'>1</a></td>
      <td>Nearshore, Genomics</td>
      <td>2026-10-16</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_91107fce-93a4-4bc9-bce4-e7d9e1cf02a0'>Sentinel 3A and 3B Chlorophyll and Suspended Matter Concentrations for Coastal British Columbia and Southeast Alaska, 8-Day Average (Research)</a></td>
      <td><a title='185462b6-5d10-43d8-91b2-b92010e80ff4' href='records/185462b6-5d10-43d8-91b2-b92010e80ff4'>2</a></td>
      <td>Oceanography</td>
      <td>2026-10-29</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d1bef0b7-4d15-4bc1-bf34-faca6352891f'>Daily satellite (Sentinel 3A and 3B) chlorophyll and suspended matter concentrations for coastal British Columbia and southeast Alaska</a></td>
      <td><a title='caf810f0-228a-4827-856c-f9b07a2377af' href='records/caf810f0-228a-4827-856c-f9b07a2377af'>3</a></td>
      <td>Oceanography</td>
      <td>2026-10-29</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ba41d935-f293-447f-be3d-7098e569b431'>Water Property Measurements from Conductivity-Temperature-Depth Profilers, BC, Canada (Research)</a></td>
      <td><a title='613ba2f9-b21d-445f-8eaa-f42950c9350b' href='records/613ba2f9-b21d-445f-8eaa-f42950c9350b'>1</a></td>
      <td>Oceanography, Nearshore, Watersheds, Juvenile Salmon Program</td>
      <td>2026-09-28</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_84820f31-b6db-479c-a47e-f22f2899b4d2'>Biogeochemical Sampling of 28 Streams on Vancouver Island</a></td>
      <td><a title='0e92249d-74e1-4253-a8a5-876d08a8ff65' href='records/0e92249d-74e1-4253-a8a5-876d08a8ff65'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a924b31b-9882-4abe-8d8e-e875dbbbec82'>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Bute Inlet Ocean Observing Station (BIOOS) Buoy, Bute Inlet, BC, Canada (Provisional)</a></td>
      <td><a title='5dea887f-9b1d-4b20-a59a-3d4a2877a52c' href='records/5dea887f-9b1d-4b20-a59a-3d4a2877a52c'>1</a></td>
      <td>Oceanography</td>
      <td>2026-07-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bfefcdf9-c922-4e4f-a958-aa6da739d3cd'>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Bute Inlet Ocean Observing Station (BIOOS) Buoy, Bute Inlet, BC, Canada (Research)</a></td>
      <td><a title='0894f661-f9cb-48cb-a0b4-8a001eb69420' href='records/0894f661-f9cb-48cb-a0b4-8a001eb69420'>1</a></td>
      <td>Oceanography</td>
      <td>2026-07-28</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_39a83551-ab8e-45be-a564-cece4b229371'>Zooplankton taxonomic abundance and biomass along the BC Coast</a></td>
      <td><a title='139df6dd-772b-424f-b830-30a5ba6abfc6' href='records/139df6dd-772b-424f-b830-30a5ba6abfc6'>1</a></td>
      <td>Oceanography</td>
      <td>2026-10-29</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dbb33efe-c207-4d9c-abef-2350595bf47a'>Size-fractionated zooplankton biomass and isotopes along the BC coast</a></td>
      <td><a title='186d3139-66a1-43f9-9ac7-c5607252146e' href='records/186d3139-66a1-43f9-9ac7-c5607252146e'>1</a></td>
      <td>Oceanography</td>
      <td>2026-10-27</td>
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d55021c3-a142-4e14-8208-36c9826c1893'>Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, BC, Canada (Research)</a></td>
      <td><a title='8882a149-fabd-4ecd-98d3-68a2a88aee38' href='records/8882a149-fabd-4ecd-98d3-68a2a88aee38'>1</a></td>
      <td>Oceanography</td>
      <td>2026-10-29</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_86343dd1-28d0-4d02-8eaf-402d51a7fef7'>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program (Provisional)</a></td>
      <td><a title='acd6c43f-6cbd-43c8-9bff-7d9ae6630295' href='records/acd6c43f-6cbd-43c8-9bff-7d9ae6630295'>2</a></td>
      <td>Juvenile Salmon Program</td>
      <td>2026-09-28</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d049351d-b806-461f-85fb-451f100fd7d6'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)</a></td>
      <td><a title='78b2edef-dab3-47a9-93bb-af63dfcd178d' href='records/78b2edef-dab3-47a9-93bb-af63dfcd178d'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-30</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c981d76-5fea-44af-904f-58b159838b0a'>Stream Event Sampling - Calvert Island</a></td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='records/def2a409-2319-4e8c-a584-9a467f044ada'>1</a></td>
      <td>Watersheds, Geospatial</td>
      <td>2026-07-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_25674e9b-1d49-4270-b917-cfe6cdc30f95'>Watersheds of the northern Pacific coastal temperate rainforest margin</a></td>
      <td><a title='30560220-bc44-4020-b424-0abf617d1c00' href='records/30560220-bc44-4020-b424-0abf617d1c00'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-03</td>
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
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dd325fc4-033c-4696-b38d-0ac883ad67eb'>Underway Surface Seawater and Marine CO2 Boundary Layer Observations from the M/V Columbia (Research)</a></td>
      <td><a title='8bcf556e-26e2-41d4-af2c-2192c0426523' href='records/8bcf556e-26e2-41d4-af2c-2192c0426523'>1</a></td>
      <td>Oceanography</td>
      <td>2026-09-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8b069feb-57fc-4d57-bf5c-761fd7cf0b45'>Surface Seawater and Marine Boundary Layer CO2 Observations from the Kwakshua Channel (KC) Buoy on the Central Coast of British Columbia (Research)</a></td>
      <td><a title='3f883dc6-56ac-42f5-a1d4-6de554a9e63d' href='records/3f883dc6-56ac-42f5-a1d4-6de554a9e63d'>1</a></td>
      <td>Oceanography</td>
      <td>2026-09-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b62c3aaa-c3b8-41cb-b035-4da16209f26a'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Provisional)</a></td>
      <td><a title='5143957b-ee18-44d3-8000-a9c8f9a34a0d' href='records/5143957b-ee18-44d3-8000-a9c8f9a34a0d'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fe76ef4c-254a-44fe-87bc-052cd3aa9663'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Research)</a></td>
      <td><a title='79433a1f-ec07-4cd5-a31a-8c2c53069085' href='records/79433a1f-ec07-4cd5-a31a-8c2c53069085'>1</a></td>
      <td>Oceanography</td>
      <td>2026-09-08</td>
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