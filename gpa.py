# Rehan Javaid rj3dxu
"""
The purpose of this program is to create different functions that all work together in order to calculate
cumulative running GPA and total number of credits taken.
"""
gpa = x = 0
course_credit = y = 0

def gpa():
    return x

def add_course(gp , cc= 3):
        global x
        global y
        x = (gp*cc + x*y)/(y+cc)
        y = y+cc
        return x, y

def credit_total():
    return y

