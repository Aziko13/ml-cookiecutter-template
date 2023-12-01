import logging
from google.cloud import bigquery
import time
import os
import json
from src.utils import constants


def setup_loggin(name, filename):
    """Setup logging parameters
    Args:
        name (string): Logger name
        filename (string): Filename to save logs
    Returns:
        logger: logger class
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(filename)
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def execute_query(query, project="unity-ads-ds-prd"):
    """Execute a BQ query
    Args:
        query (string): Query to execute

    Returns:
        pandas.DataFrame: Dataframe with results
    """
    bqclient = bigquery.Client(project=project)
    return bqclient.query(query).result().to_dataframe()


def execution_time_f(logger):
    def execution_time_d(func):
        def wrapper():
            start = time.time()
            func()
            end = time.time()
            elapsed = end - start
            logger.info("[INFO] Execution time {} min.".format(round(elapsed / 60, 2)))

        return wrapper

    return execution_time_d


def save_metadata(bucket, prefix, model_version, file_name, configs):
    """The metadata file is saved locally and exported into a GS bucket.
    This metadata file is used to check for the completion of the mismatch model training pipeline in the main model
    before reading the trained model and discount factor table.

    Args:
        bucket (string): GS bucket where the model is stored
        prefix (string): GS prefix where the model is stored
        model_version (string): version of the model
        file_name (string): name of the metadata file
        configs (dict): the configs depending on the environment

    Returns:
        (string): the path where the metadata is saved
    """
    blob_path = os.path.join(bucket, prefix, model_version, file_name)

    with open(
        os.path.join(constants.DISCOUNT_FACTOR_TABLE_DIR, file_name), "w"
    ) as outfile:
        json.dump(configs, outfile)

    os.system(
        _get_copy_command(
            os.path.join(constants.DISCOUNT_FACTOR_TABLE_DIR, file_name),
            "gs://" + blob_path,
        )
    )

    return blob_path


def _get_copy_command(local_path, destination_path):
    """Generate command string to copy metadata.

    Args:
        local_path (string): he local path where the metadata is saved
        destination_path (string): Destination path in the GS bucket where the metadata will be copied to

    Returns:
        string: command to execute
    """
    command_string = "gsutil cp " + local_path + " " + destination_path

    return command_string
