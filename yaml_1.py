#--- YAML

#1
import yaml_1
with open('network_config.yaml', 'r') as file:
    network_config = yaml_1.safe_load(file)
print(network_config)