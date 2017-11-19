import csv, os

class FileManipulator():

    def getAbsPath(self, path):
        script_dir = os.path.dirname(__file__)
        rel_path = path
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    def readInFile(self, path, outputType):
        file = open(self.getAbsPath(path), "r+")
        self.interperateFile(file, outputType)

    def interperateFile(self, file, outputType):
        absPath = getAbsPath("comparator.csv")
        csvFile = open(absPath, "r+")
        comparisonFile = csv.reader(csvFile, delimiter=" ")

fm = FileManipulator()
fm.readInFile("test.up", "js")
