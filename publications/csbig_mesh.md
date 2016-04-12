---
layout: page
---


<style>
      .node {
      stroke: #cce0ff;
      fill: #ffc;
      stroke-width: 1.9px;
      }

      .link {
      stroke: #999;
      stroke-opacity: 0.3;
      }

      #chart {
      border: 0px solid #aaa;
      width: 800px;
      height: 800px;
      background-color: #Fff;
      }
</style>

<script src="https://d3js.org/d3.v3.min.js" charset="utf-8"></script>



# MeSH Term Network

These are MeSH terms related to [this search](https://www.ncbi.nlm.nih.gov/pubmed/?term=Enrique+Hern%C3%A1ndez+Lemus). Terms are connected if they appear together in an article. Node size represents degree. The terms "Animals" and "Humans" have been removed for clarity.


Have a look at the [source code](https://github.com/CSB-IG/CSB-IG.github.io/tree/master/publications).


<div id="chart">
</div>

<script src="../csbig_mesh.js"></script>
