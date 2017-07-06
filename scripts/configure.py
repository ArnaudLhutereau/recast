#! /usr/bin/env python
"""
A script that reads configuration.json and produces a matching configuration files
for docker-compose and the pyproxy.
"""
import copy
import datetime
import json
import os

import ruamel.yaml

PATH_TO_DISPATCHER_FILE = os.path.join(os.path.dirname(__file__), "..", "pyproxy", "dispatcher.json")
PATH_TO_DOCKER_COMPOSE_FILE = os.path.join(os.path.dirname(__file__), "..", "docker-compose.yml")
PATH_TO_DOCKER_COMPOSE_PRODUCTION_FILE = os.path.join(os.path.dirname(__file__), "..", "docker-compose-production.yml")

BASIC_COMPOSE_CONFIGURATION = {
    "version": "\"3\"",
    "services": {
        "coder": {
            "container_name": "coder",
            "hostname": "coder",
            "build": "./pycoder",
            "environment": ["sec_measure=confd"],
            "env_file": ["./erasure.env"],
            "deploy": {
                "placement": {
                    "constraints": ["node.role == manager"]
                }
            }
        },
        "proxy": {
            "container_name": "proxy",
            "hostname": "proxy",
            "build": "./pyproxy",
            "ports": ["3000:8000"],
            "env_file": ["./erasure.env"],
            "deploy": {
                "placement": {
                    "constraints": ["node.role == manager"]
                }
            }
        }
    }
}

def rename_existing_file(file_path):
    """
    Renames a file with an index number at the end for backup
    """
    if not os.path.exists(file_path):
        return None
    file_index = 1
    while os.path.exists(file_path + "." + str(file_index)):
        file_index += 1
    new_file_path = file_path + "." + str(file_index)
    os.rename(file_path, new_file_path)
    return new_file_path

def read_configuration_file(path):
    """
    Read the configuration file and return a configuration object
    """
    with open(path, "r") as configuration_file:
        return json.load(configuration_file)

def create_dispatcher_configuration(configuration):
    """
    Read the configuration file and create a coherent pyproxy's dispatcher.json file
    """
    nodes = int(configuration["storage"]["nodes"])
    dispatcher_configuration = {"providers":{}}
    for i in range(1, nodes + 1):
        name = "redis" + str(i)
        provider = {
            "type": "redis",
            "host": name,
            "port": 6379
        }
        dispatcher_configuration["providers"][name] = provider
    replication_factor = int(configuration["storage"].get("replication_factor", 3))
    dispatcher_configuration["replication_factor"] = replication_factor
    return dispatcher_configuration

def write_dispatcher_file(dispatcher_configuration):
    """
    Writes the new dispatcher file
    """
    if os.path.exists(PATH_TO_DISPATCHER_FILE):
        rename_existing_file(PATH_TO_DISPATCHER_FILE)
    # Write new dispatcher file
    dispatcher_configuration["_comment"] = "Generated by configure.py on " + datetime.datetime.now().isoformat()
    json_dispatcher = json.dumps(dispatcher_configuration, indent=4, separators=(',', ': ')).strip()
    with open(PATH_TO_DISPATCHER_FILE, "w") as dispatcher_dump_file:
        dispatcher_dump_file.write(json_dispatcher)



def create_docker_compose_configuration(configuration):
    """
    Read the configuration file and create a coherent docker-compose file
    """
    nodes = int(configuration["storage"]["nodes"])

    compose_configuration = copy.deepcopy(BASIC_COMPOSE_CONFIGURATION)
    if os.path.exists(PATH_TO_DOCKER_COMPOSE_FILE):
        with open(PATH_TO_DOCKER_COMPOSE_FILE) as dc_file:
            compose_configuration = ruamel.yaml.round_trip_load(dc_file.read().strip(),
                                                                preserve_quotes=True)

    redis_keys = [key for key in compose_configuration["services"] if key.startswith("redis")]
    for key in redis_keys:
        del compose_configuration["services"][key]
    for i in range(1, nodes + 1):
        container_name = "redis" + str(i)
        compose_configuration["services"][container_name] = {
            "container_name": container_name,
            "image": "redis:3.2.8",
            "deploy": {
                "placement": {
                    "constraints": ["node.role == worker"]
                }
            }
        }
    return compose_configuration

def create_docker_compose_configuration_for_production(configuration):
    """
    Read the configuration file and create a coherent docker-compose file
    """
    dev_compose_configuration = create_docker_compose_configuration(configuration)
    del dev_compose_configuration["services"]["proxy"]["build"]
    dev_compose_configuration["services"]["proxy"]["image"] = "dburihabwa/playcloud_proxy"
    del dev_compose_configuration["services"]["coder"]["build"]
    dev_compose_configuration["services"]["coder"]["image"] = "dburihabwa/playcloud_coder"
    return dev_compose_configuration

def write_docker_compose_file(compose_configuration, path):
    """
    Writes the new docker-compose file
    """
    # Check if docker-compose file already exists
    if os.path.exists(path):
        rename_existing_file(path)
    # Write new docker-compose file
    yaml_for_compose = ruamel.yaml.round_trip_dump(compose_configuration,
                                                   indent=4,
                                                   block_seq_indent=2,
                                                   explicit_start=True)
    with open(path, "w") as compose_dump_file:
        gen_line = "# Generated by configure.py on " + datetime.datetime.now().isoformat() + "\n"
        compose_dump_file.write(gen_line)
        compose_dump_file.write(yaml_for_compose)

def write_docker_compose_file_for_dev(compose_configuration):
    """
    Writes to the given docker-compose content to PATH_TO_DOCKER_COMPOSE_FILE
    """
    write_docker_compose_file(compose_configuration, PATH_TO_DOCKER_COMPOSE_FILE)

def write_docker_compose_file_for_production(compose_configuration):
    """
    Writes to the given docker-compose content to PATH_TO_DOCKER_COMPOSE_PRODUCTION_FILE
    """
    write_docker_compose_file(compose_configuration, PATH_TO_DOCKER_COMPOSE_PRODUCTION_FILE)

if __name__ == "__main__":
    PATH_TO_CONFIGURATION_FILE = os.path.join(os.path.dirname(__file__), "..", "configuration.json")
    GLOBAL_CONFIGURATION = read_configuration_file(PATH_TO_CONFIGURATION_FILE)
    DISPATCHER_CONFIGURATION = create_dispatcher_configuration(GLOBAL_CONFIGURATION)
    write_dispatcher_file(DISPATCHER_CONFIGURATION)
    COMPOSE_CONFIGURATION = create_docker_compose_configuration(GLOBAL_CONFIGURATION)
    write_docker_compose_file_for_dev(COMPOSE_CONFIGURATION)
    COMPOSE_PRODUCTION_CONFIGURATION = create_docker_compose_configuration_for_production(GLOBAL_CONFIGURATION)
    write_docker_compose_file_for_production(COMPOSE_PRODUCTION_CONFIGURATION)
