# Install
curl -LfO 'https://airflow.apache.org/docs/\
apache-airflow/stable/docker-compose.yaml'

# Permissions
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# Create directors
mkdir ./dags ./plugins ./logs

# Init
docker-compose up airflow-init

# run
docker-compose up
