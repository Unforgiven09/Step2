from abc import ABC, abstractmethod


class DataSource(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass


    # Class responsible for reading and writing data to a text file
class TextFileOperations(DataSource):
    # Reads the data from the file
    def read_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data

    # Writes data to the file
    def write_data(self, data):
        with open(self.path, 'w') as file:
            file.write(data)


# Class for operations on the text data
class TextOperations:
    def __init__(self, text_source):
        self.text_source = text_source
        self.data = self.text_source.read_data()

    # Searches for a word in the data
    def search_for_word(self, word):
        return word in self.data

    # Counts the occurrences of a word in the data
    def count_occurences(self, word):
        return self.data.count(word)


file = TextFileOperations("data.txt")

obj = TextOperations(file)
print(f"{obj.search_for_word('more')}")
print(f"{obj.count_occurences('be')}")
