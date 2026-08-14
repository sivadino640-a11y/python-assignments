from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def start_course(self):
        pass


class OnlineCourse(Course):
    def start_course(self):
        print("Online Course Started")
        print("Course:", self.course_name)
        print("Duration:", self.duration)


class OfflineCourse(Course):
    def start_course(self):
        print("Offline Course Started")
        print("Course:", self.course_name)
        print("Duration:", self.duration)


online = OnlineCourse("Python Programming", "3 Months")
offline = OfflineCourse("Java Programming", "6 Months")

online.start_course()
print()

offline.start_course()