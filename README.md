# knowledge-graph

This is a place to share the knowledge graph for this project.

The method and code for creating the Knowledge Graph are originally from https://github.com/diatomsRcool/eco-kg.

For this repository we have made minor changes. These will be iteratively updated over time.

## Prerequisites

* Basic understanding of Python
* Basic understanding of Docker containers
* Familiarity with what a graph database is 
* Know how to construct a property graph data model 
* Basics of the Cypher query language. 

## Installation

First, clone this GitHub repository to the location where you intend to serve the data from.

To (re)run or regenerate this model from a CLI terminal:

```bash
git clone https://github.com/genophenoenvo/knowledge-graph

cd knowledge-graph
```

### Create a Python Environment with Conda

Next, create an environment for running the graph using `conda` or `mamba`

```bash
# create a Conda environment using the provided environment.yml

conda install -c conda-forge mamba

mamba env create -f environment.yml

conda init bash

exit
```

Open a new temerminal and activate the new environemnt

```bash
conda activate genophenoenvo
```

```bash
# if already created, update the environment
conda env update -f environment.yml

# check Python version -- tested on v3.8.5
python --version
```

## Download the data

After the environment has been tested, 

```bash
# change directory

cd knowledge-graph

# Create a data directory and pull the compressed tsv files

mkdir -p data/merged

wget wget https://data.cyverse.org/dav-anon/iplant/commons/community_released/genophenoenvo/kg/merged-kg_edges.tsv -O ./data/merged/edges.tsv
wget https://data.cyverse.org/dav-anon/iplant/commons/community_released/genophenoenvo/kg/merged-kg_nodes.tsv -O ./data/merged/nodes.tsv


## (re)Generate the Graphs
```
# run download on the rest of the datasets
python run.py download

```

```
# run transform
python run.py transform
```
# run model
python run.py merge
```

Documentation about the KGX `tsv` file format can be found [here](https://github.com/biolink/kgx/blob/master/specification/kgx-format.md).

## Merged TSF files on CyVerse

|.tsv files|
|----------|
|[merged-kg_edges.tsv](https://data.cyverse.org/dav-anon/iplant/projects/genophenoenvo/kg/merged-kg_edges.tsv)|
|[merged-kg_nodes.tsv](https://data.cyverse.org/dav-anon/iplant/projects/genophenoenvo/kg/merged-kg_nodes.tsv)|

The screenshot shows some helfpul statistics about the number of nodes and edges added from each resource.

The final merge statistics can be found at https://github.com/genophenoenvo/knowledge-graph/blob/main/merged-kg_stats.yaml

## Visualization of the Graph in Neo4J

Download the `edges` and `nodes` data from the [CyVerse Data Commons WebDav](https://data.cyverse.org/dav-anon/iplant/commons/community_released/genophenoenvo):

```
cd
cd ~/knowledge-graph/
wget https://data.cyverse.org/dav-anon/iplant/commons/community_released/genophenoenvo/kg/merged-kg_edges.tsv
wget https://data.cyverse.org/dav-anon/iplant/commons/community_released/genophenoenvo/kg/merged-kg_nodes.tsv
```

Rename the files as `nodes.tsv` and `edges.tsv`

Run [NEO4j with Docker](https://hub.docker.com/_/neo4j):

```
cd ~/genophenoenvo/kg
 docker run -it --rm \
 --publish=7474:7474 \
 --publish=7687:7687 \
 -e NEO4J_dbms_connector_https_advertised__address=":7473" \
 -e NEO4J_dbms_connector_http_advertised__address=":7474" \
 -e NEO4J_dbms_connector_bolt_advertised__address=":7687" \
 --env=NEO4J_AUTH=none  \
 -v ${PWD}:/data  \
 neo4j
```

Open local address: `http://localhost:7474`

### Loading the KG data into Neo4J

[Importing CSV Data into Neo4j](https://neo4j.com/developer/guide-import-csv/)

Loading the .tsv files using [Aura DB Importer]()

```cypher
// Create nodes
LOAD CSV WITH HEADERS FROM 'https://data.cyverse.org/dav-anon/iplant/commons/community_released/genophenoenvo/kg/merged-kg_nodes.csv' AS row
MERGE (g:Gene {id: row.id})
  ON CREATE SET g.name = row.name;
```

```cypher
LOAD CSV WITH HEADERS FROM 'https://data.cyverse.org/dav-anon/iplant/commons/community_released/genophenoenvo/kg/merged-kg_nodes.csv' AS row
MERGE (g:Gene {geneId: row.id, name: row.name})
WITH g, row
UNWIND split(row.category, ':') AS category
MERGE (c:Category {name: category})
MERGE (g)-[r:has_attribute_type]->(c)

```

### Querying the Graph in Neo4J


#### Prerequisites 

The merged `node.tsv` file and `edge.tsv` file should be uploaded into `neo4j` for exploration and query. 

A Cypher query can be used to find all of the homologous genes that had also been documented to have differential gene expression in either a drought or a saline environment:

#### Cypher Query

```
MATCH (e {id:'PECO:0007404'})-[r]->(g),(g)-[q:`biolink:orthologous_to`]-(h),(e {id:'PECO:0007404'})-[s]->(h) RETURN *
```

```
MATCH (g {id:'AT5G15850'})-[r:`biolink:orthologous_to`]->(h),(h)-[q:`biolink:has_phenotype`]->(p),(g)-[q]->(s) RETURN *
```

```
MATCH (g)-[r:`biolink:has_phenotype`]->(p {id:'TO:0000207'}),(g)-[q:`in_taxon`]->(t {id:'NCBITaxon:4577'}) RETURN *
```