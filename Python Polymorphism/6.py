class developer:
    def work(self):
        return "Writing code"
class tester:
    def work(self):
        return "Testing code"
class manager:
    def work(self):
        return "Managing team"
developer = developer()
tester = tester()
manager = manager()
print(developer.work())
print(tester.work())
print(manager.work())