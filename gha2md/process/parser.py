


from gha2md.appinfra.applogging import LogManager
from gha2md.models.ghaction_models import ActionDocItem, DocProject
import yaml
import os

def get_files(dir):
    result = []
    for (dirpath, dirnames, filenames) in os.walk(dir):
        result.extend([os.path.join(dirpath, filename) for filename in filenames])
        break
    return result
    

def parse_action(doc_project: DocProject, action_path: str) -> ActionDocItem:
    result:ActionDocItem = None

    abs_action_dir = os.path.dirname(action_path)
    action_dir = os.path.relpath(abs_action_dir, doc_project.source_dir)
    with open(action_path, "r", encoding="utf-8") as file:
        content = yaml.load(file, Loader=yaml.FullLoader)

    files = get_files(action_dir)

    source_files=[os.path.relpath(file, action_dir) for file in files if os.path.dirname(file)==action_dir]
    additional_files=[os.path.relpath(file, action_dir) for file in files if os.path.dirname(file)!=action_dir]

    result = ActionDocItem(action_dir, action_path, content, source_files, additional_files)

    doc_project.add_item(result)

    return result

def parse(doc_project: DocProject, action_paths):

    logger = LogManager().get_logger(__name__)
    result = []
    
    for action_path in action_paths:
        logger.info(f"Parsing {action_path}")
        parse_action(doc_project, action_path)
        