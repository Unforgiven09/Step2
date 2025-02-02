import io
import os
from abc import ABC, abstractmethod


class Output(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def display(self):
        pass


# The Output class is responsible for managing the output of data to different types of destinations.
class ConsoleOutput(Output):
    # The display method outputs the data to the chosen destination.
    def display(self):
        print(f"{self.data}")


class FileOutput(Output):
    def display(self):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        # Change the working directory to the directory of the script.
        os.chdir(file_dir)
        # Open the output file and write the data to it.
        with open('output.txt', 'w') as f:
            # Write the data to the file.
            f.write(self.data)
