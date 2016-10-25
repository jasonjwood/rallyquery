from abc import ABCMeta, abstractmethod


def colour_text(text, condition_for_red):
    if condition_for_red:
        return '<font color="red">' + text + '</font>'

    return '<font color="green">' + text + '</font>'


class rally_analysis_base:
    __metaclass__ = ABCMeta

    @abstractmethod
    def analyse(self, rally): pass

    @abstractmethod
    def print_advice(self): pass


class rally_analysis_grooming_health(rally_analysis_base):
    planned_sum = 0
    num_dev_ready = 0
    backlog_count = 0
    num_prioritized = 0
    num_sized = 0

    def analyse(self, rally_context):
        i = 0

        for story in rally_context.backlog_stories:
            i += 1

            # Sum dev ready size
            if story.Ready is True:
                # Count dev ready stories
                self.num_dev_ready += 1

                # Sum dev ready size
                size = 0
                if story.PlanEstimate is not None:
                    size = float(story.PlanEstimate)

                self.planned_sum += size

            #Find the grooming line
            if story.FormattedID == "US65112":
                self.num_prioritized = i-1

            #Count sized stories
            if story.PlanEstimate is not None and float(story.PlanEstimate) > 0:
                self.num_sized += 1

        self.backlog_count = i

    def print_advice(self):
        s = 'GROOMING:\n'
        s += '\tTotal Backlog COUNT = ' + str(self.backlog_count) + '\n\n'
        s += '\tPrioritized COUNT = ' + str(self.num_prioritized) + '\n'
        s += '\tUnnprioritized COUNT = ' + str(self.backlog_count - self.num_prioritized) + '\n\n'
        s += '\tDev Ready COUNT of stories = ' + str(self.num_dev_ready) + '\n'
        s += '\tDev Ready sum of SIZE = ' + str(self.planned_sum) + '\n'
        s += '\tCOUNT of sized stories = ' + str(self.num_sized) + '\n\n'

        return s


class rally_analysis_wip(rally_analysis_base):
    current_ip_count = 0
    current_ip_size = 0
    current_complete_count = 0
    current_complete_size = 0

    def analyse(self, rally_context):
        for story in rally_context.in_progress_stories:

            size = 0
            if story.PlanEstimate is not None:
                size = float(story.PlanEstimate)

            if story.ScheduleState == 'In-Progress':
                self.current_ip_count += 1
                self.current_ip_size += size
            elif story.ScheduleState == 'Completed':
                self.current_complete_count += 1
                self.current_complete_size += size
            else:
                print "Unexpected story state:"+story.ScheduleState

    def print_advice(self):
        s = 'WIP:\n'
        s += '\tWIP COUNT = ' + str(self.current_ip_count) + '\n'
        s += '\tWIP SIZE = ' + str(self.current_ip_size) + '\n\n'
        s += '\tREADY TO ACCEPT COUNT = ' + str(self.current_complete_count) + '\n'
        s += '\tREADY TO ACCEPT SIZE = ' + str(self.current_complete_size) + '\n\n'

        return s

class rally_analysis_cycle_time(rally_analysis_base):
    current_ip_count = 0
    current_ip_size = 0
    current_complete_count = 0
    current_complete_size = 0


InProgressDate
AcceptedDate



    def analyse(self, rally_context):
        for story in rally_context.in_progress_stories:

            size = 0
            if story.PlanEstimate is not None:
                size = float(story.PlanEstimate)

            if story.ScheduleState == 'In-Progress':
                self.current_ip_count += 1
                self.current_ip_size += size
            elif story.ScheduleState == 'Completed':
                self.current_complete_count += 1
                self.current_complete_size += size
            else:
                print "Unexpected story state:"+story.ScheduleState

    def print_advice(self):
        s = 'WIP:\n'
        s += '\tWIP COUNT = ' + str(self.current_ip_count) + '\n'
        s += '\tWIP SIZE = ' + str(self.current_ip_size) + '\n\n'
        s += '\tREADY TO ACCEPT COUNT = ' + str(self.current_complete_count) + '\n'
        s += '\tREADY TO ACCEPT SIZE = ' + str(self.current_complete_size) + '\n\n'

        return s