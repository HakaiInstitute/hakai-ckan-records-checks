---
hide:
  - navigation
  - toc
---

<style>.md-content__inner > h1 { display: none; }</style>

*Last updated: 2026-07-14*

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2.5rem;">

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">266</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Total Records</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">-1 since 2026-07-13</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid red;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">39</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Records with Issues</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:red;margin-top:0.5rem;">+27 since 2026-07-13</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">97.0%</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">% Records with DOI</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-07-13</div>
  
  
</div>

</div>

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {"data": [{"hovertemplate": "Number of Records with Issue=%{text}<br>message=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#AA2026", "pattern": {"shape": ""}}, "name": "", "orientation": "h", "showlegend": false, "text": [2.0, 2.0, 3.0, 9.0, 26.0], "textposition": "outside", "x": [2, 2, 3, 9, 26], "xaxis": "x", "y": ["No funder", "No DOI defined", "Tentative dataset should not have a version", "Invalid Resource URL", "Contact missing affiliation"], "yaxis": "y", "type": "bar", "cliponaxis": false}], "layout": {"template": {"data": {"scatter": [{"type": "scatter"}]}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "Number of Records with Issue"}, "tickformat": "d"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {}, "tickfont": {"size": 10}, "linecolor": "black", "automargin": true}, "legend": {"tracegroupgap": 0}, "margin": {"t": 20, "l": 0, "r": 60, "b": 40}, "barmode": "relative", "plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)", "showlegend": false}};
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a8671db6-81cc-4c92-b681-58595fe66182'>Water Property Measurements from the Bute Inlet Ocean Observing Station (BIOOS) Wirewalker, Bute Inlet, BC, Canada (Provisional)</a></td>
      <td><a title='2510cc69-bd46-4534-a62f-dae1903b388d' href='records/2510cc69-bd46-4534-a62f-dae1903b388d'>2</a></td>
      <td>Oceanography</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f7538807-4d49-4ed8-ad36-836c0e71428a'>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</a></td>
      <td><a title='b7b923ed-b3fa-48b3-878d-40a3797046bc' href='records/b7b923ed-b3fa-48b3-878d-40a3797046bc'>1</a></td>
      <td>Geospatial, Airborne Coastal Observatory</td>
      <td>2026-04-16</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ba41d935-f293-447f-be3d-7098e569b431'>Water Property Measurements from Conductivity-Temperature-Depth Profiles, BC, Canada (Research)</a></td>
      <td><a title='613ba2f9-b21d-445f-8eaa-f42950c9350b' href='records/613ba2f9-b21d-445f-8eaa-f42950c9350b'>3</a></td>
      <td>Oceanography, Nearshore, Watersheds, Juvenile Salmon Program</td>
      <td>2026-06-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_84820f31-b6db-479c-a47e-f22f2899b4d2'>Biogeochemical Sampling of 28 Streams on Vancouver Island</a></td>
      <td><a title='0e92249d-74e1-4253-a8a5-876d08a8ff65' href='records/0e92249d-74e1-4253-a8a5-876d08a8ff65'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-22</td>
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
      <td>2026-03-19</td>
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_314a0846-0fe9-4c2e-81e2-d2b24ac98b6e'>Understory kelp biomass data from BC Central Coast</a></td>
      <td><a title='5576c279-6d3a-4323-8104-0e1040d9906c' href='records/5576c279-6d3a-4323-8104-0e1040d9906c'>1</a></td>
      <td>Nearshore</td>
      <td>2025-03-04</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9fafb4c8-e61f-4372-ac71-c1ddbe57d80c'>Data record does not exist anymore: Geomorphology - Calvert Island</a></td>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='records/49967494-a7b6-4128-b336-671971d1e2c6'>2</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2026-06-09</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_52797e17-c0ed-46a4-9dcd-e34f801c6205'>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</a></td>
      <td><a title='a8f61379-14f9-4ccc-bc9b-4408ba8340d7' href='records/a8f61379-14f9-4ccc-bc9b-4408ba8340d7'>1</a></td>
      <td>Nearshore</td>
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_67e89414-a93f-496d-9766-9311f0d3954e'>Motile Invertebrate Surveys - BC Central Coast</a></td>
      <td><a title='1dfdbadf-6314-4411-8d18-752f6dd920e9' href='records/1dfdbadf-6314-4411-8d18-752f6dd920e9'>5</a></td>
      <td>Nearshore</td>
      <td>2026-03-25</td>
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_93a9bb9a-b54e-4623-9e0e-93d8b7d0020b'>Surfgrass Community Structure - Length & Density - BC Central Coast</a></td>
      <td><a title='f51d96b5-1827-4aab-b1ce-575faff1fd03' href='records/f51d96b5-1827-4aab-b1ce-575faff1fd03'>1</a></td>
      <td>Nearshore</td>
      <td>2026-06-11</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c89e35df-8a16-4efc-ae29-15f4e3da8a55'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</a></td>
      <td><a title='6ce6e697-d539-41b1-9771-b5e859a6ff50' href='records/6ce6e697-d539-41b1-9771-b5e859a6ff50'>4</a></td>
      <td>Nearshore</td>
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cec3dcef-8dba-4d91-aee6-b60ce416497c'>Mussel Dynamics - Point Intercepts - BC Central Coast</a></td>
      <td><a title='46377bf0-06d5-4612-970d-29cd972e4870' href='records/46377bf0-06d5-4612-970d-29cd972e4870'>2</a></td>
      <td>Nearshore</td>
      <td>2026-06-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d683512f-5e47-4b1d-baac-c653fb761806'>Mussel Dynamics - Length & Bed Depth - BC Central Coast</a></td>
      <td><a title='967f98cb-131a-421e-bcfd-467cff973b30' href='records/967f98cb-131a-421e-bcfd-467cff973b30'>3</a></td>
      <td>Nearshore</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c981d76-5fea-44af-904f-58b159838b0a'>Stream Event Sampling - Calvert Island</a></td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='records/def2a409-2319-4e8c-a584-9a467f044ada'>5</a></td>
      <td>Watersheds, Geospatial</td>
      <td>2026-06-09</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_de9b2a6d-9ba0-4384-9adf-22abc0eb061f'>Stream Event Sampling - Calvert Island - 2015-2018</a></td>
      <td><a title='324c5ae3-b0ac-4302-b701-598ebbb25870' href='records/324c5ae3-b0ac-4302-b701-598ebbb25870'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0e446321-34f3-4d5a-8c7d-79c89eb76373'>Stream temperature time-series – Calvert Island – 2013 - 2019</a></td>
      <td><a title='bfad4541-a06a-489e-bd95-a5e7c65e0dc1' href='records/bfad4541-a06a-489e-bd95-a5e7c65e0dc1'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-08</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0e4f324c-6498-4c89-9e19-f2f9f474a1df'>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</a></td>
      <td><a title='e1b86825-d43b-47e1-bf45-ab791f44772d' href='records/e1b86825-d43b-47e1-bf45-ab791f44772d'>1</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_184b2f81-d87f-4615-a026-15b87930d15c'>Aquatic carbon flux data package for Oliver et al. 2017</a></td>
      <td><a title='1be9154a-1497-42eb-8821-b0d63000814c' href='records/1be9154a-1497-42eb-8821-b0d63000814c'>3</a></td>
      <td>Watersheds</td>
      <td>2026-06-30</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_26443ab2-964f-4031-a53b-f132434573e8'>Ecosystem Comparison Plots - Calvert Island</a></td>
      <td><a title='d8754c99-a540-4085-8c66-d9447da5f6e9' href='records/d8754c99-a540-4085-8c66-d9447da5f6e9'>1</a></td>
      <td>Geospatial, Watersheds</td>
      <td>2026-07-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5b0b2db4-21d7-48b8-9616-255ba2267868'>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019</a></td>
      <td><a title='c06cb551-351c-456f-8d0c-c8aab9aec162' href='records/c06cb551-351c-456f-8d0c-c8aab9aec162'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_74f47ab6-a1ca-4aef-9115-cf2baaf87bef'>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada</a></td>
      <td><a title='41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' href='records/41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d'>1</a></td>
      <td>Watersheds, Oceanography</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7de2d85e-202e-4e4a-953e-539f9d18e8c7'>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</a></td>
      <td><a title='4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' href='records/4f1e8eac-8390-44d8-93d6-9263fc1dfcf9'>1</a></td>
      <td>Watersheds</td>
      <td>2026-06-03</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9201118a-b0c4-470f-a76f-396bacc5e93e'>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada</a></td>
      <td><a title='55e7c337-02e8-4200-8ea9-88241d978f96' href='records/55e7c337-02e8-4200-8ea9-88241d978f96'>2</a></td>
      <td>Oceanography</td>
      <td>2026-07-10</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_97684a5c-9b70-4d8c-854b-9de895d3d71e'>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019</a></td>
      <td><a title='49ec67e4-f7be-4658-b2b6-e4b57d9901df' href='records/49ec67e4-f7be-4658-b2b6-e4b57d9901df'>2</a></td>
      <td>Watersheds</td>
      <td>2026-06-15</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c113d7a8-6a46-46fc-b49c-a4e69afedfbc'>Hakai Institute’s Burke-o-Lator TCO2/pCO2 Analyzer Discrete Sample Analysis Protocols</a></td>
      <td><a title='9e4a38d6-eb29-44a8-b495-c56ce74a227c' href='records/9e4a38d6-eb29-44a8-b495-c56ce74a227c'>1</a></td>
      <td>Oceanography</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_154e88e6-2300-4ca0-b3f8-ee822d32a9a4'>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</a></td>
      <td><a title='a31d44d5-2ce5-4d03-8d0b-4549023840ff' href='records/a31d44d5-2ce5-4d03-8d0b-4549023840ff'>3</a></td>
      <td>Nearshore</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_15caa6c8-be9b-4f19-81ae-bb82321eafd6'>Mean Tidal Current - Coastal British Columbia - Canada</a></td>
      <td><a title='646dd927-3248-4fc9-970c-abea15f7d304' href='records/646dd927-3248-4fc9-970c-abea15f7d304'>2</a></td>
      <td>Geospatial, Oceanography</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3bc02dd8-7654-44f0-8c7c-02739937bdf4'>Seastar & Macroinvertebrate Dynamics - BC Central Coast</a></td>
      <td><a title='98bc62c7-d6a4-42bd-9110-c8021380d8a5' href='records/98bc62c7-d6a4-42bd-9110-c8021380d8a5'>5</a></td>
      <td>Nearshore</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d87de5ca-a18a-406d-a4c1-74e6f8f28e5b'>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</a></td>
      <td><a title='6a6908af-8856-431e-8277-458fee82e534' href='records/6a6908af-8856-431e-8277-458fee82e534'>4</a></td>
      <td>Nearshore</td>
      <td>2024-08-02</td>
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