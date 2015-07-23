---
author: guillermodeandajauregui, rgarcia-herrera
layout: post
description: "Current events in the PXAT development effort"
robots: none
title: PXAT development
---

We're working on the
[Pathway X-talk Analysis Toolkit](http://github.com/CSB-IG/pxat/)
(PXAT).

We're using Biopython to parse kgml files from KEGG into NetworkX
graphs. We then merge these graphs to build an extended KEGG network,
as a nice networkx object. We plan to analyze the crosstalk events
among several pathways.

<ims src="https://github.com/CSB-IG/pxat/raw/master/pxatline.png">

So far we have a pretty large network, a tool that will annotate nodes
according to their place in the topology of the network, an export
tool that will write a NetworkX edgelist, GML format and a TSV file.

We also did some visualization using the fine Pyveplot, but we're not
ready to show it.

Finally we wrote a function that will return the Jaccard Index of
similarity of two pathways, and did some cursory exploration of
trajectories using NetworkX's "all_simple_paths" method.

Cheers mate! Share and enjoy.
