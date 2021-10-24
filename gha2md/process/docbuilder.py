import os
from jinja2 import Environment, PackageLoader, select_autoescape

from gha2md.appinfra.applogging import LogManager

def build(doc_item, source_dir):
    logger = LogManager().get_logger(__name__)


    env = Environment(
        loader=PackageLoader('gha2md.process', 'templates'),
        autoescape=select_autoescape())
    template_name= "doc-ghaction.md.j2"

    template = env.get_template(template_name)
    rendered_text = template.render(action=doc_item.content)
    
    file_path = os.path.join(doc_item.source_dir, "README.md")
    with open(file_path,"w", encoding="utf-8") as file:
        file.write(rendered_text)