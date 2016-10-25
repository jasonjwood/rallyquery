
from pyral import Rally
class RallyContext:


    server = 'rally1.rallydev.com'
    apikey = ''

    backlog_stories = None
    completed_stories = None
    in_progress_stories = None

    def __init__(self, apikey):
        self.apikey = apikey

        self.fetch_common_data()

    def fetch_common_data(self):
        print "SERVER:", self.server, "APIKEY", self.apikey

        rally = Rally(server=self.server, apikey=self.apikey)

        # Get backlog contents
        # TODO: Deal with defects too
        self.backlog_stories = rally.get("UserStory", False, ['Iteration = Null', 'Project.Name = %22ILPF%20-%20Orcavengers%22'], "Rank")
        print self.backlog_stories

        # Get Completed Stories
        self.completed_stories = rally.get("UserStory", False, ['Iteration != Null', 'ScheduleState >= Accepted', 'Project.Name = %22ILPF%20-%20Orcavengers%22'], "Rank")
        print self.completed_stories

        # Get stories in progress
        self.in_progress_stories = rally.get("UserStory", False, ['Iteration != Null', 'ScheduleState >= In-Progress', 'ScheduleState <= Completed', 'Project.Name = %22ILPF%20-%20Orcavengers%22'], "Rank")
        print self.in_progress_stories

