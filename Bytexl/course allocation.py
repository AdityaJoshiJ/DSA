class Instructor:
    def __init__(self, instructor_name, experience, avg_feedback, technology_skill):
        self.__instructor_name = instructor_name
        self.__experience = experience
        self.__avg_feedback = avg_feedback
        self.__technology_skill = technology_skill

    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4:
            return True
        return False
    

    def allocate_course(self, technology):
        if self.check_eligibility() and technology in self.__technology_skill:
            return True
        return False
    

    def get_instructor_name(self):
        return self.__instructor_name
    

    def get_experience(self):
        return self.__experience
    

    def get_avg_feedback(self):
        return self.__avg_feedback
    

    def get_technology_skill(self):
        return self.__technology_skill
    

instructor = Instructor("Aditya Bhamare", 4, 4.7, ["Android", "Java", "Python"])
print(instructor.check_eligibility()) 
print(instructor.allocate_course("Python"))  
print(instructor.allocate_course("Java")) 
print(instructor.allocate_course("Ruby"))  