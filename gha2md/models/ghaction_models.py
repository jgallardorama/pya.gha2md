
class ActionDocItem:
    def __init__(self, source_dir, main_file, content, source_files, additional_files) -> None:
        self.source_dir = source_dir
        self.main_file = main_file
        self.content = content
        self.source_files = source_files
        self.additional_files = additional_files

class DocProject:
    def __init__(self) -> None:
        self.actions=[]
        pass

    