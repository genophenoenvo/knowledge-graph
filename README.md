# knowledge-graph

This is a place to share the knowledge graph for this project.

The method and code for creating the Knowledge Graph are originally from https://github.com/diatomsRcool/eco-kg.

For this repository we have made minor changes

They will be iteratively updated over time.

## Installation

First, clone this repository to the location wou want to run the program.

To (re)run this model from a terminal:

```
$ git clone https://github.com/genophenoenvo/knowledge-graph

$ cd knowledgege-graph
```

Next, create an environment for running the graph using `conda` or `mamba`

```
# create a Conda environment using the provided environment.yml

$ mamba env create -f environment.yml

$ conda activate genophenoenvo

# if already created, update it

$ conda env update -f environment.yml

# check Python version -- tested on v3.8.5

$ python --version
```

After the environment has been tested, 

```
# change directory

$ cd knowledgege-graph

# Create a data directory and pull the compressed tsv files

$ mkdir -p data/merged

$ wget https://www.dropbox.com/s/utavv8n5dxr32vr/merged-kg.tar.gz data/merged/

# run download on the rest of the datasets
$ python run.py download

# run transform

$ python run.py transform
# run model

$ python run.py merge
```

Documentation about the KGX `tsv` file format can be found [here](https://github.com/biolink/kgx/blob/master/specification/kgx-format.md).

|tsv files|
|---------|
|[merged-kg_edges.tsv](https://data.cyverse.org/dav-anon/iplant/projects/genophenoenvo/kg/merged-kg_edges.tsv)|
|[merged-kg_nodes.tsv](https://data.cyverse.org/dav-anon/iplant/projects/genophenoenvo/kg/merged-kg_nodes.tsv)|

Both files can be downloaded [here](https://www.dropbox.com/s/utavv8n5dxr32vr/merged-kg.tar.gz?dl=0) as compressed 44 MB `tar.gz` tarball. 

The screenshot shows some helfpul statistics about the number of nodes and edges added from each resource.

The final merge statistics can be found at https://github.com/diatomsRcool/eco-kg/blob/master/merged-kg_stats.yaml
