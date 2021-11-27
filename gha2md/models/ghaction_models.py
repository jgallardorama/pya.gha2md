
import os


class DocGroup:
    def __init__(self, name, source_dir, relative_dir):
        self.name = name
        self.source_dir = source_dir
        self.relative_dir = relative_dir
        self.doc_items = []
        self.groups = []
        self.parent = None

    def attach(self, child):
        self.groups.append(child)
        child.parent = self

class ActionDocItem:
    def __init__(self, source_dir, main_file, content) -> None:
        self.source_dir = source_dir
        self.name = main_file 
        self.main_file = main_file
        self.name_dir = os.path.basename(os.path.dirname(main_file))
        self.content = content
        self.source_files = []
        self.additional_files = []
        self.group = None
        self.additional_documentation = ""
        self.references=[]
        self.example=""

class DocReference:
    def __init__(self, file, location, content):
        self.location = location
        self.file = file
        self.content = content

class DocProject:
    def __init__(self, source_dir) -> None:
        self.source_dir = source_dir
        self.items=[]
        self.groups={
            '' : DocGroup('', source_dir, '.')
        }

        self.references={}
        pass

    def add_item(self, docItem: ActionDocItem):
        self.items.append(docItem)
        group_dir= os.path.dirname(docItem.source_dir)
        group = self.get_group(group_dir)
        group.doc_items.append(docItem)
        docItem.group = group

    def get_group(self, group_dir):
        result = self.groups.get(group_dir, None)
        if not result:
            head, tail = os.path.split(group_dir)            
            parent = self.get_group(head)
            result = DocGroup(tail, group_dir, group_dir)
            parent.attach(result)
            self.groups[result.source_dir]=result

        return result

    def add_reference(self, action_id, file_path, location, content):
        ref = DocReference(file_path, location, content)
        
        references = self.references.get(action_id, None)
        if not references:
            self.references[action_id]=[]

        self.references[action_id].append(ref)
