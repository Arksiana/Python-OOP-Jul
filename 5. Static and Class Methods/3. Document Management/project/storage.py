from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for el in self.categories:
            if el.id == category_id:
                el.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for el in self.topics:
            if el.id == topic_id:
                el.topic = new_topic
                el.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name: str):
        for el in self.documents:
            if el.id == document_id:
                el.file_name = new_file_name

    def delete_category(self, category_id: int):
        for el in self.categories:
            if el.id == category_id:
                self.categories.remove(el)

    def delete_topic(self, topic_id: int):
        for el in self.topics:
            if el.id == topic_id:
                self.topics.remove(el)

    def delete_document(self, document_id: int):
        for el in self.documents:
            if el.id == document_id:
                self.documents.remove(el)

    def get_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                return el.__repr__()

    def __repr__(self):
        result = []
        for el in self.documents:
            result.append(el.__repr__())
        return '\n'.join(result)
