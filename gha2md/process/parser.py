


from gha2md.appinfra.applogging import LogManager
from gha2md.models.ghaction_models import ActionDocItem, DocProject
import yaml
import os
import ruamel.yaml
from pathlib import PurePath

def get_files(dir):
    result = []
    for (dirpath, dirnames, filenames) in os.walk(dir):
        result.extend([os.path.join(dirpath, filename) for filename in filenames])
        break
    return result

def match_pattern(path, patterns):
    result = True
    for pattern in patterns:
        norm_pattern = pattern
        is_included = False
        if pattern.startswith("!"):
            norm_pattern = norm_pattern[1:]
            is_included = True
        if PurePath(path).match(norm_pattern):
            result = not is_included
            break

    return result
    
def parse_def_action(doc_project, action_path: str):
    
    pass

def parse_action(doc_project: DocProject, action_path: str) -> ActionDocItem:
    result:ActionDocItem = None

    abs_action_dir = os.path.dirname(action_path)
    action_dir = os.path.relpath(abs_action_dir, doc_project.source_dir)
    with open(action_path, "r", encoding="utf-8") as file:
        content = yaml.load(file, Loader=yaml.FullLoader)

    result = ActionDocItem(action_dir, action_path, content)
    doc_project.add_item(result)

    additional_doc_path = os.path.join(abs_action_dir, "_README.md")
    if os.path.exists(additional_doc_path) and os.path.isfile(additional_doc_path):
        with open(additional_doc_path, "r") as file:
            additional_documentation = file.read()
            result.additional_documentation = additional_documentation

    files = get_files(action_dir)
    source_files=[os.path.relpath(file, action_dir) for file in files if os.path.dirname(file)==action_dir]
    additional_files=[os.path.relpath(file, action_dir) for file in files if os.path.dirname(file)!=action_dir]

    path = PurePath(action_dir).as_posix()
    keys = doc_project.references.keys()
    first = next((key for key in keys if key.endswith(path)), None)
    if first:
        references = doc_project.references.get(first, None)
        if references:
            result.references=references
            result.example=references[0].content

    result.source_files = source_files
    result.additional_files = additional_files

    return result


def parse_workflow(doc_project: DocProject, workflow_path):

    logger = LogManager().get_logger(__name__)

    with open(workflow_path, "r") as file:
        ruamel.yaml.YAML
        yaml=ruamel.yaml.YAML(typ='safe')   # default, if not specfied, is 'rt' (round-trip)
        workflow = ruamel.yaml.round_trip_load(file)
        jobs = workflow['jobs']
        for key, job in jobs.items():
            steps = job['steps']
            for step in steps:
                uses = step.get('uses', None)
                if uses:
                    value = ruamel.yaml.dump(step, Dumper=ruamel.yaml.RoundTripDumper)
                    doc_project.add_reference(uses, workflow_path, step.lc, value)


def parse_references(doc_project: DocProject):
    workflows_dir = os.path.join(doc_project.source_dir, ".github/workflows")
    files = get_files(workflows_dir)
    patterns = [
        "*.yaml",
        "*.yml",
        "!*"
    ]

    logger = LogManager().get_logger(__name__)

    for file in files:
        if match_pattern(file, patterns):
            try:
                parse_workflow(doc_project, file)
            except:
                logger.exception(f"Parsing {file}")
                pass
    # for file in files:
    #     ruamel.yaml.YAML()

    # pass



def parse(doc_project: DocProject, action_paths):

    logger = LogManager().get_logger(__name__)
    result = []

    parse_references(doc_project)

    for action_path in action_paths:
        logger.info(f"Parsing {action_path}")
        parse_action(doc_project, action_path)

