# knowledge-graph

This is a place to share the knowledge graph for this project.

The method and code for creating it is in https://github.com/diatomsRcool/eco-kg and will be iteratively updated over time.

To (re)run this model from a terminal:

```
git clone https://github.com/diatomsRcool/eco-kg

cd eco-kg

python run.py merge merge.yml
```

Documentation about the KGX `tsv` file format can be found [here](https://github.com/biolink/kgx/blob/master/specification/kgx-format.md).

|tsv files|
|-----|
|[merged-kg_edges.tsv](https://data.cyverse.org/dav-anon/iplant/projects/genophenoenvo/kg/merged-kg_edges.tsv)|
|[merged-kg_nodes.tsv](https://data.cyverse.org/dav-anon/iplant/projects/genophenoenvo/kg/merged-kg_nodes.tsv)|

Both files can be downloaded [here](https://www.dropbox.com/s/utavv8n5dxr32vr/merged-kg.tar.gz?dl=0) as compressed 44 MB `tar.gz` tarball. 

The screen shot in this repo shows the output of the terminal after the final merge step. This has some helpful information about the number of nodes and edges merged between different data sources.

The final merge statistics can be found at https://github.com/diatomsRcool/eco-kg/blob/master/merged-kg_stats.yaml
