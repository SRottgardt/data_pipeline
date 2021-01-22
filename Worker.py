from modules import IPlugin


class Worker():

    def __init__(self):
        self.workerQue = []
    #
    def addJob(self, _job: IPlugin):
        self.workerQue.append(_job)

    def removeJob(self, _job: IPlugin):
        self.workerQue.remove(_job)

    def executeJobs(self):
        for _jobs in self.workerQue:
            _jobs.preExecute()
        self.clearJobs() 

    def clearJobs(self):
        self.workerQue = []

    def getJobs(self):
        return self.workerQue
