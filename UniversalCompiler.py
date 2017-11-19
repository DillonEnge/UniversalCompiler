import csv, os

class FileManipulator():

    def getAbsPath(self, path):
        script_dir = os.path.dirname(__file__)
        rel_path = path
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    def transformUPFile(self):
        path = "test.up"#raw_input("What is the full name of your uni file? ")
        outputType = raw_input("What is your desired file type? ")
        uniFile = open(self.getAbsPath(path), "r")
        delimitedFile = csv.reader(uniFile, delimiter=" ")
        self.interperateFile(delimitedFile, outputType)

    def interperateFile(self, uniFile, outputType):
        csvFile = open(self.getAbsPath("comparator.csv"), "r")
        comparisonFile = csv.reader(csvFile, delimiter=",")
        outputFileData = self.getRelevantData(uniFile, comparisonFile, outputType)
        self.createNewFile(outputFileData, outputType)
        

    def createNewFile(self, outputFileData, outputType):
        fileName = raw_input("What would you like your {} file to be called? ".format(outputType))
        fileName = self.getAbsPath(fileName + "." + outputType)
        outputFile = open(fileName, "w")
        for output in outputFileData:
            outputFile.write(output)
        outputFile.close()

    def processParameters(self, statement, row, outputFile, option = ""):
        parameter = ""
        if "$" in statement:
            parameterString = statement[statement.find("$") + 1:-1]
            if "," in parameterString:
                parameters = tuple(parameterString.split(","))
                print tuple(parameters)
                outputFile.append(row[1].format(*parameters) + option)
            else:
                outputFile.append(row[1].format(parameterString) + option)
        else:
            outputFile.append(row[1] + option)

    def getRelevantData(self, uniFile, comparisonFile, outputType):
        relevantData = []
        for row in comparisonFile:
            if row[0] == outputType:
                del row[0]
                relevantData.append(row)
        outputFile = []
        for line in uniFile:
            outputFile.append("\n")
            for keyword in line:
                for row in relevantData:
                    if keyword == row[0] or keyword[:keyword.find("(") - 1] == row[0][:keyword.find("(") - 1]:
                        
                        if keyword == line[len(line) - 1]:
                            self.processParameters(keyword, row, outputFile)
                        else:
                            self.processParameters(keyword, row, outputFile, " ")
        del outputFile[0]
        return outputFile
        
fm = FileManipulator()
fm.transformUPFile()
