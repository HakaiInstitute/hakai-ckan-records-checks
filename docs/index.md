---
hide:
  - navigation
  - toc
---

<style>.md-content__inner > h1 { display: none; }</style>

*Last updated: 2026-07-30*

<div style="display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0 2.5rem;">

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">284</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Total Records</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-07-30</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid red;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">32</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">Records with Issues</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:red;margin-top:0.5rem;">+1 since 2026-07-30</div>
  
  
</div>

<div style="flex:1;min-width:150px;padding:1.25rem 1.5rem;border-radius:8px;background:var(--md-code-bg-color);text-align:center;border-top:3px solid gray;box-shadow:0 1px 4px rgba(0,0,0,.08);">
  <div style="font-size:2.2rem;font-weight:700;line-height:1.1;letter-spacing:-0.02em;">96.5%</div>
  <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;opacity:0.55;margin-top:0.5rem;">% Records with DOI</div>
  
  
  <div style="font-size:0.8rem;font-weight:600;color:gray;margin-top:0.5rem;">No change since 2026-07-30</div>
  
  
</div>

</div>

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {"data": [{"hovertemplate": "Number of Records with Issue=%{text}<br>message=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#AA2026", "pattern": {"shape": ""}}, "name": "", "orientation": "h", "showlegend": false, "text": [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 4.0, 6.0, 6.0, 6.0, 7.0, 7.0, 8.0], "textposition": "outside", "x": [1, 1, 1, 1, 2, 2, 3, 4, 6, 6, 6, 7, 7, 8], "xaxis": "x", "y": ["Contact missing affiliation", "Empty resource name", "Record DOI HTTPS link is failling", "No publisher", "Contact missing ORCID", "No projects associated", "Broken link (202)", "No DOI defined", "No funder", "Broken link (404)", "Duplicate DOI shared with another record", "Invalid Resource URL", "No version", "Metadata mismatch"], "yaxis": "y", "type": "bar", "cliponaxis": false}], "layout": {"template": {"data": {"scatter": [{"type": "scatter"}]}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "Number of Records with Issue"}, "tickformat": "d"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {}, "tickfont": {"size": 10}, "linecolor": "black", "automargin": true}, "legend": {"tracegroupgap": 0}, "margin": {"t": 20, "l": 0, "r": 60, "b": 40}, "barmode": "relative", "plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)", "showlegend": false}};
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c7466354-bacc-4781-acdc-543dd03d1eab'>Nanwakolas LiDAR Surveys - Airborne Coastal Observatory</a></td>
      <td><a title='0ca4de0c-62a4-4349-a780-a07dc17bfe38' href='records/0ca4de0c-62a4-4349-a780-a07dc17bfe38'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2026-03-26</td>
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
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5843a289-2c88-4253-bed8-25b5b58b1d79'>Kelp and Seagrass Mapping – 2022 – Hakai Airborne Coastal Observatory</a></td>
      <td><a title='4c558062-0e9b-4f49-8680-15e3ccb11ea5' href='records/4c558062-0e9b-4f49-8680-15e3ccb11ea5'>1</a></td>
      <td>Geospatial, Airborne Coastal Observatory, Nearshore</td>
      <td>2024-12-05</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_58d82567-18b8-456a-a124-41b81661a5b2'>Kelp and Eelgrass Mapping – BC Central Coast – 2021 - Hakai Airborne Coastal Observatory</a></td>
      <td><a title='5ec866ea-5a7a-43d4-9ed1-d4d863304f98' href='records/5ec866ea-5a7a-43d4-9ed1-d4d863304f98'>2</a></td>
      <td>Airborne Coastal Observatory, Geospatial</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_93a9bb9a-b54e-4623-9e0e-93d8b7d0020b'>Surfgrass Community Structure - Length & Density - BC Central Coast</a></td>
      <td><a title='f51d96b5-1827-4aab-b1ce-575faff1fd03' href='records/f51d96b5-1827-4aab-b1ce-575faff1fd03'>1</a></td>
      <td>Nearshore</td>
      <td>2026-07-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c981d76-5fea-44af-904f-58b159838b0a'>Stream Event Sampling - Calvert Island</a></td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='records/def2a409-2319-4e8c-a584-9a467f044ada'>1</a></td>
      <td>Watersheds, Geospatial</td>
      <td>2026-07-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6844547c-708e-437b-aef7-157b4d9d9bcb'>Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada</a></td>
      <td><a title='3c4cc294-1e9a-410e-81b0-0d9461e4b1c9' href='records/3c4cc294-1e9a-410e-81b0-0d9461e4b1c9'>1</a></td>
      <td>Watersheds, Oceanography</td>
      <td>2026-06-26</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_74f47ab6-a1ca-4aef-9115-cf2baaf87bef'>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada</a></td>
      <td><a title='41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' href='records/41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d'>1</a></td>
      <td>Watersheds, Oceanography</td>
      <td>2026-07-17</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5cf59eac-2fb4-4ed2-8ffc-372030c9438e'>Koeye River stream temperature, stage, and conductivity time-series version 1</a></td>
      <td><a title='5c358eb3-80e8-40ab-b930-524ab8a59abe' href='records/5c358eb3-80e8-40ab-b930-524ab8a59abe'>1</a></td>
      <td>Watersheds</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b5207300-9f76-4f14-ae6f-a08ed6f5a213'>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</a></td>
      <td><a title='d39d1eb3-878d-4597-a06a-a85c50dfccee' href='records/d39d1eb3-878d-4597-a06a-a85c50dfccee'>12</a></td>
      <td>Watersheds</td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dfa79d1b-25ce-44d0-94e9-39c807bd06b6'>Koeye River stream temperature, stage, and conductivity time-series version 2</a></td>
      <td><a title='ed19c0b0-2a18-4380-a281-953fd769de92' href='records/ed19c0b0-2a18-4380-a281-953fd769de92'>7</a></td>
      <td></td>
      <td>2024-07-23</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ef59cc12-5031-4c65-b379-7ca03ad76d34'>Precipitation time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</a></td>
      <td><a title='55826c6b-772a-45b4-a869-b97a4774e232' href='records/55826c6b-772a-45b4-a869-b97a4774e232'>1</a></td>
      <td>Watersheds</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_244b5915-0ccf-4fab-9720-d2ac9394a27b'>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</a></td>
      <td><a title='36624f4e-7444-4489-be2b-f18df5b96343' href='records/36624f4e-7444-4489-be2b-f18df5b96343'>3</a></td>
      <td>Airborne Coastal Observatory</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4034f474-4d52-4a9e-9650-f3c6bd5011e0'>Kelp Canopy Extent 2006 - NW Calvert Island</a></td>
      <td><a title='0f19ac6e-dc86-445b-b2da-7b61a389222e' href='records/0f19ac6e-dc86-445b-b2da-7b61a389222e'>1</a></td>
      <td>Geospatial, Nearshore</td>
      <td>2026-05-25</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7241811a-f75c-469f-baa2-ad769d6c75cd'>Kelp Canopy Extent - Calvert Island - 2006-2016 - British Columbia - Canada</a></td>
      <td><a title='9001b91c-b03a-45e0-a4ba-ac6e301b515b' href='records/9001b91c-b03a-45e0-a4ba-ac6e301b515b'>7</a></td>
      <td></td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_73abfecf-d35c-4f9c-a991-eee5cece08ea'>Kelp Canopy Extent 2012 - NW Calvert Island</a></td>
      <td><a title='3c07678b-082b-4c23-878f-6720715dabed' href='records/3c07678b-082b-4c23-878f-6720715dabed'>2</a></td>
      <td>Geospatial</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4b5c0c20-2115-4986-bf56-237e360240bd'>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</a></td>
      <td><a title='806312b3-91f8-4651-8980-044a0ad52698' href='records/806312b3-91f8-4651-8980-044a0ad52698'>3</a></td>
      <td>Oceanography, Watersheds</td>
      <td>2025-01-30</td>
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
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0219e1d6-8dfc-4718-b89b-ea3dff06a70d'>Eelgrass Extent - Coastal British Columbia</a></td>
      <td><a title='0026051c-f514-45d2-bb17-bfe1dc53e96c' href='records/0026051c-f514-45d2-bb17-bfe1dc53e96c'>1</a></td>
      <td>Geospatial</td>
      <td>2024-07-24</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1aeeb145-8112-4268-afc7-05f14c8eae63'>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</a></td>
      <td><a title='ab883f0c-0f7c-4ef1-a8a4-c67e82020e0b' href='records/ab883f0c-0f7c-4ef1-a8a4-c67e82020e0b'>4</a></td>
      <td>Nearshore</td>
      <td>2026-06-11</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7ddae37a-e706-45d2-8060-8306300a98c8'>Oceanographic Mooring Time Series, Hyacinthe Bay, BC, Canada (Provisional)</a></td>
      <td><a title='7c2b8668-75a3-4fc8-bff3-bdae5d95f52d' href='records/7c2b8668-75a3-4fc8-bff3-bdae5d95f52d'>1</a></td>
      <td>Oceanography</td>
      <td>2026-06-22</td>
    </tr>
    <tr>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_05d92ed0-25a0-4108-bce5-0425a934361e'>Nearshore substrate classification - Northwest Calvert Island, BC (2015-2017)</a></td>
      <td><a title='b646021f-ec59-490b-b43f-8118e20d2ef6' href='records/b646021f-ec59-490b-b43f-8118e20d2ef6'>7</a></td>
      <td>Nearshore, Geospatial</td>
      <td>2024-07-23</td>
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