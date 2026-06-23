---
hide:
 - toc
---
# Hakai Metadata Records Issue Summary

This page present a summary of issues detected on the [Hakai Catalogue]().

## Issue Distribution

<div id="issue-distribution-chart" style="width:100%;min-height:400px;"></div>
<script>
(function waitForPlotly() {
  if (typeof Plotly !== 'undefined') {
    var fig = {"data": [{"hovertemplate": "Number of Records with Issue=%{text}<br>message=%{y}<extra></extra>", "legendgroup": "", "marker": {"color": "#AA2026", "pattern": {"shape": ""}}, "name": "", "orientation": "h", "showlegend": false, "text": [1.0, 2.0, 6.0, 8.0, 14.0, 24.0, 55.0, 57.0], "textposition": "outside", "x": [1, 2, 6, 8, 14, 24, 55, 57], "xaxis": "x", "y": ["Record DOI HTTPS link is failling", "Duplicate DOI shared with another record", "Malformed related work identifier (missing doi.org)", "Invalid Resource URL", "No funder", "No DOI defined", "No version", "Metadata mismatch"], "yaxis": "y", "type": "bar", "cliponaxis": false}], "layout": {"template": {"data": {"scatter": [{"type": "scatter"}]}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "Number of Records with Issue"}, "tickformat": "d"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {}, "tickfont": {"size": 10}, "linecolor": "black", "automargin": true}, "legend": {"tracegroupgap": 0}, "margin": {"t": 20, "l": 0, "r": 60, "b": 40}, "barmode": "relative", "plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)", "showlegend": false}};
    var el = document.getElementById('issue-distribution-chart');
    Plotly.newPlot(el, fig.data, fig.layout, {responsive: true}).then(function() {
      el.on('plotly_click', function(data) {
        var label = data.points[0].y;
        var slug = label.replace(/[.'"]/g, '').replace(/[^a-zA-Z0-9]/g, '-').toLowerCase().replace(/-+/g, '-');
        window.location.href = slug + '/';
      });
    });
  } else {
    setTimeout(waitForPlotly, 50);
  }
})();
</script>

## Records Summary

<table border="1" class="dataframe table table-striped table-hover table-sm" id="records_table">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>publication</th>
      <th>revision</th>
      <th>Issues</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>262</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5e4f925a-9cf2-4e33-ae22-75c5b326ce6c'>Time series of eelgrass (Zostera marina) meadow extent derived from drone surveys, Central Coast, British Columbia</a></td>
      <td>2026-06-16</td>
      <td>2026-06-16</td>
      <td></td>
    </tr>
    <tr>
      <th>261</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b45dbc9d-bf7a-4734-86cd-3397e7c9ac62'>Sea surface temperature data in False Creek, British Columbia</a></td>
      <td>2026-06-08</td>
      <td>2026-06-08</td>
      <td><a title='05dac0a6-a26c-4cb5-895d-132b5e2134cd' href='../records/05dac0a6-a26c-4cb5-895d-132b5e2134cd'>1</a></td>
    </tr>
    <tr>
      <th>259</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2e5ddbaa-4f0c-4339-8595-1ddbd35c3df4'>Glacier and Icefield Aerial Surveys in British Columbia, Washington, and Alberta - 2025 - Airborne Coastal Observatory</a></td>
      <td>2026-06-02</td>
      <td>2026-06-02</td>
      <td></td>
    </tr>
    <tr>
      <th>260</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_656ea307-fed0-48ca-b5d8-1bc017dc52d2'>Botanical Beach - Juan de Fuca Provincial Park - Drone Mapping</a></td>
      <td>2026-06-02</td>
      <td>2026-06-02</td>
      <td></td>
    </tr>
    <tr>
      <th>257</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6c34ed6e-5a17-41f2-b83a-cd59d1ce07bd'>Knight Inlet Multibeam Bathymetry Survey</a></td>
      <td>2026-05-28</td>
      <td>2026-05-28</td>
      <td></td>
    </tr>
    <tr>
      <th>258</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8755f475-2133-4205-baff-5e2937824f45'>Poole Creek Aerial Surveys - Airborne Coastal Observatory</a></td>
      <td>2026-05-28</td>
      <td>2026-05-28</td>
      <td></td>
    </tr>
    <tr>
      <th>255</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7e49967a-b5ab-443d-860b-e3c0eb0f709c'>Horne Lake Bathymetry Mapping</a></td>
      <td>2026-05-27</td>
      <td>2026-05-27</td>
      <td><a title='ed22dc0f-f2cc-41e5-ac1c-893e1b65c6d0' href='../records/ed22dc0f-f2cc-41e5-ac1c-893e1b65c6d0'>3</a></td>
    </tr>
    <tr>
      <th>256</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e897c9d0-3fca-4c89-b37f-e571413ffd12'>Joffre Provincial Park Aerial Surveys - 2025 - Airborne Coastal Observatory</a></td>
      <td>2026-05-27</td>
      <td>2026-05-28</td>
      <td></td>
    </tr>
    <tr>
      <th>254</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a8671db6-81cc-4c92-b681-58595fe66182'>Water Property Measurements from the Bute Inlet Ocean Observing Station (BIOOS) Wirewalker, Bute Inlet, BC, Canada (Provisional)</a></td>
      <td>2026-04-27</td>
      <td>2026-04-27</td>
      <td><a title='2510cc69-bd46-4534-a62f-dae1903b388d' href='../records/2510cc69-bd46-4534-a62f-dae1903b388d'>1</a></td>
    </tr>
    <tr>
      <th>253</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_33c8ce77-0674-4933-a305-01a25d253f70'>Sea star microbiome data from 16S amplicon sequencing associated with rocky intertidal sites on Calvert and Quadra Islands</a></td>
      <td>2026-04-24</td>
      <td>2026-04-28</td>
      <td><a title='e14d0456-297e-4636-8e7c-c615791b165e' href='../records/e14d0456-297e-4636-8e7c-c615791b165e'>1</a></td>
    </tr>
    <tr>
      <th>252</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f7538807-4d49-4ed8-ad36-836c0e71428a'>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</a></td>
      <td>2026-04-16</td>
      <td>2026-04-16</td>
      <td></td>
    </tr>
    <tr>
      <th>250</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_91107fce-93a4-4bc9-bce4-e7d9e1cf02a0'>Sentinel 3A and 3B Chlorophyll and Suspended Matter Concentrations for Coastal British Columbia and Southeast Alaska, 8-Day Average (Research)</a></td>
      <td>2026-04-15</td>
      <td>2026-05-08</td>
      <td></td>
    </tr>
    <tr>
      <th>251</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d1bef0b7-4d15-4bc1-bf34-faca6352891f'>Daily satellite (Sentinel 3A and 3B) chlorophyll and suspended matter concentrations for coastal British Columbia and southeast Alaska</a></td>
      <td>2026-04-15</td>
      <td>2026-05-26</td>
      <td></td>
    </tr>
    <tr>
      <th>248</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ba41d935-f293-447f-be3d-7098e569b431'>Water Property Measurements from Conductivity-Temperature-Depth Profiles, BC, Canada (Research)</a></td>
      <td>2026-04-13</td>
      <td>2026-04-13</td>
      <td></td>
    </tr>
    <tr>
      <th>249</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fb5c9e1e-a911-46b7-8c1d-e34215a105ed'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 Analyzer located at Bamfield Marine Sciences Centre, Bamfield, BC, Canada (Provisional)</a></td>
      <td>2026-04-13</td>
      <td>2026-04-15</td>
      <td><a title='c657dfa1-5970-4794-9c46-7c352df393d7' href='../records/c657dfa1-5970-4794-9c46-7c352df393d7'>1</a></td>
    </tr>
    <tr>
      <th>247</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bafcd0eb-8249-471b-b93b-0797cfeea287'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2020), Central Coast, British Columbia, Canada</a></td>
      <td>2026-03-30</td>
      <td>2026-03-30</td>
      <td></td>
    </tr>
    <tr>
      <th>245</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1efbadd2-e735-48cc-9498-e3a5a88e48a6'>Seawater Carbon Dioxide (CO2) Content from the SuperCO2 System in the Pacific Ecosystem Autonomous Research Laboratory, Bamfield Marine Sciences Centre, BC, Canada (Provisional)</a></td>
      <td>2026-03-27</td>
      <td>2026-04-13</td>
      <td><a title='c5dafa6e-f2df-4f02-a94e-8f82b29dfb66' href='../records/c5dafa6e-f2df-4f02-a94e-8f82b29dfb66'>1</a></td>
    </tr>
    <tr>
      <th>246</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b2b18171-35b6-4345-b81b-497a90c2e7c5'>Seagrass fish and macroinvertebrate swaths BC Central Coast</a></td>
      <td>2026-03-27</td>
      <td>2026-03-27</td>
      <td></td>
    </tr>
    <tr>
      <th>244</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d7b34963-67bc-404b-bdd1-b41cc750bdaa'>Fraser River Airborne Surveys - 2020 - Airborne Coastal Observatory</a></td>
      <td>2026-03-26</td>
      <td>2026-03-26</td>
      <td></td>
    </tr>
    <tr>
      <th>243</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_84820f31-b6db-479c-a47e-f22f2899b4d2'>Biogeochemical Sampling of 28 Streams on Vancouver Island</a></td>
      <td>2026-03-20</td>
      <td>2026-04-24</td>
      <td><a title='0e92249d-74e1-4253-a8a5-876d08a8ff65' href='../records/0e92249d-74e1-4253-a8a5-876d08a8ff65'>2</a></td>
    </tr>
    <tr>
      <th>242</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_984e6b72-15d0-4742-bb2d-9ac13b14383a'>Stream Temperature Observations for Three Streams Near Gold River</a></td>
      <td>2026-03-09</td>
      <td>2026-04-16</td>
      <td></td>
    </tr>
    <tr>
      <th>240</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a924b31b-9882-4abe-8d8e-e875dbbbec82'>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Bute Inlet Ocean Observing Station (BIOOS) Buoy, Bute Inlet, BC, Canada (Provisional)</a></td>
      <td>2026-02-27</td>
      <td>2026-05-26</td>
      <td><a title='5dea887f-9b1d-4b20-a59a-3d4a2877a52c' href='../records/5dea887f-9b1d-4b20-a59a-3d4a2877a52c'>4</a></td>
    </tr>
    <tr>
      <th>241</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bfefcdf9-c922-4e4f-a958-aa6da739d3cd'>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Bute Inlet Ocean Observing Station (BIOOS) Buoy, Bute Inlet, BC, Canada (Research)</a></td>
      <td>2026-02-27</td>
      <td>2026-04-15</td>
      <td></td>
    </tr>
    <tr>
      <th>239</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cfa4ad65-ee12-47c0-9527-206a0f8d92ae'>Hakai Institute Drone Data Index</a></td>
      <td>2026-02-24</td>
      <td>2026-04-15</td>
      <td></td>
    </tr>
    <tr>
      <th>238</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7cafde4f-bdd5-4b95-a41d-7939ddcf08c6'>Time series of quarterly kelp canopy extent from Landsat 5, 7, 8, and 9 since 1985</a></td>
      <td>2026-01-29</td>
      <td>2026-01-30</td>
      <td><a title='a48161da-c603-43d6-9dc6-44b861984b49' href='../records/a48161da-c603-43d6-9dc6-44b861984b49'>2</a></td>
    </tr>
    <tr>
      <th>237</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_43bad5e5-0484-4c11-80a5-c844245f940e'>Farwell Canyon Airborne Surveys - 2024 - Airborne Coastal Observatory</a></td>
      <td>2026-01-23</td>
      <td>2026-01-23</td>
      <td></td>
    </tr>
    <tr>
      <th>236</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c544ef5b-967d-46b2-bbcf-395116b50e7d'>Mystery Creek Aerial Photo and LiDAR Survey - 2025 - Airborne Coastal Observatory</a></td>
      <td>2025-12-16</td>
      <td>2025-12-15</td>
      <td></td>
    </tr>
    <tr>
      <th>234</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_35900174-c64a-493e-9a7e-390ac7e997e4'>Bowhead Whale Drone Data Collection - Cumberland Sound - Nunavut</a></td>
      <td>2025-12-15</td>
      <td>2026-05-04</td>
      <td></td>
    </tr>
    <tr>
      <th>235</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_78686602-1aa9-4246-8a24-915471fe4255'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2025), North Coast, British Columbia, Canada</a></td>
      <td>2025-12-15</td>
      <td>2025-12-15</td>
      <td></td>
    </tr>
    <tr>
      <th>232</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5b4cbe9f-8f2e-414c-80ff-741372891fe9'>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</a></td>
      <td>2025-11-12</td>
      <td>2026-02-27</td>
      <td><a title='b9671efe-5980-452b-90f8-f30e4f1bc194' href='../records/b9671efe-5980-452b-90f8-f30e4f1bc194'>2</a></td>
    </tr>
    <tr>
      <th>233</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b5f0f854-efe1-4132-808d-074244d813e1'>Gitga'at Territory Coastal Mapping Project</a></td>
      <td>2025-11-12</td>
      <td>2026-01-27</td>
      <td></td>
    </tr>
    <tr>
      <th>230</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_132cecdf-de8a-4b17-b610-0e2b3a343812'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Coast, British Columbia, Canada</a></td>
      <td>2025-10-31</td>
      <td>2025-10-31</td>
      <td></td>
    </tr>
    <tr>
      <th>231</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f815a700-c943-4d6f-afeb-a4854ad10cfc'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Vancouver Island, British Columbia, Canada</a></td>
      <td>2025-10-31</td>
      <td>2025-10-31</td>
      <td></td>
    </tr>
    <tr>
      <th>229</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9a018fe0-8bd1-41d1-af8d-079960b71473'>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</a></td>
      <td>2025-10-29</td>
      <td>2026-05-15</td>
      <td><a title='6be4c552-469a-4558-b63d-7a2c52566fe2' href='../records/6be4c552-469a-4558-b63d-7a2c52566fe2'>1</a></td>
    </tr>
    <tr>
      <th>228</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7e9c97a3-4bf1-4852-81b6-d74cedf2c94c'>Environmental DNA survey of Calvert Island, British Columbia, 2021</a></td>
      <td>2025-10-28</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>227</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_012164c6-28dd-4078-b702-f0c2ce63d548'>Biodiversity and Oceanographic data from the False Creek Bioblitz, 2022</a></td>
      <td>2025-10-18</td>
      <td>2026-03-19</td>
      <td></td>
    </tr>
    <tr>
      <th>226</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_291b98a4-d868-462c-852a-d6cf79ecf6ce'>Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia</a></td>
      <td>2025-10-14</td>
      <td>2025-10-14</td>
      <td><a title='39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' href='../records/39cc31fc-aa41-43f5-bfe7-48ea173b1f1e'>1</a></td>
    </tr>
    <tr>
      <th>223</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_34a20547-cb60-4ecf-901b-f4ca52eae451'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), Central Coast, British Columbia, Canada</a></td>
      <td>2025-10-06</td>
      <td>2025-10-31</td>
      <td></td>
    </tr>
    <tr>
      <th>224</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8343aa0-dbea-4267-9f78-662bec08d4bc'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2020-2022), Central Coast, British Columbia, Canada</a></td>
      <td>2025-10-06</td>
      <td>2025-10-06</td>
      <td></td>
    </tr>
    <tr>
      <th>225</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f7a867ce-0f18-43f6-8148-775235d800b6'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2023), Central Coast, British Columbia, Canada</a></td>
      <td>2025-10-06</td>
      <td>2025-11-18</td>
      <td><a title='e67a81ba-0ac5-49bd-a1fe-02b98f79d8a7' href='../records/e67a81ba-0ac5-49bd-a1fe-02b98f79d8a7'>2</a></td>
    </tr>
    <tr>
      <th>221</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_39a83551-ab8e-45be-a564-cece4b229371'>Zooplankton taxonomic abundance and biomass along the BC Coast</a></td>
      <td>2025-08-12</td>
      <td>2026-06-17</td>
      <td><a title='139df6dd-772b-424f-b830-30a5ba6abfc6' href='../records/139df6dd-772b-424f-b830-30a5ba6abfc6'>1</a></td>
    </tr>
    <tr>
      <th>222</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dbb33efe-c207-4d9c-abef-2350595bf47a'>Size-fractionated zooplankton biomass and isotopes along the BC coast</a></td>
      <td>2025-08-12</td>
      <td>2026-02-20</td>
      <td><a title='186d3139-66a1-43f9-9ac7-c5607252146e' href='../records/186d3139-66a1-43f9-9ac7-c5607252146e'>1</a></td>
    </tr>
    <tr>
      <th>220</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d959f8f3-6d20-42fe-94da-be49bcd3aeca'>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2024)</a></td>
      <td>2025-08-08</td>
      <td>2025-08-08</td>
      <td><a title='262f25ca-ca11-4b10-bb6c-9aec117319a9' href='../records/262f25ca-ca11-4b10-bb6c-9aec117319a9'>1</a></td>
    </tr>
    <tr>
      <th>218</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1d142201-cbbe-4c58-b2c2-1feeac112c51'>iTrack Oysters September 2023 Experiment - Environmental and Oyster Health Data</a></td>
      <td>2025-05-16</td>
      <td>2025-05-16</td>
      <td><a title='bd461764-55b0-4c63-935a-5e9d1d5a6fed' href='../records/bd461764-55b0-4c63-935a-5e9d1d5a6fed'>1</a></td>
    </tr>
    <tr>
      <th>219</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_31ac855d-bf15-42d8-b20d-754638202c66'>Sea Stars 2024 Experiment - Environmental Data</a></td>
      <td>2025-05-16</td>
      <td>2026-06-16</td>
      <td><a title='da040f55-984d-490d-b917-a67856de4bac' href='../records/da040f55-984d-490d-b917-a67856de4bac'>1</a></td>
    </tr>
    <tr>
      <th>217</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_47d8bdd4-c815-4e8d-8d75-53a9db4ae46a'>Glaciers in Western North America Mass Loss Geospatial Data (2021-2024)</a></td>
      <td>2025-05-09</td>
      <td>2026-06-15</td>
      <td><a title='d70bcd3d-dc07-479f-856f-ad70d11c51f1' href='../records/d70bcd3d-dc07-479f-856f-ad70d11c51f1'>1</a></td>
    </tr>
    <tr>
      <th>214</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_78818ed7-ec26-4004-afa1-137741ddda1e'>Calliarthron 2023 Experiment - Environmental Data</a></td>
      <td>2025-05-08</td>
      <td>2025-05-08</td>
      <td><a title='e4038a43-060b-474e-b6f2-ea68d0081053' href='../records/e4038a43-060b-474e-b6f2-ea68d0081053'>1</a></td>
    </tr>
    <tr>
      <th>215</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_87341cb3-f906-4fa5-973c-b6742aa0fbb5'>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</a></td>
      <td>2025-05-08</td>
      <td>2025-11-05</td>
      <td><a title='2916abf5-419e-4cd7-8e25-f45f07a21313' href='../records/2916abf5-419e-4cd7-8e25-f45f07a21313'>2</a></td>
    </tr>
    <tr>
      <th>216</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_96e3dd9c-7863-44d5-95cd-a3d0a8653d83'>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td>2025-05-08</td>
      <td>2025-05-08</td>
      <td></td>
    </tr>
    <tr>
      <th>213</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_53730b70-be6f-4e24-8b9d-4a5e2c491121'>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</a></td>
      <td>2025-04-23</td>
      <td>2025-04-23</td>
      <td><a title='83f387d2-f77e-4921-af15-e064d87ad01a' href='../records/83f387d2-f77e-4921-af15-e064d87ad01a'>1</a></td>
    </tr>
    <tr>
      <th>211</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_31e15496-e906-43f4-9120-2446ab6125b2'>Elliot Creek Aerial Photo and LiDAR Survey</a></td>
      <td>2025-04-02</td>
      <td>2025-04-02</td>
      <td></td>
    </tr>
    <tr>
      <th>212</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_98807d0a-ba68-41e3-a2f5-e3248b459904'>Place Glacier Aerial Photo and LiDAR Survey</a></td>
      <td>2025-04-02</td>
      <td>2025-04-02</td>
      <td></td>
    </tr>
    <tr>
      <th>210</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_52d4f546-dfdf-4bf1-b1ad-f6ec6f2663c0'>Bute Inlet Geo-Hazards & Ramsay West - 2024 - Airborne Coastal Observatory</a></td>
      <td>2025-04-01</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>209</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_314a0846-0fe9-4c2e-81e2-d2b24ac98b6e'>Understory kelp biomass data from BC Central Coast</a></td>
      <td>2025-02-14</td>
      <td>2025-03-04</td>
      <td></td>
    </tr>
    <tr>
      <th>208</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_00f42725-0a88-4d4f-87a9-4e359d2abff4'>Knight Inlet Remotely Operated Vehicle Marine Habitat Survey</a></td>
      <td>2025-02-05</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>207</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_35beb32e-8dc9-42ab-9630-2ae23e414026'>Rocky Subtidal Fish and Invertebrate Community Surveys from the Central Coast of BC</a></td>
      <td>2025-01-28</td>
      <td>2026-01-27</td>
      <td><a title='4a949e26-fe94-4f63-a3c6-a62e19301102' href='../records/4a949e26-fe94-4f63-a3c6-a62e19301102'>1</a></td>
    </tr>
    <tr>
      <th>206</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d7ffd737-5725-4a56-9134-a9ad91c2734d'>Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia</a></td>
      <td>2025-01-10</td>
      <td>2026-05-22</td>
      <td><a title='8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e' href='../records/8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e'>1</a></td>
    </tr>
    <tr>
      <th>205</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9fafb4c8-e61f-4372-ac71-c1ddbe57d80c'>Data record does not exist anymore: Geomorphology - Calvert Island</a></td>
      <td>2025-01-03</td>
      <td>2026-06-09</td>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='../records/49967494-a7b6-4128-b336-671971d1e2c6'>2</a></td>
    </tr>
    <tr>
      <th>204</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_af344fb9-4901-470c-a441-41f11ee2ccd7'>iTrack Oysters February 2023 Experiment - Environmental and Oyster Health Data</a></td>
      <td>2024-12-19</td>
      <td>2024-12-19</td>
      <td></td>
    </tr>
    <tr>
      <th>203</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7fd3ec6c-083a-4942-84b4-215e69492072'>Phytoplankton Pigment Timeseries from High-Performance Liquid Chromatography for the Northern Salish Sea and Central Coast, BC, Canada (Research)</a></td>
      <td>2024-12-11</td>
      <td>2026-02-05</td>
      <td><a title='cb0f4710-d78a-4073-959c-95f874f88711' href='../records/cb0f4710-d78a-4073-959c-95f874f88711'>2</a></td>
    </tr>
    <tr>
      <th>202</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5185ac00-8148-4472-adfd-21741d8a10ce'>Sentinels of Change Sea Surface Temperature Time Series Data Along the British Columbia Coast</a></td>
      <td>2024-11-27</td>
      <td>2026-02-05</td>
      <td><a title='0049e274-f23e-448c-b307-14aa3b4e0b4a' href='../records/0049e274-f23e-448c-b307-14aa3b4e0b4a'>1</a></td>
    </tr>
    <tr>
      <th>201</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f762a307-6dfb-41a8-a56c-ecacfb075a0a'>Denali Fault - 2024 - Airborne LiDAR Survey</a></td>
      <td>2024-11-26</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>200</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d4942b86-d362-40a3-9399-c124c4c263bd'>Larval Dungeness crab abundance and size time series along the coast of British Columbia</a></td>
      <td>2024-11-25</td>
      <td>2025-05-12</td>
      <td><a title='357b017c-6add-4bde-95d0-386bdbab92b3' href='../records/357b017c-6add-4bde-95d0-386bdbab92b3'>1</a></td>
    </tr>
    <tr>
      <th>199</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_48acba27-5e01-4b41-9a0e-f3fc8d809a13'>MusselSeg: Semantic Segmentation for Rocky Intertidal Mussel Habitat</a></td>
      <td>2024-11-22</td>
      <td>2025-10-23</td>
      <td></td>
    </tr>
    <tr>
      <th>198</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c513de71-ac9d-43fa-b693-8f865de4b137'>Fraser River Landslide Project - 2022-2024 - Drone Data</a></td>
      <td>2024-11-21</td>
      <td>2026-05-22</td>
      <td><a title='45a45b5d-e45c-453c-9d36-036f69d533ae' href='../records/45a45b5d-e45c-453c-9d36-036f69d533ae'>2</a></td>
    </tr>
    <tr>
      <th>197</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f25b00ba-ad63-42b3-8021-3fb6aa99baff'>Fraser River Landslide Project - Sites of Concern 2024</a></td>
      <td>2024-11-18</td>
      <td>2026-06-17</td>
      <td></td>
    </tr>
    <tr>
      <th>196</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6e947d50-8392-42ce-bff9-24b126c7cab7'>Spatial extent of eelgrass (Zostera marina) beds from monitoring sites within the greater park ecosystem of Pacific Rim National Park Reserve (2017, 2018)</a></td>
      <td>2024-11-06</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>195</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6756b221-28a0-4848-9761-905cbd558cd7'>Protistan plankton time series from the northern Salish Sea and Central Coast, British Columbia, Canada</a></td>
      <td>2024-10-10</td>
      <td>2026-06-17</td>
      <td></td>
    </tr>
    <tr>
      <th>190</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0507a738-cd65-4ba4-943e-42b9d022b637'>Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory</a></td>
      <td>2024-10-09</td>
      <td>2025-04-23</td>
      <td></td>
    </tr>
    <tr>
      <th>191</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_189dd319-d5ef-4f2a-a060-df8d47628b86'>Elliot Creek Landslide LiDAR Mapping - 2023 - Airborne Coastal Observatory</a></td>
      <td>2024-10-09</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>192</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_33a367c1-2706-4301-af99-4455fbe189a0'>Cryosphere Snow Surveys Southwest British Columbia - Airborne Coastal Observatory</a></td>
      <td>2024-10-09</td>
      <td>2026-05-22</td>
      <td><a title='6a28454e-107a-4059-9b7d-e43bf8ee693b' href='../records/6a28454e-107a-4059-9b7d-e43bf8ee693b'>3</a></td>
    </tr>
    <tr>
      <th>193</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3efdccb0-08ef-4e90-ac91-72969f94a99a'>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</a></td>
      <td>2024-10-09</td>
      <td>2026-06-15</td>
      <td><a title='f1aee211-bfab-46fd-b650-c5cacb782f40' href='../records/f1aee211-bfab-46fd-b650-c5cacb782f40'>2</a></td>
    </tr>
    <tr>
      <th>194</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_43422dc8-2573-4f60-bf87-df447d57ab7a'>USGS Glacier Mapping - 2023 - Hakai Airborne Coastal Observatory</a></td>
      <td>2024-10-09</td>
      <td>2026-03-26</td>
      <td><a title='78efda1b-9688-4bcf-b16e-7167c17c0bcb' href='../records/78efda1b-9688-4bcf-b16e-7167c17c0bcb'>1</a></td>
    </tr>
    <tr>
      <th>189</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_355467ad-104d-40a6-b06e-52a67bfe247e'>Water column CO2 system measurements from January 2016 to December 2023 from Hakai Institute oceanographic station QU39 in northern Strait of Georgia, British Columbia, Canada</a></td>
      <td>2024-10-08</td>
      <td>2024-10-09</td>
      <td></td>
    </tr>
    <tr>
      <th>188</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_52797e17-c0ed-46a4-9dcd-e34f801c6205'>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</a></td>
      <td>2024-09-03</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>187</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_67e89414-a93f-496d-9766-9311f0d3954e'>Motile Invertebrate Surveys - BC Central Coast</a></td>
      <td>2024-08-30</td>
      <td>2026-03-25</td>
      <td></td>
    </tr>
    <tr>
      <th>186</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f67c0c58-3225-4dac-9264-1e76f07c9374'>Data for the paper "Phylogenomic position of eupelagonemids, abundant, and diverse deep-ocean heterotrophs"</a></td>
      <td>2024-08-02</td>
      <td>2024-08-02</td>
      <td></td>
    </tr>
    <tr>
      <th>185</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6652a7a9-d27f-4cbe-ac04-435c238e991d'>Water Level Time Series, Choke Pass, Central Coast, BC, Canada (Provisional)</a></td>
      <td>2024-07-18</td>
      <td>2026-02-20</td>
      <td><a title='7607322d-6dea-4758-a257-de8353c899c1' href='../records/7607322d-6dea-4758-a257-de8353c899c1'>2</a></td>
    </tr>
    <tr>
      <th>184</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6143028b-028d-46c7-a67d-f3a513435e63'>Water Property Measurements from Conductivity-Temperature-Depth Profiles, BC, Canada (Provisional)</a></td>
      <td>2024-07-17</td>
      <td>2026-04-14</td>
      <td><a title='13dc3c6c-9dd4-47a4-92ad-681c653d3565' href='../records/13dc3c6c-9dd4-47a4-92ad-681c653d3565'>1</a></td>
    </tr>
    <tr>
      <th>182</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1755dc37-8d33-4158-8041-c22536fd5771'>Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, BC, Canada (Provisional)</a></td>
      <td>2024-07-12</td>
      <td>2026-05-08</td>
      <td><a title='bf7c05e8-510d-4449-9e81-4c358ff3f440' href='../records/bf7c05e8-510d-4449-9e81-4c358ff3f440'>1</a></td>
    </tr>
    <tr>
      <th>183</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d55021c3-a142-4e14-8208-36c9826c1893'>Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, BC, Canada (Research)</a></td>
      <td>2024-07-12</td>
      <td>2026-05-08</td>
      <td></td>
    </tr>
    <tr>
      <th>181</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_59b33373-ae4a-4719-a3df-0e36a08187d8'>Seagrass Site-Level Production on BC Central Coast</a></td>
      <td>2024-03-22</td>
      <td>2024-12-30</td>
      <td><a title='9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' href='../records/9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f'>1</a></td>
    </tr>
    <tr>
      <th>180</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b8483c9e-81e6-4e1a-b09f-2d66f8fee9a2'>Spatial extent of surface canopy kelp (Nereocystis luetkeana) derived from fixed-wing surveys (2023), Denman Island to south Quadra Island, British Columbia, Canada</a></td>
      <td>2024-03-15</td>
      <td>2024-07-17</td>
      <td><a title='abb0b617-3a3e-43ec-b62e-e2918bfc10aa' href='../records/abb0b617-3a3e-43ec-b62e-e2918bfc10aa'>1</a></td>
    </tr>
    <tr>
      <th>178</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2d693456-7e65-46be-95d7-6bb697320017'>Water Level and Weather Station Time Series, Pruth Bay, Kwakshua Channel, Central Coast, BC, Canada (Provisional)</a></td>
      <td>2024-03-14</td>
      <td>2026-04-15</td>
      <td></td>
    </tr>
    <tr>
      <th>179</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c24f23f0-8d16-4bfd-835a-5475f1ecd8e8'>Extent of Canopy-Forming Kelps, Derived from World View-2, Central Coast, Central Coast, British Columbia</a></td>
      <td>2024-03-14</td>
      <td>2024-07-24</td>
      <td><a title='b0e815da-1b17-404d-8bf6-0bdb4a22d170' href='../records/b0e815da-1b17-404d-8bf6-0bdb4a22d170'>1</a></td>
    </tr>
    <tr>
      <th>177</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6f6560e7-7497-4685-9df2-51c66080b7c9'>Genetic Stock Identification of Juvenile Sockeye Salmon Captured in the Discovery Islands and Johnstone Strait BC, Canada</a></td>
      <td>2024-01-18</td>
      <td>2024-06-27</td>
      <td></td>
    </tr>
    <tr>
      <th>176</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3e90a567-cdd7-41f3-8157-0e7be76eefb8'>Nuchatlaht Survey - Hakai Airborne Coastal Observatory Imagery and Topography Data - Nootka Island British Columbia - 2023</a></td>
      <td>2024-01-08</td>
      <td>2024-07-23</td>
      <td></td>
    </tr>
    <tr>
      <th>175</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6c449900-c726-4e9a-b241-707711e253a7'>Hakai Institute Juvenile Salmon Program Time Series</a></td>
      <td>2023-11-03</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>174</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c074bff6-408b-443a-bdaf-4713f0eadb95'>Mapping Canopy-Forming Kelps in the Northeast Pacific: A Guidebook for Decision-Makers and Practitioners</a></td>
      <td>2023-09-29</td>
      <td>2024-07-23</td>
      <td></td>
    </tr>
    <tr>
      <th>173</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b63374a9-2288-4512-9820-5d1b44d2b502'>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</a></td>
      <td>2023-09-19</td>
      <td>2024-07-23</td>
      <td><a title='e40c42ef-cabf-4969-aeb3-263407a91a68' href='../records/e40c42ef-cabf-4969-aeb3-263407a91a68'>1</a></td>
    </tr>
    <tr>
      <th>172</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_86343dd1-28d0-4d02-8eaf-402d51a7fef7'>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program, Provisional</a></td>
      <td>2023-08-29</td>
      <td>2026-06-01</td>
      <td></td>
    </tr>
    <tr>
      <th>171</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_16ae186b-9d99-42cf-b18d-09f9bb0501d7'>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</a></td>
      <td>2023-08-08</td>
      <td>2026-05-27</td>
      <td><a title='b1c4c93b-6324-4b84-b341-76be046cbf28' href='../records/b1c4c93b-6324-4b84-b341-76be046cbf28'>1</a></td>
    </tr>
    <tr>
      <th>170</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_60f653ae-a3fd-484d-807c-3d7e4a0712cb'>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</a></td>
      <td>2023-04-24</td>
      <td>2025-04-21</td>
      <td><a title='5c2aac2c-0dd8-49d8-87b2-5c52b3d42946' href='../records/5c2aac2c-0dd8-49d8-87b2-5c52b3d42946'>1</a></td>
    </tr>
    <tr>
      <th>168</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_24f1c230-6c37-470c-907d-25b9b022f5c2'>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</a></td>
      <td>2023-03-13</td>
      <td>2026-06-03</td>
      <td><a title='2709d7b1-22e1-4268-bcda-dc0c79f2878e' href='../records/2709d7b1-22e1-4268-bcda-dc0c79f2878e'>1</a></td>
    </tr>
    <tr>
      <th>169</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_476204a7-0714-4755-953d-61fa3c5df497'>Hakai Institute Nutrients (Dosser et al., 2021)</a></td>
      <td>2023-03-13</td>
      <td>2026-06-05</td>
      <td></td>
    </tr>
    <tr>
      <th>166</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_12f951d4-4155-4c05-969d-a7158412f579'>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</a></td>
      <td>2023-03-03</td>
      <td>2025-04-23</td>
      <td><a title='79ace68f-f5a9-4224-8615-20fa255cb6d4' href='../records/79ace68f-f5a9-4224-8615-20fa255cb6d4'>2</a></td>
    </tr>
    <tr>
      <th>167</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_251aef08-4017-4493-b9d8-c4583913b511'>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</a></td>
      <td>2023-03-03</td>
      <td>2024-07-23</td>
      <td><a title='3a8b11a2-5deb-469e-824b-32ab0eb5c2ca' href='../records/3a8b11a2-5deb-469e-824b-32ab0eb5c2ca'>2</a></td>
    </tr>
    <tr>
      <th>165</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4a09d56b-b120-46c8-9263-ae3c42a02e9b'>High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA</a></td>
      <td>2023-01-24</td>
      <td>2026-06-17</td>
      <td></td>
    </tr>
    <tr>
      <th>163</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_160803d3-8019-4a73-9191-5f75f0ec21be'>Mount Robson BC Parks Survey - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td>2023-01-23</td>
      <td>2024-07-23</td>
      <td><a title='550e7acb-0e3f-461f-bd47-8b6ced16bf43' href='../records/550e7acb-0e3f-461f-bd47-8b6ced16bf43'>2</a></td>
    </tr>
    <tr>
      <th>164</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e2baa28d-c063-4354-ae1f-2abdb8397d8f'>Gordon River Archaeology - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td>2023-01-23</td>
      <td>2024-07-23</td>
      <td><a title='a4e3915d-207e-493d-97ff-c1e6ad6f0ce7' href='../records/a4e3915d-207e-493d-97ff-c1e6ad6f0ce7'>2</a></td>
    </tr>
    <tr>
      <th>158</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0295e3a3-11b5-494d-ac60-ed4b95a15fad'>Fraser River - BCSRIF Landslide Mapping – 2022 – Hakai Airborne Coastal Observatory</a></td>
      <td>2023-01-18</td>
      <td>2024-11-28</td>
      <td></td>
    </tr>
    <tr>
      <th>159</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_412ae9da-7e81-4a33-90c8-ed142f36307e'>Ecstall Slide - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td>2023-01-18</td>
      <td>2026-06-08</td>
      <td></td>
    </tr>
    <tr>
      <th>160</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_532c06ad-0b55-4e86-9088-cec970a0a8e1'>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td>2023-01-18</td>
      <td>2024-12-05</td>
      <td><a title='ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' href='../records/ee2eec87-7a78-4a7f-87b7-54347a6c3b2f'>3</a></td>
    </tr>
    <tr>
      <th>161</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c39138f-8f01-4948-a3de-864044686c55'>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</a></td>
      <td>2023-01-18</td>
      <td>2024-07-23</td>
      <td><a title='f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff' href='../records/f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff'>3</a></td>
    </tr>
    <tr>
      <th>162</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bdb9229b-f594-40df-994e-e52e8a678165'>Broken Group Imagery and LiDAR - 2018 - Airborne Coastal Observatory</a></td>
      <td>2023-01-18</td>
      <td>2024-07-23</td>
      <td><a title='eb02906a-9645-4486-ba14-46d71c581352' href='../records/eb02906a-9645-4486-ba14-46d71c581352'>2</a></td>
    </tr>
    <tr>
      <th>156</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6dc431f0-3ca4-4c48-992c-df82d6f8521c'>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</a></td>
      <td>2023-01-17</td>
      <td>2024-07-23</td>
      <td><a title='b276330c-4ee9-476a-979a-cebe52d51db6' href='../records/b276330c-4ee9-476a-979a-cebe52d51db6'>3</a></td>
    </tr>
    <tr>
      <th>157</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8d36f54-4955-463c-94e5-f0030c3230f3'>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</a></td>
      <td>2023-01-17</td>
      <td>2026-06-11</td>
      <td><a title='50037e63-bfac-4b7a-8547-56337fe40026' href='../records/50037e63-bfac-4b7a-8547-56337fe40026'>1</a></td>
    </tr>
    <tr>
      <th>155</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d049351d-b806-461f-85fb-451f100fd7d6'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)</a></td>
      <td>2022-12-01</td>
      <td>2026-06-03</td>
      <td><a title='78b2edef-dab3-47a9-93bb-af63dfcd178d' href='../records/78b2edef-dab3-47a9-93bb-af63dfcd178d'>3</a></td>
    </tr>
    <tr>
      <th>153</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0fbdb22e-d039-46a8-95e3-0bbf4f55d972'>Glacier and Ice Field Mapping - 2021 - Airborne Coastal Observatory</a></td>
      <td>2022-11-25</td>
      <td>2025-05-06</td>
      <td></td>
    </tr>
    <tr>
      <th>154</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e2c7a84f-a33b-4713-9b7f-a9ed57efc5c3'>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</a></td>
      <td>2022-11-25</td>
      <td>2024-12-05</td>
      <td><a title='bdc6c492-dbb1-4d6e-90b8-d7bddf2c6356' href='../records/bdc6c492-dbb1-4d6e-90b8-d7bddf2c6356'>2</a></td>
    </tr>
    <tr>
      <th>151</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8e99157a-8daf-4e68-92ae-9d22cfd46ce7'>Elliot Creek – Homathko Estuary Mapping - 2021 - Airborne Coastal Observatory</a></td>
      <td>2022-11-24</td>
      <td>2024-07-23</td>
      <td><a title='36e9e6ae-a407-456e-8fe2-a3a78b246bf7' href='../records/36e9e6ae-a407-456e-8fe2-a3a78b246bf7'>2</a></td>
    </tr>
    <tr>
      <th>152</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f952a904-f9f7-4876-b518-c98b1fd96f7e'>Snow Mapping Coastal British Columbia - 2021 - Airborne Coastal Observatory</a></td>
      <td>2022-11-24</td>
      <td>2024-07-23</td>
      <td><a title='2168fd41-96d4-4b72-b5ec-0a5c342aad2a' href='../records/2168fd41-96d4-4b72-b5ec-0a5c342aad2a'>2</a></td>
    </tr>
    <tr>
      <th>147</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_93a9bb9a-b54e-4623-9e0e-93d8b7d0020b'>Surfgrass Community Structure - Length & Density - BC Central Coast</a></td>
      <td>2022-10-08</td>
      <td>2026-06-11</td>
      <td></td>
    </tr>
    <tr>
      <th>149</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c89e35df-8a16-4efc-ae29-15f4e3da8a55'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</a></td>
      <td>2022-10-08</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>148</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cec3dcef-8dba-4d91-aee6-b60ce416497c'>Mussel Dynamics - Point Intercepts - BC Central Coast</a></td>
      <td>2022-10-08</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>150</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d683512f-5e47-4b1d-baac-c653fb761806'>Mussel Dynamics - Length & Bed Depth - BC Central Coast</a></td>
      <td>2022-10-08</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>146</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c1b9801b-742b-41b6-a69b-5e7ae6f09bce'>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</a></td>
      <td>2022-09-01</td>
      <td>2024-07-23</td>
      <td><a title='d3c4dde5-38b2-480d-a4e7-228bde9eb537' href='../records/d3c4dde5-38b2-480d-a4e7-228bde9eb537'>2</a></td>
    </tr>
    <tr>
      <th>145</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_71447a55-3eca-41b1-87ff-b8ef69314c4d'>100 Islands Research Program Terrestrial Vegetation Data - BC Central Coast - 2015, 2016, 2017</a></td>
      <td>2022-08-31</td>
      <td>2024-12-04</td>
      <td></td>
    </tr>
    <tr>
      <th>144</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_44dbd3c8-93bf-4e2f-9532-cbaebcf4a2be'>Adjusted Koeye River stage and temperature from 2013 to 2021</a></td>
      <td>2022-07-08</td>
      <td>2026-05-14</td>
      <td></td>
    </tr>
    <tr>
      <th>143</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5eda02a9-36b6-4875-91c9-989e9e06c5ad'>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</a></td>
      <td>2022-05-05</td>
      <td>2026-05-14</td>
      <td><a title='b47e53cd-74dd-4580-80d0-260860064f4b' href='../records/b47e53cd-74dd-4580-80d0-260860064f4b'>1</a></td>
    </tr>
    <tr>
      <th>142</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_41770c7d-27ea-4593-ba55-040bdc5b99f0'>Oceanographic Mooring Time Series, Rivers Inlet, BC, Canada (Research)</a></td>
      <td>2022-04-11</td>
      <td>2026-05-08</td>
      <td><a title='4a9b4584-a5ef-4baf-9d4a-bacf8e6a5d1d' href='../records/4a9b4584-a5ef-4baf-9d4a-bacf8e6a5d1d'>1</a></td>
    </tr>
    <tr>
      <th>140</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c981d76-5fea-44af-904f-58b159838b0a'>Stream Event Sampling - Calvert Island</a></td>
      <td>2022-03-30</td>
      <td>2026-06-09</td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='../records/def2a409-2319-4e8c-a584-9a467f044ada'>1</a></td>
    </tr>
    <tr>
      <th>141</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_de9b2a6d-9ba0-4384-9adf-22abc0eb061f'>Stream Event Sampling - Calvert Island - 2015-2018</a></td>
      <td>2022-03-30</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>120</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0e446321-34f3-4d5a-8c7d-79c89eb76373'>Stream temperature time-series – Calvert Island – 2013 - 2019</a></td>
      <td>2022-03-29</td>
      <td>2026-06-08</td>
      <td></td>
    </tr>
    <tr>
      <th>119</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0e4f324c-6498-4c89-9e19-f2f9f474a1df'>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</a></td>
      <td>2022-03-29</td>
      <td>2026-06-15</td>
      <td><a title='e1b86825-d43b-47e1-bf45-ab791f44772d' href='../records/e1b86825-d43b-47e1-bf45-ab791f44772d'>1</a></td>
    </tr>
    <tr>
      <th>121</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_184b2f81-d87f-4615-a026-15b87930d15c'>Aquatic carbon flux data package for Oliver et al. 2017</a></td>
      <td>2022-03-29</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>122</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_23bc8c35-2e4e-4382-9296-a52d5ea49889'>Discharge Time Series (2013-2017) – Calvert Island</a></td>
      <td>2022-03-29</td>
      <td>2026-06-03</td>
      <td><a title='38fabad7-d7d2-405f-aa4c-592ef064895f' href='../records/38fabad7-d7d2-405f-aa4c-592ef064895f'>1</a></td>
    </tr>
    <tr>
      <th>124</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_25674e9b-1d49-4270-b917-cfe6cdc30f95'>Watersheds of the northern Pacific coastal temperate rainforest margin</a></td>
      <td>2022-03-29</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>123</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_26443ab2-964f-4031-a53b-f132434573e8'>Ecosystem Comparison Plots - Calvert Island</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='d8754c99-a540-4085-8c66-d9447da5f6e9' href='../records/d8754c99-a540-4085-8c66-d9447da5f6e9'>2</a></td>
    </tr>
    <tr>
      <th>125</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_395aa495-de81-4947-b1c5-2c98172a6def'>High-resolution hydrometeorological data from seven small coastal watersheds, British Columbia, Canada, 2013-2019</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='2b33a5f0-1172-41e4-8330-b4c77d1665c7' href='../records/2b33a5f0-1172-41e4-8330-b4c77d1665c7'>1</a></td>
    </tr>
    <tr>
      <th>126</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4c80a391-e74a-48cf-87ae-67632e485725'>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='a7a3cb32-66ff-4dcb-b05a-2c71511bd115' href='../records/a7a3cb32-66ff-4dcb-b05a-2c71511bd115'>3</a></td>
    </tr>
    <tr>
      <th>127</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5b0b2db4-21d7-48b8-9616-255ba2267868'>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019</a></td>
      <td>2022-03-29</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>128</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6844547c-708e-437b-aef7-157b4d9d9bcb'>Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada</a></td>
      <td>2022-03-29</td>
      <td>2026-06-09</td>
      <td><a title='3c4cc294-1e9a-410e-81b0-0d9461e4b1c9' href='../records/3c4cc294-1e9a-410e-81b0-0d9461e4b1c9'>1</a></td>
    </tr>
    <tr>
      <th>130</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_74f47ab6-a1ca-4aef-9115-cf2baaf87bef'>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada</a></td>
      <td>2022-03-29</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>129</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_765d00bb-beec-486c-bd00-e27f972b7324'>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</a></td>
      <td>2022-03-29</td>
      <td>2026-06-04</td>
      <td></td>
    </tr>
    <tr>
      <th>131</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9201118a-b0c4-470f-a76f-396bacc5e93e'>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</a></td>
      <td>2022-03-29</td>
      <td>2024-07-23</td>
      <td><a title='55e7c337-02e8-4200-8ea9-88241d978f96' href='../records/55e7c337-02e8-4200-8ea9-88241d978f96'>3</a></td>
    </tr>
    <tr>
      <th>132</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_97684a5c-9b70-4d8c-854b-9de895d3d71e'>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019</a></td>
      <td>2022-03-29</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>133</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9e61819e-8385-41d2-a5c5-0e2f37c522ef'>LiDAR-based Ecosystem Classification for Calvert Island</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='18911dee-9ca0-408b-8999-28da3e3dde7a' href='../records/18911dee-9ca0-408b-8999-28da3e3dde7a'>2</a></td>
    </tr>
    <tr>
      <th>134</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a242acd4-e3c7-46e0-8f43-f428fb824018'>Stage-Discharge Time Series - Calvert Island - Archived</a></td>
      <td>2022-03-29</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>135</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b52d5602-f81d-4565-9574-e448e99bc997'>Bathymetry for Six Lakes on Calvert and Hecate Islands - 2016 - British Columbia - Canada</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='f0cae885-2124-41c1-8523-2c6725c40dd6' href='../records/f0cae885-2124-41c1-8523-2c6725c40dd6'>1</a></td>
    </tr>
    <tr>
      <th>136</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b694a5c5-6a7e-4206-96aa-5b7754323345'>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019</a></td>
      <td>2022-03-29</td>
      <td>2026-06-05</td>
      <td></td>
    </tr>
    <tr>
      <th>137</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cb13f042-bf47-4874-86e6-4728aa9380d4'>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019)</a></td>
      <td>2022-03-29</td>
      <td>2026-06-15</td>
      <td><a title='39f8b771-eb65-420f-b64e-742d94bbebf0' href='../records/39f8b771-eb65-420f-b64e-742d94bbebf0'>1</a></td>
    </tr>
    <tr>
      <th>138</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d05df775-4295-4b9f-b3b3-29fe891d9ed9'>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='b36a7c12-cb56-46b7-8241-9b52ac30c766' href='../records/b36a7c12-cb56-46b7-8241-9b52ac30c766'>3</a></td>
    </tr>
    <tr>
      <th>139</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d94882f8-c069-454d-a0ea-96c2b17d789d'>LiDAR Derived Watersheds with Metrics - Calvert Island</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='79e98468-af9a-4b52-aa9c-71129fa9cb03' href='../records/79e98468-af9a-4b52-aa9c-71129fa9cb03'>2</a></td>
    </tr>
    <tr>
      <th>115</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5033d8e4-7b58-45b5-86e6-e98e14d1d6b9'>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019</a></td>
      <td>2022-03-25</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>117</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ed3c5cb4-e6b0-4c8a-808e-3583a9a6cfde'>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019</a></td>
      <td>2022-03-25</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>116</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ef59cc12-5031-4c65-b379-7ca03ad76d34'>Precipitation time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</a></td>
      <td>2022-03-25</td>
      <td>2024-07-24</td>
      <td></td>
    </tr>
    <tr>
      <th>118</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ff68a559-3de8-4ad0-9367-79697d7cc897'>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</a></td>
      <td>2022-03-25</td>
      <td>2026-06-05</td>
      <td><a title='3a6e9472-1a85-48e5-8ac6-792945e03045' href='../records/3a6e9472-1a85-48e5-8ac6-792945e03045'>1</a></td>
    </tr>
    <tr>
      <th>109</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_06ddfa63-2611-46a5-8d63-c1b576e85bcb'>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-03-15</td>
      <td>2026-06-11</td>
      <td></td>
    </tr>
    <tr>
      <th>110</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_40d86401-0e95-4ff3-b1c7-25e4e9138157'>Bamfield Region UAV Imagery and Surface Model Data</a></td>
      <td>2022-03-15</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>111</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_582909b1-c87d-4c5a-8594-5f44726f43a4'>Hakai RPAS (Drone) Operations and Methods</a></td>
      <td>2022-03-15</td>
      <td>2026-05-25</td>
      <td></td>
    </tr>
    <tr>
      <th>112</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8010e86f-5dd9-421d-8e22-668664191205'>UAV Imagery - Coastal British Columbia - 2015</a></td>
      <td>2022-03-15</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>113</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9efdd14d-9fb9-4f0e-9414-d890b4e18055'>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</a></td>
      <td>2022-03-15</td>
      <td>2026-06-11</td>
      <td><a title='21ee0a17-9de0-49d7-9b04-cb9d5f557e9f' href='../records/21ee0a17-9de0-49d7-9b04-cb9d5f557e9f'>1</a></td>
    </tr>
    <tr>
      <th>114</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c688f31b-f82c-48f1-a707-5025c37a9b5c'>UAV Imagery - 2016 - Coastal British Columbia - Canada</a></td>
      <td>2022-03-15</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>98</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0c8692f0-a103-4681-9247-9bb69c6e222e'>Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='ee09830d-dd5e-41eb-8aee-0fe9cef5fe79' href='../records/ee09830d-dd5e-41eb-8aee-0fe9cef5fe79'>2</a></td>
    </tr>
    <tr>
      <th>99</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_14bf37c7-5eb6-4194-a992-c039fd7fb38b'>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='69268e35-08ac-4e6d-b489-4bb72ac117b1' href='../records/69268e35-08ac-4e6d-b489-4bb72ac117b1'>3</a></td>
    </tr>
    <tr>
      <th>100</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4034f474-4d52-4a9e-9650-f3c6bd5011e0'>Kelp Canopy Extent 2006 - NW Calvert Island</a></td>
      <td>2022-03-11</td>
      <td>2026-05-25</td>
      <td></td>
    </tr>
    <tr>
      <th>102</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4fac74c8-f58c-46b0-87dc-ab70ce756880'>Discovery Islands LiDAR Dataset&nbsp;&nbsp;- 2014 - British Columbia - Canada</a></td>
      <td>2022-03-11</td>
      <td>2026-05-19</td>
      <td><a title='57770468-42a9-4654-bf7d-7672939ed002' href='../records/57770468-42a9-4654-bf7d-7672939ed002'>1</a></td>
    </tr>
    <tr>
      <th>101</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_51171738-7556-48f1-8757-658d99fa25dd'>Eelgrass Extent 2014 - Central Coast</a></td>
      <td>2022-03-11</td>
      <td>2026-06-09</td>
      <td><a title='017ab2c4-70ea-484a-ae6c-7d441d2ba19d' href='../records/017ab2c4-70ea-484a-ae6c-7d441d2ba19d'>1</a></td>
    </tr>
    <tr>
      <th>103</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7de69ca8-b3f3-4761-b441-dfc9e63b1fbc'>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='70f29525-f17b-4bc7-ae7f-d1e7205ba16c' href='../records/70f29525-f17b-4bc7-ae7f-d1e7205ba16c'>3</a></td>
    </tr>
    <tr>
      <th>104</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7e0f0bbc-507a-4ca0-bafc-1cc3e56db028'>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</a></td>
      <td>2022-03-11</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>105</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_abb8e676-dfcf-4eb5-bc39-4e7887fad163'>Geomorphology - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-03-11</td>
      <td>2026-06-17</td>
      <td></td>
    </tr>
    <tr>
      <th>106</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bef293d6-8721-4214-b8f5-03b5ffb28e1c'>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='f9ff815c-c57a-4750-8f80-25f5e145c8c0' href='../records/f9ff815c-c57a-4750-8f80-25f5e145c8c0'>3</a></td>
    </tr>
    <tr>
      <th>108</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e66d7bf7-6ba1-44ed-8ee5-2561fca92164'>Kelp Canopy Extent - 2014 - NW Calvert Island</a></td>
      <td>2022-03-11</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>107</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ea4e84d5-c89c-4611-9594-449e468bd76c'>Trails - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='e1baeb3c-b764-434c-b0eb-7cb43fe5ef7a' href='../records/e1baeb3c-b764-434c-b0eb-7cb43fe5ef7a'>2</a></td>
    </tr>
    <tr>
      <th>97</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_82a543b1-686c-45c9-a03d-4f93e0ab8e8a'>Big Bar Slide - 2020 - Airborne Coastal Observatory Data</a></td>
      <td>2022-03-08</td>
      <td>2026-06-10</td>
      <td></td>
    </tr>
    <tr>
      <th>89</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1b517e6f-4f0a-4577-b7c2-c37f95d5b413'>Field Station Structures - Calvert Island</a></td>
      <td>2022-03-03</td>
      <td>2026-06-03</td>
      <td><a title='7ed2118f-ecaa-41e4-aa81-911ffa47bf34' href='../records/7ed2118f-ecaa-41e4-aa81-911ffa47bf34'>2</a></td>
    </tr>
    <tr>
      <th>90</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4be1cc5e-8846-4fba-bd94-16ca933faab8'>Hyperspectral Imagery - Calvert Island - 2012</a></td>
      <td>2022-03-03</td>
      <td>2026-05-25</td>
      <td></td>
    </tr>
    <tr>
      <th>91</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7381aff7-a4fe-4309-81f1-8eebe183b4d8'>Summer sea wrack spatial data; Central Coast, British Columbia, Canada (2015 - 2017)</a></td>
      <td>2022-03-03</td>
      <td>2026-06-09</td>
      <td></td>
    </tr>
    <tr>
      <th>92</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_82a3f5ec-95c5-4aeb-a0c0-bf168c985676'>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</a></td>
      <td>2022-03-03</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>93</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c5bf06e7-29f9-404a-a454-36a5d67b2e69'>Hakai Topographic Basemap</a></td>
      <td>2022-03-03</td>
      <td>2026-05-25</td>
      <td></td>
    </tr>
    <tr>
      <th>94</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d61f51c3-7614-465f-bf27-c78986ca07c3'>McMullin Group Kelp Extent - Based on UAS Imagery - 2017</a></td>
      <td>2022-03-03</td>
      <td>2026-05-26</td>
      <td><a title='22951dd4-a9f7-4f2a-b11d-d50e184dc223' href='../records/22951dd4-a9f7-4f2a-b11d-d50e184dc223'>1</a></td>
    </tr>
    <tr>
      <th>95</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e2d3d616-9ee2-451f-8584-14801b4c6fd0'>Bathymetric Survey - Northwest Calvert Island</a></td>
      <td>2022-03-03</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>96</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fe20660b-ef3d-4f6b-90f8-5936d9c96cb5'>20m Digital Elevation Model - Calvert Island</a></td>
      <td>2022-03-03</td>
      <td>2026-06-09</td>
      <td></td>
    </tr>
    <tr>
      <th>84</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_27ba6c11-2421-4e85-bc11-1c1083514ed9'>Owikeno Lake Bathymetric Survey</a></td>
      <td>2022-03-02</td>
      <td>2026-06-03</td>
      <td><a title='2fe3bd2a-973e-48db-a599-6d44ca1ef0ad' href='../records/2fe3bd2a-973e-48db-a599-6d44ca1ef0ad'>1</a></td>
    </tr>
    <tr>
      <th>85</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2a92ca16-f5c6-4362-acea-6bb5117b8d65'>Google Earth Engine Kelp Tool - Central Coast Output</a></td>
      <td>2022-03-02</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>86</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5c13b300-e172-4010-a6d8-7586b68a3a96'>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</a></td>
      <td>2022-03-02</td>
      <td>2026-06-03</td>
      <td><a title='c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' href='../records/c8f6fd7c-7c63-440b-b69a-bd0df3abfd26'>2</a></td>
    </tr>
    <tr>
      <th>87</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6ae1b131-d903-44ca-92a9-64cf6487ddc2'>Geology - Calvert Island</a></td>
      <td>2022-03-02</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>88</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94cdfcba-bbd4-4053-8976-75de69460c14'>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</a></td>
      <td>2022-03-02</td>
      <td>2026-06-03</td>
      <td><a title='52048599-9a0c-4d33-861f-26eaedc86bd5' href='../records/52048599-9a0c-4d33-861f-26eaedc86bd5'>2</a></td>
    </tr>
    <tr>
      <th>74</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0ebfdd89-61d6-453c-870a-83167617b26a'>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</a></td>
      <td>2022-03-01</td>
      <td>2026-06-09</td>
      <td></td>
    </tr>
    <tr>
      <th>75</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0f524f76-a88b-4e0a-9c3c-ee83114c3679'>Gitanyow Archaeology, Cranberry Junction - 2020 - Airborne Coastal Observatory</a></td>
      <td>2022-03-01</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>76</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_62de21ed-90fb-422a-9c55-29c513a00f95'>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td>2022-03-01</td>
      <td>2026-06-15</td>
      <td><a title='e3205958-52b4-4c42-a02d-34d713a20a53' href='../records/e3205958-52b4-4c42-a02d-34d713a20a53'>1</a></td>
    </tr>
    <tr>
      <th>77</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_95bee6a0-ae38-4427-b5b2-5cc5835df70d'>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td>2022-03-01</td>
      <td>2026-06-09</td>
      <td><a title='b5ee0615-c04d-462e-8199-f611bc6370ce' href='../records/b5ee0615-c04d-462e-8199-f611bc6370ce'>1</a></td>
    </tr>
    <tr>
      <th>78</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a60a0468-3f56-4f22-abd4-5268fcfb9744'>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td>2022-03-01</td>
      <td>2026-06-09</td>
      <td><a title='727b8863-91cc-4765-b0c0-80cb74b11182' href='../records/727b8863-91cc-4765-b0c0-80cb74b11182'>1</a></td>
    </tr>
    <tr>
      <th>79</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bb59cb9e-887a-40a3-b41a-f4a5b2263ce6'>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</a></td>
      <td>2022-03-01</td>
      <td>2026-06-16</td>
      <td></td>
    </tr>
    <tr>
      <th>80</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c3958106-fc49-44bd-8227-bfc3e8bcb58c'>Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td>2022-03-01</td>
      <td>2026-06-10</td>
      <td></td>
    </tr>
    <tr>
      <th>81</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c3eff62f-bcee-4faa-a7e1-7b9380d94e74'>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</a></td>
      <td>2022-03-01</td>
      <td>2026-06-10</td>
      <td></td>
    </tr>
    <tr>
      <th>82</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d2e83e40-9e95-4a47-a899-b37c744be3ab'>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</a></td>
      <td>2022-03-01</td>
      <td>2026-06-09</td>
      <td></td>
    </tr>
    <tr>
      <th>83</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e0c768fc-5c37-455f-b2a3-604f766f4148'>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</a></td>
      <td>2022-03-01</td>
      <td>2026-06-08</td>
      <td></td>
    </tr>
    <tr>
      <th>71</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_77a256cd-baf7-434e-9f62-53ba809e48cb'>High-resolution record of 8-m seawater CO2 content entering Fanny Bay Oysters in Baynes Sound, British Columbia, Canada from March 2017 to November 2017</a></td>
      <td>2022-02-04</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>72</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_804b5b42-5550-4620-b789-7c2fe9572c03'>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</a></td>
      <td>2022-02-04</td>
      <td>2026-05-19</td>
      <td></td>
    </tr>
    <tr>
      <th>73</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a0263680-f0d5-46d5-85ea-483fa58c74b6'>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017</a></td>
      <td>2022-02-04</td>
      <td>2026-06-12</td>
      <td></td>
    </tr>
    <tr>
      <th>68</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_63765cc6-5730-4a28-9d96-3de38066312f'>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td>2022-02-03</td>
      <td>2026-05-14</td>
      <td></td>
    </tr>
    <tr>
      <th>69</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7c47472a-b16c-446c-89d5-eefa23e07922'>High-resolution record of surface seawater CO2 content from November 2017 to June 2018 collected in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td>2022-02-03</td>
      <td>2024-07-24</td>
      <td><a title='f31f38bf-16bc-4136-8982-a2df5fefb3a0' href='../records/f31f38bf-16bc-4136-8982-a2df5fefb3a0'>1</a></td>
    </tr>
    <tr>
      <th>70</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a72c43e2-5b4d-4d56-89d4-464b4c513710'>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</a></td>
      <td>2022-02-03</td>
      <td>2026-02-20</td>
      <td><a title='45983472-7627-4227-b312-079c2aeda7ef' href='../records/45983472-7627-4227-b312-079c2aeda7ef'>1</a></td>
    </tr>
    <tr>
      <th>65</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4b5c0c20-2115-4986-bf56-237e360240bd'>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</a></td>
      <td>2022-02-02</td>
      <td>2025-01-30</td>
      <td><a title='1a9a5aae-41ee-4272-a52e-6c37abedfbff' href='../records/1a9a5aae-41ee-4272-a52e-6c37abedfbff'>3</a></td>
    </tr>
    <tr>
      <th>66</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a0ca5d26-b457-4726-97d4-ed0c8dd6cd99'>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</a></td>
      <td>2022-02-02</td>
      <td>2026-06-03</td>
      <td><a title='dd30b32a-2099-4909-838d-6ade9804381a' href='../records/dd30b32a-2099-4909-838d-6ade9804381a'>1</a></td>
    </tr>
    <tr>
      <th>67</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fd5ada9a-5719-4ca1-89d2-17adb48d1493'>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018)</a></td>
      <td>2022-02-02</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>62</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_41b0137d-6ac0-407d-a550-dd375475b2b0'>Seafloor Observatory in Hyacinthe Bay, Quadra Island, British Columbia, Canada (Provisional)</a></td>
      <td>2022-02-01</td>
      <td>2026-03-17</td>
      <td><a title='0c864dea-998e-4a5e-94d3-c5fbda339eee' href='../records/0c864dea-998e-4a5e-94d3-c5fbda339eee'>2</a></td>
    </tr>
    <tr>
      <th>63</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_87a845e3-e71a-43cc-a75f-ec6a3b812a0e'>Acoustic Doppler Current Profiler Time Series from Fixed Platform on the British Columbia Central Coast (Provisional)</a></td>
      <td>2022-02-01</td>
      <td>2026-06-10</td>
      <td><a title='9c581481-f2ee-4353-b1ab-c5bf242945fe' href='../records/9c581481-f2ee-4353-b1ab-c5bf242945fe'>2</a></td>
    </tr>
    <tr>
      <th>64</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e09522d7-24f7-4c0e-afac-6cafd22a54f6'>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</a></td>
      <td>2022-02-01</td>
      <td>2026-06-12</td>
      <td></td>
    </tr>
    <tr>
      <th>46</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_17396d02-88ff-4240-837b-5d3a45e70ea0'>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</a></td>
      <td>2022-01-24</td>
      <td>2026-06-12</td>
      <td></td>
    </tr>
    <tr>
      <th>47</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1c9b7bcd-d3cc-4856-9428-df7abb2149f0'>Mobile Invertebrate Rocky Intertidal Surveys - BC Central Coast - 2016-2018</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='f8f299be-a37e-43bf-9416-5ff59e664f65' href='../records/f8f299be-a37e-43bf-9416-5ff59e664f65'>1</a></td>
    </tr>
    <tr>
      <th>48</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2738ef2b-0c74-422d-a140-082e5f7b3793'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a' href='../records/f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a'>1</a></td>
    </tr>
    <tr>
      <th>49</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3d7d93d0-73be-4c1b-af09-307e60a3576d'>Water column carbonate system measurements from the Pacific Salmon Foundation Citizen Science Program stations from July 2016 to October 2017 in the northern Salish Sea, British Columbia, Canada</a></td>
      <td>2022-01-24</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>50</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4624baf9-ec39-4538-83fe-1563511b722c'>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</a></td>
      <td>2022-01-24</td>
      <td>2026-06-12</td>
      <td></td>
    </tr>
    <tr>
      <th>51</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_48c8f830-f281-4ca1-9a81-ea690e70cb7a'>Water column CO2 system measurements from Hakai Oceanographic station QU39 from January 2016 to December 2017 in northern Salish Sea, British Columbia, Canada</a></td>
      <td>2022-01-24</td>
      <td>2024-07-23</td>
      <td></td>
    </tr>
    <tr>
      <th>52</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6c0697e9-7776-4d36-8219-b21ce72fbcc9'>Surface water CO2 parameters collected by Alaskan citizens around the northern Gulf of Alaska from April 2015 to August 2017. Version 1.0.</a></td>
      <td>2022-01-24</td>
      <td>2026-02-20</td>
      <td></td>
    </tr>
    <tr>
      <th>53</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6d779012-e236-4a03-b11a-a5915f0f4342'>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</a></td>
      <td>2022-01-24</td>
      <td>2026-05-14</td>
      <td></td>
    </tr>
    <tr>
      <th>54</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6ebe47c3-6d59-4cb2-a7ba-111698445d8d'>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</a></td>
      <td>2022-01-24</td>
      <td>2026-05-25</td>
      <td></td>
    </tr>
    <tr>
      <th>55</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94ded8f9-4ee7-407d-80eb-bf217ce7d260'>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</a></td>
      <td>2022-01-24</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>56</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b4cac70e-a6fa-4d77-8fdb-1d3612006bc4'>Pacific Northwest Eelgrass Sediment Carbon Data</a></td>
      <td>2022-01-24</td>
      <td>2026-06-05</td>
      <td></td>
    </tr>
    <tr>
      <th>57</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c113d7a8-6a46-46fc-b49c-a4e69afedfbc'>Hakai Institute’s Burke-o-Lator TCO2/pCO2 Analyzer Discrete Sample Analysis Protocols</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td></td>
    </tr>
    <tr>
      <th>58</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d200376b-7dd8-4778-b3f5-379243bf93b8'>High-resolution record of surface water pH at Sentry Shoal in the Northern Strait of Georgia</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='1f798a06-9c01-4025-93c6-b1a9f8ce6832' href='../records/1f798a06-9c01-4025-93c6-b1a9f8ce6832'>1</a></td>
    </tr>
    <tr>
      <th>59</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dc50a22a-44c0-478c-aa19-a46343bc764a'>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2019</a></td>
      <td>2022-01-24</td>
      <td>2024-08-02</td>
      <td></td>
    </tr>
    <tr>
      <th>60</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f00b9c87-190e-4b89-a864-7c012b989e49'>High-resolution record of surface seawater CO2 content from December 2014 to April 2016 collected in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td>2022-01-24</td>
      <td>2026-06-10</td>
      <td></td>
    </tr>
    <tr>
      <th>61</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fcb4dfb6-606b-4b4b-bdcb-90f3f480fc33'>Data on invasion of Calvert Island by Orthione griffenis</a></td>
      <td>2022-01-24</td>
      <td>2026-06-09</td>
      <td></td>
    </tr>
    <tr>
      <th>45</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_154e88e6-2300-4ca0-b3f8-ee822d32a9a4'>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</a></td>
      <td>2022-01-22</td>
      <td>2026-05-11</td>
      <td><a title='a31d44d5-2ce5-4d03-8d0b-4549023840ff' href='../records/a31d44d5-2ce5-4d03-8d0b-4549023840ff'>1</a></td>
    </tr>
    <tr>
      <th>36</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1946cc53-6e11-4428-a2c9-43b34e1dcaa1'>Orthophoto High Compression 0.25m resolution Mosaic - 2012 - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-01-21</td>
      <td>2026-06-10</td>
      <td></td>
    </tr>
    <tr>
      <th>37</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_26a09a27-7f16-4944-b88d-8c3bf2d36f03'>Wind Fetch - BC Central Coast - Canada</a></td>
      <td>2022-01-21</td>
      <td>2024-07-24</td>
      <td><a title='8275a332-8870-4300-8ca8-48b854e7dccf' href='../records/8275a332-8870-4300-8ca8-48b854e7dccf'>2</a></td>
    </tr>
    <tr>
      <th>38</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_33c870b8-3b4c-429d-bc10-99dd4c7f4c7d'>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</a></td>
      <td>2022-01-21</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>39</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3f40326a-23f9-4e30-a16a-f332ace14e2f'>Nereocystis kelp canopy productivity data from BC Central Coast</a></td>
      <td>2022-01-21</td>
      <td>2026-05-19</td>
      <td></td>
    </tr>
    <tr>
      <th>40</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5feb907e-e63e-4172-94ae-831fbe92aee5'>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-01-21</td>
      <td>2024-07-24</td>
      <td><a title='8a7cd5ea-e167-419e-a5c3-919acafe8455' href='../records/8a7cd5ea-e167-419e-a5c3-919acafe8455'>2</a></td>
    </tr>
    <tr>
      <th>41</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7d3f525a-6ba2-494b-893a-147e2a812306'>Macrocystis kelp canopy productivity data from BC Central Coast, v1.3.0</a></td>
      <td>2022-01-21</td>
      <td>2024-07-23</td>
      <td></td>
    </tr>
    <tr>
      <th>42</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_be16603d-e383-4af4-9e93-7a36a086688e'>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-01-21</td>
      <td>2026-06-12</td>
      <td></td>
    </tr>
    <tr>
      <th>43</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d342e016-1e9a-448a-bc1a-af53fe8d5dfd'>Herring Survey Data - 2016 - BC Central Coast</a></td>
      <td>2022-01-21</td>
      <td>2026-06-16</td>
      <td></td>
    </tr>
    <tr>
      <th>44</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f462be7f-ab53-409e-8f8c-9b9fecc5e16e'>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</a></td>
      <td>2022-01-21</td>
      <td>2024-07-24</td>
      <td><a title='c2b05382-684f-4349-a64b-b20521223574' href='../records/c2b05382-684f-4349-a64b-b20521223574'>3</a></td>
    </tr>
    <tr>
      <th>35</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_769311e9-1b1f-41f4-9023-38acf37a6690'>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</a></td>
      <td>2022-01-20</td>
      <td>2026-05-14</td>
      <td><a title='d1d07d48-c909-41b4-8c0f-13238720749c' href='../records/d1d07d48-c909-41b4-8c0f-13238720749c'>1</a></td>
    </tr>
    <tr>
      <th>30</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0a8ff4c9-158a-4a46-9bb0-9d480ff40466'>Hakai Place Names Service - Coastal British Columbia - Canada</a></td>
      <td>2022-01-19</td>
      <td>2026-06-17</td>
      <td></td>
    </tr>
    <tr>
      <th>31</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_15caa6c8-be9b-4f19-81ae-bb82321eafd6'>Mean Tidal Current - Coastal British Columbia - Canada</a></td>
      <td>2022-01-19</td>
      <td>2026-05-27</td>
      <td><a title='646dd927-3248-4fc9-970c-abea15f7d304' href='../records/646dd927-3248-4fc9-970c-abea15f7d304'>2</a></td>
    </tr>
    <tr>
      <th>32</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3dc0d46c-7afe-4379-901d-37a787c1c204'>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</a></td>
      <td>2022-01-19</td>
      <td>2026-06-16</td>
      <td></td>
    </tr>
    <tr>
      <th>33</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8c8ed7d-51fa-45e0-b4eb-d21ddc55526a'>Clam Garden Geospatial Data - Quadra Island - 2016</a></td>
      <td>2022-01-19</td>
      <td>2026-06-01</td>
      <td><a title='693c7ca7-a244-4375-9460-ff7c27187af2' href='../records/693c7ca7-a244-4375-9460-ff7c27187af2'>2</a></td>
    </tr>
    <tr>
      <th>34</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f68be641-0017-4311-b4de-5d0aed9e2b57'>100 Islands Project - Island Spatial Data -2017 - Coastal British Columbia - Canada</a></td>
      <td>2022-01-19</td>
      <td>2026-06-17</td>
      <td></td>
    </tr>
    <tr>
      <th>27</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1347af6c-aedf-4ec6-bd37-ed508df6c40a'>Stage-Discharge Time Series - Calvert Island - Archived</a></td>
      <td>2022-01-17</td>
      <td>2026-06-15</td>
      <td><a title='a0ada4b0-faea-4dcd-b9bf-d7ff212315fb' href='../records/a0ada4b0-faea-4dcd-b9bf-d7ff212315fb'>1</a></td>
    </tr>
    <tr>
      <th>28</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_62336906-31e6-4c32-968c-2312e703e08f'>Underwater Video Transects - Calvert Island - 2016</a></td>
      <td>2022-01-17</td>
      <td>2024-07-24</td>
      <td><a title='d64fd03b-46d4-4662-a123-c11bc42199b6' href='../records/d64fd03b-46d4-4662-a123-c11bc42199b6'>3</a></td>
    </tr>
    <tr>
      <th>29</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94b4992f-19e2-46d4-875e-f0c952ea62f7'>Kelp Field Data for Remote Sensing - BC Central Coast</a></td>
      <td>2022-01-17</td>
      <td>2026-05-22</td>
      <td><a title='cd3ca52d-dc83-4501-9e53-7b00c8ab9090' href='../records/cd3ca52d-dc83-4501-9e53-7b00c8ab9090'>1</a></td>
    </tr>
    <tr>
      <th>23</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_288ea4b2-3706-4256-8146-02bd0265585b'>Nearshore Macrophyte Stable Isotopes - BC Central Coast</a></td>
      <td>2022-01-13</td>
      <td>2026-03-25</td>
      <td></td>
    </tr>
    <tr>
      <th>24</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3bc02dd8-7654-44f0-8c7c-02739937bdf4'>Seastar & Macroinvertebrate Dynamics - BC Central Coast</a></td>
      <td>2022-01-13</td>
      <td>2024-11-29</td>
      <td><a title='98bc62c7-d6a4-42bd-9110-c8021380d8a5' href='../records/98bc62c7-d6a4-42bd-9110-c8021380d8a5'>1</a></td>
    </tr>
    <tr>
      <th>25</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d87de5ca-a18a-406d-a4c1-74e6f8f28e5b'>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</a></td>
      <td>2022-01-13</td>
      <td>2024-08-02</td>
      <td></td>
    </tr>
    <tr>
      <th>26</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ea6c0e20-9b99-48f7-adfb-6c1b70f6bd2a'>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</a></td>
      <td>2022-01-13</td>
      <td>2024-07-23</td>
      <td><a title='35dd16d8-20b1-49d5-8c59-9cdc02475cd0' href='../records/35dd16d8-20b1-49d5-8c59-9cdc02475cd0'>1</a></td>
    </tr>
    <tr>
      <th>22</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_66ad87d2-bb96-4515-a907-6367ca6c0a2b'>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</a></td>
      <td>2021-12-03</td>
      <td>2026-06-12</td>
      <td><a title='3031aa60-689f-4b94-9dc6-9912cc742431' href='../records/3031aa60-689f-4b94-9dc6-9912cc742431'>2</a></td>
    </tr>
    <tr>
      <th>21</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ee2791c3-3d99-41e5-8cdf-fa5d1d19944d'>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</a></td>
      <td>2021-12-02</td>
      <td>2024-07-23</td>
      <td><a title='3fbbd892-55cd-4c96-9669-cecefe726b3f' href='../records/3fbbd892-55cd-4c96-9669-cecefe726b3f'>2</a></td>
    </tr>
    <tr>
      <th>20</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_64f74489-b9a3-4e6f-9f25-be141b8e285c'>Juvenile Sockeye Diets Hakai 2015-2016</a></td>
      <td>2021-11-26</td>
      <td>2026-05-12</td>
      <td></td>
    </tr>
    <tr>
      <th>18</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1769a04e-b77b-409b-8e48-bc2098bbad3e'>Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017</a></td>
      <td>2021-11-19</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>19</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_eb1feb98-b11a-4663-b7ab-2216df8187bd'>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</a></td>
      <td>2021-11-19</td>
      <td>2026-05-11</td>
      <td></td>
    </tr>
    <tr>
      <th>17</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7ddae37a-e706-45d2-8060-8306300a98c8'>Oceanographic Mooring Time Series, Hyacinthe Bay, BC, Canada (Provisional)</a></td>
      <td>2021-10-20</td>
      <td>2026-02-20</td>
      <td><a title='7c2b8668-75a3-4fc8-bff3-bdae5d95f52d' href='../records/7c2b8668-75a3-4fc8-bff3-bdae5d95f52d'>2</a></td>
    </tr>
    <tr>
      <th>16</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8853a375-f067-4760-b5d1-98c1fcf40c6d'>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</a></td>
      <td>2021-10-05</td>
      <td>2026-05-11</td>
      <td></td>
    </tr>
    <tr>
      <th>15</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_89b3c6d8-983b-48f4-a0b5-04eea65602f6'>Juvenile pink and chum salmon diet study – Discovery Islands and Johnstone Strait – May to July 2015 and 2016</a></td>
      <td>2021-09-28</td>
      <td>2026-06-15</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1815be54-9081-4031-80fa-d3d071340a7d'>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</a></td>
      <td>2021-09-23</td>
      <td>2026-05-25</td>
      <td></td>
    </tr>
    <tr>
      <th>7</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_30bb20f4-1d7a-4167-a00f-613d0ff3e2fc'>Hakai Institute Sensor Network</a></td>
      <td>2021-09-23</td>
      <td>2026-05-22</td>
      <td></td>
    </tr>
    <tr>
      <th>8</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3732444b-7a97-4d9c-9f2e-2fc6f9618bae'>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</a></td>
      <td>2021-09-23</td>
      <td>2026-05-25</td>
      <td><a title='f409100d-95e4-4933-a927-fdf8d3b83204' href='../records/f409100d-95e4-4933-a927-fdf8d3b83204'>2</a></td>
    </tr>
    <tr>
      <th>9</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4bf1e341-637c-4884-b373-033e033b3cba'>Northwest Calvert Substrate Mapping</a></td>
      <td>2021-09-23</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>10</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_55daf524-146e-4b06-8c6c-3255c7e3c77a'>Vegetated Islands Polygons - 100 Islands Research</a></td>
      <td>2021-09-23</td>
      <td>2026-05-25</td>
      <td><a title='0c08a4f0-b28c-40fe-aaa8-a03113a7c735' href='../records/0c08a4f0-b28c-40fe-aaa8-a03113a7c735'>1</a></td>
    </tr>
    <tr>
      <th>11</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_82c07005-9313-436c-9239-7be3f5907be2'>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</a></td>
      <td>2021-09-23</td>
      <td>2024-07-24</td>
      <td><a title='dc84cb4c-ba14-4632-a595-eed526bf9db1' href='../records/dc84cb4c-ba14-4632-a595-eed526bf9db1'>2</a></td>
    </tr>
    <tr>
      <th>12</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ab901b46-43f6-4044-b0c3-b5fd825622f4'>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</a></td>
      <td>2021-09-23</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>13</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_af65bf72-27af-4747-8911-ab05591762ac'>Kelp forest communities along an otter gradient</a></td>
      <td>2021-09-23</td>
      <td>2026-06-12</td>
      <td><a title='f5d51d99-ce24-4713-a317-7927dd283f1a' href='../records/f5d51d99-ce24-4713-a317-7927dd283f1a'>2</a></td>
    </tr>
    <tr>
      <th>14</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cf7a6149-b34a-404c-88e1-c556bf361408'>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</a></td>
      <td>2021-09-23</td>
      <td>2026-06-03</td>
      <td><a title='c83b5cbf-cc8c-4676-823c-77e28c0ec9da' href='../records/c83b5cbf-cc8c-4676-823c-77e28c0ec9da'>1</a></td>
    </tr>
    <tr>
      <th>5</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c3c86a9-1201-479d-b2b7-a1615183ffea'>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</a></td>
      <td>2021-09-20</td>
      <td>2024-07-23</td>
      <td><a title='dcde7ad3-f54e-4210-ae4e-33db5aac63fe' href='../records/dcde7ad3-f54e-4210-ae4e-33db5aac63fe'>2</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dd325fc4-033c-4696-b38d-0ac883ad67eb'>Underway Surface Seawater and Marine Boundary Layer Observations from the M/V Columbia (Research)</a></td>
      <td>2021-06-11</td>
      <td>2026-06-03</td>
      <td></td>
    </tr>
    <tr>
      <th>0</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_763f3e59-49fe-420a-91da-a046b4690bea'>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Kwakshua Channel (KC) Buoy, Central Coast, BC, Canada (Provisional)</a></td>
      <td>2021-03-31</td>
      <td>2026-02-20</td>
      <td><a title='c68b9ec8-9f26-4fb0-9333-79730f4ea1ca' href='../records/c68b9ec8-9f26-4fb0-9333-79730f4ea1ca'>2</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8b069feb-57fc-4d57-bf5c-761fd7cf0b45'>Surface Seawater and Marine Boundary Layer CO2 Observations from the Kwakshua Channel (KC) Buoy on the Central Coast of British Columbia (Research)</a></td>
      <td>2021-03-31</td>
      <td>2026-06-08</td>
      <td><a title='3f883dc6-56ac-42f5-a1d4-6de554a9e63d' href='../records/3f883dc6-56ac-42f5-a1d4-6de554a9e63d'>1</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b62c3aaa-c3b8-41cb-b035-4da16209f26a'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Provisional)</a></td>
      <td>2021-03-31</td>
      <td>2026-06-15</td>
      <td><a title='5143957b-ee18-44d3-8000-a9c8f9a34a0d' href='../records/5143957b-ee18-44d3-8000-a9c8f9a34a0d'>2</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fe76ef4c-254a-44fe-87bc-052cd3aa9663'>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Research)</a></td>
      <td>2021-03-31</td>
      <td>2026-06-15</td>
      <td><a title='79433a1f-ec07-4cd5-a31a-8c2c53069085' href='../records/79433a1f-ec07-4cd5-a31a-8c2c53069085'>1</a></td>
    </tr>
    <tr>
      <th>263</th>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_66fbb7f5-3644-471a-95ee-f8d3758e888b'>Mount Robson Aerial Photo and LiDAR Survey</a></td>
      <td></td>
      <td>2025-04-02</td>
      <td></td>
    </tr>
  </tbody>
</table>

## Issues

<table border="1" class="dataframe table table-striped table-hover table-sm" id="issues_table">
  <thead>
    <tr style="text-align: right;">
      <th>metadata_revision</th>
      <th>title</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2026-06-17</td>
      <td>Zooplankton taxonomic abundance and biomass along the BC Coast</td>
      <td>Invalid Resource URL: https://github.com/HakaiInstitute/hakai-zooplankton-microscopy-dataset returned status_code=404</td>
    </tr>
    <tr>
      <td>2026-06-16</td>
      <td>Sea Stars 2024 Experiment - Environmental Data</td>
      <td>Invalid Resource URL: https://github.com/HakaiInstitute/hakai-wetlab-seastars2024 returned status_code=404</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Glaciers in Western North America Mass Loss Geospatial Data (2021-2024)</td>
      <td>Malformed related work identifier (missing doi.org): https://10.1029/2025GL115235</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived</td>
      <td>Metadata mismatch: creator 'Maartje Korver' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related work 'https://drive.google.com/file/d/1mt2v_uv78afjp5z_lhi1gu52bqwko4ms/view?usp=drive_link' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related work 'https://hakai.maps.arcgis.com/home/webmap/viewer.html?webmap=75ee2603aa5a45068c7e3579796c3aab' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Provisional)</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019)</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-15</td>
      <td>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at the Hakai Institute’s Quadra Island Field Station, Hyacinthe Bay, BC, Canada (Research)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-12</td>
      <td>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-12</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-12</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2026-06-12</td>
      <td>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-11</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-11</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-10</td>
      <td>Acoustic Doppler Current Profiler Time Series from Fixed Platform on the British Columbia Central Coast (Provisional)</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-10</td>
      <td>Acoustic Doppler Current Profiler Time Series from Fixed Platform on the British Columbia Central Coast (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-09</td>
      <td>Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada</td>
      <td>Duplicate DOI shared with another record: 10.21966/n0h9-cq15</td>
    </tr>
    <tr>
      <td>2026-06-09</td>
      <td>Stream Event Sampling - Calvert Island</td>
      <td>Invalid Resource URL: https://drive.google.com/open?id=0B3dfJwMwT2k4RzNYOGFUcFNpUms returned status_code=404</td>
    </tr>
    <tr>
      <td>2026-06-09</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-09</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-09</td>
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-09</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-06-09</td>
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2026-06-08</td>
      <td>Sea surface temperature data in False Creek, British Columbia</td>
      <td>Metadata mismatch: related identifier 'https://www.onsetcomp.com/products/data-loggers/mx2203' (IsDocumentedBy) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-06-08</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Observations from the Kwakshua Channel (KC) Buoy on the Central Coast of British Columbia (Research)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Field Station Structures - Calvert Island</td>
      <td>Metadata mismatch: author 'Hakai Geospatial Technology Team' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</td>
      <td>Metadata mismatch: author 'Hakai Geospatial Technology Team' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Owikeno Lake Bathymetric Survey</td>
      <td>Metadata mismatch: creator 'Hakai Geospatial' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>Metadata mismatch: related work '10.1002/eap.1897' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)</td>
      <td>Metadata mismatch: related work '10.25921/9vnv-0g64' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)</td>
      <td>Metadata mismatch: title CKAN='Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)' | DataCite='High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA from 2017-06-01 to 2021-04-27 (NCEI Accession 0247208)'</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Field Station Structures - Calvert Island</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-03</td>
      <td>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 analyzer located at Sitka Harbor, Sitka, Alaska, USA (Research)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-06-01</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>Metadata mismatch: related work 'https://drive.google.com/file/d/16gyd2kqiddmvnb9u9hmy12qlp8muxsbb/view?usp=sharing' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-06-01</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>Metadata mismatch: related work 'https://hakai.org/stories/great-walls-quadra' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-05-27</td>
      <td>Horne Lake Bathymetry Mapping</td>
      <td>Metadata mismatch: license CKAN='CC-BY-NC-4.0' | DataCite='cc-by-4.0'</td>
    </tr>
    <tr>
      <td>2026-05-27</td>
      <td>Horne Lake Bathymetry Mapping</td>
      <td>Metadata mismatch: related identifier 'https://drive.google.com/file/d/1tCkBSbg8viQE8RDHg-0B3K9qfWbKU_Em/view' (HasMetadata) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-05-27</td>
      <td>Horne Lake Bathymetry Mapping</td>
      <td>Metadata mismatch: related work 'https://hecate.hakai.org/auth/access-request.php?ref=10.21966/tqj2-wh77' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-05-27</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-05-27</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2026-05-27</td>
      <td>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2026-05-26</td>
      <td>McMullin Group Kelp Extent - Based on UAS Imagery - 2017</td>
      <td>Invalid Resource URL: https://drive.google.com/open?id=1jukkkqR46AAO14Q80XMWzwojRotSkuYS returned status_code=404</td>
    </tr>
    <tr>
      <td>2026-05-26</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Bute Inlet Ocean Observing Station (BIOOS) Buoy, Bute Inlet, BC, Canada (Provisional)</td>
      <td>Metadata mismatch: related identifier 'https://doi.org/10.21966/adbg-d170' (IsVersionOf) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-05-26</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Bute Inlet Ocean Observing Station (BIOOS) Buoy, Bute Inlet, BC, Canada (Provisional)</td>
      <td>Metadata mismatch: related work '10.21966/4jvz-bv44' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-05-26</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Bute Inlet Ocean Observing Station (BIOOS) Buoy, Bute Inlet, BC, Canada (Provisional)</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-05-26</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Bute Inlet Ocean Observing Station (BIOOS) Buoy, Bute Inlet, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-05-25</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>Invalid Resource URL: https://drive.google.com/open?id=12Spn0fnOC91dLOahgcf94_lrELHvXFX6 returned status_code=404</td>
    </tr>
    <tr>
      <td>2026-05-25</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2026-05-25</td>
      <td>Vegetated Islands Polygons - 100 Islands Research</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2026-05-22</td>
      <td>Fraser River Landslide Project - 2022-2024 - Drone Data</td>
      <td>Malformed related work identifier (missing doi.org): https://10.21966/xp9x-m243</td>
    </tr>
    <tr>
      <td>2026-05-22</td>
      <td>Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-05-22</td>
      <td>Cryosphere Snow Surveys Southwest British Columbia - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related work 'https://drive.google.com/file/d/1blzfowqmictyuet4mnip2d2nnmd2pxjg/view?usp=sharing' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-05-22</td>
      <td>Cryosphere Snow Surveys Southwest British Columbia - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related work 'https://drive.google.com/file/d/1sqnqvcxxcuqjfqasluneu6r311tfiogw/view?usp=sharing' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-05-22</td>
      <td>Cryosphere Snow Surveys Southwest British Columbia - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: version CKAN='2.0' | DataCite='1.0'</td>
    </tr>
    <tr>
      <td>2026-05-22</td>
      <td>Kelp Field Data for Remote Sensing - BC Central Coast</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-05-22</td>
      <td>Fraser River Landslide Project - 2022-2024 - Drone Data</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/qpe8-ay93 status_code=502</td>
    </tr>
    <tr>
      <td>2026-05-19</td>
      <td>Discovery Islands LiDAR Dataset&nbsp;&nbsp;- 2014 - British Columbia - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-05-15</td>
      <td>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-05-14</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>Metadata mismatch: author 'Debora Obrist' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-05-14</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-05-11</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-05-08</td>
      <td>Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, BC, Canada (Provisional)</td>
      <td>Metadata mismatch: related identifier 'http://docs.turnerdesigns.com/t2/doc/manuals/998-7210.pdf' (IsDocumentedBy) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-05-08</td>
      <td>Oceanographic Mooring Time Series, Rivers Inlet, BC, Canada (Research)</td>
      <td>Metadata mismatch: title CKAN='Oceanographic Mooring Time Series, Rivers Inlet, BC, Canada (Research)' | DataCite='Hakai Mooring Water Properties Timeseries Research'</td>
    </tr>
    <tr>
      <td>2026-04-28</td>
      <td>Sea star microbiome data from 16S amplicon sequencing associated with rocky intertidal sites on Calvert and Quadra Islands</td>
      <td>Malformed related work identifier (missing doi.org): https://10.21966/5n09-aq76</td>
    </tr>
    <tr>
      <td>2026-04-27</td>
      <td>Water Property Measurements from the Bute Inlet Ocean Observing Station (BIOOS) Wirewalker, Bute Inlet, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-04-24</td>
      <td>Biogeochemical Sampling of 28 Streams on Vancouver Island</td>
      <td>Invalid Resource URL: https://github.com/HakaiInstitute/Biogeochemical-Sampling-of-28-Streams-on-Vancouver-Island returned status_code=404</td>
    </tr>
    <tr>
      <td>2026-04-24</td>
      <td>Biogeochemical Sampling of 28 Streams on Vancouver Island</td>
      <td>Malformed related work identifier (missing doi.org): https://10.21966/cqrt-sk09</td>
    </tr>
    <tr>
      <td>2026-04-15</td>
      <td>Seawater Carbon Dioxide (CO2) Content from the Burke-o-Lator pCO2/TCO2 Analyzer located at Bamfield Marine Sciences Centre, Bamfield, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-04-14</td>
      <td>Water Property Measurements from Conductivity-Temperature-Depth Profiles, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-04-13</td>
      <td>Seawater Carbon Dioxide (CO2) Content from the SuperCO2 System in the Pacific Ecosystem Autonomous Research Laboratory, Bamfield Marine Sciences Centre, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-03-26</td>
      <td>USGS Glacier Mapping - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related work 'https://drive.google.com/file/d/1darjhrdmvvzesny0d_8arbos95rkufjr/view?usp=drive_link' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-03-17</td>
      <td>Seafloor Observatory in Hyacinthe Bay, Quadra Island, British Columbia, Canada (Provisional)</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-03-17</td>
      <td>Seafloor Observatory in Hyacinthe Bay, Quadra Island, British Columbia, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-02-27</td>
      <td>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related identifier 'https://drive.google.com/file/d/1JzY5ELRe1sIbZdq7wBmAOT1t7Y1dNJ2v/view?usp=sharing' (HasMetadata) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-02-27</td>
      <td>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related work 'https://drive.google.com/file/d/1yg1ec4-lvj0ut6csylv0p1udmcq-a5xu/view?usp=sharing' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2026-02-20</td>
      <td>Size-fractionated zooplankton biomass and isotopes along the BC coast</td>
      <td>Malformed related work identifier (missing doi.org): https://10.21966/kace-2d24</td>
    </tr>
    <tr>
      <td>2026-02-20</td>
      <td>Water Level Time Series, Choke Pass, Central Coast, BC, Canada (Provisional)</td>
      <td>Metadata mismatch: title CKAN='Water Level Time Series, Choke Pass, Central Coast, BC, Canada (Provisional)' | DataCite='Water Level measured from a Pressure Tide Gauge Instrument Deployed in Choke Pass on Calvert Island Research'</td>
    </tr>
    <tr>
      <td>2026-02-20</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Kwakshua Channel (KC) Buoy, Central Coast, BC, Canada (Provisional)</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-02-20</td>
      <td>Oceanographic Mooring Time Series, Hyacinthe Bay, BC, Canada (Provisional)</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2026-02-20</td>
      <td>Water Level Time Series, Choke Pass, Central Coast, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-02-20</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Time Series from the Kwakshua Channel (KC) Buoy, Central Coast, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-02-20</td>
      <td>Oceanographic Mooring Time Series, Hyacinthe Bay, BC, Canada (Provisional)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-02-20</td>
      <td>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2026-02-05</td>
      <td>Phytoplankton Pigment Timeseries from High-Performance Liquid Chromatography for the Northern Salish Sea and Central Coast, BC, Canada (Research)</td>
      <td>Metadata mismatch: related identifier 'https://ntrs.nasa.gov/citations/20110008482' (IsDocumentedBy) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-02-05</td>
      <td>Sentinels of Change Sea Surface Temperature Time Series Data Along the British Columbia Coast</td>
      <td>Metadata mismatch: related identifier 'https://www.onsetcomp.com/products/data-loggers/mx2203/' (IsDocumentedBy) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-02-05</td>
      <td>Phytoplankton Pigment Timeseries from High-Performance Liquid Chromatography for the Northern Salish Sea and Central Coast, BC, Canada (Research)</td>
      <td>Metadata mismatch: title CKAN='Phytoplankton Pigment Timeseries from High-Performance Liquid Chromatography for the Northern Salish Sea and Central Coast, BC, Canada (Research)' | DataCite='High performance liquid chromatography phytoplankton pigment timeseries for the northern Salish Sea and central coast, British Columbia'</td>
    </tr>
    <tr>
      <td>2026-01-30</td>
      <td>Time series of quarterly kelp canopy extent from Landsat 5, 7, 8, and 9 since 1985</td>
      <td>Metadata mismatch: related identifier 'https://doi.org/10.1016/j.rse.2018.06.039' (IsDocumentedBy) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-01-30</td>
      <td>Time series of quarterly kelp canopy extent from Landsat 5, 7, 8, and 9 since 1985</td>
      <td>Metadata mismatch: related identifier 'https://doi.org/10.1371/journal.pone.0271477' (IsDerivedFrom) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2026-01-27</td>
      <td>Rocky Subtidal Fish and Invertebrate Community Surveys from the Central Coast of BC</td>
      <td>Metadata mismatch: related work 'https://obis.org/dataset/80afee46-3e18-4669-ad1b-00f71b0544f5' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2025-11-18</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2023), Central Coast, British Columbia, Canada</td>
      <td>Metadata mismatch: related identifier 'https://docs.google.com/document/d/1j4ENgAW_2XtIHzDYbL8u2E5kOK2JkPEBVYdxcuv8NrE/edit?usp=drive_web&ouid=110988987704080303629' (HasMetadata) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2025-11-18</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2023), Central Coast, British Columbia, Canada</td>
      <td>Metadata mismatch: related work 'https://drive.google.com/file/d/1vzyfwx7jwwlxw8wosydkfgt7vxydwlan/view' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2025-11-05</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related identifier 'https://drive.google.com/file/d/1ZgcHBPDNHUNRvoaYmpj-IcbDrtPWoviN/view?usp=sharing' (HasMetadata) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2025-11-05</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: related work 'https://drive.google.com/file/d/1crbcqqcmvk3ibyxufqxgj7yv7s5a2-1y/view?usp=sharing' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2025-10-14</td>
      <td>Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia</td>
      <td>Metadata mismatch: related identifier 'https://hakai-segmentation.readthedocs.io/en/latest/' (IsDocumentedBy) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2025-08-08</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2024)</td>
      <td>Malformed related work identifier (missing doi.org): https://10.21966/t8hm-ge90</td>
    </tr>
    <tr>
      <td>2025-05-16</td>
      <td>iTrack Oysters September 2023 Experiment - Environmental and Oyster Health Data</td>
      <td>Invalid Resource URL: https://github.com/HakaiInstitute/hakai-wetlab-itracksept2023 returned status_code=404</td>
    </tr>
    <tr>
      <td>2025-05-12</td>
      <td>Larval Dungeness crab abundance and size time series along the coast of British Columbia</td>
      <td>Metadata mismatch: related identifier 'https://github.com/HakaiInstitute/sentinels-light-trap-public/blob/main/docs/Protocols/2024%20Light%20Trap%20Protocols.pdf' (IsDocumentedBy) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2025-05-08</td>
      <td>Calliarthron 2023 Experiment - Environmental Data</td>
      <td>Invalid Resource URL: https://github.com/HakaiInstitute/hakai-wetlab-calliarthron2023 returned status_code=404</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</td>
      <td>Metadata mismatch: related identifier '10.1098/rspb.2020.0108' (HasPart) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-01-30</td>
      <td>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</td>
      <td>Duplicate DOI shared with another record: 10.21966/n0h9-cq15</td>
    </tr>
    <tr>
      <td>2025-01-30</td>
      <td>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</td>
      <td>Metadata mismatch: creator 'Allison Oliver' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2025-01-30</td>
      <td>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</td>
      <td>Metadata mismatch: title CKAN='Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018' | DataCite='Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada'</td>
    </tr>
    <tr>
      <td>2024-12-30</td>
      <td>Seagrass Site-Level Production on BC Central Coast</td>
      <td>Metadata mismatch: related work 'http://ipt.iobis.org/obiscanada/resource?r=hakai_seagrassdensitysurveys' in CKAN not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>Metadata mismatch: related identifier 'https://doi.org/10.21966/7RX8-DK31' (Continues) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>Metadata mismatch: author 'Geospatial Technology Team Hakai' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>Metadata mismatch: author 'Geospatial Technology Team' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</td>
      <td>Metadata mismatch: author 'Hakai Geospatial Technology Team' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>Metadata mismatch: author 'Hakai Geospatial Technology Team' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underwater Video Transects - Calvert Island - 2016</td>
      <td>Metadata mismatch: author 'Hakai Geospatial Technology Team' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</td>
      <td>Metadata mismatch: author 'Hakai Geospatial Technology Team' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Extent of Canopy-Forming Kelps, Derived from World View-2, Central Coast, Central Coast, British Columbia</td>
      <td>Metadata mismatch: author 'Hakai Institute Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada</td>
      <td>Metadata mismatch: author 'Jenn Burt' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Derived Watersheds with Metrics - Calvert Island</td>
      <td>Metadata mismatch: author 'Santiago Gonzalez Arriola' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underwater Video Transects - Calvert Island - 2016</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Wind Fetch - BC Central Coast - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Trails - Calvert Island - British Columbia - Canada</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Wind Fetch - BC Central Coast - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Mobile Invertebrate Rocky Intertidal Surveys - BC Central Coast - 2016-2018</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution hydrometeorological data from seven small coastal watersheds, British Columbia, Canada, 2013-2019</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underwater Video Transects - Calvert Island - 2016</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface seawater CO2 content from November 2017 to June 2018 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Bathymetry for Six Lakes on Calvert and Hecate Islands - 2016 - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface water pH at Sentry Shoal in the Northern Strait of Georgia</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Derived Watersheds with Metrics - Calvert Island</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Trails - Calvert Island - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>Metadata mismatch: author 'Hakai Geospatial Science' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mount Robson BC Parks Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek – Homathko Estuary Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Mapping Coastal British Columbia - 2021 - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: author 'Hakai Geospatial' in CKAN record not found in DataCite</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mount Robson BC Parks Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek – Homathko Estuary Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Broken Group Imagery and LiDAR - 2018 - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gordon River Archaeology - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Mapping Coastal British Columbia - 2021 - Airborne Coastal Observatory</td>
      <td>Metadata mismatch: creator 'Hakai Institute' in DataCite not found in CKAN record</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</td>
      <td>Metadata mismatch: related identifier '10.21966/q31x-qg72' (References) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</td>
      <td>Metadata mismatch: related identifier '10.21966/v57r-g944' (References) in DataCite not found in CKAN</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Broken Group Imagery and LiDAR - 2018 - Airborne Coastal Observatory</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gordon River Archaeology - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-17</td>
      <td>Spatial extent of surface canopy kelp (Nereocystis luetkeana) derived from fixed-wing surveys (2023), Denman Island to south Quadra Island, British Columbia, Canada</td>
      <td>Metadata mismatch: related identifier 'https://doi.org/10.48321/D18S8D' (Documents) in DataCite not found in CKAN</td>
    </tr>
  </tbody>
</table>

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