# neo4j_kaggle_brazilian_ecommerce

![Neo4j](./images/neo4j.png)

If using Docker to host Neo4J
```
Initial image download and how to run:

cd docker
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

pyenv install 3.10.14
pyenv virtualenv 3.10.14 venv
pyenv activate venv
```
