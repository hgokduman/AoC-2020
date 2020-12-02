import os
import re

class Resource:
    _fileName = None
    _fileContents = None
    _dataList = None
    _dataStr = None
    _dataRegExMatches = None
    _outputFormat = "str"

    def __init__(self, day):
        self._fileName = f"input/{day:02d}.txt"
        with open(self._fileName, "r") as fp:
            self._fileContents = fp.read()
            self._dataStr = self._fileContents  

    def Get(self):
        if self._outputFormat == "str":
            return (self._fileContents)
        elif self._outputFormat == "list":
            return (self._dataList)
        elif self._outputFormat == "regex":
            return (self._dataRegExMatches)

    def Numeric(self):
        if self._outputFormat == "str":
            self._dataStr = int(self._dataStr)
        elif self._outputFormat == "list":
            self._dataList = list(map(int, self._dataList))

        return (self)

    def RegEx(self, pattern):
        p = re.compile(pattern)
        if self._outputFormat == "str":
            self._dataRegExMatches = p.findall(self._dataStr)
        elif self._outputFormat == "list":
            self._dataRegExMatches = list(map(p.findall, self._dataList))
            self._dataRegExMatches = [x[0] for x in self._dataRegExMatches]
        
        self._outputFormat = "regex"        
        return (self)

    def SplitLines(self):
        self._outputFormat = "list"
        self._dataList = self._fileContents.splitlines()

        return (self)