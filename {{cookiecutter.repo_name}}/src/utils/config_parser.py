""" Parser for configuration file.

configargparser is bit limiting as it does not allow nested configuration files

"""
import logging
import yaml
import configargparse
from src.utils import helpers, constants
import os


logger = helpers.setup_loggin(__name__, os.path.join(constants.LOGS_DIR, "configs.log"))


def process_config_file_args(conf):
    """Process arguments that are paths to config fields

    Args:
        conf: config dictionary
    Returns: config dictionary enriched with data from config file
    """
    with open(conf["configs_path"]) as file:
        conf["configs"] = yaml.full_load(file)

    return conf


def args_processing():
    """Process arguments that are send throgh the command line and from the config file.
    src/configs/data_configs.yaml is used as a default value if nothing else is specified

    Returns:
        Dict: config dictionary
    """
    logger.info("Processing Args")
    g = configargparse.ArgParser()
    g.add(
        "-c",
        "--configs_path",
        required=False,
        default="src/configs/data_configs_dev.yaml",
        is_config_file=True,
        help="configs file path",
    )
    conf = g.parse_known_args()
    conf = vars(conf[0])
    conf = process_config_file_args(conf)

    logger.info("Path to the configs file is: {}".format(conf["configs_path"]))
    logger.info("Configs are: \n {}".format(conf["configs"]))
    return conf


if __name__ == "__main__":
    conf = args_processing()
