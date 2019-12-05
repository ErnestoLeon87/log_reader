import re

path = "smsts.log"


class LogReader:
    def __init__(self, logPath: "", readlog=None):
        self.logPath = logPath
        self.loglist = []
        self.threadRegex = r"thread=\"[0-9]+\""
        self.failedRegex = r""
        self.nameRegex = r"\[+[\w\s\d\t\$.:\\'-_\]]+"
        self.timeRegex = r"[0-9]+:[0-9]+:[0-9]+\.[0-9]+\+[0-9]+"
        self.dateRegex = r"[0-9]{2}-[0-9]{2}-[0-9]{4}"
        self.errorCodeRegex = r"0x[A-F0-9]{8}"
        if readlog == None:
            self.loglist = self.__readlog()

    def __readlog(self):
        listResult = []
        with open(self.logPath, "r") as log:
            for item in log:
                if ("Failed" in item) or ("failed" in item):
                    listResult.append(item)
        return listResult

    def getThreadFailed(self):
        listResult = []
        with open(self.logPath, "r") as log:
            patternThread = re.compile(self.threadRegex)
            for item in log:
                if ("Failed" in item) or ("failed" in item):
                    found = False
                    itemFound = patternThread.findall(item)
                    if len(listResult) == 0:
                        listResult.append(itemFound)
                    else:
                        for r in listResult:
                            if itemFound[0] in r:
                                found = True
                            else:
                                found = False
                        if not found:
                            listResult.append(itemFound)
                else:
                    pass
        return listResult

    def readLogName(self):
        with open(self.logPath, "r") as log:
            for logItem in log:
                for item in re.finditer(self.nameRegex, logItem, re.S):
                    math_text = item.group()
                    math_text = math_text[5: (len(math_text) - 5)]
                    self.loglist.append(math_text)

    def readErrorCode(self):
        with open(self.logPath, "r") as log:
            for logItem in log:
                for item in re.finditer(self.errorCodeRegex, logItem, re.S):
                    math_text = item.group()
                    math_text = math_text[0:]
                    self.loglist.append(math_text)

    def getErrorLogList(self, logList):
        resutl = []
        log_item = {"name": "", "time": "", "date": ""}
        patternName = re.compile(self.nameRegex)
        patternTime = re.compile(self.timeRegex)
        patternDate = re.compile(self.dateRegex)
        for i in logList:
            log_item["name"] = patternName.findall(i)
            log_item["time"] = patternTime.findall(i)
            log_item["date"] = patternDate.findall(i)

            resutl.append(log_item)
        return resutl


logreader = LogReader(path)
print(logreader.getThreadFailed())
