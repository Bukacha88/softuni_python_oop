class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return "\n".join(str(doc) for doc in self.documents)

    @staticmethod
    def find_category(category_id, categories):
        return [category for category in categories if category.id == category_id][0]

    @staticmethod
    def find_topic(topic_id, topics):
        return [topic for topic in topics if topic_id == topic.id][0]

    @staticmethod
    def find_document(document_id, documents):
        return [document for document in documents if document_id == document.id][0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        self.find_category(category_id, self.categories).name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        self.find_topic(topic_id, self.topics).topic = new_topic
        self.find_topic(topic_id, self.topics).storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        self.find_document(document_id, self.documents).file_name = new_file_name

    def delete_category(self, category_id):
        self.categories.remove(self.find_category(category_id, self.categories))

    def delete_topic(self, topic_id):
        self.topics.remove(self.find_topic(topic_id, self.topics))

    def delete_document(self, document_id):
        self.documents.remove(self.find_document(document_id, self.documents))

    def get_document(self, document_id):
        return self.find_document(document_id, self.documents)

