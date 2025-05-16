class Document:
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Pdf(Document):
    def show(self):
        return "Show PDF"
class Word(Document):
    def show(self):
        return "Show Word"   

docs = [Pdf(),Word()]

for doc in docs:
    print(doc.show())