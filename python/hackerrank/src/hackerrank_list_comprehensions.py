from functools import reduce

# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

def conditional_grid_coordinates_with_for( w: int, h:int , d:int , n:int ) -> list:

    coordinates = []

    for x in range(w+1):
        for y in range(h+1):
            for z in range(d+1):
                if x+y+z != n:
                    coordinates.append([x, y, z])

    return coordinates

def conditional_grid_coordinates_with_list_comprehension( w: int, h:int , d:int , n:int ) -> list:
    return [[x, y, z] for x in range(w+1) for y in range(h+1) for z in range(d+1) if x+y+z != n]

coordinates = conditional_grid_coordinates_with_for(1, 1, 1, 2)
print(coordinates)

coordinates2 = conditional_grid_coordinates_with_list_comprehension(1, 1, 1, 2)
print(coordinates2)


# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

def find_second_maximum_number( arr: list ) -> int:
    sorted_arr = sorted(arr, reverse=True)
    max_number = sorted_arr[0]
    for number in sorted_arr:
        if number < max_number:
            return number

def find_second_maximum_number2( arr: list ) -> int:
    first_max = float('-inf')
    second_max = float('-inf')

    for number in arr:
        if number > first_max:
            second_max = first_max
            first_max = number
        elif number > second_max and number != first_max:
            second_max = number

    return second_max

arr = [2, 3, 6, 6, 5]

print(find_second_maximum_number(arr))
print(find_second_maximum_number2(arr))


# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

def find_students_with_second_lowest_grade( students: list ) -> list:
    lowest_grade = float('inf')
    second_lowest_grade = float('inf')

    for student in students:
        if student[1] < lowest_grade:
            second_lowest_grade = lowest_grade
            lowest_grade = student[1]
        elif student[1] < second_lowest_grade and student[1] != lowest_grade:
            second_lowest_grade = student[1]

    students_with_second_lowest_grade = [ student[0] for student in students if student[1] == second_lowest_grade ]
    students_with_second_lowest_grade.sort()

    return students_with_second_lowest_grade

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

students_with_second_lowest_grade = find_students_with_second_lowest_grade(students)

for student in students_with_second_lowest_grade:
    print(student)

# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true


def find_average_grade_of_student(student_grades: dict, student_name: str) -> float:
    student_grade_list = student_grades.get(student_name)
    return (
        0.0
        if not student_grade_list
        else reduce(lambda x, y: x + y, student_grade_list) / len(student_grade_list)
    )


student_grades = { 'Krishna': [67, 68, 69], 'Arjun': [70, 98, 63], 'Malika': [52, 56, 60] }

average_grade = find_average_grade_of_student(student_grades, 'Malika')
print(f'{average_grade:0.2f}')
