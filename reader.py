import re

path = "smsts.log"


class Log_Reader:
    def __init__(self, logPath: "Log file path"):
        self.logPath = logPath
        self.loglist = []
        self.failedRegex = r""
        self.nameRegex = r"\[+[\w\s\d\t\$.:\\'-_\]]+"
        self.timeRegex = r"[0-9]+:[0-9]+:[0-9]+\.[0-9]+\+[0-9]+"
        self.dateRegex = r"[0-9]{2}-[0-9]{2}-[0-9]{4}"
        self.errorCodeRegex = r"0x[A-F0-9]{8}"

    def readLogName(self):
        with open(self.logPath, "r") as log:
            for logItem in log:
                for item in re.finditer(self.nameRegex, logItem, re.S):
                    math_text = item.group()
                    math_text = math_text[5: (len(math_text)-5)]
                    self.loglist.append(math_text)

    def readErrorCode(self):
        with open(self.logPath, "r") as log:
            for logItem in log:
                for item in re.finditer(self.errorCodeRegex, logItem, re.S):
                    math_text = item.group()
                    math_text = math_text[0:]
                    self.loglist.append(math_text)

    def readLog(self):
        with open(self.logPath) as log:
            for item in log:
                if item.__contains__("failed"):
                    self.loglist.append(item)

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


logreader = Log_Reader(path)
# logreader.readLogName()
# logreader.readErrorCode()
logreader.readLog()
# print(logreader.list)
print(logreader.loglist[0:2])
