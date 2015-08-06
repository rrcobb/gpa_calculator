# Write your solution here!
def calculate(courses):
    # Create a dictionary of the values corresponding to letter grades
    # This is much easier than trying to handle the values with
    # a series of conditional statements - less code, more meaning.
    mappings = {
        'A+':4,
        'A': 4,
        'A-': 3.7,
        'B+':3.3,
        'B': 3,
        'B-':2.7,
        'C+':2.3,
        'C': 2,
        'C-':1.7,
        'D+':1.3,
        'D': 1,
        'D-':0.7,
        'F': 0
    }

    # loop through the courses, adding their weight to the
    # total weight and adding their weighted value to the sum
    sum = 0.0
    total_weight = 0.0
    for course in courses:
        weight = course.get('credits',1)
        total_weight += weight
        sum += weight*mappings[course['grade']]

    # gpa is the sum of the weighted values divided by the total weight
    gpa = sum/total_weight

    return gpa
