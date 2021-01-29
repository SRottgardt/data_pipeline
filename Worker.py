from modules import IPlugin


class Worker():

    def __init__(self):
        self.workerQue = []
    
    def addJob(self, _job: IPlugin):
        """
        Args:
            _job (IPlugin): adds a Job to the workerque, the job is a module with inheritance from IPlugin
        """
        self.workerQue.append(_job)

    def removeJob(self, _job: IPlugin):
        """
        Args:
            _job (IPlugin): remove a Job to the workerque, the job is a module with inheritance from IPlugin
        """
        self.workerQue.remove(_job)

    def executeJobs(self):
        """execute all jobs in the workerque and reset the jobs
        """
        for _jobs in self.workerQue:
            _jobs.preExecute()
        self.clearJobs() 

    def clearJobs(self):
        """clean the workerque
        """
        self.workerQue = []

    def getJobs(self) :
        """
        Returns:
            [list]: returns the workerque as list
        """
        return self.workerQue
