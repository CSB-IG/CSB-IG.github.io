# coding: utf8
import json
import networkx as nx
from Bio import Medline
import time, datetime
from itertools import combinations
import networkx as nx
from networkx.readwrite import json_graph


from Bio import Entrez
Entrez.email='rgarcia@inmegen.gob.mx'


# fetch articles from pubmed
h = Entrez.esearch(db="pubmed", term='Enrique Hernández Lemus', field='author', retmax=200)
r = Entrez.read(h)

medline = []
for Id in r['IdList']:
    h2 = Entrez.efetch(db="pubmed", id=Id, rettype="medline", retmode="text")
    medline += h2.readlines()




# connect mesh terms
g = nx.Graph()
records = Medline.parse( medline )
for r in records:
    # evenly format dates
    if 'CRDT' in r.keys():
        conv = time.strptime( r['CRDT'][0], "%Y/%m/%d %H:%M" )
        r['CRDT'] = datetime.datetime(*conv[:6]) # date created
    if 'DCOM' in r.keys():
        conv = time.strptime( r['DCOM'], "%Y%m%d" )
        r['DCOM'] = datetime.datetime(*conv[:6]) # date completed
    if 'LR' in r.keys():
        conv = time.strptime( r['LR'], "%Y%m%d" )
        r['LR'] = datetime.datetime(*conv[:6]) # date revised
    if 'DEP' in r.keys():
        conv = time.strptime( r['DEP'], "%Y%m%d" )
        r['DEP'] = datetime.datetime(*conv[:6]) # date of electronic publication

    if 'MH' in r:
        for edge in combinations(r['MH'], 2):
            if g.get_edge_data(*edge):
                w = g.get_edge_data(*edge)['w'] + 1
            else:
                w =1
            g.add_edge(*edge, w=w)


# annotate nodes with their degrees
for n in g.degree_iter():
    g.add_node(n[0], {'degree': n[1]})
    
g.remove_node('Humans')
g.remove_node('Animals')

            

# write json output
data = json_graph.node_link_data(g)
s    = json.dumps(data)
with open('csbig_mesh.json','w') as f:
    f.write(s)

