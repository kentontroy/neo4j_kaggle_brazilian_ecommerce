# neo4j_kaggle_brazilian_ecommerce

![Neo4j](./images/neo4j.png)

Clone the git repo
```
git clone https://github.com/kentontroy/neo4j_kaggle_brazilian_ecommerce.git
```

If using Docker to host Neo4J
```
Initial image download and how to run:

cd ${PROJECT_ROOT}/docker
mkdir graph_plugins
mkdir graph_data
docker-compose up -d
docker exec -it docker-demo_neo4j-1 bash
```

Create a python virtual environment
```
python3 -m pip install --upgrade pip

sudo curl https://pyenv.run | bash
cat $HOME/.bash_profile
...
# User specific environment and startup programs
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.11.9
pyenv virtualenv 3.11.9 venv
```

Prepare the environment
```
cd ${PROJECT_ROOT}/src/python
pyenv activate venv
pip install -r ${PROJECT_ROOT}/requirements.txt

Next change the Neo4j settings in the .env file to point to your installation.
```

Load data into the Neo4j graph
```
cd ${PROJECT_ROOT}/src/python

Create a random sample of customers (in this case, 50)
python3 randomly_sample_customers.py --sample-size 50

Filter the data sets to only load Order data specific to the customers sampled
python3 filter_by_customer.py

Load the data set nodes (i.e. vertices)
python3 load_customer_nodes.py
python3 load_order_nodes.py
python3 load_order_item_nodes.py
python3 load_product_nodes.py
python3 load_tier_nodes.py

Create the relationships (i.e. edges)
python3 create_customer_order_edges.py
python3 create_order_product_edges.py

Finally, load the rewards calculations
python3 load_lifetime_rewards_node.py
```

Experiment with Cypher queries
```
python3 query_wrapper.py
```


