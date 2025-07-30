#!/bin/bash

# Define the base directory (e.g., your home directory or a specific project folder)
# You can change 'my_project_root' to whatever you want the top-level folder to be called.
BASE_DIR="my_project_root"

# Create the base directory
mkdir -p "$BASE_DIR"
cd "$BASE_DIR"

# Create root-level files
touch api_gateway.log
touch create_table.py
touch dire_struct.txt
touch drop_table.py
touch OptiFlow_VS_project.py
touch OptiFlow_VS_project.pyproj
touch OptiFlow_VS_project.sln
touch orchestrator.db
touch orchestrator.zip
touch "proposal submission link.txt"
touch run_project.bat
touch testtable.py

# Create agents directory and its subdirectories
mkdir -p agents/{ai_models,medical_ai,predictive_analytics,supply_chain_ai,utils,versioning}

# Create api_gateway directory and its subdirectories and files
mkdir -p api_gateway/{.ipynb_checkpoints,models,routers/__pycache__,services/__pycache__,utils,__pycache__}
touch api_gateway/api_gateway_entry.py
touch api_gateway/consumer-test.py
touch api_gateway/server_config.env
touch api_gateway/__init__.py
touch api_gateway/.ipynb_checkpoints/api_gateway_entry-checkpoint.ipynb
touch api_gateway/models/best_payment_order_model.pth
touch api_gateway/models/payment_order_model_main.py
touch api_gateway/models/requirements.txt
touch api_gateway/routers/api_gateway_router.py
touch api_gateway/services/apigw_services.py
touch api_gateway/services/auth_middleware.py

# Create config directory and its subdirectories
mkdir -p config/env/secrets/{dev,prod,stage}

# Create docs directory
mkdir -p docs

# Create etcd-v3.5.13-linux-amd64 directory and its subdirectories and files
mkdir -p "etcd-v3.5.13-linux-amd64/Documentation/dev-guide/apispec/swagger"
touch "etcd-v3.5.13-linux-amd64/etcdutl"
touch "etcd-v3.5.13-linux-amd64/get_all.sh"
touch "etcd-v3.5.13-linux-amd64/populate_etcd.sh"
touch "etcd-v3.5.13-linux-amd64/README-etcdctl.md"
touch "etcd-v3.5.13-linux-amd64/README-etcdutl.md"
touch "etcd-v3.5.13-linux-amd64/README.md"
touch "etcd-v3.5.13-linux-amd64/READMEv2-etcdctl.md"
touch "etcd-v3.5.13-linux-amd64/Documentation/README.md"
touch "etcd-v3.5.13-linux-amd64/Documentation/dev-guide/apispec/swagger/rpc.swagger.json"
touch "etcd-v3.5.13-linux-amd64/Documentation/dev-guide/apispec/swagger/v3election.swagger.json"
touch "etcd-v3.5.13-linux-amd64/Documentation/dev-guide/apispec/swagger/v3lock.swagger.json"

# Create frontend directory and its subdirectories and files
mkdir -p frontend/{components,static,templates}
touch frontend/app.py
touch frontend/NewFile
touch frontend/static/script.js
touch frontend/static/style.css
touch frontend/templates/index.html

# Create load_balancer directory and its subdirectories
mkdir -p load_balancer/{algorithms,utils}

# Create logs directory and its subdirectories
mkdir -p logs/{alerts,elk_stack,prometheus_grafana}

# Create networking directory and its subdirectories
mkdir -p networking/{gateway,load_balancer,service_discovery}

# Create orchestrator directory and its subdirectories and files
mkdir -p orchestrator/{apiserver/__pycache__,caliconetwork,controller/__pycache__,core/__pycache__,db/__pycache__,models/__pycache__,registry,scheduler,schema_model/__pycache__,utils,__pycache__}
touch orchestrator/init_db.py
touch orchestrator/apiserver/developer_api.py
touch orchestrator/apiserver/developer_api_v01.py
touch orchestrator/caliconetwork/calicoctl
touch orchestrator/caliconetwork/calico_setup.py
touch orchestrator/controller/controller.py
touch orchestrator/controller/controller_bkup.py
touch orchestrator/controller/controller_bkup_01.py
touch orchestrator/core/containerd_wrapper.py
touch orchestrator/core/container_client.py
touch orchestrator/core/container_interface.py
touch orchestrator/core/container_main.py
touch orchestrator/core/container_test.py
touch orchestrator/db/database_query.py
touch orchestrator/db/init_db.py
touch orchestrator/db/query_db_node_notrequired.py
touch orchestrator/db/schema_model_notrequired.py
touch orchestrator/db/__init__.py
touch orchestrator/models/core_models.py
touch orchestrator/models/models.py
touch orchestrator/models/models_bkup_notrequired.py
touch orchestrator/models/support_models.py
touch orchestrator/models/testtable.py
touch orchestrator/registry/service_registry.py
touch orchestrator/scheduler/oschedular.py
touch orchestrator/schema_model/base.py
touch orchestrator/schema_model/events.py
touch orchestrator/schema_model/mpods.py
touch orchestrator/schema_model/node.py
touch orchestrator/schema_model/workloads.py
touch orchestrator/schema_model/__init__.py

# Create scripts directory
mkdir -p scripts

# Create storage directory and its subdirectories
mkdir -p storage/{postgres,redis,sqlite,test_data}

# Create tests directory and its subdirectories and files
mkdir -p tests/{agents_tests,api_tests/.ipynb_checkpoints,frontend_tests,load_tests,orchestrator_tests,test_data,__pycache__}
touch tests/__init__.py
touch tests/api_tests/testapigw.py
touch tests/api_tests/test_api_gateway.ipynb
touch tests/api_tests/__init__.py
touch tests/api_tests/.ipynb_checkpoints/test_api_gateway-checkpoint.ipynb

echo "Directory structure created successfully in '$BASE_DIR/'"