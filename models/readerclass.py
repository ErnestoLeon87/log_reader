import re
from logclass import Log


path = "smsts.log"


class LogReader:
    def __init__(self, logPath: "", readlog=None):
        self.logPath = logPath
        self.threadRegex = r"thread=\"[0-9]+\""
        self.failedRegex = r""
        # ----> ERROR
        self.nameRegex = r"!\[LOG\[[\w\s\d\(\)\[\]'\".,_:\\\/(=)]*\]LOG\]!"
        self.timeRegex = r"[0-9]+:[0-9]+:[0-9]+\.[0-9]+\+[0-9]+"
        self.dateRegex = r"[0-9]{2}-[0-9]{2}-[0-9]{4}"
        self.errorCodeRegex = r"0x[A-F0-9]{8}"
        if readlog == None:
            self.loglist = self.readlog()

    def readlog(self):
        listResult = []
        threadlist = self.getThreadFailed()

        patternName = re.compile(self.nameRegex)
        patternTime = re.compile(self.timeRegex)
        patternDate = re.compile(self.dateRegex)

        with open(self.logPath, "r") as log:
            for i in range(0, len(threadlist)):
                for itemlog in log:
                    if threadlist[i] in itemlog:
                        print(threadlist[i])
                        nameParam = patternName.findall(itemlog)
                        nameParam = nameParam[0][6:-6]
                        dateParam = patternDate.findall(itemlog)
                        dateParam = dateParam[0]

                        timeParam = patternTime.findall(itemlog)
                        timeParam = timeParam[0]

                        itemthread = threadlist[i][8:(len(threadlist[i]) - 1)]
                        newlogobj = Log(nameParam, dateParam,
                                        timeParam, itemthread)
                        listResult.append(newlogobj)
        return listResult

    # Function to get just thread failed

    def getThreadFailed(self):  # Function to get the thread numbers of failed log
        listResult = []
        with open(self.logPath, "r") as log:
            patternThread = re.compile(self.threadRegex)
            for item in log:
                found = False
                if ("Failed" in item) or ("failed" in item):
                    itemFound = patternThread.findall(item)
                    # itemFound = int(itemFound[0][8:(len(itemFound[0])-1)])

                    if len(listResult) == 0:
                        listResult.append(itemFound[0])
                    else:
                        for resl in listResult:
                            if resl != itemFound[0]:
                                pass
                            if resl == itemFound[0]:
                                found = True
                        if not found:
                            listResult.append(itemFound[0])
                else:
                    pass
        return listResult  # List of thread

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
print(logreader.loglist[1].name)
# print(logreader.getThreadFailed())
