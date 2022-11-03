class Student:
    def __init__(self, name, branch, year, attendance) -> None:
        self.name = name
        self.branch = branch
        self.year = year
        self.attendance = attendance

    def eligibility(self):
        if  self.attendance >= 75:
            return f("{self.name} is eligible for PUE")

    student1 = Student("Devyanshi", "CSE", "II", 81)
    student2 = Student("Kanishk", )
