class Manager:
    def work(self):
        print("Manager is working")
class Developer:
    def work(self):
        print("Developer is working")
class Teacher:
    def work(self):
        print("Teacher is working")
def assign_work(employee):
    employee.work()
assign_work(Manager())
assign_work(Developer())
assign_work(Teacher())