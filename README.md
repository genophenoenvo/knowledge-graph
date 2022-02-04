# knowledge-graph

This is a place to share the knowledge graph for this project.

The method and code for creating it is in https://github.com/diatomsRcool/eco-kg and will be iteratively updated over time.

To (re)run this model from a terminal:

```
# create Conda environment

$ conda env create -f environment.yml

$ conda activate genophenoenvo

# if already created, update it

$ conda env update -f environment.yml

# check Python version -- tested on v3.8.5

$ python --version

# install requirements

$ pip install git+https://github.com/OntoGene/OGER.git pyyaml kgx

# clone eco-kg repo

$ git clone https://github.com/diatomsRcool/eco-kg

# change directory

$ cd eco-kg

# copy data

$ mkdir data
$ python run.py download

# run model

$python run.py merge
```

Documentation about the KGX `tsv` file format can be found [here](https://github.com/biolink/kgx/blob/master/specification/kgx-format.md).

|tsv files|
|-----|
|[merged-kg_edges.tsv](https://data.cyverse.org/dav-anon/iplant/projects/genophenoenvo/kg/merged-kg_edges.tsv)|
|[merged-kg_nodes.tsv](https://data.cyverse.org/dav-anon/iplant/projects/genophenoenvo/kg/merged-kg_nodes.tsv)|

Both files can be downloaded [here](https://www.dropbox.com/s/utavv8n5dxr32vr/merged-kg.tar.gz?dl=0) as compressed 44 MB `tar.gz` tarball. 

The screenshot shows some helfpul statistics about the number of nodes and edges added from each resource.

The final merge statistics can be found at https://github.com/diatomsRcool/eco-kg/blob/master/merged-kg_stats.yaml
