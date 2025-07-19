---
hide:
 - toc
---
# Hakai Metadata Records Issue Summary

This page present a summary of issues detected on the [Hakai Catalogue]().

## Issue Distribution

```plotly
{"data":[{"alignmentgroup":"True","bingroup":"x","histfunc":"sum","hovertemplate":"level=INFO\u003cbr\u003emessage=%{x}\u003cbr\u003esum of Issue=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"INFO","marker":{"color":"lightblue","pattern":{"shape":""}},"name":"INFO","offsetgroup":"INFO","orientation":"v","showlegend":true,"x":["Contact missing ORCID","Contact missing organization ROR","DOI is not redirecting to Hakai's catalogue","Empty resource name","Invalid distributor organisation-name","Invalid licence","Invalid resource format","Invalid resources.url.status_code","No DOI defined","No funder","No projects associated","No publisher","No version","Record DOI HTTPS link is failling","Record isn't accesible via a standard data repository","Title contains acronyms potentially","Title is greater than 60 characters"],"xaxis":"x","y":[28,8,2,0,0,0,0,0,0,0,0,0,31,0,32,0,36],"yaxis":"y","type":"histogram","textposition":"inside"},{"alignmentgroup":"True","bingroup":"x","histfunc":"sum","hovertemplate":"level=WARNING\u003cbr\u003emessage=%{x}\u003cbr\u003esum of Issue=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"WARNING","marker":{"color":"orange","pattern":{"shape":""}},"name":"WARNING","offsetgroup":"WARNING","orientation":"v","showlegend":true,"x":["Contact missing ORCID","Contact missing organization ROR","DOI is not redirecting to Hakai's catalogue","Empty resource name","Invalid distributor organisation-name","Invalid licence","Invalid resource format","Invalid resources.url.status_code","No DOI defined","No funder","No projects associated","No publisher","No version","Record DOI HTTPS link is failling","Record isn't accesible via a standard data repository","Title contains acronyms potentially","Title is greater than 60 characters"],"xaxis":"x","y":[77,4,0,0,0,0,0,0,7,12,0,5,0,0,0,9,0],"yaxis":"y","type":"histogram","textposition":"inside"},{"alignmentgroup":"True","bingroup":"x","histfunc":"sum","hovertemplate":"level=ERROR\u003cbr\u003emessage=%{x}\u003cbr\u003esum of Issue=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"ERROR","marker":{"color":"red","pattern":{"shape":""}},"name":"ERROR","offsetgroup":"ERROR","orientation":"v","showlegend":true,"x":["Contact missing ORCID","Contact missing organization ROR","DOI is not redirecting to Hakai's catalogue","Empty resource name","Invalid distributor organisation-name","Invalid licence","Invalid resource format","Invalid resources.url.status_code","No DOI defined","No funder","No projects associated","No publisher","No version","Record DOI HTTPS link is failling","Record isn't accesible via a standard data repository","Title contains acronyms potentially","Title is greater than 60 characters"],"xaxis":"x","y":[0,0,0,1,5,1,1,2,0,0,5,0,0,17,0,0,0],"yaxis":"y","type":"histogram","textposition":"inside"}],"layout":{"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{},"tickfont":{"size":10},"linecolor":"black"},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"sum of Issue"}},"legend":{"title":{"text":"level"},"tracegroupgap":0,"font":{"size":10},"orientation":"h","yanchor":"bottom","y":1,"xanchor":"left","x":0,"itemwidth":30},"margin":{"t":60},"barmode":"relative","plot_bgcolor":"rgba(0,0,0,0)","uniformtext":{"minsize":12,"mode":"hide"}}}
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
      <th>40</th>
      <td><a title='1f6380fd-6917-4f64-bdcf-3511fdda73a9' href='../records/1f6380fd-6917-4f64-bdcf-3511fdda73a9' target='_blank'>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_96e3dd9c-7863-44d5-95cd-a3d0a8653d83' target='_blank'>link</a></td>
      <td>2025-05-08</td>
      <td>2025-05-08</td>
      <td><a title='1f6380fd-6917-4f64-bdcf-3511fdda73a9' href='../records/1f6380fd-6917-4f64-bdcf-3511fdda73a9' target='_blank'>2</a></td>
      <td><a title='1f6380fd-6917-4f64-bdcf-3511fdda73a9' href='../records/1f6380fd-6917-4f64-bdcf-3511fdda73a9' target='_blank'>2</a></td>
      <td><a title='1f6380fd-6917-4f64-bdcf-3511fdda73a9' href='../records/1f6380fd-6917-4f64-bdcf-3511fdda73a9' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>39</th>
      <td><a title='e3973346-0462-4cfe-9c00-0d057b1b7a89' href='../records/e3973346-0462-4cfe-9c00-0d057b1b7a89' target='_blank'>Place Glacier Aerial Photo and LiDAR Survey</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_98807d0a-ba68-41e3-a2f5-e3248b459904' target='_blank'>link</a></td>
      <td>2025-04-02</td>
      <td>2025-04-02</td>
      <td><a title='e3973346-0462-4cfe-9c00-0d057b1b7a89' href='../records/e3973346-0462-4cfe-9c00-0d057b1b7a89' target='_blank'>1</a></td>
      <td><a title='e3973346-0462-4cfe-9c00-0d057b1b7a89' href='../records/e3973346-0462-4cfe-9c00-0d057b1b7a89' target='_blank'>3</a></td>
      <td><a title='e3973346-0462-4cfe-9c00-0d057b1b7a89' href='../records/e3973346-0462-4cfe-9c00-0d057b1b7a89' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>38</th>
      <td><a title='cdc17df1-0a25-4d4f-bd10-f0e15ca412b2' href='../records/cdc17df1-0a25-4d4f-bd10-f0e15ca412b2' target='_blank'>Data record does not exist anymore: Geomorphology - Calvert Island</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9fafb4c8-e61f-4372-ac71-c1ddbe57d80c' target='_blank'>link</a></td>
      <td>2025-01-03</td>
      <td>2025-01-03</td>
      <td><a title='cdc17df1-0a25-4d4f-bd10-f0e15ca412b2' href='../records/cdc17df1-0a25-4d4f-bd10-f0e15ca412b2' target='_blank'>2</a></td>
      <td><a title='cdc17df1-0a25-4d4f-bd10-f0e15ca412b2' href='../records/cdc17df1-0a25-4d4f-bd10-f0e15ca412b2' target='_blank'>2</a></td>
      <td><a title='cdc17df1-0a25-4d4f-bd10-f0e15ca412b2' href='../records/cdc17df1-0a25-4d4f-bd10-f0e15ca412b2' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>37</th>
      <td><a title='74623ae6-b474-4709-a426-e84a4d983e84' href='../records/74623ae6-b474-4709-a426-e84a4d983e84' target='_blank'>Larval Dungeness crab abundance and size time series along the coast of British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d4942b86-d362-40a3-9399-c124c4c263bd' target='_blank'>link</a></td>
      <td>2024-11-25</td>
      <td>2025-05-12</td>
      <td><a title='74623ae6-b474-4709-a426-e84a4d983e84' href='../records/74623ae6-b474-4709-a426-e84a4d983e84' target='_blank'>2</a></td>
      <td></td>
      <td><a title='74623ae6-b474-4709-a426-e84a4d983e84' href='../records/74623ae6-b474-4709-a426-e84a4d983e84' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>36</th>
      <td><a title='b2262e15-9109-42d8-bd88-b379c6fb5eb8' href='../records/b2262e15-9109-42d8-bd88-b379c6fb5eb8' target='_blank'>Fraser River Landslide Project - Sites of Concern 2024</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_f25b00ba-ad63-42b3-8021-3fb6aa99baff' target='_blank'>link</a></td>
      <td>2024-11-18</td>
      <td>2024-11-20</td>
      <td><a title='b2262e15-9109-42d8-bd88-b379c6fb5eb8' href='../records/b2262e15-9109-42d8-bd88-b379c6fb5eb8' target='_blank'>4</a></td>
      <td><a title='b2262e15-9109-42d8-bd88-b379c6fb5eb8' href='../records/b2262e15-9109-42d8-bd88-b379c6fb5eb8' target='_blank'>1</a></td>
      <td><a title='b2262e15-9109-42d8-bd88-b379c6fb5eb8' href='../records/b2262e15-9109-42d8-bd88-b379c6fb5eb8' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>35</th>
      <td><a title='e867379a-180c-4b00-b5e6-2f60a6a08203' href='../records/e867379a-180c-4b00-b5e6-2f60a6a08203' target='_blank'>Spatial extent of surface canopy kelp (Nereocystis luetkeana) derived from fixed-wing surveys (2023), Denman Island to south Quadra Island, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b8483c9e-81e6-4e1a-b09f-2d66f8fee9a2' target='_blank'>link</a></td>
      <td>2024-03-15</td>
      <td>2024-07-17</td>
      <td><a title='e867379a-180c-4b00-b5e6-2f60a6a08203' href='../records/e867379a-180c-4b00-b5e6-2f60a6a08203' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>34</th>
      <td><a title='277dcb2c-0fe6-4a45-b774-181a71bbec1b' href='../records/277dcb2c-0fe6-4a45-b774-181a71bbec1b' target='_blank'>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_532c06ad-0b55-4e86-9088-cec970a0a8e1' target='_blank'>link</a></td>
      <td>2023-01-18</td>
      <td>2024-12-05</td>
      <td><a title='277dcb2c-0fe6-4a45-b774-181a71bbec1b' href='../records/277dcb2c-0fe6-4a45-b774-181a71bbec1b' target='_blank'>2</a></td>
      <td><a title='277dcb2c-0fe6-4a45-b774-181a71bbec1b' href='../records/277dcb2c-0fe6-4a45-b774-181a71bbec1b' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>33</th>
      <td><a title='2cfd812a-b031-4cf8-b801-e58dc1331a63' href='../records/2cfd812a-b031-4cf8-b801-e58dc1331a63' target='_blank'>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_e8d36f54-4955-463c-94e5-f0030c3230f3' target='_blank'>link</a></td>
      <td>2023-01-17</td>
      <td>2024-07-12</td>
      <td><a title='2cfd812a-b031-4cf8-b801-e58dc1331a63' href='../records/2cfd812a-b031-4cf8-b801-e58dc1331a63' target='_blank'>6</a></td>
      <td><a title='2cfd812a-b031-4cf8-b801-e58dc1331a63' href='../records/2cfd812a-b031-4cf8-b801-e58dc1331a63' target='_blank'>1</a></td>
      <td><a title='2cfd812a-b031-4cf8-b801-e58dc1331a63' href='../records/2cfd812a-b031-4cf8-b801-e58dc1331a63' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>32</th>
      <td><a title='40dce4cd-a607-4641-9da5-8196ce6678af' href='../records/40dce4cd-a607-4641-9da5-8196ce6678af' target='_blank'>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d049351d-b806-461f-85fb-451f100fd7d6' target='_blank'>link</a></td>
      <td>2022-12-01</td>
      <td>2025-04-23</td>
      <td><a title='40dce4cd-a607-4641-9da5-8196ce6678af' href='../records/40dce4cd-a607-4641-9da5-8196ce6678af' target='_blank'>12</a></td>
      <td><a title='40dce4cd-a607-4641-9da5-8196ce6678af' href='../records/40dce4cd-a607-4641-9da5-8196ce6678af' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>31</th>
      <td><a title='30ca4e7c-9618-4b03-9363-ebc0596155e2' href='../records/30ca4e7c-9618-4b03-9363-ebc0596155e2' target='_blank'>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c89e35df-8a16-4efc-ae29-15f4e3da8a55' target='_blank'>link</a></td>
      <td>2022-10-08</td>
      <td>2024-11-29</td>
      <td><a title='30ca4e7c-9618-4b03-9363-ebc0596155e2' href='../records/30ca4e7c-9618-4b03-9363-ebc0596155e2' target='_blank'>5</a></td>
      <td><a title='30ca4e7c-9618-4b03-9363-ebc0596155e2' href='../records/30ca4e7c-9618-4b03-9363-ebc0596155e2' target='_blank'>2</a></td>
      <td><a title='30ca4e7c-9618-4b03-9363-ebc0596155e2' href='../records/30ca4e7c-9618-4b03-9363-ebc0596155e2' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>30</th>
      <td><a title='fa79cbe9-5333-4723-aaf1-838a5befd0ea' href='../records/fa79cbe9-5333-4723-aaf1-838a5befd0ea' target='_blank'>Mussel Dynamics - Point Intercepts - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cec3dcef-8dba-4d91-aee6-b60ce416497c' target='_blank'>link</a></td>
      <td>2022-10-08</td>
      <td>2024-11-29</td>
      <td><a title='fa79cbe9-5333-4723-aaf1-838a5befd0ea' href='../records/fa79cbe9-5333-4723-aaf1-838a5befd0ea' target='_blank'>5</a></td>
      <td><a title='fa79cbe9-5333-4723-aaf1-838a5befd0ea' href='../records/fa79cbe9-5333-4723-aaf1-838a5befd0ea' target='_blank'>9</a></td>
      <td><a title='fa79cbe9-5333-4723-aaf1-838a5befd0ea' href='../records/fa79cbe9-5333-4723-aaf1-838a5befd0ea' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>28</th>
      <td><a title='521a73f1-1a6a-42ac-8138-e261a7e7f936' href='../records/521a73f1-1a6a-42ac-8138-e261a7e7f936' target='_blank'>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_d05df775-4295-4b9f-b3b3-29fe891d9ed9' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-24</td>
      <td><a title='521a73f1-1a6a-42ac-8138-e261a7e7f936' href='../records/521a73f1-1a6a-42ac-8138-e261a7e7f936' target='_blank'>3</a></td>
      <td><a title='521a73f1-1a6a-42ac-8138-e261a7e7f936' href='../records/521a73f1-1a6a-42ac-8138-e261a7e7f936' target='_blank'>4</a></td>
      <td></td>
    </tr>
    <tr>
      <th>29</th>
      <td><a title='765b3a4d-7a99-4352-bafe-af044f375fdf' href='../records/765b3a4d-7a99-4352-bafe-af044f375fdf' target='_blank'>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9201118a-b0c4-470f-a76f-396bacc5e93e' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2024-07-23</td>
      <td><a title='765b3a4d-7a99-4352-bafe-af044f375fdf' href='../records/765b3a4d-7a99-4352-bafe-af044f375fdf' target='_blank'>3</a></td>
      <td></td>
      <td><a title='765b3a4d-7a99-4352-bafe-af044f375fdf' href='../records/765b3a4d-7a99-4352-bafe-af044f375fdf' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>27</th>
      <td><a title='c681d278-c882-4906-81b3-aec84230ceff' href='../records/c681d278-c882-4906-81b3-aec84230ceff' target='_blank'>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b694a5c5-6a7e-4206-96aa-5b7754323345' target='_blank'>link</a></td>
      <td>2022-03-29</td>
      <td>2025-04-23</td>
      <td><a title='c681d278-c882-4906-81b3-aec84230ceff' href='../records/c681d278-c882-4906-81b3-aec84230ceff' target='_blank'>3</a></td>
      <td><a title='c681d278-c882-4906-81b3-aec84230ceff' href='../records/c681d278-c882-4906-81b3-aec84230ceff' target='_blank'>8</a></td>
      <td></td>
    </tr>
    <tr>
      <th>25</th>
      <td><a title='de7a25e2-9140-44bb-baff-781f49cd0173' href='../records/de7a25e2-9140-44bb-baff-781f49cd0173' target='_blank'>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b5207300-9f76-4f14-ae6f-a08ed6f5a213' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-07-23</td>
      <td><a title='de7a25e2-9140-44bb-baff-781f49cd0173' href='../records/de7a25e2-9140-44bb-baff-781f49cd0173' target='_blank'>4</a></td>
      <td><a title='de7a25e2-9140-44bb-baff-781f49cd0173' href='../records/de7a25e2-9140-44bb-baff-781f49cd0173' target='_blank'>1</a></td>
      <td><a title='de7a25e2-9140-44bb-baff-781f49cd0173' href='../records/de7a25e2-9140-44bb-baff-781f49cd0173' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>24</th>
      <td><a title='e88286d7-1388-4258-a56b-8b5b8be4a293' href='../records/e88286d7-1388-4258-a56b-8b5b8be4a293' target='_blank'>Precipitation time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ef59cc12-5031-4c65-b379-7ca03ad76d34' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-07-24</td>
      <td><a title='e88286d7-1388-4258-a56b-8b5b8be4a293' href='../records/e88286d7-1388-4258-a56b-8b5b8be4a293' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>26</th>
      <td><a title='f63a7bf1-777f-44a0-94d1-4211a9a17cdb' href='../records/f63a7bf1-777f-44a0-94d1-4211a9a17cdb' target='_blank'>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019 Version 4.1</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ed3c5cb4-e6b0-4c8a-808e-3583a9a6cfde' target='_blank'>link</a></td>
      <td>2022-03-25</td>
      <td>2024-12-05</td>
      <td><a title='f63a7bf1-777f-44a0-94d1-4211a9a17cdb' href='../records/f63a7bf1-777f-44a0-94d1-4211a9a17cdb' target='_blank'>4</a></td>
      <td></td>
      <td><a title='f63a7bf1-777f-44a0-94d1-4211a9a17cdb' href='../records/f63a7bf1-777f-44a0-94d1-4211a9a17cdb' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>23</th>
      <td><a title='57bfc450-48a6-4790-a598-e751fde31ee7' href='../records/57bfc450-48a6-4790-a598-e751fde31ee7' target='_blank'>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_9efdd14d-9fb9-4f0e-9414-d890b4e18055' target='_blank'>link</a></td>
      <td>2022-03-15</td>
      <td>2024-07-23</td>
      <td><a title='57bfc450-48a6-4790-a598-e751fde31ee7' href='../records/57bfc450-48a6-4790-a598-e751fde31ee7' target='_blank'>2</a></td>
      <td><a title='57bfc450-48a6-4790-a598-e751fde31ee7' href='../records/57bfc450-48a6-4790-a598-e751fde31ee7' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>22</th>
      <td><a title='0438cf3f-f2b0-419a-aa23-38d27767fe88' href='../records/0438cf3f-f2b0-419a-aa23-38d27767fe88' target='_blank'>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_bef293d6-8721-4214-b8f5-03b5ffb28e1c' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-24</td>
      <td><a title='0438cf3f-f2b0-419a-aa23-38d27767fe88' href='../records/0438cf3f-f2b0-419a-aa23-38d27767fe88' target='_blank'>3</a></td>
      <td><a title='0438cf3f-f2b0-419a-aa23-38d27767fe88' href='../records/0438cf3f-f2b0-419a-aa23-38d27767fe88' target='_blank'>3</a></td>
      <td><a title='0438cf3f-f2b0-419a-aa23-38d27767fe88' href='../records/0438cf3f-f2b0-419a-aa23-38d27767fe88' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>21</th>
      <td><a title='27d7c029-6dc8-499b-96db-670fc86ef98c' href='../records/27d7c029-6dc8-499b-96db-670fc86ef98c' target='_blank'>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_4fac74c8-f58c-46b0-87dc-ab70ce756880' target='_blank'>link</a></td>
      <td>2022-03-11</td>
      <td>2024-07-23</td>
      <td><a title='27d7c029-6dc8-499b-96db-670fc86ef98c' href='../records/27d7c029-6dc8-499b-96db-670fc86ef98c' target='_blank'>3</a></td>
      <td><a title='27d7c029-6dc8-499b-96db-670fc86ef98c' href='../records/27d7c029-6dc8-499b-96db-670fc86ef98c' target='_blank'>6</a></td>
      <td></td>
    </tr>
    <tr>
      <th>19</th>
      <td><a title='2bc069dc-f1e8-4988-a12e-063dfa4c5125' href='../records/2bc069dc-f1e8-4988-a12e-063dfa4c5125' target='_blank'>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5e4f925a-9cf2-4e33-ae22-75c5b326ce6c' target='_blank'>link</a></td>
      <td>2022-03-02</td>
      <td>2024-07-23</td>
      <td><a title='2bc069dc-f1e8-4988-a12e-063dfa4c5125' href='../records/2bc069dc-f1e8-4988-a12e-063dfa4c5125' target='_blank'>3</a></td>
      <td><a title='2bc069dc-f1e8-4988-a12e-063dfa4c5125' href='../records/2bc069dc-f1e8-4988-a12e-063dfa4c5125' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>20</th>
      <td><a title='77360042-77f4-49fc-8ba3-907f95b50d4b' href='../records/77360042-77f4-49fc-8ba3-907f95b50d4b' target='_blank'>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_5c13b300-e172-4010-a6d8-7586b68a3a96' target='_blank'>link</a></td>
      <td>2022-03-02</td>
      <td>2024-07-23</td>
      <td><a title='77360042-77f4-49fc-8ba3-907f95b50d4b' href='../records/77360042-77f4-49fc-8ba3-907f95b50d4b' target='_blank'>3</a></td>
      <td><a title='77360042-77f4-49fc-8ba3-907f95b50d4b' href='../records/77360042-77f4-49fc-8ba3-907f95b50d4b' target='_blank'>2</a></td>
      <td><a title='77360042-77f4-49fc-8ba3-907f95b50d4b' href='../records/77360042-77f4-49fc-8ba3-907f95b50d4b' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>17</th>
      <td><a title='30c73db0-37ff-4790-8f7e-b7b127179308' href='../records/30c73db0-37ff-4790-8f7e-b7b127179308' target='_blank'>Owikeno Basin LiDAR Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a60a0468-3f56-4f22-abd4-5268fcfb9744' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='30c73db0-37ff-4790-8f7e-b7b127179308' href='../records/30c73db0-37ff-4790-8f7e-b7b127179308' target='_blank'>2</a></td>
      <td><a title='30c73db0-37ff-4790-8f7e-b7b127179308' href='../records/30c73db0-37ff-4790-8f7e-b7b127179308' target='_blank'>9</a></td>
      <td><a title='30c73db0-37ff-4790-8f7e-b7b127179308' href='../records/30c73db0-37ff-4790-8f7e-b7b127179308' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>15</th>
      <td><a title='8bd510f9-09a0-4c18-8367-a6b77578c713' href='../records/8bd510f9-09a0-4c18-8367-a6b77578c713' target='_blank'>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c3eff62f-bcee-4faa-a7e1-7b9380d94e74' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='8bd510f9-09a0-4c18-8367-a6b77578c713' href='../records/8bd510f9-09a0-4c18-8367-a6b77578c713' target='_blank'>2</a></td>
      <td><a title='8bd510f9-09a0-4c18-8367-a6b77578c713' href='../records/8bd510f9-09a0-4c18-8367-a6b77578c713' target='_blank'>3</a></td>
      <td><a title='8bd510f9-09a0-4c18-8367-a6b77578c713' href='../records/8bd510f9-09a0-4c18-8367-a6b77578c713' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>18</th>
      <td><a title='dd36f4af-b377-4abd-bdcd-194698209a70' href='../records/dd36f4af-b377-4abd-bdcd-194698209a70' target='_blank'>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_95bee6a0-ae38-4427-b5b2-5cc5835df70d' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='dd36f4af-b377-4abd-bdcd-194698209a70' href='../records/dd36f4af-b377-4abd-bdcd-194698209a70' target='_blank'>2</a></td>
      <td><a title='dd36f4af-b377-4abd-bdcd-194698209a70' href='../records/dd36f4af-b377-4abd-bdcd-194698209a70' target='_blank'>8</a></td>
      <td><a title='dd36f4af-b377-4abd-bdcd-194698209a70' href='../records/dd36f4af-b377-4abd-bdcd-194698209a70' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>16</th>
      <td><a title='e83af7c3-d1bf-4292-83d0-680607ab27ae' href='../records/e83af7c3-d1bf-4292-83d0-680607ab27ae' target='_blank'>Moore Island Archaeology Survey - 2019 - Airborne Coastal Observatory</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_c3958106-fc49-44bd-8227-bfc3e8bcb58c' target='_blank'>link</a></td>
      <td>2022-03-01</td>
      <td>2024-07-23</td>
      <td><a title='e83af7c3-d1bf-4292-83d0-680607ab27ae' href='../records/e83af7c3-d1bf-4292-83d0-680607ab27ae' target='_blank'>2</a></td>
      <td><a title='e83af7c3-d1bf-4292-83d0-680607ab27ae' href='../records/e83af7c3-d1bf-4292-83d0-680607ab27ae' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>14</th>
      <td><a title='e1bbfc23-d529-4b5a-88bf-5bf2b25e4c00' href='../records/e1bbfc23-d529-4b5a-88bf-5bf2b25e4c00' target='_blank'>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a0263680-f0d5-46d5-85ea-483fa58c74b6' target='_blank'>link</a></td>
      <td>2022-02-04</td>
      <td>2024-07-23</td>
      <td><a title='e1bbfc23-d529-4b5a-88bf-5bf2b25e4c00' href='../records/e1bbfc23-d529-4b5a-88bf-5bf2b25e4c00' target='_blank'>3</a></td>
      <td><a title='e1bbfc23-d529-4b5a-88bf-5bf2b25e4c00' href='../records/e1bbfc23-d529-4b5a-88bf-5bf2b25e4c00' target='_blank'>3</a></td>
      <td><a title='e1bbfc23-d529-4b5a-88bf-5bf2b25e4c00' href='../records/e1bbfc23-d529-4b5a-88bf-5bf2b25e4c00' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>13</th>
      <td><a title='1c64dcdb-6bbc-496f-8038-6c631c1a3970' href='../records/1c64dcdb-6bbc-496f-8038-6c631c1a3970' target='_blank'>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a72c43e2-5b4d-4d56-89d4-464b4c513710' target='_blank'>link</a></td>
      <td>2022-02-03</td>
      <td>2024-07-24</td>
      <td><a title='1c64dcdb-6bbc-496f-8038-6c631c1a3970' href='../records/1c64dcdb-6bbc-496f-8038-6c631c1a3970' target='_blank'>3</a></td>
      <td></td>
      <td><a title='1c64dcdb-6bbc-496f-8038-6c631c1a3970' href='../records/1c64dcdb-6bbc-496f-8038-6c631c1a3970' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>12</th>
      <td><a title='9b5bf504-c1aa-4f00-ae16-7b87701eba0a' href='../records/9b5bf504-c1aa-4f00-ae16-7b87701eba0a' target='_blank'>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_63765cc6-5730-4a28-9d96-3de38066312f' target='_blank'>link</a></td>
      <td>2022-02-03</td>
      <td>2024-07-23</td>
      <td><a title='9b5bf504-c1aa-4f00-ae16-7b87701eba0a' href='../records/9b5bf504-c1aa-4f00-ae16-7b87701eba0a' target='_blank'>3</a></td>
      <td><a title='9b5bf504-c1aa-4f00-ae16-7b87701eba0a' href='../records/9b5bf504-c1aa-4f00-ae16-7b87701eba0a' target='_blank'>4</a></td>
      <td><a title='9b5bf504-c1aa-4f00-ae16-7b87701eba0a' href='../records/9b5bf504-c1aa-4f00-ae16-7b87701eba0a' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>11</th>
      <td><a title='7d3f25e0-cc38-419b-bca9-051f8d8569fa' href='../records/7d3f25e0-cc38-419b-bca9-051f8d8569fa' target='_blank'>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_a0ca5d26-b457-4726-97d4-ed0c8dd6cd99' target='_blank'>link</a></td>
      <td>2022-02-02</td>
      <td>2024-07-24</td>
      <td><a title='7d3f25e0-cc38-419b-bca9-051f8d8569fa' href='../records/7d3f25e0-cc38-419b-bca9-051f8d8569fa' target='_blank'>6</a></td>
      <td><a title='7d3f25e0-cc38-419b-bca9-051f8d8569fa' href='../records/7d3f25e0-cc38-419b-bca9-051f8d8569fa' target='_blank'>3</a></td>
      <td></td>
    </tr>
    <tr>
      <th>10</th>
      <td><a title='bae4b824-6150-454b-b862-fa6b0034f3da' href='../records/bae4b824-6150-454b-b862-fa6b0034f3da' target='_blank'>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2019</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_dc50a22a-44c0-478c-aa19-a46343bc764a' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2024-08-02</td>
      <td><a title='bae4b824-6150-454b-b862-fa6b0034f3da' href='../records/bae4b824-6150-454b-b862-fa6b0034f3da' target='_blank'>2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>9</th>
      <td><a title='d5301037-93d9-4d8e-9e27-ac1a5676a444' href='../records/d5301037-93d9-4d8e-9e27-ac1a5676a444' target='_blank'>Pacific Northwest Eelgrass Sediment Carbon Data</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_b4cac70e-a6fa-4d77-8fdb-1d3612006bc4' target='_blank'>link</a></td>
      <td>2022-01-24</td>
      <td>2025-04-23</td>
      <td><a title='d5301037-93d9-4d8e-9e27-ac1a5676a444' href='../records/d5301037-93d9-4d8e-9e27-ac1a5676a444' target='_blank'>6</a></td>
      <td><a title='d5301037-93d9-4d8e-9e27-ac1a5676a444' href='../records/d5301037-93d9-4d8e-9e27-ac1a5676a444' target='_blank'>4</a></td>
      <td><a title='d5301037-93d9-4d8e-9e27-ac1a5676a444' href='../records/d5301037-93d9-4d8e-9e27-ac1a5676a444' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>8</th>
      <td><a title='7a855654-e7b7-4e4e-aeac-301b47e893e4' href='../records/7a855654-e7b7-4e4e-aeac-301b47e893e4' target='_blank'>Kelp Field Data for Remote Sensing - BC Central Coast</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_94b4992f-19e2-46d4-875e-f0c952ea62f7' target='_blank'>link</a></td>
      <td>2022-01-17</td>
      <td>2024-07-24</td>
      <td><a title='7a855654-e7b7-4e4e-aeac-301b47e893e4' href='../records/7a855654-e7b7-4e4e-aeac-301b47e893e4' target='_blank'>2</a></td>
      <td><a title='7a855654-e7b7-4e4e-aeac-301b47e893e4' href='../records/7a855654-e7b7-4e4e-aeac-301b47e893e4' target='_blank'>1</a></td>
      <td><a title='7a855654-e7b7-4e4e-aeac-301b47e893e4' href='../records/7a855654-e7b7-4e4e-aeac-301b47e893e4' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>7</th>
      <td><a title='10fdd7a8-f733-496e-ab52-c7109504b710' href='../records/10fdd7a8-f733-496e-ab52-c7109504b710' target='_blank'>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ea6c0e20-9b99-48f7-adfb-6c1b70f6bd2a' target='_blank'>link</a></td>
      <td>2022-01-13</td>
      <td>2024-07-23</td>
      <td><a title='10fdd7a8-f733-496e-ab52-c7109504b710' href='../records/10fdd7a8-f733-496e-ab52-c7109504b710' target='_blank'>5</a></td>
      <td><a title='10fdd7a8-f733-496e-ab52-c7109504b710' href='../records/10fdd7a8-f733-496e-ab52-c7109504b710' target='_blank'>5</a></td>
      <td><a title='10fdd7a8-f733-496e-ab52-c7109504b710' href='../records/10fdd7a8-f733-496e-ab52-c7109504b710' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>6</th>
      <td><a title='152454fc-1b67-4980-a8c2-6853616936b4' href='../records/152454fc-1b67-4980-a8c2-6853616936b4' target='_blank'>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ee2791c3-3d99-41e5-8cdf-fa5d1d19944d' target='_blank'>link</a></td>
      <td>2021-12-02</td>
      <td>2024-07-23</td>
      <td><a title='152454fc-1b67-4980-a8c2-6853616936b4' href='../records/152454fc-1b67-4980-a8c2-6853616936b4' target='_blank'>3</a></td>
      <td><a title='152454fc-1b67-4980-a8c2-6853616936b4' href='../records/152454fc-1b67-4980-a8c2-6853616936b4' target='_blank'>1</a></td>
      <td><a title='152454fc-1b67-4980-a8c2-6853616936b4' href='../records/152454fc-1b67-4980-a8c2-6853616936b4' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>5</th>
      <td><a title='220c76b1-88b1-4b19-a7d6-99123de85d30' href='../records/220c76b1-88b1-4b19-a7d6-99123de85d30' target='_blank'>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_eb1feb98-b11a-4663-b7ab-2216df8187bd' target='_blank'>link</a></td>
      <td>2021-11-19</td>
      <td>2024-07-23</td>
      <td><a title='220c76b1-88b1-4b19-a7d6-99123de85d30' href='../records/220c76b1-88b1-4b19-a7d6-99123de85d30' target='_blank'>5</a></td>
      <td><a title='220c76b1-88b1-4b19-a7d6-99123de85d30' href='../records/220c76b1-88b1-4b19-a7d6-99123de85d30' target='_blank'>5</a></td>
      <td><a title='220c76b1-88b1-4b19-a7d6-99123de85d30' href='../records/220c76b1-88b1-4b19-a7d6-99123de85d30' target='_blank'>1</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a title='75656423-abb5-46cd-b0af-a9cf2379030b' href='../records/75656423-abb5-46cd-b0af-a9cf2379030b' target='_blank'>QU5M Oceanographic Mooring in Hyacinthe Bay, Quadra Island, Provisional</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_7ddae37a-e706-45d2-8060-8306300a98c8' target='_blank'>link</a></td>
      <td>2021-10-20</td>
      <td>2024-08-21</td>
      <td><a title='75656423-abb5-46cd-b0af-a9cf2379030b' href='../records/75656423-abb5-46cd-b0af-a9cf2379030b' target='_blank'>2</a></td>
      <td><a title='75656423-abb5-46cd-b0af-a9cf2379030b' href='../records/75656423-abb5-46cd-b0af-a9cf2379030b' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a title='c0fc3026-26de-4c95-8685-837552c39901' href='../records/c0fc3026-26de-4c95-8685-837552c39901' target='_blank'>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_1aeeb145-8112-4268-afc7-05f14c8eae63' target='_blank'>link</a></td>
      <td>2021-10-20</td>
      <td>2024-07-24</td>
      <td><a title='c0fc3026-26de-4c95-8685-837552c39901' href='../records/c0fc3026-26de-4c95-8685-837552c39901' target='_blank'>3</a></td>
      <td></td>
      <td><a title='c0fc3026-26de-4c95-8685-837552c39901' href='../records/c0fc3026-26de-4c95-8685-837552c39901' target='_blank'>2</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a title='2190b7fe-9430-4550-83c1-142a6a9eee2e' href='../records/2190b7fe-9430-4550-83c1-142a6a9eee2e' target='_blank'>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_ab901b46-43f6-4044-b0c3-b5fd825622f4' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-24</td>
      <td><a title='2190b7fe-9430-4550-83c1-142a6a9eee2e' href='../records/2190b7fe-9430-4550-83c1-142a6a9eee2e' target='_blank'>3</a></td>
      <td><a title='2190b7fe-9430-4550-83c1-142a6a9eee2e' href='../records/2190b7fe-9430-4550-83c1-142a6a9eee2e' target='_blank'>2</a></td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a title='63dce394-08c9-47f9-9251-b5ee4ae0cde5' href='../records/63dce394-08c9-47f9-9251-b5ee4ae0cde5' target='_blank'>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_cf7a6149-b34a-404c-88e1-c556bf361408' target='_blank'>link</a></td>
      <td>2021-09-23</td>
      <td>2024-07-24</td>
      <td><a title='63dce394-08c9-47f9-9251-b5ee4ae0cde5' href='../records/63dce394-08c9-47f9-9251-b5ee4ae0cde5' target='_blank'>3</a></td>
      <td><a title='63dce394-08c9-47f9-9251-b5ee4ae0cde5' href='../records/63dce394-08c9-47f9-9251-b5ee4ae0cde5' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>0</th>
      <td><a title='51e844ed-bf2f-44cf-b53e-cd81547e77fd' href='../records/51e844ed-bf2f-44cf-b53e-cd81547e77fd' target='_blank'>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_fe76ef4c-254a-44fe-87bc-052cd3aa9663' target='_blank'>link</a></td>
      <td>2021-03-31</td>
      <td>2024-07-24</td>
      <td><a title='51e844ed-bf2f-44cf-b53e-cd81547e77fd' href='../records/51e844ed-bf2f-44cf-b53e-cd81547e77fd' target='_blank'>3</a></td>
      <td><a title='51e844ed-bf2f-44cf-b53e-cd81547e77fd' href='../records/51e844ed-bf2f-44cf-b53e-cd81547e77fd' target='_blank'>1</a></td>
      <td></td>
    </tr>
    <tr>
      <th>41</th>
      <td><a title='c3b43863-c64a-4c9f-a8a9-b4dbd4f2d75c' href='../records/c3b43863-c64a-4c9f-a8a9-b4dbd4f2d75c' target='_blank'>Mount Robson Aerial Photo and LiDAR Survey</a></td>
      <td><a href='https://catalogue.hakai.org/dataset/ca-cioos_66fbb7f5-3644-471a-95ee-f8d3758e888b' target='_blank'>link</a></td>
      <td></td>
      <td>2025-04-02</td>
      <td><a title='c3b43863-c64a-4c9f-a8a9-b4dbd4f2d75c' href='../records/c3b43863-c64a-4c9f-a8a9-b4dbd4f2d75c' target='_blank'>1</a></td>
      <td><a title='c3b43863-c64a-4c9f-a8a9-b4dbd4f2d75c' href='../records/c3b43863-c64a-4c9f-a8a9-b4dbd4f2d75c' target='_blank'>3</a></td>
      <td><a title='c3b43863-c64a-4c9f-a8a9-b4dbd4f2d75c' href='../records/c3b43863-c64a-4c9f-a8a9-b4dbd4f2d75c' target='_blank'>1</a></td>
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
      <td>2025-05-12</td>
      <td>Larval Dungeness crab abundance and size time series along the coast of British Columbia</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/36hp-7f40 status_code=502</td>
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
      <td>Glacier and Ice Aerial Surveys in British Columbia - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/n3b4-d226 status_code=502</td>
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
      <td>2025-04-23</td>
      <td>Pacific Northwest Eelgrass Sediment Carbon Data</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/20SJ-J017 status_code=502</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Brunsting, Ray' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Floyd, William C.' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
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
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
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
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0247208</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
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
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>Air temperature and relative humidity time-series – Central Coast and Quadra Island – 2013 - 2019 Version 1.0</td>
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
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2025-04-23</td>
      <td>High-resolution record of surface seawater carbon dioxide (CO2) content, water temperature, sea surface salinity and other parameters collected in Sitka Harbor, Alaska, USA</td>
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
      <td>Place Glacier Aerial Photo and LiDAR Survey</td>
      <td>ERROR</td>
      <td>Invalid resource format: resources[0].format=JSON</td>
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
      <td>2025-01-03</td>
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>ERROR</td>
      <td>No projects associated</td>
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
      <td>Data record does not exist anymore: Geomorphology - Calvert Island</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019 Version 4.1</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/zvwf-qn04 status_code=502</td>
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
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Title contains acronyms potentially</td>
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
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Observed stream flow from seven small coastal watersheds in British Columbia, Canada, Sept 2013 – April 2019 Version 4.1</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-12-05</td>
      <td>Snow Mapping LiDAR Survey - 2022 - Hakai Airborne Coastal Observatory</td>
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
      <td>2024-11-29</td>
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/0yk3-9b74 status_code=502</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/ns9h-1126 status_code=502</td>
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
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gehman, Alyssa' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hessing-Lewis, Margot' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Jordinson, Eva' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Monteith, Zach' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Contact missing ORCID: contact['individual-name']='Olsen, Angeleen' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
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
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Clark, Jennifer' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-11-29</td>
      <td>Mussel Dynamics - Point Intercepts - BC Central Coast</td>
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
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')=''</td>
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
      <td>Surfgrass Communities - Motile Invertebrate Surveys - BC Central Coast</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
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
      <td>2024-08-21</td>
      <td>QU5M Oceanographic Mooring in Hyacinthe Bay, Quadra Island, Provisional</td>
      <td>WARNING</td>
      <td>No DOI defined</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>QU5M Oceanographic Mooring in Hyacinthe Bay, Quadra Island, Provisional</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-08-21</td>
      <td>QU5M Oceanographic Mooring in Hyacinthe Bay, Quadra Island, Provisional</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2019</td>
      <td>INFO</td>
      <td>Record isn't accesible via a standard data repository</td>
    </tr>
    <tr>
      <td>2024-08-02</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2019</td>
      <td>INFO</td>
      <td>Title is greater than 60 characters</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/1.715756 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/rf3y-8j78 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Kelp Field Data for Remote Sensing - BC Central Coast</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/tqj2-wh77 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/ywpm-xf34 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>LIDAR Derived Forest Metrics - Calvert Island - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Frazer, G.W.' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Northwest Calvert sea wrack temporal data, Central Coast, British Columbia (2016-2017)</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hakai Geospatial Technology Team' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hare, Alex' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>WARNING</td>
      <td>No funder</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
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
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Haggarty, D' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hessing-Lewis, Margot' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Juanes, Francis' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>DOI is not redirecting to Hakai's catalogue: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0208638</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
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
      <td>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</td>
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
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
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
      <td>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
      <td>INFO</td>
      <td>No version</td>
    </tr>
    <tr>
      <td>2024-07-24</td>
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
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
      <td>Surface water CO2 parameters collected by shellfish growers and partners in the northern Salish Sea from 2016 to 2018</td>
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
      <td>Jellyfish Monitoring UAV Imagery - Pruth Bay - Calvert Island - British Columbia - Canada</td>
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
      <td>Surfgrass Community Structure - Length & Density - BC Central Coast - 2017-2019</td>
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
      <td>Seascape connectivity data from a sub-tidal Zostera marina meadow, Choked Passage, Calvert Island, 2015</td>
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
      <td>World View 2 Imagery - Coverage of three regions of the BC Central Coast - Summer 2014, 2015, & 2016</td>
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
      <td>High-Resolution Record of Surface Seawater Carbon Dioxide (CO2) Content Collected From Hakai Institute Quadra Island Field Station in Hyacinthe Bay, British Columbia, Canada</td>
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
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>ERROR</td>
      <td>Invalid distributor organisation-name: organization_name='University of British Columbia' expects 'Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 401 for resources[0].url=https://drive.google.com/file/d/1w7TLX1RIP6F6S_inRKU3x-A27srXzFSa/view?usp=sharing</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
      <td>ERROR</td>
      <td>Invalid resources.url.status_code: 502 for resources[1].url=http://dx.doi.org/10.21966/1.614670</td>
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
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>ERROR</td>
      <td>No projects associated</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/66x5-a210 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Fatty acids of particulate matter collected from 2015 to 2018 near Quadra Island, British Columbia, Canada</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/RR8V-6Y52 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/eysg-7a26 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Particulate organic matter composition for freshwater and marine stations from 2015 through 2018 on the Central Coast, British Columbia, Canada.</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/hpqq-0k76 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/kg0p-mt85 status_code=502</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/yk87-4x24 status_code=502</td>
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
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Coastal Observatory, Airborne' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Gan, Julian C.L.' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Hall, Kyle' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='LiDAR Research Group, UNBC' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Mai, Thea' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Hunter Island UAV Survey - June 2016 - British Columbia - Canada</td>
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
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Pocock, Katie' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Rechsteiner, Erin' contact.get('organisation-name')='Hakai Institute'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='Sadlier-Brown, Gillian' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>WARNING</td>
      <td>Contact missing ORCID: contact['individual-name']='VanMaanen, Derek' contact.get('organisation-name')='Hakai Institute'</td>
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
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
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
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
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
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
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
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
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
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
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
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
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
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Clark, Jennifer' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Hunt, Brian P.V.' contact.get('organisation-name')='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Oliver, A. A.' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Barnacle Dynamics: Point Intercept Surveys - BC Central Coast - 2016-2018</td>
      <td>INFO</td>
      <td>Contact missing ORCID: contact['individual-name']='Prinzing, Tanya' contact.get('organisation-name')=''</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Juvenile Salmon Migration Observations from the Hakai Institute Juvenile Salmon Program in the Discovery Islands in British Columbia, Canada in 2020</td>
      <td>INFO</td>
      <td>Contact missing organization ROR:  contact['individual-name']='Hunt, Brian P.V.' contact['organisation-name']='University of British Columbia'</td>
    </tr>
    <tr>
      <td>2024-07-23</td>
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
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
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
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
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
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
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
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
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
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
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
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
      <td>High-resolution record of surface seawater CO2 content from April 2016 to November 2017 collected in Hyacinthe Bay, British Columbia, Canada</td>
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
      <td>Eelgrass (Z. marina) extent at sites along the Central Coast, British Columbia</td>
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
      <td>High-resolution record of sea surface nitrate at Sentry Shoal in the Northern Strait of Georgia, British Columbia, Canada from 2015 to 2017.</td>
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
      <td>Discovery Islands LiDAR Dataset  - 2014 - British Columbia - Canada</td>
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
      <td>North Vancouver Island Survey - 2019 - Airborne Coastal Observatory</td>
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
      <td>Kelp extent for the McNaughton Group Islands (2017), Manley Island (2017), and Serpent Group Islands (2016), British Columbia, Canada</td>
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
      <td>Organic Carbon at Land-Ocean Interface - Calvert Island - 2014-2016</td>
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
      <td>Ancient Forest Wetlands, BC - Upper Fraser River - 2019 - Airborne Coastal Observatory</td>
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
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>ERROR</td>
      <td>Invalid licence: CC-BY-NC-4.0</td>
    </tr>
    <tr>
      <td>2024-07-12</td>
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
      <td>ERROR</td>
      <td>Record DOI HTTPS link is failling: https://doi.org/10.21966/hy20-x379 status_code=502</td>
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
      <td>Ancestral sea gardens supported human settlements for at least 3800 years on the Northwest Coast of North America</td>
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