import os
from jinja2 import Environment, PackageLoader, select_autoescape

from gha2md.appinfra.applogging import LogManager
from gha2md.models.ghaction_models import DocGroup

def build(doc_item, source_dir):
    logger = LogManager().get_logger(__name__)

    env = Environment(
        loader=PackageLoader('gha2md.process', 'templates'),
        autoescape=select_autoescape())
    template_name= "doc-ghaction.md.j2"

    template = env.get_template(template_name)
    rendered_text = template.render(action=doc_item)
    
    file_path = os.path.join(doc_item.source_dir, "README.md")    
    file_full_path = os.path.join(source_dir, file_path)
    with open(file_full_path,"w", encoding="utf-8") as file:
        file.write(rendered_text)

def get_flatten_groups(doc_group:DocGroup):
    result = []
    for child in doc_group.groups:
        result.append(child)
        result.extend(get_flatten_groups(child))

    return result


def build_index(doc_group: DocGroup, source_dir):

    flatten_groups = get_flatten_groups(doc_group)

    env = Environment(
        loader=PackageLoader('gha2md.process', 'templates'),
        autoescape=select_autoescape())
    template_name= "doc-index.md.j2"

    template = env.get_template(template_name)
    rendered_text = template.render(main_group = doc_group, groups=flatten_groups)
    
    file_path = os.path.join(doc_group.source_dir, "README.md")
    file_full_path = os.path.join(source_dir, file_path)
    with open(file_full_path,"w", encoding="utf-8") as file:
        file.write(rendered_text)
