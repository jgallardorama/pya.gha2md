
import os


class DocGroup:
    def __init__(self, parent, name, source_dir, relative_dir):
        self.parent = parent
        self.name = name
        self.source_dir = source_dir
        self.relative_dir = relative_dir
        self.doc_items = []
        self.groups = []
        if self.parent:
            self.parent.groups.append(self)
        pass

class ActionDocItem:
    def __init__(self, source_dir, main_file, content, source_files, additional_files) -> None:
        self.source_dir = source_dir
        self.name = main_file 
        self.main_file = main_file
        self.content = content
        self.source_files = source_files
        self.additional_files = additional_files
        self.group = None

class DocProject:
    def __init__(self, source_dir) -> None:
        self.source_dir = source_dir
        self.items=[]
        self.groups={
            '' : DocGroup(None, '', source_dir, '.')
        }
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
            result = DocGroup(parent, tail, group_dir, group_dir)
            self.groups[result.source_dir]=result

        return result