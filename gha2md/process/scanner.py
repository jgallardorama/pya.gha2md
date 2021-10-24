import os

from gha2md.appinfra.applogging import LogManager

def scan(source_dir):
    result = []
    
    logger = LogManager().get_logger(__name__)

    for root, _, files in os.walk(source_dir):
        logger.debug(f"Scanning {root}")
        action_files = list(filter(lambda file: (file == "action.yaml" or file == "action.yml"), files))
        if len(action_files) > 0:
            logger.info(f"Found {root} action")
            action_path = os.path.join(root, action_files[0])
            result.append(action_path)

    return result