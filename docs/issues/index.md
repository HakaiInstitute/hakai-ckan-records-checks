---
hide:
 - toc
---
# Hakai Metadata Records Issue Summary

This page present a summary of issues detected on the [Hakai Catalogue]().

## Issue Distribution

```plotly
{"data":[{"alignmentgroup":"True","bingroup":"x","histfunc":"sum","hovertemplate":"level=INFO\u003cbr\u003emessage=%{x}\u003cbr\u003esum of Issue=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"INFO","marker":{"color":"lightblue","pattern":{"shape":""}},"name":"INFO","offsetgroup":"INFO","orientation":"v","showlegend":true,"x":["Contact missing ORCID","Contact missing organization ROR","DOI is not redirecting to Hakai's catalogue","Empty resource name","Invalid distributor organisation-name","Invalid licence","Invalid resource format","Invalid resources.url.status_code","No DOI defined","No funder","No projects associated","No publisher","No version","Record isn't accesible via a standard data repository","Title contains acronyms potentially","Title contains the word dataset","Title is greater than 60 characters"],"xaxis":"x","y":[156,45,6,0,0,0,0,0,0,0,0,0,146,156,0,1,188],"yaxis":"y","type":"histogram","textposition":"inside"},{"alignmentgroup":"True","bingroup":"x","histfunc":"sum","hovertemplate":"level=WARNING\u003cbr\u003emessage=%{x}\u003cbr\u003esum of Issue=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"WARNING","marker":{"color":"orange","pattern":{"shape":""}},"name":"WARNING","offsetgroup":"WARNING","orientation":"v","showlegend":true,"x":["Contact missing ORCID","Contact missing organization ROR","DOI is not redirecting to Hakai's catalogue","Empty resource name","Invalid distributor organisation-name","Invalid licence","Invalid resource format","Invalid resources.url.status_code","No DOI defined","No funder","No projects associated","No publisher","No version","Record isn't accesible via a standard data repository","Title contains acronyms potentially","Title contains the word dataset","Title is greater than 60 characters"],"xaxis":"x","y":[432,11,0,0,0,0,0,0,55,72,0,33,0,0,40,0,0],"yaxis":"y","type":"histogram","textposition":"inside"},{"alignmentgroup":"True","bingroup":"x","histfunc":"sum","hovertemplate":"level=ERROR\u003cbr\u003emessage=%{x}\u003cbr\u003esum of Issue=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"ERROR","marker":{"color":"red","pattern":{"shape":""}},"name":"ERROR","offsetgroup":"ERROR","orientation":"v","showlegend":true,"x":["Contact missing ORCID","Contact missing organization ROR","DOI is not redirecting to Hakai's catalogue","Empty resource name","Invalid distributor organisation-name","Invalid licence","Invalid resource format","Invalid resources.url.status_code","No DOI defined","No funder","No projects associated","No publisher","No version","Record isn't accesible via a standard data repository","Title contains acronyms potentially","Title contains the word dataset","Title is greater than 60 characters"],"xaxis":"x","y":[0,0,0,3,24,5,2,12,0,0,17,0,0,0,0,0,0],"yaxis":"y","type":"histogram","textposition":"inside"}],"layout":{"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{},"tickfont":{"size":10},"linecolor":"black"},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"sum of Issue"}},"legend":{"title":{"text":"level"},"tracegroupgap":0,"font":{"size":10},"orientation":"h","yanchor":"bottom","y":1,"xanchor":"left","x":0,"itemwidth":30},"margin":{"t":60},"barmode":"relative","plot_bgcolor":"rgba(0,0,0,0)","uniformtext":{"minsize":12,"mode":"hide"}}}
```

## Records Summary

<table border="1" class="dataframe table table-striped table-hover table-sm" id="records_table">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Catalogue</th>
      <th>publication</th>
      <th>revision</th>
      <th>inf.</th>
      <th>war.</th>
      <th>err.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>240</th>
      <td><a title='b9671efe-5980-452b-90f8-f30e4f1bc194' href='../records/b9671efe-5980-452b-90f8-f30e4f1bc194' target='_blank'>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5b4cbe9f-8f2e-414c-80ff-741372891fe9' target='_blank'>link</a></td>
      <td>2025-11-12</td>
      <td>2025-11-12</td>
      <td><a title='b9671efe-5980-452b-90f8-f30e4f1bc194' href='../records/b9671efe-5980-452b-90f8-f30e4f1bc194' target='_blank'>2</a></td>
      <td><a title='b9671efe-5980-452b-90f8-f30e4f1bc194' href='../records/b9671efe-5980-452b-90f8-f30e4f1bc194' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>238</th>
      <td><a title='0272fd06-6ac8-48cd-80c9-b6e05f15be0f' href='../records/0272fd06-6ac8-48cd-80c9-b6e05f15be0f' target='_blank'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Coast, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_132cecdf-de8a-4b17-b610-0e2b3a343812' target='_blank'>link</a></td>
      <td>2025-10-31</td>
      <td>2025-10-31</td>
      <td><a title='0272fd06-6ac8-48cd-80c9-b6e05f15be0f' href='../records/0272fd06-6ac8-48cd-80c9-b6e05f15be0f' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>239</th>
      <td><a title='b01f58f7-1518-4829-aff6-ac4a8f2c0616' href='../records/b01f58f7-1518-4829-aff6-ac4a8f2c0616' target='_blank'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Vancouver Island, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f815a700-c943-4d6f-afeb-a4854ad10cfc' target='_blank'>link</a></td>
      <td>2025-10-31</td>
      <td>2025-10-31</td>
      <td><a title='b01f58f7-1518-4829-aff6-ac4a8f2c0616' href='../records/b01f58f7-1518-4829-aff6-ac4a8f2c0616' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>237</th>
      <td><a title='6be4c552-469a-4558-b63d-7a2c52566fe2' href='../records/6be4c552-469a-4558-b63d-7a2c52566fe2' target='_blank'>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9a018fe0-8bd1-41d1-af8d-079960b71473' target='_blank'>link</a></td>
      <td>2025-10-29</td>
      <td>2025-10-29</td>
      <td><a title='6be4c552-469a-4558-b63d-7a2c52566fe2' href='../records/6be4c552-469a-4558-b63d-7a2c52566fe2' target='_blank'>3</a></td>
      <td><a title='6be4c552-469a-4558-b63d-7a2c52566fe2' href='../records/6be4c552-469a-4558-b63d-7a2c52566fe2' target='_blank'>1</a></td>
      <td><a title='6be4c552-469a-4558-b63d-7a2c52566fe2' href='../records/6be4c552-469a-4558-b63d-7a2c52566fe2' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>236</th>
      <td><a title='c5e60545-c6f2-4945-af0a-21812ba5f0d9' href='../records/c5e60545-c6f2-4945-af0a-21812ba5f0d9' target='_blank'>Environmental DNA survey of Calvert Island, British Columbia, 2021</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7e9c97a3-4bf1-4852-81b6-d74cedf2c94c' target='_blank'>link</a></td>
      <td>2025-10-28</td>
      <td>2025-10-28</td>
      <td><a title='c5e60545-c6f2-4945-af0a-21812ba5f0d9' href='../records/c5e60545-c6f2-4945-af0a-21812ba5f0d9' target='_blank'>7</a></td>
      <td><a title='c5e60545-c6f2-4945-af0a-21812ba5f0d9' href='../records/c5e60545-c6f2-4945-af0a-21812ba5f0d9' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>235</th>
      <td><a title='44bdc298-1329-400a-bc02-4d35d251865d' href='../records/44bdc298-1329-400a-bc02-4d35d251865d' target='_blank'>Biodiversity and Oceanographic data from the False Creek Bioblitz, 2022</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_012164c6-28dd-4078-b702-f0c2ce63d548' target='_blank'>link</a></td>
      <td>2025-10-18</td>
      <td>2025-10-18</td>
      <td><a title='44bdc298-1329-400a-bc02-4d35d251865d' href='../records/44bdc298-1329-400a-bc02-4d35d251865d' target='_blank'>4</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>234</th>
      <td><a title='39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' href='../records/39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' target='_blank'>Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_291b98a4-d868-462c-852a-d6cf79ecf6ce' target='_blank'>link</a></td>
      <td>2025-10-14</td>
      <td>2025-10-14</td>
      <td><a title='39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' href='../records/39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' target='_blank'>2</a></td>
      <td><a title='39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' href='../records/39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' target='_blank'>1</a></td>
      <td><a title='39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' href='../records/39cc31fc-aa41-43f5-bfe7-48ea173b1f1e' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>232</th>
      <td><a title='328b062b-3af6-4149-b90f-a85b99dc40eb' href='../records/328b062b-3af6-4149-b90f-a85b99dc40eb' target='_blank'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), Central Coast, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_34a20547-cb60-4ecf-901b-f4ca52eae451' target='_blank'>link</a></td>
      <td>2025-10-06</td>
      <td>2025-10-31</td>
      <td><a title='328b062b-3af6-4149-b90f-a85b99dc40eb' href='../records/328b062b-3af6-4149-b90f-a85b99dc40eb' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>233</th>
      <td><a title='439d703a-2132-4dbd-8d39-a4cacdb8f81d' href='../records/439d703a-2132-4dbd-8d39-a4cacdb8f81d' target='_blank'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2020-2022), Central Coast, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8343aa0-dbea-4267-9f78-662bec08d4bc' target='_blank'>link</a></td>
      <td>2025-10-06</td>
      <td>2025-10-06</td>
      <td><a title='439d703a-2132-4dbd-8d39-a4cacdb8f81d' href='../records/439d703a-2132-4dbd-8d39-a4cacdb8f81d' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>231</th>
      <td><a title='e67a81ba-0ac5-49bd-a1fe-02b98f79d8a7' href='../records/e67a81ba-0ac5-49bd-a1fe-02b98f79d8a7' target='_blank'>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2023), Central Coast, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f7a867ce-0f18-43f6-8148-775235d800b6' target='_blank'>link</a></td>
      <td>2025-10-06</td>
      <td>2025-11-18</td>
      <td><a title='e67a81ba-0ac5-49bd-a1fe-02b98f79d8a7' href='../records/e67a81ba-0ac5-49bd-a1fe-02b98f79d8a7' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>230</th>
      <td><a title='186d3139-66a1-43f9-9ac7-c5607252146e' href='../records/186d3139-66a1-43f9-9ac7-c5607252146e' target='_blank'>Size-fractionated zooplankton biomass and isotopes along the BC coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dbb33efe-c207-4d9c-abef-2350595bf47a' target='_blank'>link</a></td>
      <td>2025-08-12</td>
      <td>2025-08-12</td>
      <td><a title='186d3139-66a1-43f9-9ac7-c5607252146e' href='../records/186d3139-66a1-43f9-9ac7-c5607252146e' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>229</th>
      <td><a title='262f25ca-ca11-4b10-bb6c-9aec117319a9' href='../records/262f25ca-ca11-4b10-bb6c-9aec117319a9' target='_blank'>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2024)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d959f8f3-6d20-42fe-94da-be49bcd3aeca' target='_blank'>link</a></td>
      <td>2025-08-08</td>
      <td>2025-08-08</td>
      <td><a title='262f25ca-ca11-4b10-bb6c-9aec117319a9' href='../records/262f25ca-ca11-4b10-bb6c-9aec117319a9' target='_blank'>3</a></td>
      <td></td>
      <td><a title='262f25ca-ca11-4b10-bb6c-9aec117319a9' href='../records/262f25ca-ca11-4b10-bb6c-9aec117319a9' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>227</th>
      <td><a title='bd461764-55b0-4c63-935a-5e9d1d5a6fed' href='../records/bd461764-55b0-4c63-935a-5e9d1d5a6fed' target='_blank'>iTrack Oysters September 2023 Experiment - Environmental and Oyster Health Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1d142201-cbbe-4c58-b2c2-1feeac112c51' target='_blank'>link</a></td>
      <td>2025-05-16</td>
      <td>2025-05-16</td>
      <td><a title='bd461764-55b0-4c63-935a-5e9d1d5a6fed' href='../records/bd461764-55b0-4c63-935a-5e9d1d5a6fed' target='_blank'>2</a></td>
      <td></td>
      <td><a title='bd461764-55b0-4c63-935a-5e9d1d5a6fed' href='../records/bd461764-55b0-4c63-935a-5e9d1d5a6fed' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>228</th>
      <td><a title='da040f55-984d-490d-b917-a67856de4bac' href='../records/da040f55-984d-490d-b917-a67856de4bac' target='_blank'>Sea Stars 2024 Experiment - Environmental Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_31ac855d-bf15-42d8-b20d-754638202c66' target='_blank'>link</a></td>
      <td>2025-05-16</td>
      <td>2025-05-16</td>
      <td><a title='da040f55-984d-490d-b917-a67856de4bac' href='../records/da040f55-984d-490d-b917-a67856de4bac' target='_blank'>1</a></td>
      <td></td>
      <td><a title='da040f55-984d-490d-b917-a67856de4bac' href='../records/da040f55-984d-490d-b917-a67856de4bac' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>226</th>
      <td><a title='d70bcd3d-dc07-479f-856f-ad70d11c51f1' href='../records/d70bcd3d-dc07-479f-856f-ad70d11c51f1' target='_blank'>Glaciers in Western North America Mass Loss Geospatial Data (2021-2024)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_47d8bdd4-c815-4e8d-8d75-53a9db4ae46a' target='_blank'>link</a></td>
      <td>2025-05-09</td>
      <td>2025-05-21</td>
      <td><a title='d70bcd3d-dc07-479f-856f-ad70d11c51f1' href='../records/d70bcd3d-dc07-479f-856f-ad70d11c51f1' target='_blank'>3</a></td>
      <td><a title='d70bcd3d-dc07-479f-856f-ad70d11c51f1' href='../records/d70bcd3d-dc07-479f-856f-ad70d11c51f1' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>223</th>
      <td><a title='2916abf5-419e-4cd7-8e25-f45f07a21313' href='../records/2916abf5-419e-4cd7-8e25-f45f07a21313' target='_blank'>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_87341cb3-f906-4fa5-973c-b6742aa0fbb5' target='_blank'>link</a></td>
      <td>2025-05-08</td>
      <td>2025-11-05</td>
      <td><a title='2916abf5-419e-4cd7-8e25-f45f07a21313' href='../records/2916abf5-419e-4cd7-8e25-f45f07a21313' target='_blank'>2</a></td>
      <td><a title='2916abf5-419e-4cd7-8e25-f45f07a21313' href='../records/2916abf5-419e-4cd7-8e25-f45f07a21313' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>225</th>
      <td><a title='6c99bd67-3be1-4818-bf01-dfa56e910db3' href='../records/6c99bd67-3be1-4818-bf01-dfa56e910db3' target='_blank'>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_96e3dd9c-7863-44d5-95cd-a3d0a8653d83' target='_blank'>link</a></td>
      <td>2025-05-08</td>
      <td>2025-05-08</td>
      <td><a title='6c99bd67-3be1-4818-bf01-dfa56e910db3' href='../records/6c99bd67-3be1-4818-bf01-dfa56e910db3' target='_blank'>2</a></td>
      <td><a title='6c99bd67-3be1-4818-bf01-dfa56e910db3' href='../records/6c99bd67-3be1-4818-bf01-dfa56e910db3' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>224</th>
      <td><a title='e4038a43-060b-474e-b6f2-ea68d0081053' href='../records/e4038a43-060b-474e-b6f2-ea68d0081053' target='_blank'>Calliarthron 2023 Experiment - Environmental Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_78818ed7-ec26-4004-afa1-137741ddda1e' target='_blank'>link</a></td>
      <td>2025-05-08</td>
      <td>2025-05-08</td>
      <td><a title='e4038a43-060b-474e-b6f2-ea68d0081053' href='../records/e4038a43-060b-474e-b6f2-ea68d0081053' target='_blank'>1</a></td>
      <td></td>
      <td><a title='e4038a43-060b-474e-b6f2-ea68d0081053' href='../records/e4038a43-060b-474e-b6f2-ea68d0081053' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>222</th>
      <td><a title='83f387d2-f77e-4921-af15-e064d87ad01a' href='../records/83f387d2-f77e-4921-af15-e064d87ad01a' target='_blank'>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_53730b70-be6f-4e24-8b9d-4a5e2c491121' target='_blank'>link</a></td>
      <td>2025-04-23</td>
      <td>2025-04-23</td>
      <td><a title='83f387d2-f77e-4921-af15-e064d87ad01a' href='../records/83f387d2-f77e-4921-af15-e064d87ad01a' target='_blank'>3</a></td>
      <td><a title='83f387d2-f77e-4921-af15-e064d87ad01a' href='../records/83f387d2-f77e-4921-af15-e064d87ad01a' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>220</th>
      <td><a title='046e5ef5-1480-4868-a65f-23171088bdb8' href='../records/046e5ef5-1480-4868-a65f-23171088bdb8' target='_blank'>Elliot Creek Aerial Photo and LiDAR Survey</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_31e15496-e906-43f4-9120-2446ab6125b2' target='_blank'>link</a></td>
      <td>2025-04-02</td>
      <td>2025-04-02</td>
      <td><a title='046e5ef5-1480-4868-a65f-23171088bdb8' href='../records/046e5ef5-1480-4868-a65f-23171088bdb8' target='_blank'>1</a></td>
      <td><a title='046e5ef5-1480-4868-a65f-23171088bdb8' href='../records/046e5ef5-1480-4868-a65f-23171088bdb8' target='_blank'>3</a></td>
      <td><a title='046e5ef5-1480-4868-a65f-23171088bdb8' href='../records/046e5ef5-1480-4868-a65f-23171088bdb8' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>221</th>
      <td><a title='8ce79018-75da-42f8-b7cd-195a412ab532' href='../records/8ce79018-75da-42f8-b7cd-195a412ab532' target='_blank'>Place Glacier Aerial Photo and LiDAR Survey</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_98807d0a-ba68-41e3-a2f5-e3248b459904' target='_blank'>link</a></td>
      <td>2025-04-02</td>
      <td>2025-04-02</td>
      <td><a title='8ce79018-75da-42f8-b7cd-195a412ab532' href='../records/8ce79018-75da-42f8-b7cd-195a412ab532' target='_blank'>1</a></td>
      <td><a title='8ce79018-75da-42f8-b7cd-195a412ab532' href='../records/8ce79018-75da-42f8-b7cd-195a412ab532' target='_blank'>3</a></td>
      <td><a title='8ce79018-75da-42f8-b7cd-195a412ab532' href='../records/8ce79018-75da-42f8-b7cd-195a412ab532' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>219</th>
      <td><a title='cc016896-78d9-46e8-887d-6c1dd106c0e8' href='../records/cc016896-78d9-46e8-887d-6c1dd106c0e8' target='_blank'>Bute Inlet Geo-Hazards & Ramsay West - 2024 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_52d4f546-dfdf-4bf1-b1ad-f6ec6f2663c0' target='_blank'>link</a></td>
      <td>2025-04-01</td>
      <td>2025-04-01</td>
      <td><a title='cc016896-78d9-46e8-887d-6c1dd106c0e8' href='../records/cc016896-78d9-46e8-887d-6c1dd106c0e8' target='_blank'>2</a></td>
      <td><a title='cc016896-78d9-46e8-887d-6c1dd106c0e8' href='../records/cc016896-78d9-46e8-887d-6c1dd106c0e8' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>218</th>
      <td><a title='5576c279-6d3a-4323-8104-0e1040d9906c' href='../records/5576c279-6d3a-4323-8104-0e1040d9906c' target='_blank'>Understory kelp biomass data from BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_314a0846-0fe9-4c2e-81e2-d2b24ac98b6e' target='_blank'>link</a></td>
      <td>2025-02-14</td>
      <td>2025-03-04</td>
      <td><a title='5576c279-6d3a-4323-8104-0e1040d9906c' href='../records/5576c279-6d3a-4323-8104-0e1040d9906c' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>217</th>
      <td><a title='7fa8cfec-e2e3-4459-9b9d-836335b9fcfa' href='../records/7fa8cfec-e2e3-4459-9b9d-836335b9fcfa' target='_blank'>Knight Inlet Remotely Operated Vehicle Marine Habitat Survey</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_00f42725-0a88-4d4f-87a9-4e359d2abff4' target='_blank'>link</a></td>
      <td>2025-02-05</td>
      <td>2025-02-05</td>
      <td><a title='7fa8cfec-e2e3-4459-9b9d-836335b9fcfa' href='../records/7fa8cfec-e2e3-4459-9b9d-836335b9fcfa' target='_blank'>2</a></td>
      <td><a title='7fa8cfec-e2e3-4459-9b9d-836335b9fcfa' href='../records/7fa8cfec-e2e3-4459-9b9d-836335b9fcfa' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>216</th>
      <td><a title='4a949e26-fe94-4f63-a3c6-a62e19301102' href='../records/4a949e26-fe94-4f63-a3c6-a62e19301102' target='_blank'>Rocky Subtidal Fish and Invertebrate Community Surveys from the Central Coast of BC</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_35beb32e-8dc9-42ab-9630-2ae23e414026' target='_blank'>link</a></td>
      <td>2025-01-28</td>
      <td>2025-11-06</td>
      <td><a title='4a949e26-fe94-4f63-a3c6-a62e19301102' href='../records/4a949e26-fe94-4f63-a3c6-a62e19301102' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>215</th>
      <td><a title='8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e' href='../records/8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e' target='_blank'>Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d7ffd737-5725-4a56-9134-a9ad91c2734d' target='_blank'>link</a></td>
      <td>2025-01-10</td>
      <td>2025-03-04</td>
      <td><a title='8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e' href='../records/8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e' target='_blank'>2</a></td>
      <td><a title='8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e' href='../records/8dc6dfd7-cda8-4fbf-af6a-dcae7d92ed0e' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>214</th>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='../records/49967494-a7b6-4128-b336-671971d1e2c6' target='_blank'>Data record does not exist anymore: Geomorphology - Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9fafb4c8-e61f-4372-ac71-c1ddbe57d80c' target='_blank'>link</a></td>
      <td>2025-01-03</td>
      <td>2025-01-03</td>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='../records/49967494-a7b6-4128-b336-671971d1e2c6' target='_blank'>2</a></td>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='../records/49967494-a7b6-4128-b336-671971d1e2c6' target='_blank'>2</a></td>
      <td><a title='49967494-a7b6-4128-b336-671971d1e2c6' href='../records/49967494-a7b6-4128-b336-671971d1e2c6' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>213</th>
      <td><a title='0781c19a-7efb-4680-92fd-8cd5faf0cfe4' href='../records/0781c19a-7efb-4680-92fd-8cd5faf0cfe4' target='_blank'>iTrack Oysters February 2023 Experiment - Environmental and Oyster Health Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_af344fb9-4901-470c-a441-41f11ee2ccd7' target='_blank'>link</a></td>
      <td>2024-12-19</td>
      <td>2024-12-19</td>
      <td><a title='0781c19a-7efb-4680-92fd-8cd5faf0cfe4' href='../records/0781c19a-7efb-4680-92fd-8cd5faf0cfe4' target='_blank'>2</a></td>
      <td></td>
      <td><a title='0781c19a-7efb-4680-92fd-8cd5faf0cfe4' href='../records/0781c19a-7efb-4680-92fd-8cd5faf0cfe4' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>212</th>
      <td><a title='cb0f4710-d78a-4073-959c-95f874f88711' href='../records/cb0f4710-d78a-4073-959c-95f874f88711' target='_blank'>High performance liquid chromatography phytoplankton pigment timeseries for the northern Salish Sea and central coast, British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7fd3ec6c-083a-4942-84b4-215e69492072' target='_blank'>link</a></td>
      <td>2024-12-11</td>
      <td>2024-12-11</td>
      <td><a title='cb0f4710-d78a-4073-959c-95f874f88711' href='../records/cb0f4710-d78a-4073-959c-95f874f88711' target='_blank'>1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>211</th>
      <td><a title='0049e274-f23e-448c-b307-14aa3b4e0b4a' href='../records/0049e274-f23e-448c-b307-14aa3b4e0b4a' target='_blank'>Sentinels of Change Sea surface temperature time series data along the British Columbia Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5185ac00-8148-4472-adfd-21741d8a10ce' target='_blank'>link</a></td>
      <td>2024-11-27</td>
      <td>2024-11-27</td>
      <td><a title='0049e274-f23e-448c-b307-14aa3b4e0b4a' href='../records/0049e274-f23e-448c-b307-14aa3b4e0b4a' target='_blank'>1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>210</th>
      <td><a title='265e0ec8-1d85-4e73-b85d-371845dbd08f' href='../records/265e0ec8-1d85-4e73-b85d-371845dbd08f' target='_blank'>Denali Fault - 2024 - Airborne LiDAR Survey</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f762a307-6dfb-41a8-a56c-ecacfb075a0a' target='_blank'>link</a></td>
      <td>2024-11-26</td>
      <td>2024-11-26</td>
      <td><a title='265e0ec8-1d85-4e73-b85d-371845dbd08f' href='../records/265e0ec8-1d85-4e73-b85d-371845dbd08f' target='_blank'>3</a></td>
      <td><a title='265e0ec8-1d85-4e73-b85d-371845dbd08f' href='../records/265e0ec8-1d85-4e73-b85d-371845dbd08f' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>209</th>
      <td><a title='357b017c-6add-4bde-95d0-386bdbab92b3' href='../records/357b017c-6add-4bde-95d0-386bdbab92b3' target='_blank'>Larval Dungeness crab abundance and size time series along the coast of British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d4942b86-d362-40a3-9399-c124c4c263bd' target='_blank'>link</a></td>
      <td>2024-11-25</td>
      <td>2025-05-12</td>
      <td><a title='357b017c-6add-4bde-95d0-386bdbab92b3' href='../records/357b017c-6add-4bde-95d0-386bdbab92b3' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>208</th>
      <td><a title='e8414189-54c9-4311-874e-b97f9b7916ae' href='../records/e8414189-54c9-4311-874e-b97f9b7916ae' target='_blank'>MusselSeg: Semantic Segmentation for Rocky Intertidal Mussel Habitat</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_48acba27-5e01-4b41-9a0e-f3fc8d809a13' target='_blank'>link</a></td>
      <td>2024-11-22</td>
      <td>2025-10-23</td>
      <td><a title='e8414189-54c9-4311-874e-b97f9b7916ae' href='../records/e8414189-54c9-4311-874e-b97f9b7916ae' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>207</th>
      <td><a title='45a45b5d-e45c-453c-9d36-036f69d533ae' href='../records/45a45b5d-e45c-453c-9d36-036f69d533ae' target='_blank'>Fraser River Landslide Project - 2022-2024 - Drone Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c513de71-ac9d-43fa-b693-8f865de4b137' target='_blank'>link</a></td>
      <td>2024-11-21</td>
      <td>2024-11-21</td>
      <td><a title='45a45b5d-e45c-453c-9d36-036f69d533ae' href='../records/45a45b5d-e45c-453c-9d36-036f69d533ae' target='_blank'>2</a></td>
      <td><a title='45a45b5d-e45c-453c-9d36-036f69d533ae' href='../records/45a45b5d-e45c-453c-9d36-036f69d533ae' target='_blank'>1</a></td>
      <td><a title='45a45b5d-e45c-453c-9d36-036f69d533ae' href='../records/45a45b5d-e45c-453c-9d36-036f69d533ae' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>206</th>
      <td><a title='5c162406-4886-4a66-9d9c-12c3d0316e2e' href='../records/5c162406-4886-4a66-9d9c-12c3d0316e2e' target='_blank'>Fraser River Landslide Project - Sites of Concern 2024</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f25b00ba-ad63-42b3-8021-3fb6aa99baff' target='_blank'>link</a></td>
      <td>2024-11-18</td>
      <td>2024-11-20</td>
      <td><a title='5c162406-4886-4a66-9d9c-12c3d0316e2e' href='../records/5c162406-4886-4a66-9d9c-12c3d0316e2e' target='_blank'>4</a></td>
      <td><a title='5c162406-4886-4a66-9d9c-12c3d0316e2e' href='../records/5c162406-4886-4a66-9d9c-12c3d0316e2e' target='_blank'>1</a></td>
      <td><a title='5c162406-4886-4a66-9d9c-12c3d0316e2e' href='../records/5c162406-4886-4a66-9d9c-12c3d0316e2e' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>205</th>
      <td><a title='9d1749f8-9be2-468c-946e-965f92fcdc67' href='../records/9d1749f8-9be2-468c-946e-965f92fcdc67' target='_blank'>Spatial extent of eelgrass (Zostera marina) beds from monitoring sites within the greater park ecosystem of Pacific Rim National Park Reserve (2017, 2018)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6e947d50-8392-42ce-bff9-24b126c7cab7' target='_blank'>link</a></td>
      <td>2024-11-06</td>
      <td>2024-11-06</td>
      <td><a title='9d1749f8-9be2-468c-946e-965f92fcdc67' href='../records/9d1749f8-9be2-468c-946e-965f92fcdc67' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>204</th>
      <td><a title='5042c858-d375-42f5-82e0-ee1e4da962b6' href='../records/5042c858-d375-42f5-82e0-ee1e4da962b6' target='_blank'>Protistan plankton time series from the northern Salish Sea and Central Coast, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6756b221-28a0-4848-9761-905cbd558cd7' target='_blank'>link</a></td>
      <td>2024-10-10</td>
      <td>2024-10-10</td>
      <td><a title='5042c858-d375-42f5-82e0-ee1e4da962b6' href='../records/5042c858-d375-42f5-82e0-ee1e4da962b6' target='_blank'>1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>203</th>
      <td><a title='52d607c9-46cd-4be9-a752-1b5446272f32' href='../records/52d607c9-46cd-4be9-a752-1b5446272f32' target='_blank'>Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0507a738-cd65-4ba4-943e-42b9d022b637' target='_blank'>link</a></td>
      <td>2024-10-09</td>
      <td>2025-04-23</td>
      <td><a title='52d607c9-46cd-4be9-a752-1b5446272f32' href='../records/52d607c9-46cd-4be9-a752-1b5446272f32' target='_blank'>2</a></td>
      <td><a title='52d607c9-46cd-4be9-a752-1b5446272f32' href='../records/52d607c9-46cd-4be9-a752-1b5446272f32' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>200</th>
      <td><a title='551bbe09-f182-478b-8d50-2f9a4dbd93ae' href='../records/551bbe09-f182-478b-8d50-2f9a4dbd93ae' target='_blank'>Elliot Creek Landslide LiDAR Mapping - 2023 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_189dd319-d5ef-4f2a-a060-df8d47628b86' target='_blank'>link</a></td>
      <td>2024-10-09</td>
      <td>2025-11-04</td>
      <td><a title='551bbe09-f182-478b-8d50-2f9a4dbd93ae' href='../records/551bbe09-f182-478b-8d50-2f9a4dbd93ae' target='_blank'>1</a></td>
      <td><a title='551bbe09-f182-478b-8d50-2f9a4dbd93ae' href='../records/551bbe09-f182-478b-8d50-2f9a4dbd93ae' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>202</th>
      <td><a title='6a28454e-107a-4059-9b7d-e43bf8ee693b' href='../records/6a28454e-107a-4059-9b7d-e43bf8ee693b' target='_blank'>Cryosphere Snow Surveys Southwest British Columbia - 2023 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_33a367c1-2706-4301-af99-4455fbe189a0' target='_blank'>link</a></td>
      <td>2024-10-09</td>
      <td>2024-12-16</td>
      <td><a title='6a28454e-107a-4059-9b7d-e43bf8ee693b' href='../records/6a28454e-107a-4059-9b7d-e43bf8ee693b' target='_blank'>1</a></td>
      <td><a title='6a28454e-107a-4059-9b7d-e43bf8ee693b' href='../records/6a28454e-107a-4059-9b7d-e43bf8ee693b' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>199</th>
      <td><a title='78efda1b-9688-4bcf-b16e-7167c17c0bcb' href='../records/78efda1b-9688-4bcf-b16e-7167c17c0bcb' target='_blank'>USGS Glacier Mapping - 2023 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_43422dc8-2573-4f60-bf87-df447d57ab7a' target='_blank'>link</a></td>
      <td>2024-10-09</td>
      <td>2025-04-30</td>
      <td><a title='78efda1b-9688-4bcf-b16e-7167c17c0bcb' href='../records/78efda1b-9688-4bcf-b16e-7167c17c0bcb' target='_blank'>1</a></td>
      <td><a title='78efda1b-9688-4bcf-b16e-7167c17c0bcb' href='../records/78efda1b-9688-4bcf-b16e-7167c17c0bcb' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>201</th>
      <td><a title='f1aee211-bfab-46fd-b650-c5cacb782f40' href='../records/f1aee211-bfab-46fd-b650-c5cacb782f40' target='_blank'>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3efdccb0-08ef-4e90-ac91-72969f94a99a' target='_blank'>link</a></td>
      <td>2024-10-09</td>
      <td>2025-04-23</td>
      <td><a title='f1aee211-bfab-46fd-b650-c5cacb782f40' href='../records/f1aee211-bfab-46fd-b650-c5cacb782f40' target='_blank'>2</a></td>
      <td><a title='f1aee211-bfab-46fd-b650-c5cacb782f40' href='../records/f1aee211-bfab-46fd-b650-c5cacb782f40' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>198</th>
      <td><a title='c4d3a53a-faa2-4c3e-bcd3-cfdb0aef0078' href='../records/c4d3a53a-faa2-4c3e-bcd3-cfdb0aef0078' target='_blank'>Water column CO2 system measurements from January 2016 to December 2023 from Hakai Institute oceanographic station QU39 in northern Strait of Georgia, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_355467ad-104d-40a6-b06e-52a67bfe247e' target='_blank'>link</a></td>
      <td>2024-10-08</td>
      <td>2024-10-09</td>
      <td><a title='c4d3a53a-faa2-4c3e-bcd3-cfdb0aef0078' href='../records/c4d3a53a-faa2-4c3e-bcd3-cfdb0aef0078' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>197</th>
      <td><a title='a8f61379-14f9-4ccc-bc9b-4408ba8340d7' href='../records/a8f61379-14f9-4ccc-bc9b-4408ba8340d7' target='_blank'>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_52797e17-c0ed-46a4-9dcd-e34f801c6205' target='_blank'>link</a></td>
      <td>2024-09-03</td>
      <td>2024-08-30</td>
      <td><a title='a8f61379-14f9-4ccc-bc9b-4408ba8340d7' href='../records/a8f61379-14f9-4ccc-bc9b-4408ba8340d7' target='_blank'>3</a></td>
      <td><a title='a8f61379-14f9-4ccc-bc9b-4408ba8340d7' href='../records/a8f61379-14f9-4ccc-bc9b-4408ba8340d7' target='_blank'>8</a></td>
      <td></td>
    </tr>
    <tr>
      <th>196</th>
      <td><a title='1dfdbadf-6314-4411-8d18-752f6dd920e9' href='../records/1dfdbadf-6314-4411-8d18-752f6dd920e9' target='_blank'>Motile Invertebrate Surveys - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_67e89414-a93f-496d-9766-9311f0d3954e' target='_blank'>link</a></td>
      <td>2024-08-30</td>
      <td>2025-08-14</td>
      <td><a title='1dfdbadf-6314-4411-8d18-752f6dd920e9' href='../records/1dfdbadf-6314-4411-8d18-752f6dd920e9' target='_blank'>5</a></td>
      <td><a title='1dfdbadf-6314-4411-8d18-752f6dd920e9' href='../records/1dfdbadf-6314-4411-8d18-752f6dd920e9' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>195</th>
      <td><a title='2081eb2e-67c5-44b7-b048-aeb2c646f238' href='../records/2081eb2e-67c5-44b7-b048-aeb2c646f238' target='_blank'>Data for the paper "Phylogenomic position of eupelagonemids, abundant, and diverse deep-ocean heterotrophs"</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f67c0c58-3225-4dac-9264-1e76f07c9374' target='_blank'>link</a></td>
      <td>2024-08-02</td>
      <td>2024-08-02</td>
      <td><a title='2081eb2e-67c5-44b7-b048-aeb2c646f238' href='../records/2081eb2e-67c5-44b7-b048-aeb2c646f238' target='_blank'>2</a></td>
      <td></td>
      <td><a title='2081eb2e-67c5-44b7-b048-aeb2c646f238' href='../records/2081eb2e-67c5-44b7-b048-aeb2c646f238' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>194</th>
      <td><a title='7607322d-6dea-4758-a257-de8353c899c1' href='../records/7607322d-6dea-4758-a257-de8353c899c1' target='_blank'>Water Level measured from a Pressure Tide Gauge Instrument Deployed in Choke Pass on Calvert Island Research</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6652a7a9-d27f-4cbe-ac04-435c238e991d' target='_blank'>link</a></td>
      <td>2024-07-18</td>
      <td>2024-07-18</td>
      <td><a title='7607322d-6dea-4758-a257-de8353c899c1' href='../records/7607322d-6dea-4758-a257-de8353c899c1' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>193</th>
      <td><a title='13dc3c6c-9dd4-47a4-92ad-681c653d3565' href='../records/13dc3c6c-9dd4-47a4-92ad-681c653d3565' target='_blank'>Hakai Water Properties Vertical Profile Data Measured by Oceanographic Profilers, Provisional</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6143028b-028d-46c7-a67d-f3a513435e63' target='_blank'>link</a></td>
      <td>2024-07-17</td>
      <td>2024-12-04</td>
      <td><a title='13dc3c6c-9dd4-47a4-92ad-681c653d3565' href='../records/13dc3c6c-9dd4-47a4-92ad-681c653d3565' target='_blank'>2</a></td>
      <td><a title='13dc3c6c-9dd4-47a4-92ad-681c653d3565' href='../records/13dc3c6c-9dd4-47a4-92ad-681c653d3565' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>192</th>
      <td><a title='0cf058db-a52c-404a-9332-17c946f13e8e' href='../records/0cf058db-a52c-404a-9332-17c946f13e8e' target='_blank'>Hakai Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, Research</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d55021c3-a142-4e14-8208-36c9826c1893' target='_blank'>link</a></td>
      <td>2024-07-12</td>
      <td>2024-07-12</td>
      <td><a title='0cf058db-a52c-404a-9332-17c946f13e8e' href='../records/0cf058db-a52c-404a-9332-17c946f13e8e' target='_blank'>1</a></td>
      <td><a title='0cf058db-a52c-404a-9332-17c946f13e8e' href='../records/0cf058db-a52c-404a-9332-17c946f13e8e' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>191</th>
      <td><a title='bf7c05e8-510d-4449-9e81-4c358ff3f440' href='../records/bf7c05e8-510d-4449-9e81-4c358ff3f440' target='_blank'>Hakai Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, Provisional</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1755dc37-8d33-4158-8041-c22536fd5771' target='_blank'>link</a></td>
      <td>2024-07-12</td>
      <td>2025-04-23</td>
      <td><a title='bf7c05e8-510d-4449-9e81-4c358ff3f440' href='../records/bf7c05e8-510d-4449-9e81-4c358ff3f440' target='_blank'>1</a></td>
      <td><a title='bf7c05e8-510d-4449-9e81-4c358ff3f440' href='../records/bf7c05e8-510d-4449-9e81-4c358ff3f440' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>190</th>
      <td><a title='3b713ae6-f805-41ed-b7ed-25fc731d752e' href='../records/3b713ae6-f805-41ed-b7ed-25fc731d752e' target='_blank'>8-day average satellite (Sentinel 3A and 3B) chlorophyll and suspended matter concentrations for coastal British Columbia and southeast Alaska</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_91107fce-93a4-4bc9-bce4-e7d9e1cf02a0' target='_blank'>link</a></td>
      <td>2024-04-05</td>
      <td>2024-07-18</td>
      <td><a title='3b713ae6-f805-41ed-b7ed-25fc731d752e' href='../records/3b713ae6-f805-41ed-b7ed-25fc731d752e' target='_blank'>1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>189</th>
      <td><a title='9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' href='../records/9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' target='_blank'>Seagrass Site-Level Production on BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_59b33373-ae4a-4719-a3df-0e36a08187d8' target='_blank'>link</a></td>
      <td>2024-03-22</td>
      <td>2024-12-30</td>
      <td><a title='9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' href='../records/9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' target='_blank'>1</a></td>
      <td><a title='9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' href='../records/9df42f88-b8d8-4e2d-97bb-ad5ba49f6f1f' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>188</th>
      <td><a title='0aa06844-3141-4d02-833d-d65b0659bd6f' href='../records/0aa06844-3141-4d02-833d-d65b0659bd6f' target='_blank'>Hakai Water Properties Vertical Profile Data Measured by Oceanographic Profilers, Research</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ba41d935-f293-447f-be3d-7098e569b431' target='_blank'>link</a></td>
      <td>2024-03-19</td>
      <td>2024-07-31</td>
      <td><a title='0aa06844-3141-4d02-833d-d65b0659bd6f' href='../records/0aa06844-3141-4d02-833d-d65b0659bd6f' target='_blank'>1</a></td>
      <td><a title='0aa06844-3141-4d02-833d-d65b0659bd6f' href='../records/0aa06844-3141-4d02-833d-d65b0659bd6f' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>187</th>
      <td><a title='abb0b617-3a3e-43ec-b62e-e2918bfc10aa' href='../records/abb0b617-3a3e-43ec-b62e-e2918bfc10aa' target='_blank'>Spatial extent of surface canopy kelp (Nereocystis luetkeana) derived from fixed-wing surveys (2023), Denman Island to south Quadra Island, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b8483c9e-81e6-4e1a-b09f-2d66f8fee9a2' target='_blank'>link</a></td>
      <td>2024-03-15</td>
      <td>2024-07-17</td>
      <td><a title='abb0b617-3a3e-43ec-b62e-e2918bfc10aa' href='../records/abb0b617-3a3e-43ec-b62e-e2918bfc10aa' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>185</th>
      <td><a title='11051c56-8d67-43fc-a13c-b706e851a5a4' href='../records/11051c56-8d67-43fc-a13c-b706e851a5a4' target='_blank'>Pruth Dock, Calvert Island Tide and Weather Station Provisional</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2d693456-7e65-46be-95d7-6bb697320017' target='_blank'>link</a></td>
      <td>2024-03-14</td>
      <td>2024-07-23</td>
      <td><a title='11051c56-8d67-43fc-a13c-b706e851a5a4' href='../records/11051c56-8d67-43fc-a13c-b706e851a5a4' target='_blank'>1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>186</th>
      <td><a title='b0e815da-1b17-404d-8bf6-0bdb4a22d170' href='../records/b0e815da-1b17-404d-8bf6-0bdb4a22d170' target='_blank'>Extent of Canopy-Forming Kelps, Derived from World View-2, Central Coast, Central Coast, British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c24f23f0-8d16-4bfd-835a-5475f1ecd8e8' target='_blank'>link</a></td>
      <td>2024-03-14</td>
      <td>2024-07-24</td>
      <td><a title='b0e815da-1b17-404d-8bf6-0bdb4a22d170' href='../records/b0e815da-1b17-404d-8bf6-0bdb4a22d170' target='_blank'>1</a></td>
      <td><a title='b0e815da-1b17-404d-8bf6-0bdb4a22d170' href='../records/b0e815da-1b17-404d-8bf6-0bdb4a22d170' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>184</th>
      <td><a title='582c6ff0-029e-44ba-8ba1-d3f2f39f2005' href='../records/582c6ff0-029e-44ba-8ba1-d3f2f39f2005' target='_blank'>Genetic Stock Identification of Juvenile Sockeye Salmon Captured in the Discovery Islands and Johnstone Strait BC, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6f6560e7-7497-4685-9df2-51c66080b7c9' target='_blank'>link</a></td>
      <td>2024-01-18</td>
      <td>2024-06-27</td>
      <td><a title='582c6ff0-029e-44ba-8ba1-d3f2f39f2005' href='../records/582c6ff0-029e-44ba-8ba1-d3f2f39f2005' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>183</th>
      <td><a title='432b05ce-8904-4094-94bf-b97fb6636e41' href='../records/432b05ce-8904-4094-94bf-b97fb6636e41' target='_blank'>Nuchatlaht Survey - Hakai Airborne Coastal Observatory Imagery and Topography Data - Nootka Island British Columbia - 2023</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3e90a567-cdd7-41f3-8157-0e7be76eefb8' target='_blank'>link</a></td>
      <td>2024-01-08</td>
      <td>2024-07-23</td>
      <td><a title='432b05ce-8904-4094-94bf-b97fb6636e41' href='../records/432b05ce-8904-4094-94bf-b97fb6636e41' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>182</th>
      <td><a title='aa3c29bd-294d-4da2-aed1-3c40bb6bc0d9' href='../records/aa3c29bd-294d-4da2-aed1-3c40bb6bc0d9' target='_blank'>Real-Time Provisional High-Resolution Record of Seawater Carbon Dioxide (CO2) Content Collected from the Bamfield Marine Sciences Centre in Bamfield, BC, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fb5c9e1e-a911-46b7-8c1d-e34215a105ed' target='_blank'>link</a></td>
      <td>2023-10-20</td>
      <td>2024-07-17</td>
      <td><a title='aa3c29bd-294d-4da2-aed1-3c40bb6bc0d9' href='../records/aa3c29bd-294d-4da2-aed1-3c40bb6bc0d9' target='_blank'>2</a></td>
      <td><a title='aa3c29bd-294d-4da2-aed1-3c40bb6bc0d9' href='../records/aa3c29bd-294d-4da2-aed1-3c40bb6bc0d9' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>181</th>
      <td><a title='3f7bca49-27cf-4f39-9366-35808e82f2a8' href='../records/3f7bca49-27cf-4f39-9366-35808e82f2a8' target='_blank'>Mapping Canopy-Forming Kelps in the Northeast Pacific: A Guidebook for Decision-Makers and Practitioners</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c074bff6-408b-443a-bdaf-4713f0eadb95' target='_blank'>link</a></td>
      <td>2023-09-29</td>
      <td>2024-07-23</td>
      <td><a title='3f7bca49-27cf-4f39-9366-35808e82f2a8' href='../records/3f7bca49-27cf-4f39-9366-35808e82f2a8' target='_blank'>2</a></td>
      <td></td>
      <td><a title='3f7bca49-27cf-4f39-9366-35808e82f2a8' href='../records/3f7bca49-27cf-4f39-9366-35808e82f2a8' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>180</th>
      <td><a title='e40c42ef-cabf-4969-aeb3-263407a91a68' href='../records/e40c42ef-cabf-4969-aeb3-263407a91a68' target='_blank'>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b63374a9-2288-4512-9820-5d1b44d2b502' target='_blank'>link</a></td>
      <td>2023-09-19</td>
      <td>2024-07-23</td>
      <td><a title='e40c42ef-cabf-4969-aeb3-263407a91a68' href='../records/e40c42ef-cabf-4969-aeb3-263407a91a68' target='_blank'>4</a></td>
      <td><a title='e40c42ef-cabf-4969-aeb3-263407a91a68' href='../records/e40c42ef-cabf-4969-aeb3-263407a91a68' target='_blank'>1</a></td>
      <td><a title='e40c42ef-cabf-4969-aeb3-263407a91a68' href='../records/e40c42ef-cabf-4969-aeb3-263407a91a68' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>179</th>
      <td><a title='acd6c43f-6cbd-43c8-9bff-7d9ae6630295' href='../records/acd6c43f-6cbd-43c8-9bff-7d9ae6630295' target='_blank'>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program, Provisional</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_86343dd1-28d0-4d02-8eaf-402d51a7fef7' target='_blank'>link</a></td>
      <td>2023-08-29</td>
      <td>2024-06-12</td>
      <td><a title='acd6c43f-6cbd-43c8-9bff-7d9ae6630295' href='../records/acd6c43f-6cbd-43c8-9bff-7d9ae6630295' target='_blank'>1</a></td>
      <td><a title='acd6c43f-6cbd-43c8-9bff-7d9ae6630295' href='../records/acd6c43f-6cbd-43c8-9bff-7d9ae6630295' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>178</th>
      <td><a title='b1c4c93b-6324-4b84-b341-76be046cbf28' href='../records/b1c4c93b-6324-4b84-b341-76be046cbf28' target='_blank'>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_16ae186b-9d99-42cf-b18d-09f9bb0501d7' target='_blank'>link</a></td>
      <td>2023-08-08</td>
      <td>2024-07-23</td>
      <td><a title='b1c4c93b-6324-4b84-b341-76be046cbf28' href='../records/b1c4c93b-6324-4b84-b341-76be046cbf28' target='_blank'>4</a></td>
      <td><a title='b1c4c93b-6324-4b84-b341-76be046cbf28' href='../records/b1c4c93b-6324-4b84-b341-76be046cbf28' target='_blank'>2</a></td>
      <td><a title='b1c4c93b-6324-4b84-b341-76be046cbf28' href='../records/b1c4c93b-6324-4b84-b341-76be046cbf28' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>177</th>
      <td><a title='5c2aac2c-0dd8-49d8-87b2-5c52b3d42946' href='../records/5c2aac2c-0dd8-49d8-87b2-5c52b3d42946' target='_blank'>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_60f653ae-a3fd-484d-807c-3d7e4a0712cb' target='_blank'>link</a></td>
      <td>2023-04-24</td>
      <td>2025-04-21</td>
      <td><a title='5c2aac2c-0dd8-49d8-87b2-5c52b3d42946' href='../records/5c2aac2c-0dd8-49d8-87b2-5c52b3d42946' target='_blank'>3</a></td>
      <td><a title='5c2aac2c-0dd8-49d8-87b2-5c52b3d42946' href='../records/5c2aac2c-0dd8-49d8-87b2-5c52b3d42946' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>176</th>
      <td><a title='2709d7b1-22e1-4268-bcda-dc0c79f2878e' href='../records/2709d7b1-22e1-4268-bcda-dc0c79f2878e' target='_blank'>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_24f1c230-6c37-470c-907d-25b9b022f5c2' target='_blank'>link</a></td>
      <td>2023-03-13</td>
      <td>2025-04-21</td>
      <td><a title='2709d7b1-22e1-4268-bcda-dc0c79f2878e' href='../records/2709d7b1-22e1-4268-bcda-dc0c79f2878e' target='_blank'>8</a></td>
      <td><a title='2709d7b1-22e1-4268-bcda-dc0c79f2878e' href='../records/2709d7b1-22e1-4268-bcda-dc0c79f2878e' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>175</th>
      <td><a title='75b60436-da51-4ccf-b14a-27f45f782b2b' href='../records/75b60436-da51-4ccf-b14a-27f45f782b2b' target='_blank'>Hakai Institute Nutrients (Dosser et al., 2021)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_476204a7-0714-4755-953d-61fa3c5df497' target='_blank'>link</a></td>
      <td>2023-03-13</td>
      <td>2024-07-23</td>
      <td><a title='75b60436-da51-4ccf-b14a-27f45f782b2b' href='../records/75b60436-da51-4ccf-b14a-27f45f782b2b' target='_blank'>2</a></td>
      <td><a title='75b60436-da51-4ccf-b14a-27f45f782b2b' href='../records/75b60436-da51-4ccf-b14a-27f45f782b2b' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>174</th>
      <td><a title='3a8b11a2-5deb-469e-824b-32ab0eb5c2ca' href='../records/3a8b11a2-5deb-469e-824b-32ab0eb5c2ca' target='_blank'>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_251aef08-4017-4493-b9d8-c4583913b511' target='_blank'>link</a></td>
      <td>2023-03-03</td>
      <td>2024-07-23</td>
      <td><a title='3a8b11a2-5deb-469e-824b-32ab0eb5c2ca' href='../records/3a8b11a2-5deb-469e-824b-32ab0eb5c2ca' target='_blank'>2</a></td>
      <td><a title='3a8b11a2-5deb-469e-824b-32ab0eb5c2ca' href='../records/3a8b11a2-5deb-469e-824b-32ab0eb5c2ca' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>173</th>
      <td><a title='79ace68f-f5a9-4224-8615-20fa255cb6d4' href='../records/79ace68f-f5a9-4224-8615-20fa255cb6d4' target='_blank'>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_12f951d4-4155-4c05-969d-a7158412f579' target='_blank'>link</a></td>
      <td>2023-03-03</td>
      <td>2025-04-23</td>
      <td><a title='79ace68f-f5a9-4224-8615-20fa255cb6d4' href='../records/79ace68f-f5a9-4224-8615-20fa255cb6d4' target='_blank'>3</a></td>
      <td><a title='79ace68f-f5a9-4224-8615-20fa255cb6d4' href='../records/79ace68f-f5a9-4224-8615-20fa255cb6d4' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>172</th>
      <td><a title='96b5a7f2-5f23-413a-b060-d268bcff83ba' href='../records/96b5a7f2-5f23-413a-b060-d268bcff83ba' target='_blank'>High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4a09d56b-b120-46c8-9263-ae3c42a02e9b' target='_blank'>link</a></td>
      <td>2023-01-24</td>
      <td>2025-04-23</td>
      <td><a title='96b5a7f2-5f23-413a-b060-d268bcff83ba' href='../records/96b5a7f2-5f23-413a-b060-d268bcff83ba' target='_blank'>3</a></td>
      <td><a title='96b5a7f2-5f23-413a-b060-d268bcff83ba' href='../records/96b5a7f2-5f23-413a-b060-d268bcff83ba' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>171</th>
      <td><a title='550e7acb-0e3f-461f-bd47-8b6ced16bf43' href='../records/550e7acb-0e3f-461f-bd47-8b6ced16bf43' target='_blank'>Mount Robson BC Parks Survey - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_160803d3-8019-4a73-9191-5f75f0ec21be' target='_blank'>link</a></td>
      <td>2023-01-23</td>
      <td>2024-07-23</td>
      <td><a title='550e7acb-0e3f-461f-bd47-8b6ced16bf43' href='../records/550e7acb-0e3f-461f-bd47-8b6ced16bf43' target='_blank'>1</a></td>
      <td><a title='550e7acb-0e3f-461f-bd47-8b6ced16bf43' href='../records/550e7acb-0e3f-461f-bd47-8b6ced16bf43' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>170</th>
      <td><a title='a4e3915d-207e-493d-97ff-c1e6ad6f0ce7' href='../records/a4e3915d-207e-493d-97ff-c1e6ad6f0ce7' target='_blank'>Gordon River Archaeology - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e2baa28d-c063-4354-ae1f-2abdb8397d8f' target='_blank'>link</a></td>
      <td>2023-01-23</td>
      <td>2024-07-23</td>
      <td><a title='a4e3915d-207e-493d-97ff-c1e6ad6f0ce7' href='../records/a4e3915d-207e-493d-97ff-c1e6ad6f0ce7' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>169</th>
      <td><a title='074ffcad-2e2f-496c-9378-dec5289d4336' href='../records/074ffcad-2e2f-496c-9378-dec5289d4336' target='_blank'>Ecstall Slide - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_412ae9da-7e81-4a33-90c8-ed142f36307e' target='_blank'>link</a></td>
      <td>2023-01-18</td>
      <td>2024-06-12</td>
      <td></td>
      <td><a title='074ffcad-2e2f-496c-9378-dec5289d4336' href='../records/074ffcad-2e2f-496c-9378-dec5289d4336' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>168</th>
      <td><a title='10f825fb-14a9-4b35-b1d9-6f759b188f9a' href='../records/10f825fb-14a9-4b35-b1d9-6f759b188f9a' target='_blank'>Fraser River - BCSRIF Landslide Mapping – 2022 – Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0295e3a3-11b5-494d-ac60-ed4b95a15fad' target='_blank'>link</a></td>
      <td>2023-01-18</td>
      <td>2024-11-28</td>
      <td><a title='10f825fb-14a9-4b35-b1d9-6f759b188f9a' href='../records/10f825fb-14a9-4b35-b1d9-6f759b188f9a' target='_blank'>1</a></td>
      <td><a title='10f825fb-14a9-4b35-b1d9-6f759b188f9a' href='../records/10f825fb-14a9-4b35-b1d9-6f759b188f9a' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>166</th>
      <td><a title='eb02906a-9645-4486-ba14-46d71c581352' href='../records/eb02906a-9645-4486-ba14-46d71c581352' target='_blank'>Broken Group Imagery and LiDAR - 2018 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bdb9229b-f594-40df-994e-e52e8a678165' target='_blank'>link</a></td>
      <td>2023-01-18</td>
      <td>2024-07-23</td>
      <td><a title='eb02906a-9645-4486-ba14-46d71c581352' href='../records/eb02906a-9645-4486-ba14-46d71c581352' target='_blank'>2</a></td>
      <td><a title='eb02906a-9645-4486-ba14-46d71c581352' href='../records/eb02906a-9645-4486-ba14-46d71c581352' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>167</th>
      <td><a title='ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' href='../records/ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' target='_blank'>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_532c06ad-0b55-4e86-9088-cec970a0a8e1' target='_blank'>link</a></td>
      <td>2023-01-18</td>
      <td>2024-12-05</td>
      <td><a title='ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' href='../records/ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' target='_blank'>2</a></td>
      <td><a title='ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' href='../records/ee2eec87-7a78-4a7f-87b7-54347a6c3b2f' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>165</th>
      <td><a title='f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff' href='../records/f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff' target='_blank'>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c39138f-8f01-4948-a3de-864044686c55' target='_blank'>link</a></td>
      <td>2023-01-18</td>
      <td>2024-07-23</td>
      <td><a title='f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff' href='../records/f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff' target='_blank'>2</a></td>
      <td><a title='f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff' href='../records/f1f4ee29-1d0d-49f9-9a5b-64768f24a6ff' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>164</th>
      <td><a title='50037e63-bfac-4b7a-8547-56337fe40026' href='../records/50037e63-bfac-4b7a-8547-56337fe40026' target='_blank'>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8d36f54-4955-463c-94e5-f0030c3230f3' target='_blank'>link</a></td>
      <td>2023-01-17</td>
      <td>2024-07-12</td>
      <td><a title='50037e63-bfac-4b7a-8547-56337fe40026' href='../records/50037e63-bfac-4b7a-8547-56337fe40026' target='_blank'>6</a></td>
      <td><a title='50037e63-bfac-4b7a-8547-56337fe40026' href='../records/50037e63-bfac-4b7a-8547-56337fe40026' target='_blank'>1</a></td>
      <td><a title='50037e63-bfac-4b7a-8547-56337fe40026' href='../records/50037e63-bfac-4b7a-8547-56337fe40026' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>163</th>
      <td><a title='b276330c-4ee9-476a-979a-cebe52d51db6' href='../records/b276330c-4ee9-476a-979a-cebe52d51db6' target='_blank'>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6dc431f0-3ca4-4c48-992c-df82d6f8521c' target='_blank'>link</a></td>
      <td>2023-01-17</td>
      <td>2024-07-23</td>
      <td><a title='b276330c-4ee9-476a-979a-cebe52d51db6' href='../records/b276330c-4ee9-476a-979a-cebe52d51db6' target='_blank'>2</a></td>
      <td><a title='b276330c-4ee9-476a-979a-cebe52d51db6' href='../records/b276330c-4ee9-476a-979a-cebe52d51db6' target='_blank'>3</a></td>
      <td><a title='b276330c-4ee9-476a-979a-cebe52d51db6' href='../records/b276330c-4ee9-476a-979a-cebe52d51db6' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>162</th>
      <td><a title='78b2edef-dab3-47a9-93bb-af63dfcd178d' href='../records/78b2edef-dab3-47a9-93bb-af63dfcd178d' target='_blank'>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d049351d-b806-461f-85fb-451f100fd7d6' target='_blank'>link</a></td>
      <td>2022-12-01</td>
      <td>2025-04-23</td>
      <td><a title='78b2edef-dab3-47a9-93bb-af63dfcd178d' href='../records/78b2edef-dab3-47a9-93bb-af63dfcd178d' target='_blank'>12</a></td>
      <td><a title='78b2edef-dab3-47a9-93bb-af63dfcd178d' href='../records/78b2edef-dab3-47a9-93bb-af63dfcd178d' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>160</th>
      <td><a title='bdc6c492-dbb1-4d6e-90b8-d7bddf2c6356' href='../records/bdc6c492-dbb1-4d6e-90b8-d7bddf2c6356' target='_blank'>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e2c7a84f-a33b-4713-9b7f-a9ed57efc5c3' target='_blank'>link</a></td>
      <td>2022-11-25</td>
      <td>2024-12-05</td>
      <td><a title='bdc6c492-dbb1-4d6e-90b8-d7bddf2c6356' href='../records/bdc6c492-dbb1-4d6e-90b8-d7bddf2c6356' target='_blank'>1</a></td>
      <td><a title='bdc6c492-dbb1-4d6e-90b8-d7bddf2c6356' href='../records/bdc6c492-dbb1-4d6e-90b8-d7bddf2c6356' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>161</th>
      <td><a title='f20621b4-90c1-4925-a747-5e98f924d6a9' href='../records/f20621b4-90c1-4925-a747-5e98f924d6a9' target='_blank'>Glacier and Ice Field Mapping - 2021 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0fbdb22e-d039-46a8-95e3-0bbf4f55d972' target='_blank'>link</a></td>
      <td>2022-11-25</td>
      <td>2025-05-06</td>
      <td><a title='f20621b4-90c1-4925-a747-5e98f924d6a9' href='../records/f20621b4-90c1-4925-a747-5e98f924d6a9' target='_blank'>2</a></td>
      <td><a title='f20621b4-90c1-4925-a747-5e98f924d6a9' href='../records/f20621b4-90c1-4925-a747-5e98f924d6a9' target='_blank'>1</a></td>
      <td><a title='f20621b4-90c1-4925-a747-5e98f924d6a9' href='../records/f20621b4-90c1-4925-a747-5e98f924d6a9' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>159</th>
      <td><a title='2168fd41-96d4-4b72-b5ec-0a5c342aad2a' href='../records/2168fd41-96d4-4b72-b5ec-0a5c342aad2a' target='_blank'>Snow Mapping Coastal British Columbia - 2021 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f952a904-f9f7-4876-b518-c98b1fd96f7e' target='_blank'>link</a></td>
      <td>2022-11-24</td>
      <td>2024-07-23</td>
      <td><a title='2168fd41-96d4-4b72-b5ec-0a5c342aad2a' href='../records/2168fd41-96d4-4b72-b5ec-0a5c342aad2a' target='_blank'>1</a></td>
      <td><a title='2168fd41-96d4-4b72-b5ec-0a5c342aad2a' href='../records/2168fd41-96d4-4b72-b5ec-0a5c342aad2a' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>158</th>
      <td><a title='36e9e6ae-a407-456e-8fe2-a3a78b246bf7' href='../records/36e9e6ae-a407-456e-8fe2-a3a78b246bf7' target='_blank'>Elliot Creek – Homathko Estuary Mapping - 2021 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8e99157a-8daf-4e68-92ae-9d22cfd46ce7' target='_blank'>link</a></td>
      <td>2022-11-24</td>
      <td>2024-07-23</td>
      <td><a title='36e9e6ae-a407-456e-8fe2-a3a78b246bf7' href='../records/36e9e6ae-a407-456e-8fe2-a3a78b246bf7' target='_blank'>1</a></td>
      <td><a title='36e9e6ae-a407-456e-8fe2-a3a78b246bf7' href='../records/36e9e6ae-a407-456e-8fe2-a3a78b246bf7' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>157</th>
      <td><a title='46377bf0-06d5-4612-970d-29cd972e4870' href='../records/46377bf0-06d5-4612-970d-29cd972e4870' target='_blank'>Mussel Dynamics - Point Intercepts - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cec3dcef-8dba-4d91-aee6-b60ce416497c' target='_blank'>link</a></td>
      <td>2022-10-08</td>
      <td>2024-11-29</td>
      <td><a title='46377bf0-06d5-4612-970d-29cd972e4870' href='../records/46377bf0-06d5-4612-970d-29cd972e4870' target='_blank'>5</a></td>
      <td><a title='46377bf0-06d5-4612-970d-29cd972e4870' href='../records/46377bf0-06d5-4612-970d-29cd972e4870' target='_blank'>9</a></td>
      <td></td>
    </tr>
    <tr>
      <th>155</th>
      <td><a title='6ce6e697-d539-41b1-9771-b5e859a6ff50' href='../records/6ce6e697-d539-41b1-9771-b5e859a6ff50' target='_blank'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c89e35df-8a16-4efc-ae29-15f4e3da8a55' target='_blank'>link</a></td>
      <td>2022-10-08</td>
      <td>2024-11-29</td>
      <td><a title='6ce6e697-d539-41b1-9771-b5e859a6ff50' href='../records/6ce6e697-d539-41b1-9771-b5e859a6ff50' target='_blank'>5</a></td>
      <td><a title='6ce6e697-d539-41b1-9771-b5e859a6ff50' href='../records/6ce6e697-d539-41b1-9771-b5e859a6ff50' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>154</th>
      <td><a title='967f98cb-131a-421e-bcfd-467cff973b30' href='../records/967f98cb-131a-421e-bcfd-467cff973b30' target='_blank'>Mussel Dynamics - Length & Bed Depth - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d683512f-5e47-4b1d-baac-c653fb761806' target='_blank'>link</a></td>
      <td>2022-10-08</td>
      <td>2024-11-29</td>
      <td><a title='967f98cb-131a-421e-bcfd-467cff973b30' href='../records/967f98cb-131a-421e-bcfd-467cff973b30' target='_blank'>5</a></td>
      <td><a title='967f98cb-131a-421e-bcfd-467cff973b30' href='../records/967f98cb-131a-421e-bcfd-467cff973b30' target='_blank'>7</a></td>
      <td></td>
    </tr>
    <tr>
      <th>156</th>
      <td><a title='f51d96b5-1827-4aab-b1ce-575faff1fd03' href='../records/f51d96b5-1827-4aab-b1ce-575faff1fd03' target='_blank'>Surfgrass Community Structure - Length & Density - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_93a9bb9a-b54e-4623-9e0e-93d8b7d0020b' target='_blank'>link</a></td>
      <td>2022-10-08</td>
      <td>2024-11-29</td>
      <td><a title='f51d96b5-1827-4aab-b1ce-575faff1fd03' href='../records/f51d96b5-1827-4aab-b1ce-575faff1fd03' target='_blank'>7</a></td>
      <td><a title='f51d96b5-1827-4aab-b1ce-575faff1fd03' href='../records/f51d96b5-1827-4aab-b1ce-575faff1fd03' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>153</th>
      <td><a title='d3c4dde5-38b2-480d-a4e7-228bde9eb537' href='../records/d3c4dde5-38b2-480d-a4e7-228bde9eb537' target='_blank'>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c1b9801b-742b-41b6-a69b-5e7ae6f09bce' target='_blank'>link</a></td>
      <td>2022-09-01</td>
      <td>2024-07-23</td>
      <td><a title='d3c4dde5-38b2-480d-a4e7-228bde9eb537' href='../records/d3c4dde5-38b2-480d-a4e7-228bde9eb537' target='_blank'>1</a></td>
      <td><a title='d3c4dde5-38b2-480d-a4e7-228bde9eb537' href='../records/d3c4dde5-38b2-480d-a4e7-228bde9eb537' target='_blank'>3</a></td>
      <td><a title='d3c4dde5-38b2-480d-a4e7-228bde9eb537' href='../records/d3c4dde5-38b2-480d-a4e7-228bde9eb537' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>152</th>
      <td><a title='2ec7aa05-6a81-4836-bf79-0893cef2db95' href='../records/2ec7aa05-6a81-4836-bf79-0893cef2db95' target='_blank'>100 Islands Research Program Terrestrial Vegetation Data - BC Central Coast - 2015, 2016, 2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_71447a55-3eca-41b1-87ff-b8ef69314c4d' target='_blank'>link</a></td>
      <td>2022-08-31</td>
      <td>2024-12-04</td>
      <td><a title='2ec7aa05-6a81-4836-bf79-0893cef2db95' href='../records/2ec7aa05-6a81-4836-bf79-0893cef2db95' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>151</th>
      <td><a title='782fef82-e6e7-451d-a7ac-39d08129c1d3' href='../records/782fef82-e6e7-451d-a7ac-39d08129c1d3' target='_blank'>Adjusted Koeye River stage and temperature from 2013 to 2021</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_44dbd3c8-93bf-4e2f-9532-cbaebcf4a2be' target='_blank'>link</a></td>
      <td>2022-07-08</td>
      <td>2024-07-23</td>
      <td><a title='782fef82-e6e7-451d-a7ac-39d08129c1d3' href='../records/782fef82-e6e7-451d-a7ac-39d08129c1d3' target='_blank'>5</a></td>
      <td><a title='782fef82-e6e7-451d-a7ac-39d08129c1d3' href='../records/782fef82-e6e7-451d-a7ac-39d08129c1d3' target='_blank'>4</a></td>
      <td><a title='782fef82-e6e7-451d-a7ac-39d08129c1d3' href='../records/782fef82-e6e7-451d-a7ac-39d08129c1d3' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>150</th>
      <td><a title='b47e53cd-74dd-4580-80d0-260860064f4b' href='../records/b47e53cd-74dd-4580-80d0-260860064f4b' target='_blank'>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5eda02a9-36b6-4875-91c9-989e9e06c5ad' target='_blank'>link</a></td>
      <td>2022-05-05</td>
      <td>2024-07-23</td>
      <td><a title='b47e53cd-74dd-4580-80d0-260860064f4b' href='../records/b47e53cd-74dd-4580-80d0-260860064f4b' target='_blank'>3</a></td>
      <td><a title='b47e53cd-74dd-4580-80d0-260860064f4b' href='../records/b47e53cd-74dd-4580-80d0-260860064f4b' target='_blank'>12</a></td>
      <td></td>
    </tr>
    <tr>
      <th>149</th>
      <td><a title='4a9b4584-a5ef-4baf-9d4a-bacf8e6a5d1d' href='../records/4a9b4584-a5ef-4baf-9d4a-bacf8e6a5d1d' target='_blank'>Hakai Rivers Inlet Mooring Research</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_41770c7d-27ea-4593-ba55-040bdc5b99f0' target='_blank'>link</a></td>
      <td>2022-04-11</td>
      <td>2024-08-29</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>148</th>
      <td><a title='324c5ae3-b0ac-4302-b701-598ebbb25870' href='../records/324c5ae3-b0ac-4302-b701-598ebbb25870' target='_blank'>Stream Event Sampling - Calvert Island - 2015-2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_de9b2a6d-9ba0-4384-9adf-22abc0eb061f' target='_blank'>link</a></td>
      <td>2022-03-30</td>
      <td>2024-12-05</td>
      <td><a title='324c5ae3-b0ac-4302-b701-598ebbb25870' href='../records/324c5ae3-b0ac-4302-b701-598ebbb25870' target='_blank'>4</a></td>
      <td><a title='324c5ae3-b0ac-4302-b701-598ebbb25870' href='../records/324c5ae3-b0ac-4302-b701-598ebbb25870' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>147</th>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='../records/def2a409-2319-4e8c-a584-9a467f044ada' target='_blank'>Stream Event Sampling - Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c981d76-5fea-44af-904f-58b159838b0a' target='_blank'>link</a></td>
      <td>2022-03-30</td>
      <td>2024-07-24</td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='../records/def2a409-2319-4e8c-a584-9a467f044ada' target='_blank'>3</a></td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='../records/def2a409-2319-4e8c-a584-9a467f044ada' target='_blank'>2</a></td>
      <td><a title='def2a409-2319-4e8c-a584-9a467f044ada' href='../records/def2a409-2319-4e8c-a584-9a467f044ada' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>125</th>
      <td><a title='17680b42-fb77-4ab5-8645-23bb2f28c3e0' href='../records/17680b42-fb77-4ab5-8645-23bb2f28c3e0' target='_blank'>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b694a5c5-6a7e-4206-96aa-5b7754323345' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2025-04-23</td>
      <td><a title='17680b42-fb77-4ab5-8645-23bb2f28c3e0' href='../records/17680b42-fb77-4ab5-8645-23bb2f28c3e0' target='_blank'>3</a></td>
      <td><a title='17680b42-fb77-4ab5-8645-23bb2f28c3e0' href='../records/17680b42-fb77-4ab5-8645-23bb2f28c3e0' target='_blank'>8</a></td>
      <td></td>
    </tr>
    <tr>
      <th>127</th>
      <td><a title='18911dee-9ca0-408b-8999-28da3e3dde7a' href='../records/18911dee-9ca0-408b-8999-28da3e3dde7a' target='_blank'>LiDAR-based Ecosystem Classification for Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9e61819e-8385-41d2-a5c5-0e2f37c522ef' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='18911dee-9ca0-408b-8999-28da3e3dde7a' href='../records/18911dee-9ca0-408b-8999-28da3e3dde7a' target='_blank'>6</a></td>
      <td><a title='18911dee-9ca0-408b-8999-28da3e3dde7a' href='../records/18911dee-9ca0-408b-8999-28da3e3dde7a' target='_blank'>4</a></td>
      <td><a title='18911dee-9ca0-408b-8999-28da3e3dde7a' href='../records/18911dee-9ca0-408b-8999-28da3e3dde7a' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>136</th>
      <td><a title='1be9154a-1497-42eb-8821-b0d63000814c' href='../records/1be9154a-1497-42eb-8821-b0d63000814c' target='_blank'>Aquatic carbon flux data package for Oliver et al. 2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_184b2f81-d87f-4615-a026-15b87930d15c' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='1be9154a-1497-42eb-8821-b0d63000814c' href='../records/1be9154a-1497-42eb-8821-b0d63000814c' target='_blank'>5</a></td>
      <td></td>
      <td><a title='1be9154a-1497-42eb-8821-b0d63000814c' href='../records/1be9154a-1497-42eb-8821-b0d63000814c' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>145</th>
      <td><a title='2b33a5f0-1172-41e4-8330-b4c77d1665c7' href='../records/2b33a5f0-1172-41e4-8330-b4c77d1665c7' target='_blank'>High-resolution hydrometeorological data from seven small coastal watersheds, British Columbia, Canada, 2013-2019</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_395aa495-de81-4947-b1c5-2c98172a6def' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='2b33a5f0-1172-41e4-8330-b4c77d1665c7' href='../records/2b33a5f0-1172-41e4-8330-b4c77d1665c7' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>140</th>
      <td><a title='30560220-bc44-4020-b424-0abf617d1c00' href='../records/30560220-bc44-4020-b424-0abf617d1c00' target='_blank'>Watersheds of the northern Pacific coastal temperate rainforest margin</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_25674e9b-1d49-4270-b917-cfe6cdc30f95' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='30560220-bc44-4020-b424-0abf617d1c00' href='../records/30560220-bc44-4020-b424-0abf617d1c00' target='_blank'>5</a></td>
      <td><a title='30560220-bc44-4020-b424-0abf617d1c00' href='../records/30560220-bc44-4020-b424-0abf617d1c00' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>146</th>
      <td><a title='38fabad7-d7d2-405f-aa4c-592ef064895f' href='../records/38fabad7-d7d2-405f-aa4c-592ef064895f' target='_blank'>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_23bc8c35-2e4e-4382-9296-a52d5ea49889' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-12-05</td>
      <td><a title='38fabad7-d7d2-405f-aa4c-592ef064895f' href='../records/38fabad7-d7d2-405f-aa4c-592ef064895f' target='_blank'>4</a></td>
      <td><a title='38fabad7-d7d2-405f-aa4c-592ef064895f' href='../records/38fabad7-d7d2-405f-aa4c-592ef064895f' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>128</th>
      <td><a title='39f8b771-eb65-420f-b64e-742d94bbebf0' href='../records/39f8b771-eb65-420f-b64e-742d94bbebf0' target='_blank'>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cb13f042-bf47-4874-86e6-4728aa9380d4' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='39f8b771-eb65-420f-b64e-742d94bbebf0' href='../records/39f8b771-eb65-420f-b64e-742d94bbebf0' target='_blank'>3</a></td>
      <td><a title='39f8b771-eb65-420f-b64e-742d94bbebf0' href='../records/39f8b771-eb65-420f-b64e-742d94bbebf0' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>138</th>
      <td><a title='3c4cc294-1e9a-410e-81b0-0d9461e4b1c9' href='../records/3c4cc294-1e9a-410e-81b0-0d9461e4b1c9' target='_blank'>Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada. Version 1.0.</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6844547c-708e-437b-aef7-157b4d9d9bcb' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='3c4cc294-1e9a-410e-81b0-0d9461e4b1c9' href='../records/3c4cc294-1e9a-410e-81b0-0d9461e4b1c9' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>141</th>
      <td><a title='41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' href='../records/41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' target='_blank'>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_74f47ab6-a1ca-4aef-9115-cf2baaf87bef' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' href='../records/41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' target='_blank'>12</a></td>
      <td><a title='41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' href='../records/41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' target='_blank'>5</a></td>
      <td><a title='41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' href='../records/41e0fbeb-9e27-429c-84ea-7bb1be3f2a0d' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>130</th>
      <td><a title='49ec67e4-f7be-4658-b2b6-e4b57d9901df' href='../records/49ec67e4-f7be-4658-b2b6-e4b57d9901df' target='_blank'>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019 v2.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_97684a5c-9b70-4d8c-854b-9de895d3d71e' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='49ec67e4-f7be-4658-b2b6-e4b57d9901df' href='../records/49ec67e4-f7be-4658-b2b6-e4b57d9901df' target='_blank'>3</a></td>
      <td><a title='49ec67e4-f7be-4658-b2b6-e4b57d9901df' href='../records/49ec67e4-f7be-4658-b2b6-e4b57d9901df' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>135</th>
      <td><a title='4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' href='../records/4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' target='_blank'>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7de2d85e-202e-4e4a-953e-539f9d18e8c7' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-23</td>
      <td><a title='4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' href='../records/4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' target='_blank'>6</a></td>
      <td><a title='4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' href='../records/4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' target='_blank'>5</a></td>
      <td><a title='4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' href='../records/4f1e8eac-8390-44d8-93d6-9263fc1dfcf9' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>129</th>
      <td><a title='55e7c337-02e8-4200-8ea9-88241d978f96' href='../records/55e7c337-02e8-4200-8ea9-88241d978f96' target='_blank'>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9201118a-b0c4-470f-a76f-396bacc5e93e' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-23</td>
      <td><a title='55e7c337-02e8-4200-8ea9-88241d978f96' href='../records/55e7c337-02e8-4200-8ea9-88241d978f96' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>126</th>
      <td><a title='6f261f49-dd1b-4250-ac59-e88c3d1b2470' href='../records/6f261f49-dd1b-4250-ac59-e88c3d1b2470' target='_blank'>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a242acd4-e3c7-46e0-8f43-f428fb824018' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-12-05</td>
      <td><a title='6f261f49-dd1b-4250-ac59-e88c3d1b2470' href='../records/6f261f49-dd1b-4250-ac59-e88c3d1b2470' target='_blank'>4</a></td>
      <td><a title='6f261f49-dd1b-4250-ac59-e88c3d1b2470' href='../records/6f261f49-dd1b-4250-ac59-e88c3d1b2470' target='_blank'>5</a></td>
      <td><a title='6f261f49-dd1b-4250-ac59-e88c3d1b2470' href='../records/6f261f49-dd1b-4250-ac59-e88c3d1b2470' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>132</th>
      <td><a title='79e98468-af9a-4b52-aa9c-71129fa9cb03' href='../records/79e98468-af9a-4b52-aa9c-71129fa9cb03' target='_blank'>LiDAR Derived Watersheds with Metrics - Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d94882f8-c069-454d-a0ea-96c2b17d789d' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='79e98468-af9a-4b52-aa9c-71129fa9cb03' href='../records/79e98468-af9a-4b52-aa9c-71129fa9cb03' target='_blank'>1</a></td>
      <td><a title='79e98468-af9a-4b52-aa9c-71129fa9cb03' href='../records/79e98468-af9a-4b52-aa9c-71129fa9cb03' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>133</th>
      <td><a title='81436551-f025-47e1-bc7b-3f769bb5b0f4' href='../records/81436551-f025-47e1-bc7b-3f769bb5b0f4' target='_blank'>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f7538807-4d49-4ed8-ad36-836c0e71428a' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='81436551-f025-47e1-bc7b-3f769bb5b0f4' href='../records/81436551-f025-47e1-bc7b-3f769bb5b0f4' target='_blank'>3</a></td>
      <td><a title='81436551-f025-47e1-bc7b-3f769bb5b0f4' href='../records/81436551-f025-47e1-bc7b-3f769bb5b0f4' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>134</th>
      <td><a title='9a930f50-82e2-4d7c-9686-6b551b9a458e' href='../records/9a930f50-82e2-4d7c-9686-6b551b9a458e' target='_blank'>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_765d00bb-beec-486c-bd00-e27f972b7324' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='9a930f50-82e2-4d7c-9686-6b551b9a458e' href='../records/9a930f50-82e2-4d7c-9686-6b551b9a458e' target='_blank'>12</a></td>
      <td><a title='9a930f50-82e2-4d7c-9686-6b551b9a458e' href='../records/9a930f50-82e2-4d7c-9686-6b551b9a458e' target='_blank'>1</a></td>
      <td><a title='9a930f50-82e2-4d7c-9686-6b551b9a458e' href='../records/9a930f50-82e2-4d7c-9686-6b551b9a458e' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>142</th>
      <td><a title='a7a3cb32-66ff-4dcb-b05a-2c71511bd115' href='../records/a7a3cb32-66ff-4dcb-b05a-2c71511bd115' target='_blank'>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4c80a391-e74a-48cf-87ae-67632e485725' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='a7a3cb32-66ff-4dcb-b05a-2c71511bd115' href='../records/a7a3cb32-66ff-4dcb-b05a-2c71511bd115' target='_blank'>2</a></td>
      <td><a title='a7a3cb32-66ff-4dcb-b05a-2c71511bd115' href='../records/a7a3cb32-66ff-4dcb-b05a-2c71511bd115' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>131</th>
      <td><a title='b36a7c12-cb56-46b7-8241-9b52ac30c766' href='../records/b36a7c12-cb56-46b7-8241-9b52ac30c766' target='_blank'>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d05df775-4295-4b9f-b3b3-29fe891d9ed9' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='b36a7c12-cb56-46b7-8241-9b52ac30c766' href='../records/b36a7c12-cb56-46b7-8241-9b52ac30c766' target='_blank'>3</a></td>
      <td><a title='b36a7c12-cb56-46b7-8241-9b52ac30c766' href='../records/b36a7c12-cb56-46b7-8241-9b52ac30c766' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>143</th>
      <td><a title='bfad4541-a06a-489e-bd95-a5e7c65e0dc1' href='../records/bfad4541-a06a-489e-bd95-a5e7c65e0dc1' target='_blank'>Stream temperature time-series – Calvert Island – 2013 - 2019 Version 1.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0e446321-34f3-4d5a-8c7d-79c89eb76373' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='bfad4541-a06a-489e-bd95-a5e7c65e0dc1' href='../records/bfad4541-a06a-489e-bd95-a5e7c65e0dc1' target='_blank'>4</a></td>
      <td><a title='bfad4541-a06a-489e-bd95-a5e7c65e0dc1' href='../records/bfad4541-a06a-489e-bd95-a5e7c65e0dc1' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>139</th>
      <td><a title='c06cb551-351c-456f-8d0c-c8aab9aec162' href='../records/c06cb551-351c-456f-8d0c-c8aab9aec162' target='_blank'>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5b0b2db4-21d7-48b8-9616-255ba2267868' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='c06cb551-351c-456f-8d0c-c8aab9aec162' href='../records/c06cb551-351c-456f-8d0c-c8aab9aec162' target='_blank'>6</a></td>
      <td><a title='c06cb551-351c-456f-8d0c-c8aab9aec162' href='../records/c06cb551-351c-456f-8d0c-c8aab9aec162' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>137</th>
      <td><a title='d8754c99-a540-4085-8c66-d9447da5f6e9' href='../records/d8754c99-a540-4085-8c66-d9447da5f6e9' target='_blank'>Ecosystem Comparison Plots - Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_26443ab2-964f-4031-a53b-f132434573e8' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='d8754c99-a540-4085-8c66-d9447da5f6e9' href='../records/d8754c99-a540-4085-8c66-d9447da5f6e9' target='_blank'>5</a></td>
      <td><a title='d8754c99-a540-4085-8c66-d9447da5f6e9' href='../records/d8754c99-a540-4085-8c66-d9447da5f6e9' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>144</th>
      <td><a title='e1b86825-d43b-47e1-bf45-ab791f44772d' href='../records/e1b86825-d43b-47e1-bf45-ab791f44772d' target='_blank'>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0e4f324c-6498-4c89-9e19-f2f9f474a1df' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='e1b86825-d43b-47e1-bf45-ab791f44772d' href='../records/e1b86825-d43b-47e1-bf45-ab791f44772d' target='_blank'>3</a></td>
      <td><a title='e1b86825-d43b-47e1-bf45-ab791f44772d' href='../records/e1b86825-d43b-47e1-bf45-ab791f44772d' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>124</th>
      <td><a title='f0cae885-2124-41c1-8523-2c6725c40dd6' href='../records/f0cae885-2124-41c1-8523-2c6725c40dd6' target='_blank'>Bathymetry for Six Lakes on Calvert and Hecate Islands - 2016 - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b52d5602-f81d-4565-9574-e448e99bc997' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='f0cae885-2124-41c1-8523-2c6725c40dd6' href='../records/f0cae885-2124-41c1-8523-2c6725c40dd6' target='_blank'>2</a></td>
      <td><a title='f0cae885-2124-41c1-8523-2c6725c40dd6' href='../records/f0cae885-2124-41c1-8523-2c6725c40dd6' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>121</th>
      <td><a title='08d2c4ef-d157-480d-b3a9-6d0210c8d6ff' href='../records/08d2c4ef-d157-480d-b3a9-6d0210c8d6ff' target='_blank'>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b5207300-9f76-4f14-ae6f-a08ed6f5a213' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-07-23</td>
      <td><a title='08d2c4ef-d157-480d-b3a9-6d0210c8d6ff' href='../records/08d2c4ef-d157-480d-b3a9-6d0210c8d6ff' target='_blank'>4</a></td>
      <td><a title='08d2c4ef-d157-480d-b3a9-6d0210c8d6ff' href='../records/08d2c4ef-d157-480d-b3a9-6d0210c8d6ff' target='_blank'>1</a></td>
      <td><a title='08d2c4ef-d157-480d-b3a9-6d0210c8d6ff' href='../records/08d2c4ef-d157-480d-b3a9-6d0210c8d6ff' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>123</th>
      <td><a title='0efd0a21-637c-4cb5-9dc3-74daef3ef4f2' href='../records/0efd0a21-637c-4cb5-9dc3-74daef3ef4f2' target='_blank'>Koeye River stream temperature, stage, and conductivity time-series version 2</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dfa79d1b-25ce-44d0-94e9-39c807bd06b6' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-07-23</td>
      <td><a title='0efd0a21-637c-4cb5-9dc3-74daef3ef4f2' href='../records/0efd0a21-637c-4cb5-9dc3-74daef3ef4f2' target='_blank'>3</a></td>
      <td><a title='0efd0a21-637c-4cb5-9dc3-74daef3ef4f2' href='../records/0efd0a21-637c-4cb5-9dc3-74daef3ef4f2' target='_blank'>4</a></td>
      <td><a title='0efd0a21-637c-4cb5-9dc3-74daef3ef4f2' href='../records/0efd0a21-637c-4cb5-9dc3-74daef3ef4f2' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>118</th>
      <td><a title='372841fb-b091-414d-abc8-f1272473fa23' href='../records/372841fb-b091-414d-abc8-f1272473fa23' target='_blank'>Koeye River stream temperature, stage, and conductivity time-series version 1</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5cf59eac-2fb4-4ed2-8ffc-372030c9438e' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-07-23</td>
      <td><a title='372841fb-b091-414d-abc8-f1272473fa23' href='../records/372841fb-b091-414d-abc8-f1272473fa23' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>122</th>
      <td><a title='3a6e9472-1a85-48e5-8ac6-792945e03045' href='../records/3a6e9472-1a85-48e5-8ac6-792945e03045' target='_blank'>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ff68a559-3de8-4ad0-9367-79697d7cc897' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-12-05</td>
      <td><a title='3a6e9472-1a85-48e5-8ac6-792945e03045' href='../records/3a6e9472-1a85-48e5-8ac6-792945e03045' target='_blank'>6</a></td>
      <td><a title='3a6e9472-1a85-48e5-8ac6-792945e03045' href='../records/3a6e9472-1a85-48e5-8ac6-792945e03045' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>117</th>
      <td><a title='55826c6b-772a-45b4-a869-b97a4774e232' href='../records/55826c6b-772a-45b4-a869-b97a4774e232' target='_blank'>Precipitation time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ef59cc12-5031-4c65-b379-7ca03ad76d34' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-07-24</td>
      <td><a title='55826c6b-772a-45b4-a869-b97a4774e232' href='../records/55826c6b-772a-45b4-a869-b97a4774e232' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>119</th>
      <td><a title='67871f51-9f69-44f6-9206-747e4d2a1553' href='../records/67871f51-9f69-44f6-9206-747e4d2a1553' target='_blank'>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019 Version 4.1</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ed3c5cb4-e6b0-4c8a-808e-3583a9a6cfde' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-12-05</td>
      <td><a title='67871f51-9f69-44f6-9206-747e4d2a1553' href='../records/67871f51-9f69-44f6-9206-747e4d2a1553' target='_blank'>4</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>120</th>
      <td><a title='8c6f32be-1f60-4fcb-bf8b-a63cbac302f7' href='../records/8c6f32be-1f60-4fcb-bf8b-a63cbac302f7' target='_blank'>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5033d8e4-7b58-45b5-86e6-e98e14d1d6b9' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-12-05</td>
      <td><a title='8c6f32be-1f60-4fcb-bf8b-a63cbac302f7' href='../records/8c6f32be-1f60-4fcb-bf8b-a63cbac302f7' target='_blank'>4</a></td>
      <td><a title='8c6f32be-1f60-4fcb-bf8b-a63cbac302f7' href='../records/8c6f32be-1f60-4fcb-bf8b-a63cbac302f7' target='_blank'>6</a></td>
      <td><a title='8c6f32be-1f60-4fcb-bf8b-a63cbac302f7' href='../records/8c6f32be-1f60-4fcb-bf8b-a63cbac302f7' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>112</th>
      <td><a title='151f5813-8d7c-4042-8b7a-a878c814145e' href='../records/151f5813-8d7c-4042-8b7a-a878c814145e' target='_blank'>UAV Imagery - Coastal British Columbia - 2015</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8010e86f-5dd9-421d-8e22-668664191205' target='_blank'>link</a></td>
      <td>2022-03-15</td>
      <td>2024-07-23</td>
      <td><a title='151f5813-8d7c-4042-8b7a-a878c814145e' href='../records/151f5813-8d7c-4042-8b7a-a878c814145e' target='_blank'>1</a></td>
      <td><a title='151f5813-8d7c-4042-8b7a-a878c814145e' href='../records/151f5813-8d7c-4042-8b7a-a878c814145e' target='_blank'>10</a></td>
      <td><a title='151f5813-8d7c-4042-8b7a-a878c814145e' href='../records/151f5813-8d7c-4042-8b7a-a878c814145e' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>113</th>
      <td><a title='21ee0a17-9de0-49d7-9b04-cb9d5f557e9f' href='../records/21ee0a17-9de0-49d7-9b04-cb9d5f557e9f' target='_blank'>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9efdd14d-9fb9-4f0e-9414-d890b4e18055' target='_blank'>link</a></td>
      <td>2022-03-15</td>
      <td>2024-07-23</td>
      <td><a title='21ee0a17-9de0-49d7-9b04-cb9d5f557e9f' href='../records/21ee0a17-9de0-49d7-9b04-cb9d5f557e9f' target='_blank'>2</a></td>
      <td><a title='21ee0a17-9de0-49d7-9b04-cb9d5f557e9f' href='../records/21ee0a17-9de0-49d7-9b04-cb9d5f557e9f' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>115</th>
      <td><a title='5b4d3afa-e0bd-417f-ba08-437cc7e7f864' href='../records/5b4d3afa-e0bd-417f-ba08-437cc7e7f864' target='_blank'>UAV Imagery - 2016 - Coastal British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c688f31b-f82c-48f1-a707-5025c37a9b5c' target='_blank'>link</a></td>
      <td>2022-03-15</td>
      <td>2024-07-24</td>
      <td><a title='5b4d3afa-e0bd-417f-ba08-437cc7e7f864' href='../records/5b4d3afa-e0bd-417f-ba08-437cc7e7f864' target='_blank'>1</a></td>
      <td><a title='5b4d3afa-e0bd-417f-ba08-437cc7e7f864' href='../records/5b4d3afa-e0bd-417f-ba08-437cc7e7f864' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>114</th>
      <td><a title='75a7ec78-6f48-41f3-92c4-9b734206d6af' href='../records/75a7ec78-6f48-41f3-92c4-9b734206d6af' target='_blank'>Hakai RPAS (Drone) Operations and Methods</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_582909b1-c87d-4c5a-8594-5f44726f43a4' target='_blank'>link</a></td>
      <td>2022-03-15</td>
      <td>2024-07-23</td>
      <td><a title='75a7ec78-6f48-41f3-92c4-9b734206d6af' href='../records/75a7ec78-6f48-41f3-92c4-9b734206d6af' target='_blank'>1</a></td>
      <td><a title='75a7ec78-6f48-41f3-92c4-9b734206d6af' href='../records/75a7ec78-6f48-41f3-92c4-9b734206d6af' target='_blank'>8</a></td>
      <td><a title='75a7ec78-6f48-41f3-92c4-9b734206d6af' href='../records/75a7ec78-6f48-41f3-92c4-9b734206d6af' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>116</th>
      <td><a title='abd11340-660f-48b0-8bf0-9ccb142f513d' href='../records/abd11340-660f-48b0-8bf0-9ccb142f513d' target='_blank'>Bamfield Region UAV Imagery and Surface Model Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_40d86401-0e95-4ff3-b1c7-25e4e9138157' target='_blank'>link</a></td>
      <td>2022-03-15</td>
      <td>2024-07-23</td>
      <td><a title='abd11340-660f-48b0-8bf0-9ccb142f513d' href='../records/abd11340-660f-48b0-8bf0-9ccb142f513d' target='_blank'>2</a></td>
      <td><a title='abd11340-660f-48b0-8bf0-9ccb142f513d' href='../records/abd11340-660f-48b0-8bf0-9ccb142f513d' target='_blank'>7</a></td>
      <td></td>
    </tr>
    <tr>
      <th>111</th>
      <td><a title='fa913b04-1c29-4449-a78a-466f6b4fb110' href='../records/fa913b04-1c29-4449-a78a-466f6b4fb110' target='_blank'>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_06ddfa63-2611-46a5-8d63-c1b576e85bcb' target='_blank'>link</a></td>
      <td>2022-03-15</td>
      <td>2024-07-23</td>
      <td><a title='fa913b04-1c29-4449-a78a-466f6b4fb110' href='../records/fa913b04-1c29-4449-a78a-466f6b4fb110' target='_blank'>2</a></td>
      <td><a title='fa913b04-1c29-4449-a78a-466f6b4fb110' href='../records/fa913b04-1c29-4449-a78a-466f6b4fb110' target='_blank'>8</a></td>
      <td></td>
    </tr>
    <tr>
      <th>109</th>
      <td><a title='017ab2c4-70ea-484a-ae6c-7d441d2ba19d' href='../records/017ab2c4-70ea-484a-ae6c-7d441d2ba19d' target='_blank'>Eelgrass Extent 2014 - Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_51171738-7556-48f1-8757-658d99fa25dd' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='017ab2c4-70ea-484a-ae6c-7d441d2ba19d' href='../records/017ab2c4-70ea-484a-ae6c-7d441d2ba19d' target='_blank'>1</a></td>
      <td><a title='017ab2c4-70ea-484a-ae6c-7d441d2ba19d' href='../records/017ab2c4-70ea-484a-ae6c-7d441d2ba19d' target='_blank'>8</a></td>
      <td><a title='017ab2c4-70ea-484a-ae6c-7d441d2ba19d' href='../records/017ab2c4-70ea-484a-ae6c-7d441d2ba19d' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>105</th>
      <td><a title='0f19ac6e-dc86-445b-b2da-7b61a389222e' href='../records/0f19ac6e-dc86-445b-b2da-7b61a389222e' target='_blank'>Kelp Canopy Extent 2006 - NW Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4034f474-4d52-4a9e-9650-f3c6bd5011e0' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-23</td>
      <td><a title='0f19ac6e-dc86-445b-b2da-7b61a389222e' href='../records/0f19ac6e-dc86-445b-b2da-7b61a389222e' target='_blank'>1</a></td>
      <td><a title='0f19ac6e-dc86-445b-b2da-7b61a389222e' href='../records/0f19ac6e-dc86-445b-b2da-7b61a389222e' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>100</th>
      <td><a title='57770468-42a9-4654-bf7d-7672939ed002' href='../records/57770468-42a9-4654-bf7d-7672939ed002' target='_blank'>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4fac74c8-f58c-46b0-87dc-ab70ce756880' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-23</td>
      <td><a title='57770468-42a9-4654-bf7d-7672939ed002' href='../records/57770468-42a9-4654-bf7d-7672939ed002' target='_blank'>3</a></td>
      <td><a title='57770468-42a9-4654-bf7d-7672939ed002' href='../records/57770468-42a9-4654-bf7d-7672939ed002' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>107</th>
      <td><a title='688660f4-dfcc-49b9-866a-1cf2521c9e2d' href='../records/688660f4-dfcc-49b9-866a-1cf2521c9e2d' target='_blank'>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_244b5915-0ccf-4fab-9720-d2ac9394a27b' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='688660f4-dfcc-49b9-866a-1cf2521c9e2d' href='../records/688660f4-dfcc-49b9-866a-1cf2521c9e2d' target='_blank'>4</a></td>
      <td><a title='688660f4-dfcc-49b9-866a-1cf2521c9e2d' href='../records/688660f4-dfcc-49b9-866a-1cf2521c9e2d' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>104</th>
      <td><a title='69268e35-08ac-4e6d-b489-4bb72ac117b1' href='../records/69268e35-08ac-4e6d-b489-4bb72ac117b1' target='_blank'>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_14bf37c7-5eb6-4194-a992-c039fd7fb38b' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='69268e35-08ac-4e6d-b489-4bb72ac117b1' href='../records/69268e35-08ac-4e6d-b489-4bb72ac117b1' target='_blank'>3</a></td>
      <td><a title='69268e35-08ac-4e6d-b489-4bb72ac117b1' href='../records/69268e35-08ac-4e6d-b489-4bb72ac117b1' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>99</th>
      <td><a title='70f29525-f17b-4bc7-ae7f-d1e7205ba16c' href='../records/70f29525-f17b-4bc7-ae7f-d1e7205ba16c' target='_blank'>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7de69ca8-b3f3-4761-b441-dfc9e63b1fbc' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='70f29525-f17b-4bc7-ae7f-d1e7205ba16c' href='../records/70f29525-f17b-4bc7-ae7f-d1e7205ba16c' target='_blank'>3</a></td>
      <td><a title='70f29525-f17b-4bc7-ae7f-d1e7205ba16c' href='../records/70f29525-f17b-4bc7-ae7f-d1e7205ba16c' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>101</th>
      <td><a title='9001166d-e7eb-410f-92d6-17df0593cb2e' href='../records/9001166d-e7eb-410f-92d6-17df0593cb2e' target='_blank'>Geomorphology - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_abb8e676-dfcf-4eb5-bc39-4e7887fad163' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2025-01-03</td>
      <td><a title='9001166d-e7eb-410f-92d6-17df0593cb2e' href='../records/9001166d-e7eb-410f-92d6-17df0593cb2e' target='_blank'>1</a></td>
      <td><a title='9001166d-e7eb-410f-92d6-17df0593cb2e' href='../records/9001166d-e7eb-410f-92d6-17df0593cb2e' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>103</th>
      <td><a title='b3e5b67d-2425-4a4f-80b0-d1076df5492a' href='../records/b3e5b67d-2425-4a4f-80b0-d1076df5492a' target='_blank'>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7e0f0bbc-507a-4ca0-bafc-1cc3e56db028' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-23</td>
      <td><a title='b3e5b67d-2425-4a4f-80b0-d1076df5492a' href='../records/b3e5b67d-2425-4a4f-80b0-d1076df5492a' target='_blank'>2</a></td>
      <td><a title='b3e5b67d-2425-4a4f-80b0-d1076df5492a' href='../records/b3e5b67d-2425-4a4f-80b0-d1076df5492a' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>106</th>
      <td><a title='e1baeb3c-b764-434c-b0eb-7cb43fe5ef7a' href='../records/e1baeb3c-b764-434c-b0eb-7cb43fe5ef7a' target='_blank'>Trails - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ea4e84d5-c89c-4611-9594-449e468bd76c' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='e1baeb3c-b764-434c-b0eb-7cb43fe5ef7a' href='../records/e1baeb3c-b764-434c-b0eb-7cb43fe5ef7a' target='_blank'>1</a></td>
      <td><a title='e1baeb3c-b764-434c-b0eb-7cb43fe5ef7a' href='../records/e1baeb3c-b764-434c-b0eb-7cb43fe5ef7a' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>102</th>
      <td><a title='ee09830d-dd5e-41eb-8aee-0fe9cef5fe79' href='../records/ee09830d-dd5e-41eb-8aee-0fe9cef5fe79' target='_blank'>Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0c8692f0-a103-4681-9247-9bb69c6e222e' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='ee09830d-dd5e-41eb-8aee-0fe9cef5fe79' href='../records/ee09830d-dd5e-41eb-8aee-0fe9cef5fe79' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>110</th>
      <td><a title='f9ff815c-c57a-4750-8f80-25f5e145c8c0' href='../records/f9ff815c-c57a-4750-8f80-25f5e145c8c0' target='_blank'>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bef293d6-8721-4214-b8f5-03b5ffb28e1c' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='f9ff815c-c57a-4750-8f80-25f5e145c8c0' href='../records/f9ff815c-c57a-4750-8f80-25f5e145c8c0' target='_blank'>3</a></td>
      <td><a title='f9ff815c-c57a-4750-8f80-25f5e145c8c0' href='../records/f9ff815c-c57a-4750-8f80-25f5e145c8c0' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>108</th>
      <td><a title='fd691f42-76e9-4e18-80b1-9fb0d6960d95' href='../records/fd691f42-76e9-4e18-80b1-9fb0d6960d95' target='_blank'>Kelp Canopy Extent - 2014 - NW Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e66d7bf7-6ba1-44ed-8ee5-2561fca92164' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='fd691f42-76e9-4e18-80b1-9fb0d6960d95' href='../records/fd691f42-76e9-4e18-80b1-9fb0d6960d95' target='_blank'>1</a></td>
      <td><a title='fd691f42-76e9-4e18-80b1-9fb0d6960d95' href='../records/fd691f42-76e9-4e18-80b1-9fb0d6960d95' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>98</th>
      <td><a title='384dbb32-4bc8-4bd1-a741-6abbd332a50a' href='../records/384dbb32-4bc8-4bd1-a741-6abbd332a50a' target='_blank'>Big Bar Slide - 2020 - Airborne Coastal Observatory Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_82a543b1-686c-45c9-a03d-4f93e0ab8e8a' target='_blank'>link</a></td>
      <td>2022-03-08</td>
      <td>2024-07-23</td>
      <td><a title='384dbb32-4bc8-4bd1-a741-6abbd332a50a' href='../records/384dbb32-4bc8-4bd1-a741-6abbd332a50a' target='_blank'>1</a></td>
      <td><a title='384dbb32-4bc8-4bd1-a741-6abbd332a50a' href='../records/384dbb32-4bc8-4bd1-a741-6abbd332a50a' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>97</th>
      <td><a title='0ca539a4-217f-43ff-947e-5679dd8d64dd' href='../records/0ca539a4-217f-43ff-947e-5679dd8d64dd' target='_blank'>Hakai Topographic Basemap</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c5bf06e7-29f9-404a-a454-36a5d67b2e69' target='_blank'>link</a></td>
      <td>2022-03-03</td>
      <td>2024-07-23</td>
      <td><a title='0ca539a4-217f-43ff-947e-5679dd8d64dd' href='../records/0ca539a4-217f-43ff-947e-5679dd8d64dd' target='_blank'>1</a></td>
      <td><a title='0ca539a4-217f-43ff-947e-5679dd8d64dd' href='../records/0ca539a4-217f-43ff-947e-5679dd8d64dd' target='_blank'>7</a></td>
      <td></td>
    </tr>
    <tr>
      <th>95</th>
      <td><a title='362130df-bc83-48b7-80f9-ad11ad6a91c9' href='../records/362130df-bc83-48b7-80f9-ad11ad6a91c9' target='_blank'>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_82a3f5ec-95c5-4aeb-a0c0-bf168c985676' target='_blank'>link</a></td>
      <td>2022-03-03</td>
      <td>2024-07-23</td>
      <td><a title='362130df-bc83-48b7-80f9-ad11ad6a91c9' href='../records/362130df-bc83-48b7-80f9-ad11ad6a91c9' target='_blank'>3</a></td>
      <td><a title='362130df-bc83-48b7-80f9-ad11ad6a91c9' href='../records/362130df-bc83-48b7-80f9-ad11ad6a91c9' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>96</th>
      <td><a title='44754736-c8be-49b1-8806-a0ca4a78255a' href='../records/44754736-c8be-49b1-8806-a0ca4a78255a' target='_blank'>Hyperspectral Imagery - Calvert Island - 2012</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4be1cc5e-8846-4fba-bd94-16ca933faab8' target='_blank'>link</a></td>
      <td>2022-03-03</td>
      <td>2024-07-23</td>
      <td><a title='44754736-c8be-49b1-8806-a0ca4a78255a' href='../records/44754736-c8be-49b1-8806-a0ca4a78255a' target='_blank'>5</a></td>
      <td><a title='44754736-c8be-49b1-8806-a0ca4a78255a' href='../records/44754736-c8be-49b1-8806-a0ca4a78255a' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>92</th>
      <td><a title='7ed2118f-ecaa-41e4-aa81-911ffa47bf34' href='../records/7ed2118f-ecaa-41e4-aa81-911ffa47bf34' target='_blank'>Field Station Structures - Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1b517e6f-4f0a-4577-b7c2-c37f95d5b413' target='_blank'>link</a></td>
      <td>2022-03-03</td>
      <td>2024-07-23</td>
      <td><a title='7ed2118f-ecaa-41e4-aa81-911ffa47bf34' href='../records/7ed2118f-ecaa-41e4-aa81-911ffa47bf34' target='_blank'>1</a></td>
      <td><a title='7ed2118f-ecaa-41e4-aa81-911ffa47bf34' href='../records/7ed2118f-ecaa-41e4-aa81-911ffa47bf34' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>93</th>
      <td><a title='b307d1bd-61be-4059-b4af-db36555dbd77' href='../records/b307d1bd-61be-4059-b4af-db36555dbd77' target='_blank'>Summer sea wrack spatial data; Central Coast, British Columbia, Canada (2015 - 2017)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7381aff7-a4fe-4309-81f1-8eebe183b4d8' target='_blank'>link</a></td>
      <td>2022-03-03</td>
      <td>2024-07-24</td>
      <td><a title='b307d1bd-61be-4059-b4af-db36555dbd77' href='../records/b307d1bd-61be-4059-b4af-db36555dbd77' target='_blank'>4</a></td>
      <td><a title='b307d1bd-61be-4059-b4af-db36555dbd77' href='../records/b307d1bd-61be-4059-b4af-db36555dbd77' target='_blank'>1</a></td>
      <td><a title='b307d1bd-61be-4059-b4af-db36555dbd77' href='../records/b307d1bd-61be-4059-b4af-db36555dbd77' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>91</th>
      <td><a title='e1c64faf-88ac-4d28-8144-fad156971b4e' href='../records/e1c64faf-88ac-4d28-8144-fad156971b4e' target='_blank'>Bathymetric Survey - Northwest Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e2d3d616-9ee2-451f-8584-14801b4c6fd0' target='_blank'>link</a></td>
      <td>2022-03-03</td>
      <td>2024-07-23</td>
      <td><a title='e1c64faf-88ac-4d28-8144-fad156971b4e' href='../records/e1c64faf-88ac-4d28-8144-fad156971b4e' target='_blank'>1</a></td>
      <td><a title='e1c64faf-88ac-4d28-8144-fad156971b4e' href='../records/e1c64faf-88ac-4d28-8144-fad156971b4e' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>94</th>
      <td><a title='fd4f6cd0-c6aa-4061-8caa-0ccade085615' href='../records/fd4f6cd0-c6aa-4061-8caa-0ccade085615' target='_blank'>20m Digital Elevation Model - Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fe20660b-ef3d-4f6b-90f8-5936d9c96cb5' target='_blank'>link</a></td>
      <td>2022-03-03</td>
      <td>2024-07-23</td>
      <td><a title='fd4f6cd0-c6aa-4061-8caa-0ccade085615' href='../records/fd4f6cd0-c6aa-4061-8caa-0ccade085615' target='_blank'>1</a></td>
      <td><a title='fd4f6cd0-c6aa-4061-8caa-0ccade085615' href='../records/fd4f6cd0-c6aa-4061-8caa-0ccade085615' target='_blank'>5</a></td>
      <td><a title='fd4f6cd0-c6aa-4061-8caa-0ccade085615' href='../records/fd4f6cd0-c6aa-4061-8caa-0ccade085615' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>90</th>
      <td><a title='1ad9809b-16a0-44f4-abc8-a1474b728c15' href='../records/1ad9809b-16a0-44f4-abc8-a1474b728c15' target='_blank'>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5e4f925a-9cf2-4e33-ae22-75c5b326ce6c' target='_blank'>link</a></td>
      <td>2022-03-02</td>
      <td>2024-07-23</td>
      <td><a title='1ad9809b-16a0-44f4-abc8-a1474b728c15' href='../records/1ad9809b-16a0-44f4-abc8-a1474b728c15' target='_blank'>3</a></td>
      <td><a title='1ad9809b-16a0-44f4-abc8-a1474b728c15' href='../records/1ad9809b-16a0-44f4-abc8-a1474b728c15' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>87</th>
      <td><a title='2fe3bd2a-973e-48db-a599-6d44ca1ef0ad' href='../records/2fe3bd2a-973e-48db-a599-6d44ca1ef0ad' target='_blank'>Owikeno Lake Bathymetric Survey</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_27ba6c11-2421-4e85-bc11-1c1083514ed9' target='_blank'>link</a></td>
      <td>2022-03-02</td>
      <td>2025-01-08</td>
      <td><a title='2fe3bd2a-973e-48db-a599-6d44ca1ef0ad' href='../records/2fe3bd2a-973e-48db-a599-6d44ca1ef0ad' target='_blank'>4</a></td>
      <td></td>
      <td><a title='2fe3bd2a-973e-48db-a599-6d44ca1ef0ad' href='../records/2fe3bd2a-973e-48db-a599-6d44ca1ef0ad' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>86</th>
      <td><a title='52048599-9a0c-4d33-861f-26eaedc86bd5' href='../records/52048599-9a0c-4d33-861f-26eaedc86bd5' target='_blank'>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94cdfcba-bbd4-4053-8976-75de69460c14' target='_blank'>link</a></td>
      <td>2022-03-02</td>
      <td>2024-07-23</td>
      <td><a title='52048599-9a0c-4d33-861f-26eaedc86bd5' href='../records/52048599-9a0c-4d33-861f-26eaedc86bd5' target='_blank'>3</a></td>
      <td><a title='52048599-9a0c-4d33-861f-26eaedc86bd5' href='../records/52048599-9a0c-4d33-861f-26eaedc86bd5' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>88</th>
      <td><a title='571ef4fa-eda3-4e67-baae-2e9b5e598f56' href='../records/571ef4fa-eda3-4e67-baae-2e9b5e598f56' target='_blank'>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2a92ca16-f5c6-4362-acea-6bb5117b8d65' target='_blank'>link</a></td>
      <td>2022-03-02</td>
      <td>2024-07-23</td>
      <td><a title='571ef4fa-eda3-4e67-baae-2e9b5e598f56' href='../records/571ef4fa-eda3-4e67-baae-2e9b5e598f56' target='_blank'>3</a></td>
      <td><a title='571ef4fa-eda3-4e67-baae-2e9b5e598f56' href='../records/571ef4fa-eda3-4e67-baae-2e9b5e598f56' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>85</th>
      <td><a title='6b93216b-4bbe-4204-a2c3-551a667d00fd' href='../records/6b93216b-4bbe-4204-a2c3-551a667d00fd' target='_blank'>Geology - Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6ae1b131-d903-44ca-92a9-64cf6487ddc2' target='_blank'>link</a></td>
      <td>2022-03-02</td>
      <td>2024-07-23</td>
      <td><a title='6b93216b-4bbe-4204-a2c3-551a667d00fd' href='../records/6b93216b-4bbe-4204-a2c3-551a667d00fd' target='_blank'>1</a></td>
      <td><a title='6b93216b-4bbe-4204-a2c3-551a667d00fd' href='../records/6b93216b-4bbe-4204-a2c3-551a667d00fd' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>89</th>
      <td><a title='c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' href='../records/c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' target='_blank'>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5c13b300-e172-4010-a6d8-7586b68a3a96' target='_blank'>link</a></td>
      <td>2022-03-02</td>
      <td>2024-07-23</td>
      <td><a title='c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' href='../records/c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' target='_blank'>3</a></td>
      <td><a title='c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' href='../records/c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' target='_blank'>2</a></td>
      <td><a title='c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' href='../records/c8f6fd7c-7c63-440b-b69a-bd0df3abfd26' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>82</th>
      <td><a title='281d7444-efa6-4b18-ac0a-55c8f8b484be' href='../records/281d7444-efa6-4b18-ac0a-55c8f8b484be' target='_blank'>Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c3958106-fc49-44bd-8227-bfc3e8bcb58c' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='281d7444-efa6-4b18-ac0a-55c8f8b484be' href='../records/281d7444-efa6-4b18-ac0a-55c8f8b484be' target='_blank'>2</a></td>
      <td><a title='281d7444-efa6-4b18-ac0a-55c8f8b484be' href='../records/281d7444-efa6-4b18-ac0a-55c8f8b484be' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>83</th>
      <td><a title='5b78f1a7-6adb-4610-9ebe-019c3da65ae8' href='../records/5b78f1a7-6adb-4610-9ebe-019c3da65ae8' target='_blank'>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bb59cb9e-887a-40a3-b41a-f4a5b2263ce6' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='5b78f1a7-6adb-4610-9ebe-019c3da65ae8' href='../records/5b78f1a7-6adb-4610-9ebe-019c3da65ae8' target='_blank'>2</a></td>
      <td><a title='5b78f1a7-6adb-4610-9ebe-019c3da65ae8' href='../records/5b78f1a7-6adb-4610-9ebe-019c3da65ae8' target='_blank'>9</a></td>
      <td><a title='5b78f1a7-6adb-4610-9ebe-019c3da65ae8' href='../records/5b78f1a7-6adb-4610-9ebe-019c3da65ae8' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>77</th>
      <td><a title='727b8863-91cc-4765-b0c0-80cb74b11182' href='../records/727b8863-91cc-4765-b0c0-80cb74b11182' target='_blank'>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a60a0468-3f56-4f22-abd4-5268fcfb9744' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='727b8863-91cc-4765-b0c0-80cb74b11182' href='../records/727b8863-91cc-4765-b0c0-80cb74b11182' target='_blank'>2</a></td>
      <td><a title='727b8863-91cc-4765-b0c0-80cb74b11182' href='../records/727b8863-91cc-4765-b0c0-80cb74b11182' target='_blank'>9</a></td>
      <td><a title='727b8863-91cc-4765-b0c0-80cb74b11182' href='../records/727b8863-91cc-4765-b0c0-80cb74b11182' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>84</th>
      <td><a title='826d8228-baab-4191-82de-44701cd93806' href='../records/826d8228-baab-4191-82de-44701cd93806' target='_blank'>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e0c768fc-5c37-455f-b2a3-604f766f4148' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='826d8228-baab-4191-82de-44701cd93806' href='../records/826d8228-baab-4191-82de-44701cd93806' target='_blank'>2</a></td>
      <td><a title='826d8228-baab-4191-82de-44701cd93806' href='../records/826d8228-baab-4191-82de-44701cd93806' target='_blank'>8</a></td>
      <td><a title='826d8228-baab-4191-82de-44701cd93806' href='../records/826d8228-baab-4191-82de-44701cd93806' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>78</th>
      <td><a title='8a71bb9f-e419-42aa-9ed7-f891631314a5' href='../records/8a71bb9f-e419-42aa-9ed7-f891631314a5' target='_blank'>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0ebfdd89-61d6-453c-870a-83167617b26a' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='8a71bb9f-e419-42aa-9ed7-f891631314a5' href='../records/8a71bb9f-e419-42aa-9ed7-f891631314a5' target='_blank'>2</a></td>
      <td><a title='8a71bb9f-e419-42aa-9ed7-f891631314a5' href='../records/8a71bb9f-e419-42aa-9ed7-f891631314a5' target='_blank'>8</a></td>
      <td><a title='8a71bb9f-e419-42aa-9ed7-f891631314a5' href='../records/8a71bb9f-e419-42aa-9ed7-f891631314a5' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>79</th>
      <td><a title='8d3f619f-e3e5-44a7-8b35-7e4ed1e6af31' href='../records/8d3f619f-e3e5-44a7-8b35-7e4ed1e6af31' target='_blank'>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d2e83e40-9e95-4a47-a899-b37c744be3ab' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='8d3f619f-e3e5-44a7-8b35-7e4ed1e6af31' href='../records/8d3f619f-e3e5-44a7-8b35-7e4ed1e6af31' target='_blank'>2</a></td>
      <td><a title='8d3f619f-e3e5-44a7-8b35-7e4ed1e6af31' href='../records/8d3f619f-e3e5-44a7-8b35-7e4ed1e6af31' target='_blank'>4</a></td>
      <td><a title='8d3f619f-e3e5-44a7-8b35-7e4ed1e6af31' href='../records/8d3f619f-e3e5-44a7-8b35-7e4ed1e6af31' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>80</th>
      <td><a title='92e1c9df-0419-4d91-93c2-b9c85f4ce74e' href='../records/92e1c9df-0419-4d91-93c2-b9c85f4ce74e' target='_blank'>Gitanyow Archaeology, Cranberry Junction - 2020 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0f524f76-a88b-4e0a-9c3c-ee83114c3679' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='92e1c9df-0419-4d91-93c2-b9c85f4ce74e' href='../records/92e1c9df-0419-4d91-93c2-b9c85f4ce74e' target='_blank'>2</a></td>
      <td><a title='92e1c9df-0419-4d91-93c2-b9c85f4ce74e' href='../records/92e1c9df-0419-4d91-93c2-b9c85f4ce74e' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>81</th>
      <td><a title='a8d40002-d393-40da-882c-73c0ad8ca7e6' href='../records/a8d40002-d393-40da-882c-73c0ad8ca7e6' target='_blank'>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c3eff62f-bcee-4faa-a7e1-7b9380d94e74' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='a8d40002-d393-40da-882c-73c0ad8ca7e6' href='../records/a8d40002-d393-40da-882c-73c0ad8ca7e6' target='_blank'>2</a></td>
      <td><a title='a8d40002-d393-40da-882c-73c0ad8ca7e6' href='../records/a8d40002-d393-40da-882c-73c0ad8ca7e6' target='_blank'>3</a></td>
      <td><a title='a8d40002-d393-40da-882c-73c0ad8ca7e6' href='../records/a8d40002-d393-40da-882c-73c0ad8ca7e6' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>75</th>
      <td><a title='b5ee0615-c04d-462e-8199-f611bc6370ce' href='../records/b5ee0615-c04d-462e-8199-f611bc6370ce' target='_blank'>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_95bee6a0-ae38-4427-b5b2-5cc5835df70d' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='b5ee0615-c04d-462e-8199-f611bc6370ce' href='../records/b5ee0615-c04d-462e-8199-f611bc6370ce' target='_blank'>2</a></td>
      <td><a title='b5ee0615-c04d-462e-8199-f611bc6370ce' href='../records/b5ee0615-c04d-462e-8199-f611bc6370ce' target='_blank'>8</a></td>
      <td><a title='b5ee0615-c04d-462e-8199-f611bc6370ce' href='../records/b5ee0615-c04d-462e-8199-f611bc6370ce' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>76</th>
      <td><a title='e3205958-52b4-4c42-a02d-34d713a20a53' href='../records/e3205958-52b4-4c42-a02d-34d713a20a53' target='_blank'>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_62de21ed-90fb-422a-9c55-29c513a00f95' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='e3205958-52b4-4c42-a02d-34d713a20a53' href='../records/e3205958-52b4-4c42-a02d-34d713a20a53' target='_blank'>2</a></td>
      <td><a title='e3205958-52b4-4c42-a02d-34d713a20a53' href='../records/e3205958-52b4-4c42-a02d-34d713a20a53' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>74</th>
      <td><a title='6338c2fa-3d4d-42dc-9c91-31761365e11e' href='../records/6338c2fa-3d4d-42dc-9c91-31761365e11e' target='_blank'>High-resolution record of 8-m seawater CO2 content entering Fanny Bay Oysters in Baynes Sound, British Columbia, Canada from March 2017 to November 2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_77a256cd-baf7-434e-9f62-53ba809e48cb' target='_blank'>link</a></td>
      <td>2022-02-04</td>
      <td>2024-07-23</td>
      <td><a title='6338c2fa-3d4d-42dc-9c91-31761365e11e' href='../records/6338c2fa-3d4d-42dc-9c91-31761365e11e' target='_blank'>3</a></td>
      <td></td>
      <td><a title='6338c2fa-3d4d-42dc-9c91-31761365e11e' href='../records/6338c2fa-3d4d-42dc-9c91-31761365e11e' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>72</th>
      <td><a title='7f23d45b-b777-491c-b602-def5402d3d83' href='../records/7f23d45b-b777-491c-b602-def5402d3d83' target='_blank'>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a0263680-f0d5-46d5-85ea-483fa58c74b6' target='_blank'>link</a></td>
      <td>2022-02-04</td>
      <td>2024-07-23</td>
      <td><a title='7f23d45b-b777-491c-b602-def5402d3d83' href='../records/7f23d45b-b777-491c-b602-def5402d3d83' target='_blank'>3</a></td>
      <td><a title='7f23d45b-b777-491c-b602-def5402d3d83' href='../records/7f23d45b-b777-491c-b602-def5402d3d83' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>73</th>
      <td><a title='d3ed88cb-4f38-4c2e-a966-3dd49c9cafec' href='../records/d3ed88cb-4f38-4c2e-a966-3dd49c9cafec' target='_blank'>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_804b5b42-5550-4620-b789-7c2fe9572c03' target='_blank'>link</a></td>
      <td>2022-02-04</td>
      <td>2024-07-23</td>
      <td><a title='d3ed88cb-4f38-4c2e-a966-3dd49c9cafec' href='../records/d3ed88cb-4f38-4c2e-a966-3dd49c9cafec' target='_blank'>7</a></td>
      <td><a title='d3ed88cb-4f38-4c2e-a966-3dd49c9cafec' href='../records/d3ed88cb-4f38-4c2e-a966-3dd49c9cafec' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>70</th>
      <td><a title='26186b9d-a292-43c4-aec6-e928aa52b002' href='../records/26186b9d-a292-43c4-aec6-e928aa52b002' target='_blank'>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_63765cc6-5730-4a28-9d96-3de38066312f' target='_blank'>link</a></td>
      <td>2022-02-03</td>
      <td>2024-07-23</td>
      <td><a title='26186b9d-a292-43c4-aec6-e928aa52b002' href='../records/26186b9d-a292-43c4-aec6-e928aa52b002' target='_blank'>3</a></td>
      <td><a title='26186b9d-a292-43c4-aec6-e928aa52b002' href='../records/26186b9d-a292-43c4-aec6-e928aa52b002' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>69</th>
      <td><a title='45983472-7627-4227-b312-079c2aeda7ef' href='../records/45983472-7627-4227-b312-079c2aeda7ef' target='_blank'>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a72c43e2-5b4d-4d56-89d4-464b4c513710' target='_blank'>link</a></td>
      <td>2022-02-03</td>
      <td>2024-07-24</td>
      <td><a title='45983472-7627-4227-b312-079c2aeda7ef' href='../records/45983472-7627-4227-b312-079c2aeda7ef' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>71</th>
      <td><a title='f31f38bf-16bc-4136-8982-a2df5fefb3a0' href='../records/f31f38bf-16bc-4136-8982-a2df5fefb3a0' target='_blank'>High-resolution record of surface seawater CO2 content from November 2017 to June 2018 collected in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7c47472a-b16c-446c-89d5-eefa23e07922' target='_blank'>link</a></td>
      <td>2022-02-03</td>
      <td>2024-07-24</td>
      <td><a title='f31f38bf-16bc-4136-8982-a2df5fefb3a0' href='../records/f31f38bf-16bc-4136-8982-a2df5fefb3a0' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>66</th>
      <td><a title='1a9a5aae-41ee-4272-a52e-6c37abedfbff' href='../records/1a9a5aae-41ee-4272-a52e-6c37abedfbff' target='_blank'>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4b5c0c20-2115-4986-bf56-237e360240bd' target='_blank'>link</a></td>
      <td>2022-02-02</td>
      <td>2025-01-30</td>
      <td><a title='1a9a5aae-41ee-4272-a52e-6c37abedfbff' href='../records/1a9a5aae-41ee-4272-a52e-6c37abedfbff' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>67</th>
      <td><a title='4becb6c2-ebdb-43f2-8f15-dee50aaa19d8' href='../records/4becb6c2-ebdb-43f2-8f15-dee50aaa19d8' target='_blank'>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fd5ada9a-5719-4ca1-89d2-17adb48d1493' target='_blank'>link</a></td>
      <td>2022-02-02</td>
      <td>2024-11-25</td>
      <td><a title='4becb6c2-ebdb-43f2-8f15-dee50aaa19d8' href='../records/4becb6c2-ebdb-43f2-8f15-dee50aaa19d8' target='_blank'>5</a></td>
      <td><a title='4becb6c2-ebdb-43f2-8f15-dee50aaa19d8' href='../records/4becb6c2-ebdb-43f2-8f15-dee50aaa19d8' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>68</th>
      <td><a title='dd30b32a-2099-4909-838d-6ade9804381a' href='../records/dd30b32a-2099-4909-838d-6ade9804381a' target='_blank'>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a0ca5d26-b457-4726-97d4-ed0c8dd6cd99' target='_blank'>link</a></td>
      <td>2022-02-02</td>
      <td>2024-07-24</td>
      <td><a title='dd30b32a-2099-4909-838d-6ade9804381a' href='../records/dd30b32a-2099-4909-838d-6ade9804381a' target='_blank'>6</a></td>
      <td><a title='dd30b32a-2099-4909-838d-6ade9804381a' href='../records/dd30b32a-2099-4909-838d-6ade9804381a' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>64</th>
      <td><a title='15f1d4a2-c82a-450c-a8f7-badb34b9c0dc' href='../records/15f1d4a2-c82a-450c-a8f7-badb34b9c0dc' target='_blank'>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e09522d7-24f7-4c0e-afac-6cafd22a54f6' target='_blank'>link</a></td>
      <td>2022-02-01</td>
      <td>2024-07-23</td>
      <td><a title='15f1d4a2-c82a-450c-a8f7-badb34b9c0dc' href='../records/15f1d4a2-c82a-450c-a8f7-badb34b9c0dc' target='_blank'>3</a></td>
      <td><a title='15f1d4a2-c82a-450c-a8f7-badb34b9c0dc' href='../records/15f1d4a2-c82a-450c-a8f7-badb34b9c0dc' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>63</th>
      <td><a title='87db0ae4-add1-4f71-a5cb-131de8783013' href='../records/87db0ae4-add1-4f71-a5cb-131de8783013' target='_blank'>Provisional Real-Time Hakai Seafloor Observatory in Hyacinthe Bay, Quadra Island, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_41b0137d-6ac0-407d-a550-dd375475b2b0' target='_blank'>link</a></td>
      <td>2022-02-01</td>
      <td>2024-07-23</td>
      <td><a title='87db0ae4-add1-4f71-a5cb-131de8783013' href='../records/87db0ae4-add1-4f71-a5cb-131de8783013' target='_blank'>2</a></td>
      <td><a title='87db0ae4-add1-4f71-a5cb-131de8783013' href='../records/87db0ae4-add1-4f71-a5cb-131de8783013' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>65</th>
      <td><a title='9c581481-f2ee-4353-b1ab-c5bf242945fe' href='../records/9c581481-f2ee-4353-b1ab-c5bf242945fe' target='_blank'>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_87a845e3-e71a-43cc-a75f-ec6a3b812a0e' target='_blank'>link</a></td>
      <td>2022-02-01</td>
      <td>2024-07-23</td>
      <td><a title='9c581481-f2ee-4353-b1ab-c5bf242945fe' href='../records/9c581481-f2ee-4353-b1ab-c5bf242945fe' target='_blank'>4</a></td>
      <td><a title='9c581481-f2ee-4353-b1ab-c5bf242945fe' href='../records/9c581481-f2ee-4353-b1ab-c5bf242945fe' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>55</th>
      <td><a title='1bba6c8a-b99c-4fbd-8eae-7c8b771a841d' href='../records/1bba6c8a-b99c-4fbd-8eae-7c8b771a841d' target='_blank'>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_17396d02-88ff-4240-837b-5d3a45e70ea0' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-23</td>
      <td><a title='1bba6c8a-b99c-4fbd-8eae-7c8b771a841d' href='../records/1bba6c8a-b99c-4fbd-8eae-7c8b771a841d' target='_blank'>3</a></td>
      <td><a title='1bba6c8a-b99c-4fbd-8eae-7c8b771a841d' href='../records/1bba6c8a-b99c-4fbd-8eae-7c8b771a841d' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>60</th>
      <td><a title='1f798a06-9c01-4025-93c6-b1a9f8ce6832' href='../records/1f798a06-9c01-4025-93c6-b1a9f8ce6832' target='_blank'>High-resolution record of surface water pH at Sentry Shoal in the Northern Strait of Georgia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d200376b-7dd8-4778-b3f5-379243bf93b8' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='1f798a06-9c01-4025-93c6-b1a9f8ce6832' href='../records/1f798a06-9c01-4025-93c6-b1a9f8ce6832' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>53</th>
      <td><a title='24c3b914-33d7-4267-a1aa-8ce7523b296d' href='../records/24c3b914-33d7-4267-a1aa-8ce7523b296d' target='_blank'>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2019</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dc50a22a-44c0-478c-aa19-a46343bc764a' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-08-02</td>
      <td><a title='24c3b914-33d7-4267-a1aa-8ce7523b296d' href='../records/24c3b914-33d7-4267-a1aa-8ce7523b296d' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>56</th>
      <td><a title='2abe9ff4-76de-4221-9ca6-ec3403a56efa' href='../records/2abe9ff4-76de-4221-9ca6-ec3403a56efa' target='_blank'>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6d779012-e236-4a03-b11a-a5915f0f4342' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-23</td>
      <td><a title='2abe9ff4-76de-4221-9ca6-ec3403a56efa' href='../records/2abe9ff4-76de-4221-9ca6-ec3403a56efa' target='_blank'>3</a></td>
      <td><a title='2abe9ff4-76de-4221-9ca6-ec3403a56efa' href='../records/2abe9ff4-76de-4221-9ca6-ec3403a56efa' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>54</th>
      <td><a title='6083b388-4d24-4ac3-9464-dfea94468203' href='../records/6083b388-4d24-4ac3-9464-dfea94468203' target='_blank'>Surface water CO2 parameters collected by Alaskan citizens around the northern Gulf of Alaska from April 2015 to August 2017. Version 1.0.</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6c0697e9-7776-4d36-8219-b21ce72fbcc9' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='6083b388-4d24-4ac3-9464-dfea94468203' href='../records/6083b388-4d24-4ac3-9464-dfea94468203' target='_blank'>4</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>49</th>
      <td><a title='7149f4c2-1e3d-4df7-8e37-fab3d36eba58' href='../records/7149f4c2-1e3d-4df7-8e37-fab3d36eba58' target='_blank'>Water column CO2 system measurements from Hakai Oceanographic station QU39 from January 2016 to December 2017 in northern Salish Sea, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_48c8f830-f281-4ca1-9a81-ea690e70cb7a' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-23</td>
      <td><a title='7149f4c2-1e3d-4df7-8e37-fab3d36eba58' href='../records/7149f4c2-1e3d-4df7-8e37-fab3d36eba58' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>50</th>
      <td><a title='876027b6-cf37-4d49-8c3d-22d40b5f5b0b' href='../records/876027b6-cf37-4d49-8c3d-22d40b5f5b0b' target='_blank'>Water column carbonate system measurements from the Pacific Salmon Foundation Citizen Science Program stations from July 2016 to October 2017 in the northern Salish Sea, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3d7d93d0-73be-4c1b-af09-307e60a3576d' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='876027b6-cf37-4d49-8c3d-22d40b5f5b0b' href='../records/876027b6-cf37-4d49-8c3d-22d40b5f5b0b' target='_blank'>3</a></td>
      <td><a title='876027b6-cf37-4d49-8c3d-22d40b5f5b0b' href='../records/876027b6-cf37-4d49-8c3d-22d40b5f5b0b' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>59</th>
      <td><a title='9b7adebb-5027-486a-8ed1-f97b5353a480' href='../records/9b7adebb-5027-486a-8ed1-f97b5353a480' target='_blank'>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_6ebe47c3-6d59-4cb2-a7ba-111698445d8d' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-23</td>
      <td><a title='9b7adebb-5027-486a-8ed1-f97b5353a480' href='../records/9b7adebb-5027-486a-8ed1-f97b5353a480' target='_blank'>5</a></td>
      <td><a title='9b7adebb-5027-486a-8ed1-f97b5353a480' href='../records/9b7adebb-5027-486a-8ed1-f97b5353a480' target='_blank'>5</a></td>
      <td><a title='9b7adebb-5027-486a-8ed1-f97b5353a480' href='../records/9b7adebb-5027-486a-8ed1-f97b5353a480' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>48</th>
      <td><a title='9e4a38d6-eb29-44a8-b495-c56ce74a227c' href='../records/9e4a38d6-eb29-44a8-b495-c56ce74a227c' target='_blank'>Hakai Institute’s Burke-o-Lator TCO2/pCO2 Analyzer Discrete Sample Analysis Protocols</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c113d7a8-6a46-46fc-b49c-a4e69afedfbc' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='9e4a38d6-eb29-44a8-b495-c56ce74a227c' href='../records/9e4a38d6-eb29-44a8-b495-c56ce74a227c' target='_blank'>2</a></td>
      <td><a title='9e4a38d6-eb29-44a8-b495-c56ce74a227c' href='../records/9e4a38d6-eb29-44a8-b495-c56ce74a227c' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>58</th>
      <td><a title='ad032cd1-86cc-47cc-ac01-fce09e4cf8d9' href='../records/ad032cd1-86cc-47cc-ac01-fce09e4cf8d9' target='_blank'>Data on invasion of Calvert Island by Orthione griffenis</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fcb4dfb6-606b-4b4b-bdcb-90f3f480fc33' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='ad032cd1-86cc-47cc-ac01-fce09e4cf8d9' href='../records/ad032cd1-86cc-47cc-ac01-fce09e4cf8d9' target='_blank'>2</a></td>
      <td><a title='ad032cd1-86cc-47cc-ac01-fce09e4cf8d9' href='../records/ad032cd1-86cc-47cc-ac01-fce09e4cf8d9' target='_blank'>4</a></td>
      <td><a title='ad032cd1-86cc-47cc-ac01-fce09e4cf8d9' href='../records/ad032cd1-86cc-47cc-ac01-fce09e4cf8d9' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>47</th>
      <td><a title='cb9c0488-666b-4869-9ca4-04d7125fdf8a' href='../records/cb9c0488-666b-4869-9ca4-04d7125fdf8a' target='_blank'>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4624baf9-ec39-4538-83fe-1563511b722c' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-23</td>
      <td><a title='cb9c0488-666b-4869-9ca4-04d7125fdf8a' href='../records/cb9c0488-666b-4869-9ca4-04d7125fdf8a' target='_blank'>3</a></td>
      <td><a title='cb9c0488-666b-4869-9ca4-04d7125fdf8a' href='../records/cb9c0488-666b-4869-9ca4-04d7125fdf8a' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>62</th>
      <td><a title='d8d3f510-8d7c-4b51-ba80-f7a77244eb4e' href='../records/d8d3f510-8d7c-4b51-ba80-f7a77244eb4e' target='_blank'>High-resolution record of surface seawater CO2 content from December 2014 to April 2016 collected in Hyacinthe Bay, British Columbia, Canada. Version 1.0.</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f00b9c87-190e-4b89-a864-7c012b989e49' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='d8d3f510-8d7c-4b51-ba80-f7a77244eb4e' href='../records/d8d3f510-8d7c-4b51-ba80-f7a77244eb4e' target='_blank'>2</a></td>
      <td><a title='d8d3f510-8d7c-4b51-ba80-f7a77244eb4e' href='../records/d8d3f510-8d7c-4b51-ba80-f7a77244eb4e' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>51</th>
      <td><a title='dd5c8784-c292-4f68-bc3d-a460adb8cdbf' href='../records/dd5c8784-c292-4f68-bc3d-a460adb8cdbf' target='_blank'>Pacific Northwest Eelgrass Sediment Carbon Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b4cac70e-a6fa-4d77-8fdb-1d3612006bc4' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2025-04-23</td>
      <td><a title='dd5c8784-c292-4f68-bc3d-a460adb8cdbf' href='../records/dd5c8784-c292-4f68-bc3d-a460adb8cdbf' target='_blank'>6</a></td>
      <td><a title='dd5c8784-c292-4f68-bc3d-a460adb8cdbf' href='../records/dd5c8784-c292-4f68-bc3d-a460adb8cdbf' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>57</th>
      <td><a title='ee30aa86-e786-4a3f-b90f-df09a134621d' href='../records/ee30aa86-e786-4a3f-b90f-df09a134621d' target='_blank'>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94ded8f9-4ee7-407d-80eb-bf217ce7d260' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-23</td>
      <td><a title='ee30aa86-e786-4a3f-b90f-df09a134621d' href='../records/ee30aa86-e786-4a3f-b90f-df09a134621d' target='_blank'>3</a></td>
      <td><a title='ee30aa86-e786-4a3f-b90f-df09a134621d' href='../records/ee30aa86-e786-4a3f-b90f-df09a134621d' target='_blank'>7</a></td>
      <td></td>
    </tr>
    <tr>
      <th>52</th>
      <td><a title='f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a' href='../records/f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a' target='_blank'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_2738ef2b-0c74-422d-a140-082e5f7b3793' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a' href='../records/f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a' target='_blank'>3</a></td>
      <td><a title='f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a' href='../records/f2f9c9d6-0385-4732-b7d5-acc6bbb2e83a' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>61</th>
      <td><a title='f8f299be-a37e-43bf-9416-5ff59e664f65' href='../records/f8f299be-a37e-43bf-9416-5ff59e664f65' target='_blank'>Mobile Invertebrate Rocky Intertidal Surveys - BC Central Coast - 2016-2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1c9b7bcd-d3cc-4856-9428-df7abb2149f0' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-07-24</td>
      <td><a title='f8f299be-a37e-43bf-9416-5ff59e664f65' href='../records/f8f299be-a37e-43bf-9416-5ff59e664f65' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>46</th>
      <td><a title='a31d44d5-2ce5-4d03-8d0b-4549023840ff' href='../records/a31d44d5-2ce5-4d03-8d0b-4549023840ff' target='_blank'>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_154e88e6-2300-4ca0-b3f8-ee822d32a9a4' target='_blank'>link</a></td>
      <td>2022-01-22</td>
      <td>2024-07-23</td>
      <td><a title='a31d44d5-2ce5-4d03-8d0b-4549023840ff' href='../records/a31d44d5-2ce5-4d03-8d0b-4549023840ff' target='_blank'>6</a></td>
      <td><a title='a31d44d5-2ce5-4d03-8d0b-4549023840ff' href='../records/a31d44d5-2ce5-4d03-8d0b-4549023840ff' target='_blank'>9</a></td>
      <td></td>
    </tr>
    <tr>
      <th>45</th>
      <td><a title='2dd906f9-e0fe-4b8c-afe6-c5f2bf7400ae' href='../records/2dd906f9-e0fe-4b8c-afe6-c5f2bf7400ae' target='_blank'>Herring Survey Data - 2016 - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d342e016-1e9a-448a-bc1a-af53fe8d5dfd' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-24</td>
      <td><a title='2dd906f9-e0fe-4b8c-afe6-c5f2bf7400ae' href='../records/2dd906f9-e0fe-4b8c-afe6-c5f2bf7400ae' target='_blank'>1</a></td>
      <td><a title='2dd906f9-e0fe-4b8c-afe6-c5f2bf7400ae' href='../records/2dd906f9-e0fe-4b8c-afe6-c5f2bf7400ae' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>42</th>
      <td><a title='401a599c-d74d-4a44-930a-8c0c90659e92' href='../records/401a599c-d74d-4a44-930a-8c0c90659e92' target='_blank'>Macrocystis kelp canopy productivity data from BC Central Coast, v1.3.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7d3f525a-6ba2-494b-893a-147e2a812306' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-23</td>
      <td><a title='401a599c-d74d-4a44-930a-8c0c90659e92' href='../records/401a599c-d74d-4a44-930a-8c0c90659e92' target='_blank'>2</a></td>
      <td><a title='401a599c-d74d-4a44-930a-8c0c90659e92' href='../records/401a599c-d74d-4a44-930a-8c0c90659e92' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>38</th>
      <td><a title='773ef9a6-64dd-4734-ba16-566470b0edad' href='../records/773ef9a6-64dd-4734-ba16-566470b0edad' target='_blank'>Orthophoto High Compression 0.25m resolution Mosaic - 2012 - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1946cc53-6e11-4428-a2c9-43b34e1dcaa1' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-24</td>
      <td><a title='773ef9a6-64dd-4734-ba16-566470b0edad' href='../records/773ef9a6-64dd-4734-ba16-566470b0edad' target='_blank'>3</a></td>
      <td><a title='773ef9a6-64dd-4734-ba16-566470b0edad' href='../records/773ef9a6-64dd-4734-ba16-566470b0edad' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>40</th>
      <td><a title='7a9adcca-b0dc-462f-aa3f-9bb9209158be' href='../records/7a9adcca-b0dc-462f-aa3f-9bb9209158be' target='_blank'>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3f40326a-23f9-4e30-a16a-f332ace14e2f' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-23</td>
      <td><a title='7a9adcca-b0dc-462f-aa3f-9bb9209158be' href='../records/7a9adcca-b0dc-462f-aa3f-9bb9209158be' target='_blank'>5</a></td>
      <td><a title='7a9adcca-b0dc-462f-aa3f-9bb9209158be' href='../records/7a9adcca-b0dc-462f-aa3f-9bb9209158be' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>43</th>
      <td><a title='8275a332-8870-4300-8ca8-48b854e7dccf' href='../records/8275a332-8870-4300-8ca8-48b854e7dccf' target='_blank'>Wind Fetch - BC Central Coast - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_26a09a27-7f16-4944-b88d-8c3bf2d36f03' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-24</td>
      <td><a title='8275a332-8870-4300-8ca8-48b854e7dccf' href='../records/8275a332-8870-4300-8ca8-48b854e7dccf' target='_blank'>2</a></td>
      <td><a title='8275a332-8870-4300-8ca8-48b854e7dccf' href='../records/8275a332-8870-4300-8ca8-48b854e7dccf' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>41</th>
      <td><a title='8a7cd5ea-e167-419e-a5c3-919acafe8455' href='../records/8a7cd5ea-e167-419e-a5c3-919acafe8455' target='_blank'>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5feb907e-e63e-4172-94ae-831fbe92aee5' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-24</td>
      <td><a title='8a7cd5ea-e167-419e-a5c3-919acafe8455' href='../records/8a7cd5ea-e167-419e-a5c3-919acafe8455' target='_blank'>2</a></td>
      <td><a title='8a7cd5ea-e167-419e-a5c3-919acafe8455' href='../records/8a7cd5ea-e167-419e-a5c3-919acafe8455' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>44</th>
      <td><a title='a9527050-a108-46f7-ac9f-7150b4abede5' href='../records/a9527050-a108-46f7-ac9f-7150b4abede5' target='_blank'>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_be16603d-e383-4af4-9e93-7a36a086688e' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-23</td>
      <td><a title='a9527050-a108-46f7-ac9f-7150b4abede5' href='../records/a9527050-a108-46f7-ac9f-7150b4abede5' target='_blank'>3</a></td>
      <td><a title='a9527050-a108-46f7-ac9f-7150b4abede5' href='../records/a9527050-a108-46f7-ac9f-7150b4abede5' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>37</th>
      <td><a title='b1d18883-a622-4f3c-9892-57564271e009' href='../records/b1d18883-a622-4f3c-9892-57564271e009' target='_blank'>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_33c870b8-3b4c-429d-bc10-99dd4c7f4c7d' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-23</td>
      <td><a title='b1d18883-a622-4f3c-9892-57564271e009' href='../records/b1d18883-a622-4f3c-9892-57564271e009' target='_blank'>4</a></td>
      <td><a title='b1d18883-a622-4f3c-9892-57564271e009' href='../records/b1d18883-a622-4f3c-9892-57564271e009' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>39</th>
      <td><a title='c2b05382-684f-4349-a64b-b20521223574' href='../records/c2b05382-684f-4349-a64b-b20521223574' target='_blank'>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f462be7f-ab53-409e-8f8c-9b9fecc5e16e' target='_blank'>link</a></td>
      <td>2022-01-21</td>
      <td>2024-07-24</td>
      <td><a title='c2b05382-684f-4349-a64b-b20521223574' href='../records/c2b05382-684f-4349-a64b-b20521223574' target='_blank'>2</a></td>
      <td><a title='c2b05382-684f-4349-a64b-b20521223574' href='../records/c2b05382-684f-4349-a64b-b20521223574' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>36</th>
      <td><a title='d1d07d48-c909-41b4-8c0f-13238720749c' href='../records/d1d07d48-c909-41b4-8c0f-13238720749c' target='_blank'>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_769311e9-1b1f-41f4-9023-38acf37a6690' target='_blank'>link</a></td>
      <td>2022-01-20</td>
      <td>2024-07-23</td>
      <td><a title='d1d07d48-c909-41b4-8c0f-13238720749c' href='../records/d1d07d48-c909-41b4-8c0f-13238720749c' target='_blank'>3</a></td>
      <td><a title='d1d07d48-c909-41b4-8c0f-13238720749c' href='../records/d1d07d48-c909-41b4-8c0f-13238720749c' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>33</th>
      <td><a title='646dd927-3248-4fc9-970c-abea15f7d304' href='../records/646dd927-3248-4fc9-970c-abea15f7d304' target='_blank'>Mean Tidal Current - Coastal British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_15caa6c8-be9b-4f19-81ae-bb82321eafd6' target='_blank'>link</a></td>
      <td>2022-01-19</td>
      <td>2024-07-23</td>
      <td><a title='646dd927-3248-4fc9-970c-abea15f7d304' href='../records/646dd927-3248-4fc9-970c-abea15f7d304' target='_blank'>4</a></td>
      <td><a title='646dd927-3248-4fc9-970c-abea15f7d304' href='../records/646dd927-3248-4fc9-970c-abea15f7d304' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>35</th>
      <td><a title='693c7ca7-a244-4375-9460-ff7c27187af2' href='../records/693c7ca7-a244-4375-9460-ff7c27187af2' target='_blank'>Clam Garden Geospatial Data - Quadra Island - 2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8c8ed7d-51fa-45e0-b4eb-d21ddc55526a' target='_blank'>link</a></td>
      <td>2022-01-19</td>
      <td>2024-07-23</td>
      <td><a title='693c7ca7-a244-4375-9460-ff7c27187af2' href='../records/693c7ca7-a244-4375-9460-ff7c27187af2' target='_blank'>2</a></td>
      <td><a title='693c7ca7-a244-4375-9460-ff7c27187af2' href='../records/693c7ca7-a244-4375-9460-ff7c27187af2' target='_blank'>5</a></td>
      <td><a title='693c7ca7-a244-4375-9460-ff7c27187af2' href='../records/693c7ca7-a244-4375-9460-ff7c27187af2' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>32</th>
      <td><a title='b6621a3c-1700-4015-a359-56b6c7155835' href='../records/b6621a3c-1700-4015-a359-56b6c7155835' target='_blank'>Hakai Place Names Service - Coastal British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_0a8ff4c9-158a-4a46-9bb0-9d480ff40466' target='_blank'>link</a></td>
      <td>2022-01-19</td>
      <td>2024-07-24</td>
      <td><a title='b6621a3c-1700-4015-a359-56b6c7155835' href='../records/b6621a3c-1700-4015-a359-56b6c7155835' target='_blank'>4</a></td>
      <td><a title='b6621a3c-1700-4015-a359-56b6c7155835' href='../records/b6621a3c-1700-4015-a359-56b6c7155835' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>34</th>
      <td><a title='d576481a-4f51-40eb-85e9-fb95933f94cd' href='../records/d576481a-4f51-40eb-85e9-fb95933f94cd' target='_blank'>100 Islands Project - Island Spatial Data -2017 - Coastal British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f68be641-0017-4311-b4de-5d0aed9e2b57' target='_blank'>link</a></td>
      <td>2022-01-19</td>
      <td>2024-07-24</td>
      <td><a title='d576481a-4f51-40eb-85e9-fb95933f94cd' href='../records/d576481a-4f51-40eb-85e9-fb95933f94cd' target='_blank'>2</a></td>
      <td><a title='d576481a-4f51-40eb-85e9-fb95933f94cd' href='../records/d576481a-4f51-40eb-85e9-fb95933f94cd' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>31</th>
      <td><a title='f15f9c5e-08a6-4e9f-8ff5-a6126447e138' href='../records/f15f9c5e-08a6-4e9f-8ff5-a6126447e138' target='_blank'>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3dc0d46c-7afe-4379-901d-37a787c1c204' target='_blank'>link</a></td>
      <td>2022-01-19</td>
      <td>2024-07-23</td>
      <td><a title='f15f9c5e-08a6-4e9f-8ff5-a6126447e138' href='../records/f15f9c5e-08a6-4e9f-8ff5-a6126447e138' target='_blank'>4</a></td>
      <td><a title='f15f9c5e-08a6-4e9f-8ff5-a6126447e138' href='../records/f15f9c5e-08a6-4e9f-8ff5-a6126447e138' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>28</th>
      <td><a title='a0ada4b0-faea-4dcd-b9bf-d7ff212315fb' href='../records/a0ada4b0-faea-4dcd-b9bf-d7ff212315fb' target='_blank'>Stage-Discharge Time Series - Calvert Island - Archived Version 2.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1347af6c-aedf-4ec6-bd37-ed508df6c40a' target='_blank'>link</a></td>
      <td>2022-01-17</td>
      <td>2024-07-24</td>
      <td><a title='a0ada4b0-faea-4dcd-b9bf-d7ff212315fb' href='../records/a0ada4b0-faea-4dcd-b9bf-d7ff212315fb' target='_blank'>2</a></td>
      <td><a title='a0ada4b0-faea-4dcd-b9bf-d7ff212315fb' href='../records/a0ada4b0-faea-4dcd-b9bf-d7ff212315fb' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>30</th>
      <td><a title='cd3ca52d-dc83-4501-9e53-7b00c8ab9090' href='../records/cd3ca52d-dc83-4501-9e53-7b00c8ab9090' target='_blank'>Kelp Field Data for Remote Sensing - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94b4992f-19e2-46d4-875e-f0c952ea62f7' target='_blank'>link</a></td>
      <td>2022-01-17</td>
      <td>2024-07-24</td>
      <td><a title='cd3ca52d-dc83-4501-9e53-7b00c8ab9090' href='../records/cd3ca52d-dc83-4501-9e53-7b00c8ab9090' target='_blank'>2</a></td>
      <td><a title='cd3ca52d-dc83-4501-9e53-7b00c8ab9090' href='../records/cd3ca52d-dc83-4501-9e53-7b00c8ab9090' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>29</th>
      <td><a title='d64fd03b-46d4-4662-a123-c11bc42199b6' href='../records/d64fd03b-46d4-4662-a123-c11bc42199b6' target='_blank'>Underwater Video Transects - Calvert Island - 2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_62336906-31e6-4c32-968c-2312e703e08f' target='_blank'>link</a></td>
      <td>2022-01-17</td>
      <td>2024-07-24</td>
      <td><a title='d64fd03b-46d4-4662-a123-c11bc42199b6' href='../records/d64fd03b-46d4-4662-a123-c11bc42199b6' target='_blank'>2</a></td>
      <td><a title='d64fd03b-46d4-4662-a123-c11bc42199b6' href='../records/d64fd03b-46d4-4662-a123-c11bc42199b6' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>26</th>
      <td><a title='2adbc714-fde2-436b-a5bd-ec51457a275c' href='../records/2adbc714-fde2-436b-a5bd-ec51457a275c' target='_blank'>Nearshore Macrophyte Stable Isotopes - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_288ea4b2-3706-4256-8146-02bd0265585b' target='_blank'>link</a></td>
      <td>2022-01-13</td>
      <td>2025-04-21</td>
      <td><a title='2adbc714-fde2-436b-a5bd-ec51457a275c' href='../records/2adbc714-fde2-436b-a5bd-ec51457a275c' target='_blank'>1</a></td>
      <td><a title='2adbc714-fde2-436b-a5bd-ec51457a275c' href='../records/2adbc714-fde2-436b-a5bd-ec51457a275c' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>24</th>
      <td><a title='35dd16d8-20b1-49d5-8c59-9cdc02475cd0' href='../records/35dd16d8-20b1-49d5-8c59-9cdc02475cd0' target='_blank'>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ea6c0e20-9b99-48f7-adfb-6c1b70f6bd2a' target='_blank'>link</a></td>
      <td>2022-01-13</td>
      <td>2024-07-23</td>
      <td><a title='35dd16d8-20b1-49d5-8c59-9cdc02475cd0' href='../records/35dd16d8-20b1-49d5-8c59-9cdc02475cd0' target='_blank'>5</a></td>
      <td><a title='35dd16d8-20b1-49d5-8c59-9cdc02475cd0' href='../records/35dd16d8-20b1-49d5-8c59-9cdc02475cd0' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>25</th>
      <td><a title='6a6908af-8856-431e-8277-458fee82e534' href='../records/6a6908af-8856-431e-8277-458fee82e534' target='_blank'>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d87de5ca-a18a-406d-a4c1-74e6f8f28e5b' target='_blank'>link</a></td>
      <td>2022-01-13</td>
      <td>2024-08-02</td>
      <td><a title='6a6908af-8856-431e-8277-458fee82e534' href='../records/6a6908af-8856-431e-8277-458fee82e534' target='_blank'>5</a></td>
      <td><a title='6a6908af-8856-431e-8277-458fee82e534' href='../records/6a6908af-8856-431e-8277-458fee82e534' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>27</th>
      <td><a title='98bc62c7-d6a4-42bd-9110-c8021380d8a5' href='../records/98bc62c7-d6a4-42bd-9110-c8021380d8a5' target='_blank'>Seastar & Macroinvertebrate Dynamics - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3bc02dd8-7654-44f0-8c7c-02739937bdf4' target='_blank'>link</a></td>
      <td>2022-01-13</td>
      <td>2024-11-29</td>
      <td><a title='98bc62c7-d6a4-42bd-9110-c8021380d8a5' href='../records/98bc62c7-d6a4-42bd-9110-c8021380d8a5' target='_blank'>5</a></td>
      <td><a title='98bc62c7-d6a4-42bd-9110-c8021380d8a5' href='../records/98bc62c7-d6a4-42bd-9110-c8021380d8a5' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>23</th>
      <td><a title='3031aa60-689f-4b94-9dc6-9912cc742431' href='../records/3031aa60-689f-4b94-9dc6-9912cc742431' target='_blank'>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_66ad87d2-bb96-4515-a907-6367ca6c0a2b' target='_blank'>link</a></td>
      <td>2021-12-03</td>
      <td>2024-08-21</td>
      <td><a title='3031aa60-689f-4b94-9dc6-9912cc742431' href='../records/3031aa60-689f-4b94-9dc6-9912cc742431' target='_blank'>2</a></td>
      <td><a title='3031aa60-689f-4b94-9dc6-9912cc742431' href='../records/3031aa60-689f-4b94-9dc6-9912cc742431' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>22</th>
      <td><a title='3fbbd892-55cd-4c96-9669-cecefe726b3f' href='../records/3fbbd892-55cd-4c96-9669-cecefe726b3f' target='_blank'>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ee2791c3-3d99-41e5-8cdf-fa5d1d19944d' target='_blank'>link</a></td>
      <td>2021-12-02</td>
      <td>2024-07-23</td>
      <td><a title='3fbbd892-55cd-4c96-9669-cecefe726b3f' href='../records/3fbbd892-55cd-4c96-9669-cecefe726b3f' target='_blank'>3</a></td>
      <td><a title='3fbbd892-55cd-4c96-9669-cecefe726b3f' href='../records/3fbbd892-55cd-4c96-9669-cecefe726b3f' target='_blank'>1</a></td>
      <td><a title='3fbbd892-55cd-4c96-9669-cecefe726b3f' href='../records/3fbbd892-55cd-4c96-9669-cecefe726b3f' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>21</th>
      <td><a title='d7ca7d43-b0fb-4dfc-beb1-7033388011a0' href='../records/d7ca7d43-b0fb-4dfc-beb1-7033388011a0' target='_blank'>Juvenile Sockeye Diets Hakai 2015-2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_64f74489-b9a3-4e6f-9f25-be141b8e285c' target='_blank'>link</a></td>
      <td>2021-11-26</td>
      <td>2024-07-23</td>
      <td><a title='d7ca7d43-b0fb-4dfc-beb1-7033388011a0' href='../records/d7ca7d43-b0fb-4dfc-beb1-7033388011a0' target='_blank'>6</a></td>
      <td><a title='d7ca7d43-b0fb-4dfc-beb1-7033388011a0' href='../records/d7ca7d43-b0fb-4dfc-beb1-7033388011a0' target='_blank'>3</a></td>
      <td><a title='d7ca7d43-b0fb-4dfc-beb1-7033388011a0' href='../records/d7ca7d43-b0fb-4dfc-beb1-7033388011a0' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>20</th>
      <td><a title='1919ea31-8ac0-4bbb-aa2e-e9121996e41e' href='../records/1919ea31-8ac0-4bbb-aa2e-e9121996e41e' target='_blank'>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_eb1feb98-b11a-4663-b7ab-2216df8187bd' target='_blank'>link</a></td>
      <td>2021-11-19</td>
      <td>2024-07-23</td>
      <td><a title='1919ea31-8ac0-4bbb-aa2e-e9121996e41e' href='../records/1919ea31-8ac0-4bbb-aa2e-e9121996e41e' target='_blank'>5</a></td>
      <td><a title='1919ea31-8ac0-4bbb-aa2e-e9121996e41e' href='../records/1919ea31-8ac0-4bbb-aa2e-e9121996e41e' target='_blank'>5</a></td>
      <td><a title='1919ea31-8ac0-4bbb-aa2e-e9121996e41e' href='../records/1919ea31-8ac0-4bbb-aa2e-e9121996e41e' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>19</th>
      <td><a title='f6ad9487-d689-41a3-b610-352224d7759b' href='../records/f6ad9487-d689-41a3-b610-352224d7759b' target='_blank'>Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1769a04e-b77b-409b-8e48-bc2098bbad3e' target='_blank'>link</a></td>
      <td>2021-11-19</td>
      <td>2024-07-24</td>
      <td><a title='f6ad9487-d689-41a3-b610-352224d7759b' href='../records/f6ad9487-d689-41a3-b610-352224d7759b' target='_blank'>3</a></td>
      <td><a title='f6ad9487-d689-41a3-b610-352224d7759b' href='../records/f6ad9487-d689-41a3-b610-352224d7759b' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>18</th>
      <td><a title='b5de5a97-7498-4e5a-8f5d-0850f9e5fc87' href='../records/b5de5a97-7498-4e5a-8f5d-0850f9e5fc87' target='_blank'>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1aeeb145-8112-4268-afc7-05f14c8eae63' target='_blank'>link</a></td>
      <td>2021-10-20</td>
      <td>2024-07-24</td>
      <td><a title='b5de5a97-7498-4e5a-8f5d-0850f9e5fc87' href='../records/b5de5a97-7498-4e5a-8f5d-0850f9e5fc87' target='_blank'>3</a></td>
      <td></td>
      <td><a title='b5de5a97-7498-4e5a-8f5d-0850f9e5fc87' href='../records/b5de5a97-7498-4e5a-8f5d-0850f9e5fc87' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>17</th>
      <td><a title='b7b4d181-123b-446a-b557-dee2707a4db9' href='../records/b7b4d181-123b-446a-b557-dee2707a4db9' target='_blank'>QU5M Oceanographic Mooring in Hyacinthe Bay, Quadra Island, Provisional</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7ddae37a-e706-45d2-8060-8306300a98c8' target='_blank'>link</a></td>
      <td>2021-10-20</td>
      <td>2024-08-21</td>
      <td><a title='b7b4d181-123b-446a-b557-dee2707a4db9' href='../records/b7b4d181-123b-446a-b557-dee2707a4db9' target='_blank'>2</a></td>
      <td><a title='b7b4d181-123b-446a-b557-dee2707a4db9' href='../records/b7b4d181-123b-446a-b557-dee2707a4db9' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>16</th>
      <td><a title='29f9a024-3b5f-46d1-a3b1-8c333eeaa89f' href='../records/29f9a024-3b5f-46d1-a3b1-8c333eeaa89f' target='_blank'>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8853a375-f067-4760-b5d1-98c1fcf40c6d' target='_blank'>link</a></td>
      <td>2021-10-05</td>
      <td>2024-07-23</td>
      <td><a title='29f9a024-3b5f-46d1-a3b1-8c333eeaa89f' href='../records/29f9a024-3b5f-46d1-a3b1-8c333eeaa89f' target='_blank'>9</a></td>
      <td><a title='29f9a024-3b5f-46d1-a3b1-8c333eeaa89f' href='../records/29f9a024-3b5f-46d1-a3b1-8c333eeaa89f' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>15</th>
      <td><a title='2a104224-c3eb-4778-adc3-865b36471b1b' href='../records/2a104224-c3eb-4778-adc3-865b36471b1b' target='_blank'>Juvenile pink and chum salmon diet study – Discovery Islands and Johnstone Strait – May to July 2015 and 2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_89b3c6d8-983b-48f4-a0b5-04eea65602f6' target='_blank'>link</a></td>
      <td>2021-09-28</td>
      <td>2024-07-24</td>
      <td><a title='2a104224-c3eb-4778-adc3-865b36471b1b' href='../records/2a104224-c3eb-4778-adc3-865b36471b1b' target='_blank'>4</a></td>
      <td><a title='2a104224-c3eb-4778-adc3-865b36471b1b' href='../records/2a104224-c3eb-4778-adc3-865b36471b1b' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>13</th>
      <td><a title='0c08a4f0-b28c-40fe-aaa8-a03113a7c735' href='../records/0c08a4f0-b28c-40fe-aaa8-a03113a7c735' target='_blank'>Vegetated Islands Polygons - 100 Islands Research</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_55daf524-146e-4b06-8c6c-3255c7e3c77a' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-23</td>
      <td><a title='0c08a4f0-b28c-40fe-aaa8-a03113a7c735' href='../records/0c08a4f0-b28c-40fe-aaa8-a03113a7c735' target='_blank'>1</a></td>
      <td><a title='0c08a4f0-b28c-40fe-aaa8-a03113a7c735' href='../records/0c08a4f0-b28c-40fe-aaa8-a03113a7c735' target='_blank'>5</a></td>
      <td></td>
    </tr>
    <tr>
      <th>14</th>
      <td><a title='0d9ca9c8-95b0-48db-87b9-7db8af77363e' href='../records/0d9ca9c8-95b0-48db-87b9-7db8af77363e' target='_blank'>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ab901b46-43f6-4044-b0c3-b5fd825622f4' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-24</td>
      <td><a title='0d9ca9c8-95b0-48db-87b9-7db8af77363e' href='../records/0d9ca9c8-95b0-48db-87b9-7db8af77363e' target='_blank'>3</a></td>
      <td><a title='0d9ca9c8-95b0-48db-87b9-7db8af77363e' href='../records/0d9ca9c8-95b0-48db-87b9-7db8af77363e' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>9</th>
      <td><a title='4f9103f8-cd13-4bb1-a86b-a3ceb201db97' href='../records/4f9103f8-cd13-4bb1-a86b-a3ceb201db97' target='_blank'>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1815be54-9081-4031-80fa-d3d071340a7d' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-23</td>
      <td><a title='4f9103f8-cd13-4bb1-a86b-a3ceb201db97' href='../records/4f9103f8-cd13-4bb1-a86b-a3ceb201db97' target='_blank'>4</a></td>
      <td><a title='4f9103f8-cd13-4bb1-a86b-a3ceb201db97' href='../records/4f9103f8-cd13-4bb1-a86b-a3ceb201db97' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>10</th>
      <td><a title='6a1254e5-3815-4289-ba1c-984fb84dc1fe' href='../records/6a1254e5-3815-4289-ba1c-984fb84dc1fe' target='_blank'>Northwest Calvert Substrate Mapping</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4bf1e341-637c-4884-b373-033e033b3cba' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-24</td>
      <td><a title='6a1254e5-3815-4289-ba1c-984fb84dc1fe' href='../records/6a1254e5-3815-4289-ba1c-984fb84dc1fe' target='_blank'>2</a></td>
      <td><a title='6a1254e5-3815-4289-ba1c-984fb84dc1fe' href='../records/6a1254e5-3815-4289-ba1c-984fb84dc1fe' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>11</th>
      <td><a title='8ad491b8-58a3-48ad-a705-18e36fad34b0' href='../records/8ad491b8-58a3-48ad-a705-18e36fad34b0' target='_blank'>Hakai Institute Sensor Network</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_30bb20f4-1d7a-4167-a00f-613d0ff3e2fc' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-23</td>
      <td><a title='8ad491b8-58a3-48ad-a705-18e36fad34b0' href='../records/8ad491b8-58a3-48ad-a705-18e36fad34b0' target='_blank'>1</a></td>
      <td><a title='8ad491b8-58a3-48ad-a705-18e36fad34b0' href='../records/8ad491b8-58a3-48ad-a705-18e36fad34b0' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td><a title='c83b5cbf-cc8c-4676-823c-77e28c0ec9da' href='../records/c83b5cbf-cc8c-4676-823c-77e28c0ec9da' target='_blank'>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cf7a6149-b34a-404c-88e1-c556bf361408' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-24</td>
      <td><a title='c83b5cbf-cc8c-4676-823c-77e28c0ec9da' href='../records/c83b5cbf-cc8c-4676-823c-77e28c0ec9da' target='_blank'>3</a></td>
      <td><a title='c83b5cbf-cc8c-4676-823c-77e28c0ec9da' href='../records/c83b5cbf-cc8c-4676-823c-77e28c0ec9da' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>7</th>
      <td><a title='dc84cb4c-ba14-4632-a595-eed526bf9db1' href='../records/dc84cb4c-ba14-4632-a595-eed526bf9db1' target='_blank'>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_82c07005-9313-436c-9239-7be3f5907be2' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-24</td>
      <td><a title='dc84cb4c-ba14-4632-a595-eed526bf9db1' href='../records/dc84cb4c-ba14-4632-a595-eed526bf9db1' target='_blank'>3</a></td>
      <td><a title='dc84cb4c-ba14-4632-a595-eed526bf9db1' href='../records/dc84cb4c-ba14-4632-a595-eed526bf9db1' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>12</th>
      <td><a title='f409100d-95e4-4933-a927-fdf8d3b83204' href='../records/f409100d-95e4-4933-a927-fdf8d3b83204' target='_blank'>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_3732444b-7a97-4d9c-9f2e-2fc6f9618bae' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-23</td>
      <td><a title='f409100d-95e4-4933-a927-fdf8d3b83204' href='../records/f409100d-95e4-4933-a927-fdf8d3b83204' target='_blank'>3</a></td>
      <td><a title='f409100d-95e4-4933-a927-fdf8d3b83204' href='../records/f409100d-95e4-4933-a927-fdf8d3b83204' target='_blank'>4</a></td>
      <td><a title='f409100d-95e4-4933-a927-fdf8d3b83204' href='../records/f409100d-95e4-4933-a927-fdf8d3b83204' target='_blank'>3</a></td>
    </tr>
    <tr>
      <th>8</th>
      <td><a title='f5d51d99-ce24-4713-a317-7927dd283f1a' href='../records/f5d51d99-ce24-4713-a317-7927dd283f1a' target='_blank'>Kelp forest communities along an otter gradient</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_af65bf72-27af-4747-8911-ab05591762ac' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-23</td>
      <td><a title='f5d51d99-ce24-4713-a317-7927dd283f1a' href='../records/f5d51d99-ce24-4713-a317-7927dd283f1a' target='_blank'>6</a></td>
      <td><a title='f5d51d99-ce24-4713-a317-7927dd283f1a' href='../records/f5d51d99-ce24-4713-a317-7927dd283f1a' target='_blank'>3</a></td>
      <td><a title='f5d51d99-ce24-4713-a317-7927dd283f1a' href='../records/f5d51d99-ce24-4713-a317-7927dd283f1a' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>5</th>
      <td><a title='dcde7ad3-f54e-4210-ae4e-33db5aac63fe' href='../records/dcde7ad3-f54e-4210-ae4e-33db5aac63fe' target='_blank'>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8c3c86a9-1201-479d-b2b7-a1615183ffea' target='_blank'>link</a></td>
      <td>2021-09-20</td>
      <td>2024-07-23</td>
      <td><a title='dcde7ad3-f54e-4210-ae4e-33db5aac63fe' href='../records/dcde7ad3-f54e-4210-ae4e-33db5aac63fe' target='_blank'>7</a></td>
      <td><a title='dcde7ad3-f54e-4210-ae4e-33db5aac63fe' href='../records/dcde7ad3-f54e-4210-ae4e-33db5aac63fe' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a title='8bcf556e-26e2-41d4-af2c-2192c0426523' href='../records/8bcf556e-26e2-41d4-af2c-2192c0426523' target='_blank'>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dd325fc4-033c-4696-b38d-0ac883ad67eb' target='_blank'>link</a></td>
      <td>2021-06-11</td>
      <td>2024-07-24</td>
      <td><a title='8bcf556e-26e2-41d4-af2c-2192c0426523' href='../records/8bcf556e-26e2-41d4-af2c-2192c0426523' target='_blank'>8</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>0</th>
      <td><a title='3f883dc6-56ac-42f5-a1d4-6de554a9e63d' href='../records/3f883dc6-56ac-42f5-a1d4-6de554a9e63d' target='_blank'>Surface Seawater and Marine Boundary Layer CO2 Observations Made from the Kwakshua Channel (KC) Buoy on the Central Coast of British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_8b069feb-57fc-4d57-bf5c-761fd7cf0b45' target='_blank'>link</a></td>
      <td>2021-03-31</td>
      <td>2024-07-23</td>
      <td><a title='3f883dc6-56ac-42f5-a1d4-6de554a9e63d' href='../records/3f883dc6-56ac-42f5-a1d4-6de554a9e63d' target='_blank'>3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a title='5143957b-ee18-44d3-8000-a9c8f9a34a0d' href='../records/5143957b-ee18-44d3-8000-a9c8f9a34a0d' target='_blank'>Real-Time Provisional High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected from Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b62c3aaa-c3b8-41cb-b035-4da16209f26a' target='_blank'>link</a></td>
      <td>2021-03-31</td>
      <td>2024-07-23</td>
      <td><a title='5143957b-ee18-44d3-8000-a9c8f9a34a0d' href='../records/5143957b-ee18-44d3-8000-a9c8f9a34a0d' target='_blank'>1</a></td>
      <td><a title='5143957b-ee18-44d3-8000-a9c8f9a34a0d' href='../records/5143957b-ee18-44d3-8000-a9c8f9a34a0d' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a title='79433a1f-ec07-4cd5-a31a-8c2c53069085' href='../records/79433a1f-ec07-4cd5-a31a-8c2c53069085' target='_blank'>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fe76ef4c-254a-44fe-87bc-052cd3aa9663' target='_blank'>link</a></td>
      <td>2021-03-31</td>
      <td>2024-07-24</td>
      <td><a title='79433a1f-ec07-4cd5-a31a-8c2c53069085' href='../records/79433a1f-ec07-4cd5-a31a-8c2c53069085' target='_blank'>3</a></td>
      <td><a title='79433a1f-ec07-4cd5-a31a-8c2c53069085' href='../records/79433a1f-ec07-4cd5-a31a-8c2c53069085' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a title='f9b1c843-e0c9-414f-a89e-bc35d26cf77d' href='../records/f9b1c843-e0c9-414f-a89e-bc35d26cf77d' target='_blank'>Real-Time Provisional Surface Seawater and Marine Boundary Layer CO2 Observations made from the Kwakshua Channel (KC) Buoy on the central coast of British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_763f3e59-49fe-420a-91da-a046b4690bea' target='_blank'>link</a></td>
      <td>2021-03-31</td>
      <td>2024-07-23</td>
      <td><a title='f9b1c843-e0c9-414f-a89e-bc35d26cf77d' href='../records/f9b1c843-e0c9-414f-a89e-bc35d26cf77d' target='_blank'>2</a></td>
      <td><a title='f9b1c843-e0c9-414f-a89e-bc35d26cf77d' href='../records/f9b1c843-e0c9-414f-a89e-bc35d26cf77d' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>243</th>
      <td><a title='0074861a-39f2-42c1-ae71-abef4f78fd78' href='../records/0074861a-39f2-42c1-ae71-abef4f78fd78' target='_blank'>Gitga'at Territory Coastal Mapping Project</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b5f0f854-efe1-4132-808d-074244d813e1' target='_blank'>link</a></td>
      <td></td>
      <td>2025-11-12</td>
      <td><a title='0074861a-39f2-42c1-ae71-abef4f78fd78' href='../records/0074861a-39f2-42c1-ae71-abef4f78fd78' target='_blank'>1</a></td>
      <td><a title='0074861a-39f2-42c1-ae71-abef4f78fd78' href='../records/0074861a-39f2-42c1-ae71-abef4f78fd78' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>242</th>
      <td><a title='0cef18ab-cea6-4522-baba-1bcd73a30646' href='../records/0cef18ab-cea6-4522-baba-1bcd73a30646' target='_blank'>Mount Robson Aerial Photo and LiDAR Survey</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_66fbb7f5-3644-471a-95ee-f8d3758e888b' target='_blank'>link</a></td>
      <td></td>
      <td>2025-04-02</td>
      <td><a title='0cef18ab-cea6-4522-baba-1bcd73a30646' href='../records/0cef18ab-cea6-4522-baba-1bcd73a30646' target='_blank'>1</a></td>
      <td><a title='0cef18ab-cea6-4522-baba-1bcd73a30646' href='../records/0cef18ab-cea6-4522-baba-1bcd73a30646' target='_blank'>3</a></td>
      <td><a title='0cef18ab-cea6-4522-baba-1bcd73a30646' href='../records/0cef18ab-cea6-4522-baba-1bcd73a30646' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>241</th>
      <td><a title='139df6dd-772b-424f-b830-30a5ba6abfc6' href='../records/139df6dd-772b-424f-b830-30a5ba6abfc6' target='_blank'>Zooplankton taxonomic abundance and biomass along the BC Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_39a83551-ab8e-45be-a564-cece4b229371' target='_blank'>link</a></td>
      <td></td>
      <td>2025-08-12</td>
      <td><a title='139df6dd-772b-424f-b830-30a5ba6abfc6' href='../records/139df6dd-772b-424f-b830-30a5ba6abfc6' target='_blank'>2</a></td>
      <td></td>
      <td><a title='139df6dd-772b-424f-b830-30a5ba6abfc6' href='../records/139df6dd-772b-424f-b830-30a5ba6abfc6' target='_blank'>1</a></td>
    </tr>
  </tbody>
</table>

## Issues

<table border="1" class="dataframe table table-striped table-hover table-sm" id="issues_table">
  <thead>
    <tr style="text-align: right;">
      <th>metadata_revision</th>
      <th>title</th>
      <th>level</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-11-18</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2023), Central Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-11-18</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2023), Central Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-11-12</td>
      <td>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-11-12</td>
      <td>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-11-12</td>
      <td>Gitga'at Territory Coastal Mapping Project</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-11-12</td>
      <td>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-11-12</td>
      <td>Gitga'at Territory Coastal Mapping Project</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-11-12</td>
      <td>Gitga'at Territory Coastal Monitoring and Mapping - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-11-06</td>
      <td>Rocky Subtidal Fish and Invertebrate Community Surveys from the Central Coast of BC</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-11-06</td>
      <td>Rocky Subtidal Fish and Invertebrate Community Surveys from the Central Coast of BC</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-11-05</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-11-05</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-11-05</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-11-05</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2023-2024 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-11-04</td>
      <td>Elliot Creek Landslide LiDAR Mapping - 2023 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-11-04</td>
      <td>Elliot Creek Landslide LiDAR Mapping - 2023 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-11-04</td>
      <td>Elliot Creek Landslide LiDAR Mapping - 2023 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-11-04</td>
      <td>Elliot Creek Landslide LiDAR Mapping - 2023 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-31</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-31</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), Central Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-31</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Vancouver Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-31</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-31</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), Central Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-31</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2024), North Vancouver Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-29</td>
      <td>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 404 for resources[2].url=https://doi.org/10.5061/dryad.5mkkwh7g9</td>
    </tr>
    <tr>
      <td>2025-10-29</td>
      <td>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-10-29</td>
      <td>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-10-29</td>
      <td>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-29</td>
      <td>Data from: Prentice et al. 2025. Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Savage, Rosie' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Jeffery, Nick' contact.get('organisation-name')='Fisheries and Oceans Canada'</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')='McGill University'</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Sheridan, Kate' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Stanley, Ryan' contact.get('organisation-name')='Fisheries and Oceans Canada'</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Tula Foundation'</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-28</td>
      <td>Environmental DNA survey of Calvert Island, British Columbia, 2021</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-23</td>
      <td>MusselSeg: Semantic Segmentation for Rocky Intertidal Mussel Habitat</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Fletcher, Nathaniel' contact.get('organisation-name')='University of California, Santa Cruz'</td>
    </tr>
    <tr>
      <td>2025-10-23</td>
      <td>MusselSeg: Semantic Segmentation for Rocky Intertidal Mussel Habitat</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-23</td>
      <td>MusselSeg: Semantic Segmentation for Rocky Intertidal Mussel Habitat</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-18</td>
      <td>Biodiversity and Oceanographic data from the False Creek Bioblitz, 2022</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Henderson, Kate' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2025-10-18</td>
      <td>Biodiversity and Oceanographic data from the False Creek Bioblitz, 2022</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='False Creek Friends Society'</td>
    </tr>
    <tr>
      <td>2025-10-18</td>
      <td>Biodiversity and Oceanographic data from the False Creek Bioblitz, 2022</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-18</td>
      <td>Biodiversity and Oceanographic data from the False Creek Bioblitz, 2022</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-14</td>
      <td>Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Tula Foundation' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-10-14</td>
      <td>Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-10-14</td>
      <td>Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-14</td>
      <td>Time series of surface kelp canopy area derived from remotely piloted aerial systems (RPAS, or drone) surveys, Central Coast, British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-10-06</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2020-2022), Central Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-10-06</td>
      <td>Spatial extent of surface canopy kelp derived from fixed-wing surveys (2020-2022), Central Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-08-14</td>
      <td>Motile Invertebrate Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Closs, Alana' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-08-14</td>
      <td>Motile Invertebrate Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Morris, Angela' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-08-14</td>
      <td>Motile Invertebrate Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-08-14</td>
      <td>Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2025-08-14</td>
      <td>Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2025-08-14</td>
      <td>Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Prinzing, Tanya' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2025-08-14</td>
      <td>Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2025-08-14</td>
      <td>Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-08-12</td>
      <td>Zooplankton taxonomic abundance and biomass along the BC Coast</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 404 for resources[1].url=https://github.com/HakaiInstitute/hakai-zooplankton-microscopy-dataset</td>
    </tr>
    <tr>
      <td>2025-08-12</td>
      <td>Zooplankton taxonomic abundance and biomass along the BC Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-08-12</td>
      <td>Size-fractionated zooplankton biomass and isotopes along the BC coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-08-12</td>
      <td>Zooplankton taxonomic abundance and biomass along the BC Coast</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-08-12</td>
      <td>Size-fractionated zooplankton biomass and isotopes along the BC coast</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-08-08</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2024)</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Gulf Islands National Park Reserve' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-08-08</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2024)</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Helms, Sibylla' contact.get('organisation-name')='Gulf Islands National Park Reserve'</td>
    </tr>
    <tr>
      <td>2025-08-08</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2024)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-08-08</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2024)</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-05-21</td>
      <td>Glaciers in Western North America Mass Loss Geospatial Data (2021-2024)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-05-21</td>
      <td>Glaciers in Western North America Mass Loss Geospatial Data (2021-2024)</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Menounos, Brian' contact.get('organisation-name')='Geological Survey of Canada'</td>
    </tr>
    <tr>
      <td>2025-05-21</td>
      <td>Glaciers in Western North America Mass Loss Geospatial Data (2021-2024)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-05-21</td>
      <td>Glaciers in Western North America Mass Loss Geospatial Data (2021-2024)</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-05-16</td>
      <td>iTrack Oysters September 2023 Experiment - Environmental and Oyster Health Data</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of Victoria' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-05-16</td>
      <td>iTrack Oysters September 2023 Experiment - Environmental and Oyster Health Data</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 404 for resources[0].url=https://github.com/HakaiInstitute/hakai-wetlab-itracksept2023</td>
    </tr>
    <tr>
      <td>2025-05-16</td>
      <td>Sea Stars 2024 Experiment - Environmental Data</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 404 for resources[0].url=https://github.com/HakaiInstitute/hakai-wetlab-seastars2024</td>
    </tr>
    <tr>
      <td>2025-05-16</td>
      <td>iTrack Oysters September 2023 Experiment - Environmental and Oyster Health Data</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-05-16</td>
      <td>Sea Stars 2024 Experiment - Environmental Data</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-05-16</td>
      <td>iTrack Oysters September 2023 Experiment - Environmental and Oyster Health Data</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-05-12</td>
      <td>Larval Dungeness crab abundance and size time series along the coast of British Columbia</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-05-12</td>
      <td>Larval Dungeness crab abundance and size time series along the coast of British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-05-08</td>
      <td>Calliarthron 2023 Experiment - Environmental Data</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of British Columbia' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-05-08</td>
      <td>Calliarthron 2023 Experiment - Environmental Data</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 404 for resources[0].url=https://github.com/HakaiInstitute/hakai-wetlab-calliarthron2023</td>
    </tr>
    <tr>
      <td>2025-05-08</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-05-08</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-05-08</td>
      <td>Calliarthron 2023 Experiment - Environmental Data</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-05-08</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-05-08</td>
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-05-06</td>
      <td>Glacier and Ice Field Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Hakai Geosptatial' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-05-06</td>
      <td>Glacier and Ice Field Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Institute' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-05-06</td>
      <td>Glacier and Ice Field Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Geosptatial'</td>
    </tr>
    <tr>
      <td>2025-05-06</td>
      <td>Glacier and Ice Field Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-30</td>
      <td>USGS Glacier Mapping - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-30</td>
      <td>USGS Glacier Mapping - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-30</td>
      <td>USGS Glacier Mapping - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-04-30</td>
      <td>USGS Glacier Mapping - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Brown, Mat' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Brunsting, Ray' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Hakai Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, Provisional</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Fedje, Bryn' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Giesbrecht, Ian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hateley, Shawn' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily R.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily R.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Prentice, Carolyn' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Prentice, Carolyn' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Weatherston, Jorin' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hales, Burke' contact.get('organisation-name')='Oregon State University'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hales, Burke' contact.get('organisation-name')='Oregon State University'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Kennedy, Estjer' contact.get('organisation-name')='Sitka Tribe of Alaska'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Lanphier, Karie' contact.get('organisation-name')='Sitka Tribe of Alaska'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Peterson, Willoughby' contact.get('organisation-name')='Sitka Tribe of Alaska'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Poppe, Katrina' contact.get('organisation-name')='Western Washington University'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Poppe, Katrina' contact.get('organisation-name')='Western Washington University'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Whitehead, Chris' contact.get('organisation-name')='Sitka Tribe of Alaska'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='GeoBC'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Kennedy, Estjer' contact['organisation-name']='Sitka Tribe of Alaska'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Lanphier, Karie' contact['organisation-name']='Sitka Tribe of Alaska'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Peterson, Willoughby' contact['organisation-name']='Sitka Tribe of Alaska'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Poppe, Katrina' contact['organisation-name']='Western Washington University'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Poppe, Katrina' contact['organisation-name']='Western Washington University'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Whitehead, Chris' contact['organisation-name']='Sitka Tribe of Alaska'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA</td>
      <td>INFO</td>
      <td>DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0246099</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0247208</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Fraser River Airborne Surveys - 2021 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Hakai Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, Provisional</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Avian and paired Vegetation data from 100 Islands Project (BC Central Coast) Hakai Institute - 2015-2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Bute Inlet Geohazard - Topography Surveys - 2023 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution time series of surface seawater CO2 content from the OceansAlaska Shellfish Hatchery in Ketchikan, Alaska, USA</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Cloud-Based LiDAR Application - ELVIZ - Place Glacier, Mt. Robson, and Elliot Creek, BC</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Nearshore Macrophyte Stable Isotopes - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Brookson, Cole' contact.get('organisation-name')='University of Alberta'</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Godwin, Sean' contact.get('organisation-name')='Dalhousie University'</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Krkosek, Martin' contact.get('organisation-name')='University of Toronto'</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Rogers, Luke' contact.get('organisation-name')='Fisheries and Oceans Canada'</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>INFO</td>
      <td>DOI is not redirecting to Hakai's catalogue: https://zenodo.org/records/4005400</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Nearshore Macrophyte Stable Isotopes - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Differential infestation of juvenile Pacific salmon by parasitic sea lice in British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-21</td>
      <td>Biodiversity Surveys of the Gwaxdlala/Nalaxdlala Indigenous Protected and Conserved Area (IPCA) in Knight Inlet, British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Mount Robson Aerial Photo and LiDAR Survey</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Tula Foundation' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Place Glacier Aerial Photo and LiDAR Survey</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Tula Foundation' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Elliot Creek Aerial Photo and LiDAR Survey</td>
      <td>ERROR</td>
      <td>Invalid resource format: resources[0].format=JSON</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Place Glacier Aerial Photo and LiDAR Survey</td>
      <td>ERROR</td>
      <td>Invalid resource format: resources[0].format=JSON</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Elliot Creek Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Elliot Creek Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Mount Robson Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Mount Robson Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Place Glacier Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Place Glacier Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Elliot Creek Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Mount Robson Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Place Glacier Aerial Photo and LiDAR Survey</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Elliot Creek Aerial Photo and LiDAR Survey</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Mount Robson Aerial Photo and LiDAR Survey</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-02</td>
      <td>Place Glacier Aerial Photo and LiDAR Survey</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-01</td>
      <td>Bute Inlet Geo-Hazards & Ramsay West - 2024 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-01</td>
      <td>Bute Inlet Geo-Hazards & Ramsay West - 2024 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-01</td>
      <td>Bute Inlet Geo-Hazards & Ramsay West - 2024 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-04-01</td>
      <td>Bute Inlet Geo-Hazards & Ramsay West - 2024 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-03-04</td>
      <td>Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-03-04</td>
      <td>Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-03-04</td>
      <td>Understory kelp biomass data from BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Krumhansl, K.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2025-03-04</td>
      <td>Understory kelp biomass data from BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-03-04</td>
      <td>Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-03-04</td>
      <td>Seton and Anderson Lake Multibeam Survey - 2024 - British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-02-05</td>
      <td>Knight Inlet Remotely Operated Vehicle Marine Habitat Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-02-05</td>
      <td>Knight Inlet Remotely Operated Vehicle Marine Habitat Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-02-05</td>
      <td>Knight Inlet Remotely Operated Vehicle Marine Habitat Survey</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-02-05</td>
      <td>Knight Inlet Remotely Operated Vehicle Marine Habitat Survey</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-01-30</td>
      <td>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-01-30</td>
      <td>Freshwater and marine water quality (nutrients and carbon) - Calvert Island - 2014 to 2018</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-01-08</td>
      <td>Owikeno Lake Bathymetric Survey</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Hakai Geospatial' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-01-08</td>
      <td>Owikeno Lake Bathymetric Survey</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Geospatial'</td>
    </tr>
    <tr>
      <td>2025-01-08</td>
      <td>Owikeno Lake Bathymetric Survey</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Geospatial'</td>
    </tr>
    <tr>
      <td>2025-01-08</td>
      <td>Owikeno Lake Bathymetric Survey</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-01-08</td>
      <td>Owikeno Lake Bathymetric Survey</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Geomorphology - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Geomorphology - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Geomorphology - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Geomorphology - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-01-03</td>
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-30</td>
      <td>Seagrass Site-Level Production on BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Van Maanen, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-30</td>
      <td>Seagrass Site-Level Production on BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-19</td>
      <td>iTrack Oysters February 2023 Experiment - Environmental and Oyster Health Data</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of Victoria' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-19</td>
      <td>iTrack Oysters February 2023 Experiment - Environmental and Oyster Health Data</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-19</td>
      <td>iTrack Oysters February 2023 Experiment - Environmental and Oyster Health Data</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-16</td>
      <td>Cryosphere Snow Surveys Southwest British Columbia - 2023 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-16</td>
      <td>Cryosphere Snow Surveys Southwest British Columbia - 2023 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-16</td>
      <td>Cryosphere Snow Surveys Southwest British Columbia - 2023 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-11</td>
      <td>High performance liquid chromatography phytoplankton pigment timeseries for the northern Salish Sea and central coast, British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Vancouver Island University' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Vancouver Island University' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stream Event Sampling - Calvert Island - 2015-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Brown, Mathew' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Brunsting, Ray' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Brunsting, Ray' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Henderson, Matthew' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stream Event Sampling - Calvert Island - 2015-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Korver, Maartje C.' contact.get('organisation-name')='Hakai Institute -  McGill University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Korver, Maartje C.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Korver, Maartje C.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Korver, Maartje C.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Korver, Maartje' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Korver, Maartje C.' contact['organisation-name']='Hakai Institute -  McGill University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, Bill' contact.get('organisation-name')='Vancouver Island University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Vancouver Island University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Vancouver Island University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stream Event Sampling - Calvert Island - 2015-2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Vancouver Island University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019 Version 4.1</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Vancouver Island University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019 Version 4.1</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Vancouver Island University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Vancouver Island University'</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stream Event Sampling - Calvert Island - 2015-2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, A. A.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stream Event Sampling - Calvert Island - 2015-2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Tank, Suzanne E.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Waterloo, M.J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='van Meerveld, H.J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stream Event Sampling - Calvert Island - 2015-2018</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019 Version 4.1</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Discharge Time Series (2013-2017) – Calvert Island - Archived Version 3.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 - Sept 2019 Version 5</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 1.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Namu British Columbia - 2021 - Hakai Institute - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019 Version 4.1</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Dissolved organic carbon fluxes of seven watersheds in a bog forest ecosystem at Calvert Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-04</td>
      <td>Hakai Water Properties Vertical Profile Data Measured by Oceanographic Profilers, Provisional</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-12-04</td>
      <td>Hakai Water Properties Vertical Profile Data Measured by Oceanographic Profilers, Provisional</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-12-04</td>
      <td>100 Islands Research Program Terrestrial Vegetation Data - BC Central Coast - 2015, 2016, 2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-04</td>
      <td>Hakai Water Properties Vertical Profile Data Measured by Oceanographic Profilers, Provisional</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-04</td>
      <td>100 Islands Research Program Terrestrial Vegetation Data - BC Central Coast - 2015, 2016, 2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Froese, Tyrel' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Froese, Tyrel' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Froese, Tyrel' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gehman, Alyssa' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gehman, Alyssa' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hessing-Lewis, Margot' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hessing-Lewis, Margot' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Jordinson, Eva' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Jordinson, Eva' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Monteith, Zach' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Monteith, Zach' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Monteith, Zach' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Morris, Angela' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Olsen, Angeleen' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Clark, Jennifer' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Clark, Jennifer' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Clark, Jennifer' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Closs, Alana' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Closs, Alana' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Closs, Alana' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Closs, Alana' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Closs, Alana' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Prinzing, Tanya' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Rechsteiner, Erin' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Length & Bed Depth - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-11-28</td>
      <td>Fraser River - BCSRIF Landslide Mapping – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-28</td>
      <td>Fraser River - BCSRIF Landslide Mapping – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-28</td>
      <td>Fraser River - BCSRIF Landslide Mapping – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-11-28</td>
      <td>Fraser River - BCSRIF Landslide Mapping – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-11-27</td>
      <td>Sentinels of Change Sea surface temperature time series data along the British Columbia Coast</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-11-26</td>
      <td>Denali Fault - 2024 - Airborne LiDAR Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-26</td>
      <td>Denali Fault - 2024 - Airborne LiDAR Survey</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-26</td>
      <td>Denali Fault - 2024 - Airborne LiDAR Survey</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-11-26</td>
      <td>Denali Fault - 2024 - Airborne LiDAR Survey</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Kîsik Geospatial & Aerial Survey' contact.get('organisation-name')='Kîsik Geospatial & Aerial Survey'</td>
    </tr>
    <tr>
      <td>2024-11-26</td>
      <td>Denali Fault - 2024 - Airborne LiDAR Survey</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Kîsik Geospatial & Aerial Survey' contact['organisation-name']='Kîsik Geospatial & Aerial Survey'</td>
    </tr>
    <tr>
      <td>2024-11-26</td>
      <td>Denali Fault - 2024 - Airborne LiDAR Survey</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-25</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-25</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Collyer, M. J. P.' contact.get('organisation-name')='Pacific Rim National Park Reserve'</td>
    </tr>
    <tr>
      <td>2024-11-25</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Helms, Sibylla' contact.get('organisation-name')='Gulf Islands National Park Reserve'</td>
    </tr>
    <tr>
      <td>2024-11-25</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Rockwell, Lisa' contact.get('organisation-name')='Gulf Islands National Park Reserve'</td>
    </tr>
    <tr>
      <td>2024-11-25</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-25</td>
      <td>Eelgrass (Z. marina) extent at Gulf Islands National Park Reserve eelgrass monitoring sites (2017, 2018) v1.0.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-11-21</td>
      <td>Fraser River Landslide Project - 2022-2024 - Drone Data</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Hakai Geospatial' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-21</td>
      <td>Fraser River Landslide Project - 2022-2024 - Drone Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-21</td>
      <td>Fraser River Landslide Project - 2022-2024 - Drone Data</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Geospatial'</td>
    </tr>
    <tr>
      <td>2024-11-21</td>
      <td>Fraser River Landslide Project - 2022-2024 - Drone Data</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-20</td>
      <td>Fraser River Landslide Project - Sites of Concern 2024</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Hakai Geospatial' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-20</td>
      <td>Fraser River Landslide Project - Sites of Concern 2024</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-20</td>
      <td>Fraser River Landslide Project - Sites of Concern 2024</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Anderson, Edward' contact.get('organisation-name')='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-11-20</td>
      <td>Fraser River Landslide Project - Sites of Concern 2024</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Standen, Sayumi' contact.get('organisation-name')='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-11-20</td>
      <td>Fraser River Landslide Project - Sites of Concern 2024</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Geospatial'</td>
    </tr>
    <tr>
      <td>2024-11-20</td>
      <td>Fraser River Landslide Project - Sites of Concern 2024</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-06</td>
      <td>Spatial extent of eelgrass (Zostera marina) beds from monitoring sites within the greater park ecosystem of Pacific Rim National Park Reserve (2017, 2018)</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Yakimishyn, Jennifer' contact.get('organisation-name')='Pacific Rim National Park Reserve'</td>
    </tr>
    <tr>
      <td>2024-11-06</td>
      <td>Spatial extent of eelgrass (Zostera marina) beds from monitoring sites within the greater park ecosystem of Pacific Rim National Park Reserve (2017, 2018)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-11-06</td>
      <td>Spatial extent of eelgrass (Zostera marina) beds from monitoring sites within the greater park ecosystem of Pacific Rim National Park Reserve (2017, 2018)</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-10-10</td>
      <td>Protistan plankton time series from the northern Salish Sea and Central Coast, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-10-09</td>
      <td>Water column CO2 system measurements from January 2016 to December 2023 from Hakai Institute oceanographic station QU39 in northern Strait of Georgia, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-10-09</td>
      <td>Water column CO2 system measurements from January 2016 to December 2023 from Hakai Institute oceanographic station QU39 in northern Strait of Georgia, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Closs, Alana' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Morris, Angela' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Opie, Rumer' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Rechsteiner, Erin' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Clark, Jennifer' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Prinzing, Tanya' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-08-30</td>
      <td>Fucus Dynamics - Point Intercept Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Barrette, Jessy' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>QU5M Oceanographic Mooring in Hyacinthe Bay, Quadra Island, Provisional</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>QU5M Oceanographic Mooring in Hyacinthe Bay, Quadra Island, Provisional</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>Pruth Bay Oceanographic Mooring on Calvert Island Provisional</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>QU5M Oceanographic Mooring in Hyacinthe Bay, Quadra Island, Provisional</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Data for the paper "Phylogenomic position of eupelagonemids, abundant, and diverse deep-ocean heterotrophs"</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of British Columbia' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2019</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Data for the paper "Phylogenomic position of eupelagonemids, abundant, and diverse deep-ocean heterotrophs"</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Surfgrass Community Structure - Monitoring - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2019</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Data for the paper "Phylogenomic position of eupelagonemids, abundant, and diverse deep-ocean heterotrophs"</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-31</td>
      <td>Hakai Water Properties Vertical Profile Data Measured by Oceanographic Profilers, Research</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hare, Alex' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-31</td>
      <td>Hakai Water Properties Vertical Profile Data Measured by Oceanographic Profilers, Research</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of British Columbia' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of Victoria' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Aquatic carbon flux data package for Oliver et al. 2017</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 401 for resources[0].url=https://drive.google.com/a/hakai.org/file/d/0Byed_WX-ZNMaM3BtUW5KQ2ZtLW8/view?usp=sharing</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Aquatic carbon flux data package for Oliver et al. 2017</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 401 for resources[1].url=https://drive.google.com/a/hakai.org/file/d/0Byed_WX-ZNMaSkItaW5ocTY4UjQ/view?usp=sharing</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream Event Sampling - Calvert Island</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 404 for resources[1].url=https://drive.google.com/open?id=0B3dfJwMwT2k4RzNYOGFUcFNpUms</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Summer sea wrack spatial data; Central Coast, British Columbia, Canada (2015 - 2017)</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Data on invasion of Calvert Island by Orthione griffenis</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2014 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Burt, Jenn' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Davidson, Katie H.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Desmarais, Isabelle' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Fedje, Bryn' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, G. W.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, G.W.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, Gordon W.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, Gordon W.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Derived Watersheds with Metrics - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, Gordon W.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Technology Team Hakai' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Technology Team Hakai' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Technology Team Hakai' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Technology Team Hakai' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Giesbrecht, Ian J. W.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Giesbrecht, Ian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Giesbrecht, Ian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Giesbrecht, Ian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gonzalez Arriola, Santiago' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gonzalez Arriola, Santiago' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Place Names Service - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Place Names Service - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 2.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Orthophoto High Compression 0.25m resolution Mosaic - 2012 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Orthophoto High Compression 0.25m resolution Mosaic - 2012 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Wind Fetch - BC Central Coast - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Wind Fetch - BC Central Coast - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underwater Video Transects - Calvert Island - 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underwater Video Transects - Calvert Island - 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream Event Sampling - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Field Data for Remote Sensing - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Bathymetry for Six Lakes on Calvert and Hecate Islands - 2016 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Herring Survey Data - 2016 - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Herring Survey Data - 2016 - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2014 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>100 Islands Project - Island Spatial Data -2017 - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>100 Islands Project - Island Spatial Data -2017 - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Northwest Calvert Substrate Mapping</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Extent of Canopy-Forming Kelps, Derived from World View-2, Central Coast, Central Coast, British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Institute Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Extent of Canopy-Forming Kelps, Derived from World View-2, Central Coast, Central Coast, British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Institute Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Water column carbonate system measurements from the Pacific Salmon Foundation Citizen Science Program stations from July 2016 to October 2017 in the northern Salish Sea, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hare, Alex' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Water column carbonate system measurements from the Pacific Salmon Foundation Citizen Science Program stations from July 2016 to October 2017 in the northern Salish Sea, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hare, Alex' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface seawater CO2 content from December 2014 to April 2016 collected in Hyacinthe Bay, British Columbia, Canada. Version 1.0.</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hare, Alex' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hare, Alex' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream temperature time-series – Calvert Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily R.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream temperature time-series – Calvert Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily R.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019 v2.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>UAV Imagery - 2016 - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2014 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2014 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Jackson, Jennifer M.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Bathymetry for Six Lakes on Calvert and Hecate Islands - 2016 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Jacob, Wayne' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Janusson, Carly' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Kellogg, Colleen T. E.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 2.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Korver, Maartje' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>UAV Imagery - 2016 - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Herring Survey Data - 2016 - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Morgan Henderson, Matthew' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Myers, Emma' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Olson, Angeleen' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Olson, Angeleen' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Trails - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Trails - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Northwest Calvert Substrate Mapping</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Viner, Nick' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Data on invasion of Calvert Island by Orthione griffenis</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Whalen, Matt' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Data on invasion of Calvert Island by Orthione griffenis</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Whalen, Matt' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019 v2.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='White, Robert' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='White, Robert' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile pink and chum salmon diet study – Discovery Islands and Johnstone Strait – May to July 2015 and 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Zahner, Vanessa' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile pink and chum salmon diet study – Discovery Islands and Johnstone Strait – May to July 2015 and 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Zahner, Vanessa' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Wind Fetch - BC Central Coast - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Summer sea wrack spatial data; Central Coast, British Columbia, Canada (2015 - 2017)</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Herring Survey Data - 2016 - BC Central Coast</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2014 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Trails - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Place Names Service - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream Event Sampling - Calvert Island</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Data on invasion of Calvert Island by Orthione griffenis</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Data on invasion of Calvert Island by Orthione griffenis</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019 v2.0</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Institute’s Burke-o-Lator TCO2/pCO2 Analyzer Discrete Sample Analysis Protocols</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>UAV Imagery - 2016 - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Derived Watersheds with Metrics - Calvert Island</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']="D'Amore, D. V." contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Place Names Service - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='BC Base Annotations data, TRIM' contact.get('organisation-name')='GEOBC TRIM Program'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Banner, Allen' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Bidlack, Allison' contact.get('organisation-name')='University of Alaska Southeast, Alaska Coastal Rainforest Center'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Biles, F. E.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Aquatic carbon flux data package for Oliver et al. 2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Bulmer, Chuck' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='D’Amore, D.V.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, Bill' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream temperature time-series – Calvert Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, Gordon W.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, Gordon' contact.get('organisation-name')='University of Northern British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Haggarty, D' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hallam, S.J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Harrington, Christen D.' contact.get('organisation-name')='Alaska Department of Transportation'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Heger, T.J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hessing-Lewis, Margot' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surface water CO2 parameters collected by Alaskan citizens around the northern Gulf of Alaska from April 2015 to August 2017. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hetrick, J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hoffman, Kira' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hunt, Brian P. V.' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile pink and chum salmon diet study – Discovery Islands and Johnstone Strait – May to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hunt, Brian' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Juanes, Francis' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Keeling, P.J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Korver, Maartje C.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Lebon, Geoffrey T.' contact.get('organisation-name')='University of Washington Joint Institute for the Study of the Atmosphere'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Lertzman, Ken P.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Levy-Booth, David J.' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Levy-Booth, David J.' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='MacKinnon, Andy' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='McEwan, Skye' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Mohn, W.W.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Nelson, Trisalyn' contact.get('organisation-name')='University of Victoria'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, Alison A.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, Alison A.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, Allison A.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, Allison A.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Aquatic carbon flux data package for Oliver et al. 2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, Allison A.' contact.get('organisation-name')='University of Alberta'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Aquatic carbon flux data package for Oliver et al. 2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, Allison A.' contact.get('organisation-name')='University of Alberta'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream Event Sampling - Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, Allison' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Quayle, Lucy' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surface water CO2 parameters collected by Alaskan citizens around the northern Gulf of Alaska from April 2015 to August 2017. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Ramsey, J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Roberts, Nelson' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Saunders, Sari' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Saunders, Sari' contact.get('organisation-name')='BC Ministry of Forests, Lands and Natural Resource Operations'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='St. Pierre, Kyra A.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Tank, Suzanne E.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Thompson, Shanley' contact.get('organisation-name')='University of Victoria'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Thompson, Shanley' contact.get('organisation-name')='University of Victoria'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream Event Sampling - Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Waterloo, Maarten' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Summer sea wrack spatial data; Central Coast, British Columbia, Canada (2015 - 2017)</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Wickham, Sara' contact.get('organisation-name')='University of Victoria'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Place Names Service - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='BC Base Annotations data, TRIM' contact['organisation-name']='GEOBC TRIM Program'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Bidlack, Allison' contact['organisation-name']='University of Alaska Southeast, Alaska Coastal Rainforest Center'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Harrington, Christen D.' contact['organisation-name']='Alaska Department of Transportation'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Hunt, Brian P. V.' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Lebon, Geoffrey T.' contact['organisation-name']='University of Washington Joint Institute for the Study of the Atmosphere'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Levy-Booth, David J.' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Levy-Booth, David J.' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Saunders, Sari' contact['organisation-name']='BC Ministry of Forests, Lands and Natural Resource Operations'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0208638</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</td>
      <td>INFO</td>
      <td>DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0209049</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream temperature time-series – Calvert Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Place Names Service - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Orthophoto High Compression 0.25m resolution Mosaic - 2012 - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Mobile Invertebrate Rocky Intertidal Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Wind Fetch - BC Central Coast - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Aquatic carbon flux data package for Oliver et al. 2017</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Ecosystem Comparison Plots - Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution hydrometeorological data from seven small coastal watersheds, British Columbia, Canada, 2013-2019</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Water column carbonate system measurements from the Pacific Salmon Foundation Citizen Science Program stations from July 2016 to October 2017 in the northern Salish Sea, British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Eelgrass Extent 2014 - Central Coast</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Northwest Calvert Substrate Mapping</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underwater Video Transects - Calvert Island - 2016</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Summer sea wrack spatial data; Central Coast, British Columbia, Canada (2015 - 2017)</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface seawater CO2 content from November 2017 to June 2018 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile pink and chum salmon diet study – Discovery Islands and Johnstone Strait – May to July 2015 and 2016</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream Event Sampling - Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Field Data for Remote Sensing - BC Central Coast</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019 v2.0</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-based Ecosystem Classification for Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Bathymetry for Six Lakes on Calvert and Hecate Islands - 2016 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>UAV Imagery - 2016 - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Herring Survey Data - 2016 - BC Central Coast</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface water pH at Sentry Shoal in the Northern Strait of Georgia</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2014 - NW Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Derived Watersheds with Metrics - Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Trails - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>100 Islands Project - Island Spatial Data -2017 - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Data on invasion of Calvert Island by Orthione griffenis</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream temperature time-series – Calvert Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 2.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Orthophoto High Compression 0.25m resolution Mosaic - 2012 - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Mobile Invertebrate Rocky Intertidal Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Wind Fetch - BC Central Coast - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Aquatic carbon flux data package for Oliver et al. 2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution hydrometeorological data from seven small coastal watersheds, British Columbia, Canada, 2013-2019</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Water column carbonate system measurements from the Pacific Salmon Foundation Citizen Science Program stations from July 2016 to October 2017 in the northern Salish Sea, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Northwest Calvert Substrate Mapping</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underwater Video Transects - Calvert Island - 2016</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surface water CO2 parameters collected by Alaskan citizens around the northern Gulf of Alaska from April 2015 to August 2017. Version 1.0.</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Summer sea wrack spatial data; Central Coast, British Columbia, Canada (2015 - 2017)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface seawater CO2 content from November 2017 to June 2018 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile pink and chum salmon diet study – Discovery Islands and Johnstone Strait – May to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Field Data for Remote Sensing - BC Central Coast</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019 v2.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Institute’s Burke-o-Lator TCO2/pCO2 Analyzer Discrete Sample Analysis Protocols</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface water pH at Sentry Shoal in the Northern Strait of Georgia</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Precipitation time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface seawater CO2 content from December 2014 to April 2016 collected in Hyacinthe Bay, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Data on invasion of Calvert Island by Orthione griffenis</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR-derived Drainage Network for Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stream temperature time-series – Calvert Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Place Names Service - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Canopy Extent - 2015 - NW Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Stage-Discharge Time Series - Calvert Island - Archived Version 2.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hunter Island Hauyat Village Site Elevation Point Data - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Orthophoto High Compression 0.25m resolution Mosaic - 2012 - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Mobile Invertebrate Rocky Intertidal Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile Salmon Migration Dynamics in the Discovery Islands and Johnstone Strait; 2015–2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast - 2018-2019</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LiDAR Dataset - Calvert Island - 2012 & 2014 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Watersheds of the northern Pacific coastal temperate rainforest margin</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution hydrometeorological data from seven small coastal watersheds, British Columbia, Canada, 2013-2019</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Water column carbonate system measurements from the Pacific Salmon Foundation Citizen Science Program stations from July 2016 to October 2017 in the northern Salish Sea, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Lidar Derived Canopy Height Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>25m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Biogeochemical Sampling of Streams in the Kwakshua Watersheds of Calvert and Hecate Islands, BC: 2013-2019. Version 1.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surface water CO2 parameters collected by Alaskan citizens around the northern Gulf of Alaska from April 2015 to August 2017. Version 1.0.</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Nutrient and dissolved organic carbon in fresh and marine waters of Kwakshua Channel, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Dissolved and particulate organic carbon chemistry for freshwater and marine stations from 2014 through 2016 on Calvert and Hecate Islands, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Summer sea wrack spatial data; Central Coast, British Columbia, Canada (2015 - 2017)</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Microbial activity and carbon fluxes in rainforest soil – Tsunami Hill, Calvert Island – June 2015 - April 2016</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface seawater CO2 content from November 2017 to June 2018 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Rocky Intertidal RPAS Mapping - 2018 - 2020 - BC Central Coast - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Keen’s Mouse Food Web Study – 100 Islands Project – Central Coast, BC (2015-2017)</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Juvenile pink and chum salmon diet study – Discovery Islands and Johnstone Strait – May to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Baseline Limnology of Lakes in the Kwakshua Watersheds of Calvert and Hecate Islands, BC. 2016-2019 v2.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Bathymetry for Six Lakes on Calvert and Hecate Islands - 2016 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Extent of Canopy-Forming Kelps, Derived from World View-2, Central Coast, Central Coast, British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Institute’s Burke-o-Lator TCO2/pCO2 Analyzer Discrete Sample Analysis Protocols</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Groundwater sampling in the Kwakshua Watersheds of Calvert and Hecate Islands, BC (2016-2019) - Version 1.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface water pH at Sentry Shoal in the Northern Strait of Georgia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Underway Surface Seawater and Marine Boundary Layer Observations Made from the Alaska Marine Highway System M/V Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Precipitation time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-resolution record of surface seawater CO2 content from December 2014 to April 2016 collected in Hyacinthe Bay, British Columbia, Canada. Version 1.0.</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Hakai Marine Sampling Survey - 2014 - BC Central Coast - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>100 Islands Project - Island Spatial Data -2017 - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>3m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>ERROR</td>
      <td>Empty resource name</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>ERROR</td>
      <td>Empty resource name</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
      <td>ERROR</td>
      <td>Empty resource name</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Simon Fraser University' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of British Columbia' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of British Columbia' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of British Columbia' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of Victoria' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='Wild Salmon Centre' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>ERROR</td>
      <td>Invalid licence: CC-BY-NC-4.0</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mapping Canopy-Forming Kelps in the Northeast Pacific: A Guidebook for Decision-Makers and Practitioners</td>
      <td>ERROR</td>
      <td>Invalid licence: CC-BY-NC-4.0</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</td>
      <td>ERROR</td>
      <td>Invalid licence: CC-BY-NC-4.0</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</td>
      <td>ERROR</td>
      <td>Invalid licence: CC-BY-NC-ND-4.0</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 401 for resources[0].url=https://drive.google.com/file/d/1w7TLX1RIP6F6S_inRKU3x-A27srXzFSa/view?usp=sharing</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of 8-m seawater CO2 content entering Fanny Bay Oysters in Baynes Sound, British Columbia, Canada from March 2017 to November 2017</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 401 for resources[1].url=https://drive.google.com/file/d/12FLUjCgtid772zCGwf322CIGkoNbReug/view</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 404 for resources[1].url=https://drive.google.com/open?id=12Spn0fnOC91dLOahgcf94_lrELHvXFX6</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 404 for resources[1].url=https://www.hakai.org/blog/life-at-hakai/great-walls-quadra</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 2</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>20m Digital Elevation Model - Calvert Island</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Airborne Coastal Observatory' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Big Bar Slide - 2020 - Airborne Coastal Observatory Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Airborne Coastal Observatory' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Airborne Coastal Observatory' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Airborne Coastal Observatory' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Barrette, Jessy' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Barrette, Jessy' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gitanyow Archaeology, Cranberry Junction - 2020 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Darimont, C T' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Ernst, C E' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Evans, Wiley' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Fitzpatrick, O. T.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Froese, Tyrel' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Froese, Tyrel' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gan, Julian C.L.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gan, Julian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gehman, Alyssa' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Giesbrecht, Ian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 2</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Giesbrecht, Ian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gonzalez Arriola, Santiago' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Topographic Basemap</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gonzalez Arriola, Santiago' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>20m Digital Elevation Model - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gonzalez Arriola, Santiago' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Grilliot, Michael' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Science' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Science' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Field Station Structures - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Field Station Structures - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Sensor Network</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Sensor Network</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp Canopy Extent 2006 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Vegetated Islands Polygons - 100 Islands Research</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Topographic Basemap</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Topographic Basemap</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bathymetric Survey - Northwest Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bathymetric Survey - Northwest Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>20m Digital Elevation Model - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>20m Digital Elevation Model - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mount Robson BC Parks Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mount Robson BC Parks Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hyperspectral Imagery - Calvert Island - 2012</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Geology - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Geology - Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Big Bar Slide - 2020 - Airborne Coastal Observatory Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek – Homathko Estuary Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek – Homathko Estuary Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Mapping Coastal British Columbia - 2021 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Mapping Coastal British Columbia - 2021 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Institute' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Institute' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Real-Time Provisional High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected from Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hare, Alex' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 2</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 2</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Haughton, Emily' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Heathfield, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Henderson, Matthew' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Henderson, Matthew' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hessing-Lewis, Margot' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hessing-Lewis, Margot' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Topographic Basemap</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Topographic Basemap</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Holmes, Keith' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Johnson, Brett T.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Johnson, Brett T.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Johnson, Brett' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Johnson, Brett' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Johnson, Brett' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp Canopy Extent 2006 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Keith Holmes, Jenn Burt, Keith Holmes, Jenn Burt' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp Canopy Extent 2006 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Keith Holmes, Jenn Burt, Keith Holmes, Jenn Burt' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Kennedy, J C' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Korver, Maartje C.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Macrocystis kelp canopy productivity data from BC Central Coast, v1.3.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Krumhansl, K.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='LiDAR Research Group, UNBC' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Nutrients (Dosser et al., 2021)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Mackenzie, Chris' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Mai, Thea' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Sensor Network</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='McInnes, Will' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Monteith, Zach' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Nijland, W.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Obrist, Debora S' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Olsen, Angeleen' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Pocock, Katie' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Pocock, Katie' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Pontier, Ondine' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Pontier, Ondine' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Rechsteiner, Erin' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hyperspectral Imagery - Calvert Island - 2012</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Remote Sensing Team, Terra' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reshitnyk, L.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Vegetated Islands Polygons - 100 Islands Research</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reshitnyk, Luba' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Reynolds, J D' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Starzomski, B M' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gitanyow Archaeology, Cranberry Junction - 2020 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gitanyow Archaeology, Cranberry Junction - 2020 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Technology Team, Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Thupaki, Pramod' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bathymetric Survey - Northwest Calvert Island</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Viner, Nick' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Weekes, Carrie' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Wickham, S B' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Coastal Observatory, Airborne' contact['organisation-name']='Airborne Coastal Observatory - Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gitanyow Archaeology, Cranberry Junction - 2020 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Sensor Network</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp Canopy Extent 2006 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Provisional Real-Time Hakai Seafloor Observatory in Hyacinthe Bay, Quadra Island, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hyperspectral Imagery - Calvert Island - 2012</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Vegetated Islands Polygons - 100 Islands Research</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Real-Time Provisional Surface Seawater and Marine Boundary Layer CO2 Observations made from the Kwakshua Channel (KC) Buoy on the central coast of British Columbia</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Real-Time Provisional High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected from Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Topographic Basemap</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>20m Digital Elevation Model - Calvert Island</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Sensor Network</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp Canopy Extent 2006 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Vegetated Islands Polygons - 100 Islands Research</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Topographic Basemap</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 2</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>20m Digital Elevation Model - Calvert Island</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Sensor Network</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp Canopy Extent 2006 - NW Calvert Island</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Vegetated Islands Polygons - 100 Islands Research</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>WARNING</td>
      <td>No publisher</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Broken Group Imagery and LiDAR - 2018 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Atlas, Will' contact.get('organisation-name')='Wild Salmon Centre'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Bidlack, Allison' contact.get('organisation-name')='University of Alaska Southeast'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Burt, J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Burton, Jake' contact.get('organisation-name')='Gwaii Haanas National Park Reserve and Haida Heritage Site'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Clark, Jennifer' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Foreman, Mike' contact.get('organisation-name')='The British Columbia Marine Conservation Analysis'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hyperspectral Imagery - Calvert Island - 2012</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, Gordon' contact.get('organisation-name')='University of Northern British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Godwin, Sean' contact.get('organisation-name')='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Nutrients (Dosser et al., 2021)</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hannah, Charles' contact.get('organisation-name')='Fisheries and Oceans Canada'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Harrington, Christen D.' contact.get('organisation-name')='Alaska Marine Highway, Department of Transportation'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hunt, Brian P.V.' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hunt, Brian' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hunt, Brian' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hunt, Brian' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='James, Sam' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Krkosek, Martin' contact.get('organisation-name')='University of Toronto'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Lebon, Geoffrey T.' contact.get('organisation-name')='NOAA Pacific Marine Environmental Laboratory'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Lee, Lynn C.' contact.get('organisation-name')='Gwaii Haanas National Park Reserve and Haida Heritage Site'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Mahara, Natalie' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Millard-Martin, Ben' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Miller, Becky' contact.get('organisation-name')='University of Victoria'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hyperspectral Imagery - Calvert Island - 2012</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Mostyn, David' contact.get('organisation-name')='Terra Remote Sensing Inc.'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Okamoto, D.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, A. A.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Pakhomov, Evgeny' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Prinzing, Tanya' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Salomon, Anne' contact.get('organisation-name')='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Salomon, Anne' contact.get('organisation-name')='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Timmer, Brian' contact.get('organisation-name')='University Of Victoria'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Waterloo, M. J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='van Meerveld, H. J.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Research Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Research Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Research Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Research Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Research Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='' contact['organisation-name']='Hakai Research Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Atlas, Will' contact['organisation-name']='Wild Salmon Centre'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Foreman, Mike' contact['organisation-name']='The British Columbia Marine Conservation Analysis'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Godwin, Sean' contact['organisation-name']='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Harrington, Christen D.' contact['organisation-name']='Alaska Marine Highway, Department of Transportation'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Hunt, Brian P.V.' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Hunt, Brian' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Hunt, Brian' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Hunt, Brian' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='James, Sam' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Krkosek, Martin' contact['organisation-name']='University of Toronto'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Mahara, Natalie' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Miller, Becky' contact['organisation-name']='University of Victoria'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hyperspectral Imagery - Calvert Island - 2012</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Mostyn, David' contact['organisation-name']='Terra Remote Sensing Inc.'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Salomon, Anne' contact['organisation-name']='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Salomon, Anne' contact['organisation-name']='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Timmer, Brian' contact['organisation-name']='University Of Victoria'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Observations Made from the Kwakshua Channel (KC) Buoy on the Central Coast of British Columbia</td>
      <td>INFO</td>
      <td>DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0208810</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gitanyow Archaeology, Cranberry Junction - 2020 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mean Tidal Current - Coastal British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Field Station Structures - Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Sensor Network</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp Canopy Extent 2006 - NW Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Provisional Real-Time Hakai Seafloor Observatory in Hyacinthe Bay, Quadra Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hyperspectral Imagery - Calvert Island - 2012</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Vegetated Islands Polygons - 100 Islands Research</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai RPAS (Drone) Operations and Methods</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Geology - Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Real-Time Provisional Surface Seawater and Marine Boundary Layer CO2 Observations made from the Kwakshua Channel (KC) Buoy on the central coast of British Columbia</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of 8-m seawater CO2 content entering Fanny Bay Oysters in Baynes Sound, British Columbia, Canada from March 2017 to November 2017</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>UAV Imagery - Coastal British Columbia - 2015</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Big Bar Slide - 2020 - Airborne Coastal Observatory Data</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Observations Made from the Kwakshua Channel (KC) Buoy on the Central Coast of British Columbia</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Broken Group Imagery and LiDAR - 2018 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Topographic Basemap</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 2</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gordon River Archaeology - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>20m Digital Elevation Model - Calvert Island</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bamfield Region UAV Imagery and Surface Model Data</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nuchatlaht Survey - Hakai Airborne Coastal Observatory Imagery and Topography Data - Nootka Island British Columbia - 2023</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute Nutrients (Dosser et al., 2021)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements from Hakai Oceanographic station QU39 from January 2016 to December 2017 in northern Salish Sea, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hyperspectral Imagery - Calvert Island - 2012</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 1</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Sockeye Diets Hakai 2015-2016</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Macrocystis kelp canopy productivity data from BC Central Coast, v1.3.0</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of 8-m seawater CO2 content entering Fanny Bay Oysters in Baynes Sound, British Columbia, Canada from March 2017 to November 2017</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp forest communities along an otter gradient</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mapping Canopy-Forming Kelps in the Northeast Pacific: A Guidebook for Decision-Makers and Practitioners</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 2</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bathymetric Survey - Northwest Calvert Island</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Clam Garden Geospatial Data - Quadra Island - 2016</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</td>
      <td>INFO</td>
      <td>Title contains the word dataset</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Glacier and Icefield Mapping - British Columbia - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and Elevation Models for Monitoring Invertebrates at Intertidal Sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gitanyow Archaeology, Cranberry Junction - 2020 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Seastar & Macroinvertebrate Dynamics - BC Central Coast - 2016-2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mount Robson BC Parks Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements collected during the 2016 National Oceanic and Atmospheric Administration West Coast Ocean Acidification survey (NOAA WCOA2016) from California to British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Killer Whale Foraging Drone Observations - Coastal British Columbia - 2019 & 2020</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Dataset for article: 'Migration timing affects the foraging ecology of Fraser River sockeye salmon stocks in coastal waters of British Columbia, Canada'</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Remotely-Piloted Aerial Systems Imagery, Terrain Data, and Derivates - 100 Islands Project, Central Coast, BC, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Pruth Dock, Calvert Island Tide and Weather Station Provisional</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Google Earth Engine Kelp Tool - Central Coast Output - Version 1.0.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore elevation and imagery models - Quadra Island Hakai Institute Facility Shoreline - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nearshore substrates of the McMullin Group Islands - British Columbia - 2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Depth Measurements from Remotely Piloted Aerial Systems - Mt. Cain - 2018 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Provisional Real-Time Hakai Seafloor Observatory in Hyacinthe Bay, Quadra Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nuchatlaht Survey - Hakai Airborne Coastal Observatory Imagery and Topography Data - Nootka Island British Columbia - 2023</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nereocystis kelp canopy productivity data from BC Central Coast, v1.2.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Adjusted Koeye River stage and temperature from 2013 to 2021</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from June 2017 to April 2019 collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Water column CO2 system measurements from Hakai Oceanographic station QU39 from January 2016 to December 2017 in northern Salish Sea, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 1</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kilbella River Estuary LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Island Food Web Study - Central Coast Islands (100 Islands Project) - April to July 2015, 2016, & 2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Underway surface seawater and marine boundary layer observations made from the Alaska Marine Highway System M/V Columbia from October 2017 to October 2018</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere - Glaciers and Icefields - 2020 - Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Real-Time Provisional Surface Seawater and Marine Boundary Layer CO2 Observations made from the Kwakshua Channel (KC) Buoy on the central coast of British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Bald eagles as vectors of marine nutrients – Central Coast Islands (100 Islands study area) – May – July 2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>30m Digital Elevation Model - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai physical plan and utility lines – Calvert Island Field Station - 2006</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Macrocystis kelp canopy productivity data from BC Central Coast, v1.3.0</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of 8-m seawater CO2 content entering Fanny Bay Oysters in Baynes Sound, British Columbia, Canada from March 2017 to November 2017</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Uncertainty analysis of stage-discharge rating curves for seven rivers at Calvert Island (2013-2015)</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hakai Institute British Columbia Central Coast Fixed Platform Acoustic Doppler Current Profiler Time Series Provisional</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Time-lapse Camera Imagery of Calvert Island Beaches (2012-Present)</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Zooplankton - Taxonomy – Northern Strait of Georgia, Discovery Islands, Johnstone Strait, and Queen Charlotte Strait – April to July 2015 and 2016</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek Landslide – 2022 – Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Elliot Creek – Homathko Estuary Mapping - 2021 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Surface Seawater and Marine Boundary Layer CO2 Observations Made from the Kwakshua Channel (KC) Buoy on the Central Coast of British Columbia</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile salmon migration observations in the Discovery Islands and Johnstone Strait in British Columbia, Canada in 2018</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Marine CO2 system variability along the Inside Passage of the Pacific Northwest coast of North America determined from an Alaskan ferry</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from August 2016 to August 2017 collected in at the OceansAlaska shellfish hatchery in Ketchikan, Alaska, USA</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Sea wrack wet to dry biomass calibrations for macroalgae of the Central Coast of British Columbia - 2018</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Real-Time Provisional High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected from Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Imagery and elevation models monitoring algae research sites - 2017 - Calvert Island - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fountain Valley LiDAR Data - 2019 & 2020 - Hakai Airborne Coastal Observatory - British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Spatial extent of eelgrass (Zostera marina) meadows from monitoring sites within Gwaii Haanas (2016, 2017, 2018) mapped using remote piloted aerial systems</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Broken Group Imagery and LiDAR - 2018 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Mapping Canopy-Forming Kelps in the Northeast Pacific: A Guidebook for Decision-Makers and Practitioners</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Cryosphere LiDAR Mapping - 2020 - Airborne Coastal Observatory -British Columbia - Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fin Island & K'yel - 2020 - Airborne Coastal Observatory Data</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Nanwakolas Watershed Surveys - Knight Inlet - 2019 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Koeye River stream temperature, stage, and conductivity time-series version 2</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of CO2 content from October 2013 to December 2018 measured in seawater entering the Alutiiq Pride Shellfish Hatchery in Seward, Alaska, USA</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Gordon River Archaeology - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Snow Mapping Coastal British Columbia - 2021 - Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-18</td>
      <td>Water Level measured from a Pressure Tide Gauge Instrument Deployed in Choke Pass on Calvert Island Research</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-18</td>
      <td>Water Level measured from a Pressure Tide Gauge Instrument Deployed in Choke Pass on Calvert Island Research</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-18</td>
      <td>8-day average satellite (Sentinel 3A and 3B) chlorophyll and suspended matter concentrations for coastal British Columbia and southeast Alaska</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-17</td>
      <td>Real-Time Provisional High-Resolution Record of Seawater Carbon Dioxide (CO2) Content Collected from the Bamfield Marine Sciences Centre in Bamfield, BC, Canada</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-07-17</td>
      <td>Real-Time Provisional High-Resolution Record of Seawater Carbon Dioxide (CO2) Content Collected from the Bamfield Marine Sciences Centre in Bamfield, BC, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-17</td>
      <td>Spatial extent of surface canopy kelp (Nereocystis luetkeana) derived from fixed-wing surveys (2023), Denman Island to south Quadra Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-17</td>
      <td>Spatial extent of surface canopy kelp (Nereocystis luetkeana) derived from fixed-wing surveys (2023), Denman Island to south Quadra Island, British Columbia, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-17</td>
      <td>Real-Time Provisional High-Resolution Record of Seawater Carbon Dioxide (CO2) Content Collected from the Bamfield Marine Sciences Centre in Bamfield, BC, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>ERROR</td>
      <td>Invalid licence: CC-BY-NC-4.0</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Hakai Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, Research</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Fedje, Bryn' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Smith, Nicole F.' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Crowell, Travis D.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Lepofsky, Dana' contact.get('organisation-name')='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Salomon, Anne K' contact.get('organisation-name')='Simon Fraser University'</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Hakai Bulk and Size-Fractionated Chlorophyll and Phaeopigment Concentrations Collected by Niskin Bottle, Research</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-06-27</td>
      <td>Genetic Stock Identification of Juvenile Sockeye Salmon Captured in the Discovery Islands and Johnstone Strait BC, Canada</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Latham, Steve' contact.get('organisation-name')='Pacific Salmon Commission'</td>
    </tr>
    <tr>
      <td>2024-06-27</td>
      <td>Genetic Stock Identification of Juvenile Sockeye Salmon Captured in the Discovery Islands and Johnstone Strait BC, Canada</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-06-27</td>
      <td>Genetic Stock Identification of Juvenile Sockeye Salmon Captured in the Discovery Islands and Johnstone Strait BC, Canada</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-06-12</td>
      <td>Ecstall Slide - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-06-12</td>
      <td>Ecstall Slide - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-06-12</td>
      <td>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program, Provisional</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-06-12</td>
      <td>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program, Provisional</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
    </tr>
    <tr>
      <td>2024-06-12</td>
      <td>Vertical Water Properties Profiles (CTD) from the Hakai Institute Juvenile Salmon Program, Provisional</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
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