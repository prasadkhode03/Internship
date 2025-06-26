'''Abstract Class for File Parsers
Create an abstract class named FileParser with an abstract method parse(data).
Create concrete classes:
JSONParser that implements parse(data) method and prints: “Parsing JSON data...”
XMLParser that implements parse(data) method and prints: “Parsing XML data...”
Test both classes.'''
from abc import ABC, abstractmethod
class FileParser(ABC):
    @abstractmethod #decorator
    def parse(data):
        pass
class JSONParser(FileParser):
    def parse(data):
        print("Parsing JSON data...")
class XMLParser(FileParser):
    def parse(data):
        print("Parsing XML data...")

json = JSONParser()
xml = XMLParser()
json.parse()
xml.parse()