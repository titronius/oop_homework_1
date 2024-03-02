class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\
                \nФамилия: {self.surname}\
                \nСредняя оценка за домашние задания: {SupportFunctions.average_grade(self)}\
                \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\
                \nЗавершенные курсы: {', '.join(self.finished_courses)}"
    
    def __eq__(self, other):
        return SupportFunctions.average_grade(self) == SupportFunctions.average_grade(other)

    def __ne__(self, other):
        return SupportFunctions.average_grade(self) != SupportFunctions.average_grade(other)
    
    def __lt__(self, other):
        return SupportFunctions.average_grade(self) < SupportFunctions.average_grade(other)

    def __le__(self, other):
        return SupportFunctions.average_grade(self) <= SupportFunctions.average_grade(other)

    def __gt__(self, other):
        return SupportFunctions.average_grade(self) > SupportFunctions.average_grade(other)
    
    def __ge__(self, other):
        return SupportFunctions.average_grade(self) >= SupportFunctions.average_grade(other)
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {SupportFunctions.average_grade(self)}"

    
    def __eq__(self, other):
        return SupportFunctions.average_grade(self) == SupportFunctions.average_grade(other)

    def __ne__(self, other):
        return SupportFunctions.average_grade(self) != SupportFunctions.average_grade(other)
    
    def __lt__(self, other):
        return SupportFunctions.average_grade(self) < SupportFunctions.average_grade(other)

    def __le__(self, other):
        return SupportFunctions.average_grade(self) <= SupportFunctions.average_grade(other)

    def __gt__(self, other):
        return SupportFunctions.average_grade(self) > SupportFunctions.average_grade(other)
    
    def __ge__(self, other):
        return SupportFunctions.average_grade(self) >= SupportFunctions.average_grade(other)

class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class SupportFunctions:
    def average_grade(self,course = None):
        sum_of_grades = 0
        num_of_grades = 0
        for k, grades in self.grades.items():
            if not course or k == course:
                for grade in grades:
                    sum_of_grades += grade
                    num_of_grades += 1
        average_grade = sum_of_grades/num_of_grades

        return average_grade
    
    def average_grade_course(subjects,course):
        sum_of_grades = 0
        number_of_subject = 0
        for subject in subjects:
            sum_of_grades += SupportFunctions.average_grade(subject,course)
            number_of_subject += 1
        average_grade = sum_of_grades/number_of_subject
        return average_grade
 
student_luke = Student('Luke', 'Skywalker', 'male')
student_leia = Student('Leia', 'Organa Solo', 'female')

mentor_anakin = Lecturer('Anakin', 'Skywalker')
mentor_obi_wan = Lecturer('Obi Wan', 'Kenobi')

reviewer_han = Reviewer('Han', 'Solo')
reviewer_chewie = Reviewer('Chewbacca', 'Vuki')

student_luke.courses_in_progress += ['Python']
student_luke.courses_in_progress += ['Git']
student_leia.courses_in_progress += ['Python']
student_leia.courses_in_progress += ['Git']

student_luke.finished_courses += ['Постановка на светлую сторону силы']
student_luke.finished_courses += ['Курсы верховой езды для магистра Йоды']
student_luke.finished_courses += ['Принятие отца-ситха']
student_leia.finished_courses += ['Повстанчество для чайников']
student_leia.finished_courses += ['История галактической республики']
student_leia.finished_courses += ['Принятие отца-ситха']

mentor_anakin.courses_attached += ['Python']
mentor_obi_wan.courses_attached += ['Python']

reviewer_han.courses_attached += ['Python']
reviewer_chewie.courses_attached += ['Python']
 
reviewer_han.rate_student(student_luke, 'Python', 10)
reviewer_chewie.rate_student(student_luke, 'Python', 10)

reviewer_han.rate_student(student_leia, 'Python', 8)
reviewer_chewie.rate_student(student_leia, 'Python', 8)

student_luke.rate_lector(mentor_anakin, 'Python', 8)
student_luke.rate_lector(mentor_obi_wan, 'Python', 10)

student_leia.rate_lector(mentor_anakin, 'Python', 7)
student_leia.rate_lector(mentor_obi_wan, 'Python', 9)

#task 3
print(f"Студенты:\n{student_luke}\n\n{student_leia}\n\nМенторы:\n{mentor_anakin}\n\n{mentor_obi_wan}\n\nПроверяющие:\n{reviewer_han}\n\n{reviewer_chewie}")

print(f"""\nСравнение Люка и Леи:
Люк круче Леи? - {student_luke > student_leia}
Люк не круче Леи? - {student_luke < student_leia}
Люк круче или равен Лее? - {student_luke >= student_leia}
Люк не круче или равен Лее? - {student_luke <= student_leia}
Люк и Лея одинаково круты? - {student_luke == student_leia}
Люк и Лея не одинаково круты? - {student_luke != student_leia}
""")

print(f"""Сравнение Энакина и Оби-Вана:
Энакин круче Оби-Вана? - {mentor_anakin > mentor_obi_wan}
Энакин не круче Оби-Вана? - {mentor_anakin < mentor_obi_wan}
Энакин круче или равен Оби-Вану? - {mentor_anakin >= mentor_obi_wan}
Энакин не круче или равен Оби-Вану? - {mentor_anakin <= mentor_obi_wan}
Энакин и Оби-Ван одинаково круты? - {mentor_anakin == mentor_obi_wan}
Энакин и Оби-Ван не одинаково круты? - {mentor_anakin != mentor_obi_wan}
""")


#task 4
print(f"Средняя оценка преподов по курсу Python: {SupportFunctions.average_grade_course([mentor_anakin,mentor_obi_wan],'Python')}")
print(f"Средняя оценка студентов за ДЗ по курсу Python: {SupportFunctions.average_grade_course([student_luke,student_leia],'Python')}")