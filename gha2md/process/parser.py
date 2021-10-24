


from gha2md.appinfra.applogging import LogManager
from gha2md.models.ghaction_models import ActionDocItem
import yaml
import os

def get_files(dir):
    result = []
    return result
    

def parse_action(action_path: str) -> ActionDocItem:
    result:ActionDocItem = None

    action_dir = os.path.dirname(action_path)
    with open(action_path, "r", encoding="utf-8") as file:
        content = yaml.load(file, Loader=yaml.FullLoader)
    source_files=[]
    additional_files=[]

    result = ActionDocItem(action_dir, action_path, content, source_files, additional_files)

    return result

def parse(action_paths):

    logger = LogManager().get_logger(__name__)
    result = []
    
    for action_path in action_paths:
        logger.info(f"Parsing {action_path}")
        doc_item=parse_action(action_path)
        result.append(doc_item)

    return result