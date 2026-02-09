import os
from pathlib import Path
import yaml
from src.data_line import logger
import json
import joblib  
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError 


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file. 
    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error while converting yaml to ConfigBox: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error while reading yaml file: {e}")
        raise e
    



    
@ensure_annotations    
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories.
    Args:
        path_to_directories (list[Path]): List of paths to directories to be created.
        verbose (bool, optional): Whether to log the created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")





@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a json file.
    Args:
        path (Path): Path to the json file to be saved.
        data (dict): Dictionary to be saved as json.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")






@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a json file and returns it as a ConfigBox object.
    Args:
        path (Path): Path to the json file to be loaded.
    Returns:
        ConfigBox: ConfigBox object containing the contents of the json file.
    """
    with open(path) as f:
        data = json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(data)





@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.
    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file to be saved.
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")




@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file using joblib.
    Args:
        path (Path): Path to the binary file to be loaded.
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data              