import random as rd
from time import sleep
#The courses
class Course:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.no_of_stds = 0

    def __repr__(self):
        desc = "Welcome to {}! this is ".format(self.name)
        if self.difficulty == 1:
            desc += "an easy course by most standards "
        elif self.difficulty == 2:
            desc += "a difficult course by most standards "
        elif self.difficulty == 3:
            desc += "a very difficult course by most standards "
        desc += "but don't take my word for it, it could easily be word of mouth! =] \n-that gets spread real quick around these parts ;)-\nWell with that said, what are you waiting for?\n\t Dive right in lets learn {} together!\n[no. of students is currently {}]".format(self.name, str(self.no_of_stds))
        return desc

    #passing a  course
    def passed(self, grade, std_name):
        if grade == "A":
            print("Superb {}! Superb! You really killed it! There's not much to say but keep up the good work!!".format(std_name))
            #name supposed to be of the student
        elif grade == "B":
            print("Wonderful {}! You weren't at the top but you did good. Its a splendid result either way.\nYou should be proud".format(std_name))
        elif grade == "C":
            print("Just in the middle! you'll need to try harder next time to be on top.")
        elif grade == "D":
            print("Not a good result by any standards {}, you just barely made it to the passing mark. Don't think you would have such luck next time.\n If you desire extra lessons, my office is open anytime. We can work together to put your grades in check".format(std_name))
    
    #failing a course
    def fail(self, std_name):
        print("\t\tCongratulations {}! You have successfully failed the course. I'll be glad to see you next year, maybe then we can work some concepts into your head".format(std_name))

#The students
class Student:
    def __init__(self, name, sex):
        self.name = name
        self.age = rd.randint(17, 21)
        self.sex = sex
        self.IQ = rd.randint(50, 70)
        self.grades = {}
        self.courses_offered = rd.sample(courses, 5)
        self.fav_courses = rd.sample(self.courses_offered, 2)
        self.friendly = rd.choice([True, False])
        self.friends = []
        self.truancy = 0

    #describing the student
    def __repr__(self):
        desc = self.name 
        #defining the students pronouns
        if self.sex == "m": 
            gender = "boy"
            prn = "he"
            pr_n = "His"
        else: 
            gender = "girl"
            prn = "she"
            pr_n = "Her"
        if self.IQ >= 65:
            desc += " is a smart {}, at {} {}'s capable of great things already! watch out lecturers, this one is a stunner.".format(gender, str(self.age), prn)
        elif self.IQ > 55:
            desc += ", {}, is an average student, {} does the most {} can to succeed and leaves the rest to the forces of nature. They're one of the few that need a little support to get that extra push needed to break their limits.".format(str(self.age), prn, prn)
        elif self.IQ <= 55: 
            desc += " is {} of age, {} isn't one of those students high up there in the mental business, {} has strengths in other places...hopefully...\n Regardless don't give up on {}, because if you do, {}'ll know. And when that happens its all downhill from there. Make sure to take care of {} because {} might just turn out to be a diamond in the rough! ;)".format(str(self.age), prn, prn, self.name, prn, self.name, prn)
        desc += " {} selected courses are ".format(pr_n)
        #loops via the courses & fav courses and prints them in presentable format
        for course in self.courses_offered:
            if course == self.courses_offered[-1]:
                desc += course.name + "."
                break
            desc += course.name + ", "
        desc += " {} favourite courses are ".format(pr_n)
        for course in self.fav_courses:
            if course == self.fav_courses[-1]:
                desc += course.name + "."
                break
            desc += course.name + ", "
        if self.friendly == True:
            desc += " {} is friendly and has a current IQ of {} and a truancy level of {}.".format(self.name, str(self.IQ), str(self.truancy))
        else:
            desc += " {} is unfriendly and has a current IQ of {} and a truancy level of {}.".format(self.name, str(self.IQ), str(self.truancy))
        desc += "{} current grades are: ".format(pr_n)
        for key, value in self.grades.items():
            print("{} : {}".format(key, value))
        return desc

    # initializing school env for the student
    def studies_init(self):
        # adding the courses to the dict[self.grades]
        self.grades = dict.fromkeys(self.courses_offered)
        # adding student objs to the lecturers list
        for lecturer in lecturers_m + lecturers_f:
            if lecturer.course in self.courses_offered:
                lecturer.students.append(self)

    # making a friend
    def make_friend(self, student):
        while 1:
            if (student in self.friends) or (self in student.friends):
                print("You and {} are already friends".format(student.name))
                break
            if student.friendly == True:
                self.friends.append(student)
                student.friends.append(self)
                print("You and {} are now friends!".format(student.name))
                break
            elif self.friendly == True and student.friendly == False:
                while tries <= 3:
                    if tries == 3:
                        print("{} has finally caved in! {} is now your friend! and because of all the trouble you went through, be rest assured that they would stay by your side till the very end!\nYou my friend, just earned yourself an ally :)".format(
                            student.name, student.name))
                        self.friends += student
                        student.friends += self
                        break
                    print("{} doesn't want to  be friends :(\n Don't give up, keep trying maybe they'll come around".format(student.name))
                    choice = input("try again?[y/n]: ")
                    while choice not in ("y", "n"):
                        choice = input("Oops! you didn't select \"y\" or \"n\". Select the right option to advance\n: ")
                    if choice == "y":
                        tries + 1
                    else: break
                break
            elif self.friendly == False and student.friendly == False:
                print("Oops! you and {} are totally incompatible, its best you drop the idea of becoming their friend".format(student.name))
                break

    # increasing truancy
    def vices(self):
        vice = rd.randint(1, 5)
        if vice == 1 or 3:
            self.truancy + 3

    # taking a test
    def take_test(self):
        if self.IQ >= 80 and self.truancy <= 24:
            self.IQ + 4
        elif self.IQ >= 70 and self.truancy <= 15:
            self.IQ + 3
        elif self.truancy >= 36:
            self.IQ + 1
        elif self.IQ <= 40:
            self.IQ + 0.5
        elif self.IQ < 40 and self.truancy >= 36:
            self.IQ + 0
        else:
            self.IQ + 1.5
        sleep(0.5)

    # taking an exam
    def take_exam(self):
        if self.IQ >= 95 and self.truancy <= 24:
            self.IQ + 6
        elif self.IQ >= 70 and self.truancy <= 25:
            self.IQ + 4.5
        elif self.truancy >= 36:
            self.IQ - 2
        elif self.IQ <= 50:
            self.IQ + 1
        elif self.IQ < 50 and self.truancy >= 36:
            self.IQ - 5
        else:
            self.IQ + 2
        sleep(1)

    # letting off some steam about the exam or test --> to be called after tests or exams
    def rant(self, course, assmt):
        rants = ["The {} {} was hard...".format(course, assmt), "My answers were not in the options!", "The {} {} was easy I knew everything!!".format(course, assmt), "Who wants to get lunch?", "..."]
        for i in range(3):
            if i == 1: 
                print(rd.choice(rants))
                sleep(0.2)
            else: break

    # getting result --> to be called before the lecturer gives the results
    def get_result(self):
        fears = ["Oh God no...", "It's finally time hehe", "I hope i did well", "Show us the results already!!", "Gosh I'm so scared...", "...I know i killed it ;}"]
        for i in range(3):
            if i == 1: 
                print(rd.choice(fears))
                sleep(0.2)
            else: break

#The Lecturers
class Lecturer:
    def __init__(self, name, sex, course):
        self.name = name
        self.course = course
        self.sex = sex
        self.age = rd.randint(28,50)
        self.exp_lvl = rd.randint(1,5)
        self.students = []
        self.favs = []
        self.std_grades = {}

    #describing the lecturer
    def __repr__(self):
         #defining the lecturers pronouns
        if self.sex == "m": 
            title = "Mr"
            gender = "man"
            prn = "he"
            pr_n = "his"
        else: 
            title = "Miss"
            gender = "woman"
            prn = "she"
            pr_n = "her"
        desc = "{} {} is".format(title, self.name)
        if self.age <= 35 and self.exp_lvl >= 4:
            desc += " a {} of great prowess. At the young age of {} {} is capable of outstanding things, {} has a great affinity with students and that would come in handy with not so strong students.\n Make sure to keep {} around {}'s a rare catch!".format(gender, str(self.age), self.name, self.name, pr_n, prn)
        elif self.age >= 40 and self.exp_lvl >= 3: 
            desc += " a well seasoned lecturer. Aged {}, {} has years in the business, a wonderful lecturer all round! A great personality to have at the head of your lecturer association, you need people like {} around.".format(str(self.age), prn, pr_n )
        elif (self.age >= 36 and self.age <= 40) and (self.exp_lvl == 1):
            desc += " a not so good lecturer to say the least. At an age of {} {} doesn't have much to write to {} name. {} is a struggling lecturer in a nutshell.".format(str(self.age),self.name, pr_n, self.name)
        else:
            desc += " your average lecturer. At the age of {} {} doesn't have much going for {}self but {} is capable of {} work. Lecture? {} {} will lecture quite alright.".format(str(self.age), self.name, pr_n, prn, pr_n, title, self.name)
        desc += "\n [Course: {} || Exprience level: {} ] \n{} students currently are: ".format(self.course.name, str(self.exp_lvl), pr_n)
        for std in self.students:
            print(std.name)
        sleep(1)
        desc += "\n{} favourite students currently are: ".format(pr_n)
        for std in self.favs:
            print(std.name) 
        return desc

    #lecturing
    def lecture(self):
        #creating a course obj for the current course
        self.course.no_of_stds = len(self.students)
        #determining the lvl of knowledge gained by each std during the lecture
        print(self.course.name + " lecture begins...")
        if self.age >= 40 and self.exp_lvl >= 3:
            for std in self.students:
                std.IQ + 4.5
                if std.truancy >= 15: std.IQ -1
                elif std.truancy >= 24: std.IQ - 2
                elif std.truancy >= 36: std.IQ - 3
                elif std.truancy >= 48: std.IQ - 4
            
        elif (self.age >= 35 and self.age <= 39) and (self.exp_lvl == 1):
            for std in self.students:
                std.IQ + 2.5
                if std.truancy >= 15: std.IQ -1
                elif std.truancy >= 24: std.IQ - 2
                elif std.truancy >= 36: std.IQ - 3
                elif std.truancy >= 48: std.IQ - 4
        elif self.age <= 34 and self.exp_lvl >= 4:
            for std in self.students:
                std.IQ + 6
                if std.truancy >= 15: std.IQ -1
                elif std.truancy >= 24: std.IQ - 2
                elif std.truancy >= 36: std.IQ - 3
                elif std.truancy >= 48: std.IQ - 4
        else:
            for std in self.students:
                std.IQ + 3
                if std.truancy >= 15: std.IQ -1
                elif std.truancy >= 24: std.IQ - 2
                elif std.truancy >= 36: std.IQ - 3
                elif std.truancy >= 48: std.IQ - 4
        sleep(3)
        print("The lecture has ended")
            
    #giving a test
    def give_test(self):
        print("The {} test will commence shortly, please take your seats".format(self.course.name))
        sleep(3)
        print("The test has begun\n\t\tYou have 10mins to complete the test\nGoodluck!")
        sleep(5)
        print("The time for the test has elapsed, please submit your papers...")
        sleep(2)
        print("Alright that's the end of it boys and girls! Hope you did your best!\nResults would be released in a week")

    #giving exams
    def give_exam(self):
        print("Good-day students\nHope you are all well read for your {} exam today\nWell if you're not then sorry for you. To those who are ready, let us begin".format(self.course.name)) 
        sleep(1)
        print("You have 2 hours for this exam, Goodluck!")
        sleep(5)
        print("Time up! Submit your papers and see you next time!")
    
    #grading the students
    def grade(self):
        for std in self.students:
            gv = (std.IQ - std.truancy) % 6
            #adding the favourite boost
            if std in self.favs:
                while True:
                    if gv == 5:
                        break
                    else: 
                        gv + 1
                        break 
            #putting the grades in their respective dicts           
            if gv == 5: 
                std.grades[self.course.name] = "A"
                self.std_grades[std.name] = "A" 
            elif gv == 4: 
                std.grades[self.course.name] = "B"
                self.std_grades[std.name] = "B"
            elif gv == 3: 
                std.grades[self.course.name] = "C"
                self.std_grades[std.name] = "C"
            elif gv == 2: 
                std.grades[self.course.name] = "D"
                self.std_grades[std.name] = "D"
            elif gv <= 1: 
                std.grades[self.course.name] = "F"
                self.std_grades[std.name] = "F"

    #informing the students about the results
    def result_prep(self):
        print("Good day Students, today is going to be a bad day for some of you and a great day for others...only time will tell")
        print("I have your papers here. Graded.\nBrace yourselves...because some of you did extremely bad")
        sleep(3)

    #giving results
    def give_result(self, assmt):
        print("Here are your results for {} {}...".format(self.course.name, assmt))
        sleep(0.2)
        for std, grade in self.std_grades.items():
            print("{}\t\t{}".format(std, grade))
            if grade == "A": self.course.passed("A", std.name)
            elif grade == "B": self.course.passed("B", std.name)
            elif grade == "C": self.course.passed("C", std.name)
            elif grade == "D": self.course.passed("D", std.name)
            else: self.course.fail(std.name)
            sleep(1)
        print("Now, in as much as you've all seen your results, those who did well do not slack because we all very much know, that pride comes before a fall. Take good care to become even more intimate with your books and the sky would be your limit!")
        print("To those who failed")
        sleep(1)
        print("Try harder next time. If you feel you could do better if you took extra lessons, meet me in my office later.")
        print("And to the class in general, make sure to stay close to your books because that's what you are here for, keep up with classes because if you dont you'll miss out. Don't think you can do it all in your own.")
        print("And with that said, Have a good holiday everyone!")
        #gfklhkjhkgjcgbkvgjhhlkhgfcjhm,jhgfxc
courses = [Course(name, rd.randint(1,3)) for name in ["MTH101", "MTH121", "PHY121", "ECE108", "CHEM101", "BIO101", "GSP101", "GSP111", "ENG101"]]
lecturers_m = [Lecturer(name, "m", course) for name, course in zip(["Bertram", "Ayodele", "Livinus", "Stephen", "Charles"], courses)]
leftover_courses = []
taken_courses = [] 
#repeated courses solved!
for lecturer in lecturers_m:
    taken_courses.append(lecturer.course)
for course in courses:
     if course not in taken_courses: leftover_courses.append(course) 
     #if course in t_courses: continue
     #else: leftover_courses.append(course)
lecturers_f = [Lecturer(name,"f", course) for name, course in zip(["Blessing", "Fiona", "Joy", "Josephine"], leftover_courses)]
#creating student objs M & F
students_m = [Student(name, "m") for name in ["Peter", "Daniel", "Elvis", "Joel", "Johnson", "Jude", "Philip", "Solomon", "Mufasa", "Kelvin", "Lucky", "James"]]
students_f = [Student(name, "f") for name in ["Laura", "Nwanneka", "Jane", "Dorathy", "Elizabeth", "Iris", "Cheryl", "Fiona"]]
#a fxn to loop via all the students triggering their vices because nobody can be good forever ^^
def activate_vice():
    for std in students_f + students_m:
        std.vices() 
#making friends
def bonding():
    stds = rd.sample(students_f + students_m, 2)
    choice = rd.randint(0, 1) 
    if choice == 0:   
        stds[0].make_friend(stds[1])
    else:
        stds[1].make_friend(stds[0])
#school work
def lecturing():
    for lecturer in lecturers_f + lecturers_m:
        lecturer.lecture() 
def exam():
    for lecturer in lecturers_f + lecturers_m:
        lecturer.give_exam()
        for std in students_f + students_m:
            std.take_exam() 
            std.rant("exam")
def test():
    for lecturer in lecturers_f + lecturers_m:
        lecturer.give_test()
        for std in students_f + students_m:
            std.take_test() 
            std.rant(lecturer.course.name, "test")
def results(assmt):
    for lecturer in lecturers_f + lecturers_m:
        lecturer.result_prep()
        for std in students_f + students_m:
            std.get_result() 
        lecturer.grade()
        lecturer.give_result(assmt)
            
#initialise the academy
def init_academy():
    #initialise each student
    for std in students_f + students_m:
        std.studies_init()
    #start lectures
    bonding()
    lecturing()
    activate_vice()
    print("\t[Day Two...]")
    sleep(2)
    bonding()
    lecturing()
    test()
    bonding()
    activate_vice()
    print("\t[Day Three...]")
    sleep(2)
    results("test")
    lecturing()
    print("\t[Day Four...]")
    sleep(2)
    lecturing()
    test()
    activate_vice()
    bonding()
    print("\t[Day Five...]")
    sleep(2)
    bonding()
    results("test")
    activate_vice()
    lecturing()
    print("\t[End of term...]")
    sleep(2)
    bonding()
    exam()
    results("exam")
print("Welcome to the academy! A place where you will be moulded into the best version of yourself")
print("Let us get enrolled right away")
tries = 1
init_academy()

#print(lecturers_f.name + lecturers_m.name)
# for lecturer in lecturers_f + lecturers_m:
#     print(lecturer.course.name) 


# lecturers_f[1].lecture()
# lecturers_f[1].give_test()
# lecturers_f[1].grade()
# lecturers_f[1].give_result("test")
# lecturers_f[1].give_exam()
# lecturers_f[1].grade()
# lecturers_f[1].give_result("test")
# print(lecturers_f[1])
 


