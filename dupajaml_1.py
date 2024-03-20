#--- YAML

#1
import yaml
with open('network_config.yaml', 'r') as file:
    network_config = yaml.safe_load(file)
print(network_config)