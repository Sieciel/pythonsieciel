#--- YAML
#import json
# #1
# import yaml
# with open('network_config.yaml', 'r') as file:
#     network_config = yaml.safe_load(file)
# print(network_config)

#2
# network_data = {
#     'switch': 'Switch1',
#     'ports': [{'name':'FastEthernet0/1', 'vlan':'10'}, {'name': 'FastEthernet0/2', 'vlan':'20'}]
# }
# with open('new_network_config.json', 'w') as file:
#   json.dump(network_data, file, indent=4)

  #3
import yaml

def read_and_modify_router_config(file_path):
    with open(file_path, 'r') as file:
      try:
        data = yaml.safe_load(file)
        if data['interfaces']:
          data['interfaces'][0]['ip'] = '10.10.10.1'
        return data
      except yamlYAMLError as exc:
        print(exc)

    def write_yaml(file_path, data):
      with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

    modified_config = read_and_modify_router_config('network_config.yml')
    write_yaml('modified_router_config.yml', modified_config)
