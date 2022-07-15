from asyncio.windows_events import NULL
import mysql.connector as connector
import pdb
import math

def mainMenu():
    print("1. Enter student grade information")
    print("2. Print all student grade information")
    print("3. Print class performance statistics")
    print("4. Exit")
    choice1 = int(input("Please enter your choice: "))

    if choice1==1:
        print("1.1 - Enter a BIT student information")
        print("1.2 - Enter a DIT student information")
        print("1.3 - Go back to the main menu")
        choice2 = float(input("Please enter your choice: "))

        if choice2==1.1:
            BIT_student_info()
        elif choice2==1.2:
            DIT_student_info()
        elif choice2 ==1.3:
            mainMenu()
        else:  
            print("Oops! Incorrect Choice. Enter 1.1-1.3") 
            
    elif choice1==2:
        # all_student_grade()
        print("2.1 - Print all student grade information ascendingly by final mark")
        print("2.2 - Print all student grade information descendingly by final mark")
        print("2.3 - Go back to the main menu")
        choice3 = float(input("Please enter your choice: "))

        if choice3==2.1:
            Asc_final_mark()
        elif choice3==2.2:
            Desc_final_mark()
        elif choice3 ==2.3:
            mainMenu()
        else:  
            print("Oops! Incorrect Choice. Enter 2.1-2.3") 

    elif choice1==3:
        performance()
    elif choice1==4:
        exit
    else :
        print("invalid choice. Enter 1-4")
        mainMenu()

mydb = connector.connect(
  host="localhost",
  user="root",
  password="saini890"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS result")
        
# BIT student information

# Create Table in sql

conn =connector.connect(host= 'localhost', username ='root', password = 'saini890', database='result')
my_cursor=conn.cursor()
# CREATE DATABASE IF NOT EXISTS DBName;
my_cursor.execute("CREATE TABLE IF NOT EXISTS Student (Stu_ID VARCHAR(9), Stu_name VARCHAR(255), Stu_type VARCHAR(5), Stu_final_mark INT(11) , Stu_grade VARCHAR(10),Assessment_1 float(5,2),Assessment_2 float(5,2),Assessment_3 float(5,2),grade_point varchar(10))")


def cal_F_SA_SE(marks):
    print(marks[0],marks[1],marks[2])

    if (marks[0] < 50 and marks[1] < 50) or (marks[1] < 50 and marks[2] < 50) or (marks[0] < 50 and marks[2] < 50):
        return 'F'
    elif (marks[0] < 50 and marks[1] >= 50) or (marks[0] >= 50 and marks[1] < 50):
        return 'SA'
    elif marks[2] < 50:
        return 'SE'        
    else:
        print("Invalid Input..")


def cal_F_AF(marks):
    if((marks[0] == 0 and marks[1] == 0) or (marks[0] == 0 and marks[2] == 0) or (marks[1]== 0 and marks[2] == 0)):
            return 'AF'
    else:
        return 'F'


def cal_marks(marks,final_marks):
    if final_marks >= 85:
        return "HD"
        # print("Grade is HD")
    elif  75 <= final_marks <=84:
        return "D"
        # print("Grade is D")
    elif 65 <= final_marks <= 74:
        return "C"
        # print("Grade is C")
    elif 50 <= final_marks <=64:
        return "P"
        # print("Grade is P")
    elif 45 <= final_marks <= 49:
        grade = cal_F_SA_SE([(marks[0]),(marks[1]),(marks[2])])
        return grade
        # print(grade)
    elif 0<= final_marks <=44:
        grade = cal_F_AF([(marks[0]),(marks[1]),(marks[2])])
        return grade
        # print(grade)
    else:
        print("Invalid Input!")


def Grade_point_BIT(grade):
    if grade in "HD" : 
        grade_score = 4.0
        return grade,grade_score
        #return Grade_Score(grade_score,grade)
    elif grade in "D":
        grade_score = 3.0 
        return grade,grade_score
        #return Grade_Score(grade_score,grade)
    elif grade in "C":
        grade_score = 2.0 
        return grade,grade_score
        #return Grade_Score(grade_score,grade)
    elif grade in "P":
        grade_score = 1.0
        return grade,grade_score
        #return Grade_Score(grade_score,grade)
    elif grade in "SA" or grade in "SE":
        sup_m = int(input("enter sumplementry exam mark :"))
        if sup_m < 50:
            grade = "F"
            print('Grade :', grade )
            grade_score = 0
            return grade,grade_score
        else:
            grade = "SP"
            print('Grade :', grade )
            grade_score = 0.5
            return grade,grade_score
    else:
        return 'F',0

def BIT_student_info():

    while(1):
        id = input("Enter student ID:")
        if len(id) == 9:
            if id[0] in "A" and id[1:].isdigit():
                print("vaild ID.")
            else:
                print("Enter vaild ID")
                BIT_student_info()
        else:
            print("Enter vaild ID")
            BIT_student_info()
        name = input('Enter student name:')
        marks = input("Enter a student's assessment marks (separated by comma):")
        marks = [float(item) for item in marks.split(",")]
        final_marks = math.ceil(marks[0] * 0.2 + marks[1] * 0.4 + marks[2] * 0.4) 
        print('final_marks :', final_marks)
        grade = cal_marks(marks,final_marks)
        print('Grade :', grade)
        Final_grade,Final_score = Grade_point_BIT(grade)
        print('Grade point value :', Final_grade,Final_score)
        s_type="BIT"

        # Insert data into Table 
            
        conn =connector.connect(host= 'localhost', username ='root', password = 'saini890', database='result')
        my_cursor=conn.cursor()
        s='INSERT INTO Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        t=(id,name,s_type,final_marks,Final_grade,marks[0],marks[1],marks[2],Final_score)
    
        my_cursor.execute(s,t)
        conn.commit()

    # conn.close()
        
        
    mainMenu()
        
# DIT student information

def DIT_cal_marks():
    marks = input("Enter a student's assessment marks (separated by comma):")
    marks = [float(item) for item in marks.split(",")]
    final_marks = math.ceil(marks[0] * 0.2 + marks[1] * 0.4 + marks[2] * 0.4) 
    print('final_marks :', final_marks)

    if final_marks >= 50 :
        grade="CP"
        # print("Grade is CP")
        return grade,final_marks,marks
    else:
        grade="NYC"
        # print("Grade is NYC")
        return grade,final_marks,marks

def Grade_point_DIT(grade):
    if grade in "NYC":
        marks = input("Enter a student’s resubmission marks (separated by comma):")
        marks = [float(item) for item in marks.split(",")]
        refinal_marks = math.ceil(marks[0] * 0.2 + marks[1] * 0.4 + marks[2] * 0.4)
        print('Re_final_marks :', refinal_marks)

        if(refinal_marks > 50):
            grade ='CP'
            grade_score = 4.0
            return grade , grade_score,refinal_marks,marks
        else:
            grade ='NC'
            grade_score = 0
            return grade , grade_score,refinal_marks,marks
    
    elif grade in "CP" :
        # print('Grade is CP')
        grade_score = 4.0
        return grade , grade_score ,NULL,NULL
    else :
        grade in "NC"
        # print("Grade is NC")
        grade_score = 0
        return grade , grade_score ,NULL ,NULL
    
def DIT_student_info():
    # Insert data into Table 

    conn =connector.connect(host= 'Localhost', username ='root', password = 'saini890', database='result')
    my_cursor=conn.cursor()
    
    while(1):
        id = input("Enter student ID:")
        if len(id) == 9:
            if id[0] in "A" and id[1:].isdigit():
                print("vaild ID.")
            else:
                print("Enter vaild ID")
                DIT_student_info()
        else:
            print("Enter vaild ID")
            DIT_student_info()

        name = input('Enter student name:')
        # marks = input("Enter a student's assessment marks (separated by comma):")
        # marks = [float(item) for item in marks.split(",")]
        grade,final_marks,marks = DIT_cal_marks()
        print('Grade :', grade,final_marks,marks)
        final_grade,final_grade_socre,refinal_marks,marks = Grade_point_DIT(grade)
        fm = NULL
        if refinal_marks:
            fm=refinal_marks
        else:
            fm=final_marks    
        print('Grade and Grade point value :',final_grade,final_grade_socre,fm)
        s_type ="DIT"

        # Insert data into Table 

        s='INSERT INTO Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        t=(id,name,s_type,fm,final_grade,marks[0],marks[1],marks[2],final_grade_socre)
    
        my_cursor.execute(s,t)
        conn.commit()


    mainMenu()

# all student grade information ascendingly by final mark

def Asc_final_mark():
    
    conn =connector.connect(host= 'Localhost', username ='root', password = 'saini890', database='result')
    cursor = conn.cursor()

    ## defining the Query
    query = "SELECT Stu_ID,Stu_name,Stu_type, Stu_final_mark,Stu_grade FROM Student ORDER BY stu_final_mark"

    ## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    for record in records:
        for i in record:
            print(i, end="  ")
        print()    
    mainMenu()

def Desc_final_mark():
    conn =connector.connect(host= 'Localhost', username ='root', password = 'saini890', database='result')
    cursor = conn.cursor()

    ## defining the Query
    query = "SELECT Stu_ID,Stu_name,Stu_type, Stu_final_mark,Stu_grade FROM Student ORDER BY Stu_final_mark DESC"

    ## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    for record in records:
        for i in record:
            print(i, end="  ")
        print()  
    
    mainMenu()

def performance():
    con=connector.connect(host = 'Localhost', 
                                username ='root', 
                                password = 'saini890', 
                                database='result')
    query = 'select count(Stu_type) from Student '
    cur = con.cursor()
    cur.execute(query)
    # cnt=cur.fetchall()
    # print("Number of students :",cnt)
    for row in cur:
        for stu in row:
            print("Total Number of students :", stu , end="  ")
    print()

    query1 = "select count(Stu_type) from Student where Stu_type = 'BIT'"
    cur = con.cursor()
    cur.execute(query1)
    for row in cur:
        for i in row:
            print("Total Number of students BIT :", i , end="  ")
    print()

    query2 = "select count(Stu_type) from Student where Stu_type = 'DIT'"
    cur = con.cursor()
    cur.execute(query1)
    for row in cur:
        for i in row:
            print("Total Number of students DIT :", i , end="  ")
    print()

    query3 = "select count(Stu_grade) from Student where Stu_grade = 'HD' or Stu_grade ='D' or Stu_grade ='C'or Stu_grade ='P'or Stu_grade ='SP'or Stu_grade ='CP'"
    cur = con.cursor()
    cur.execute(query3)
    # pass_rate = (G/stu)
    for row in cur:
        for g_grade in row:
            pass_rate = round((g_grade/stu),2)
            print("Student pass rate  :", pass_rate , end="  ")
    print()

    query4 = "select count(Stu_grade) from Student where Stu_grade = 'F'"
    cur = con.cursor()
    cur.execute(query4)
    for row in cur:
        for i in row:
            t_no = round((g_grade/stu-i),2)
            # pass_rate1 = (g_grade/t_no)
            print("Students who received an AF from the total number of students  :", t_no , end="  ")
    print()

    q1 = "SELECT AVG(Assessment_1) FROM Student"
    q2 = "SELECT AVG(Assessment_2) FROM Student"
    q3 = "SELECT AVG(Assessment_3) FROM Student"
    q4 = "SELECT AVG(Stu_final_mark) FROM Student"
    q5 = "SELECT AVG(grade_point) FROM Student"
    q6 = "SELECT count(Stu_grade) FROM Student where Stu_grade = 'HD'"
    q7 = "SELECT count(Stu_grade) FROM Student where Stu_grade = 'D'"
    q8 = "SELECT count(Stu_grade) FROM Student where Stu_grade = 'C'"
    q9 = "SELECT count(Stu_grade) FROM Student where Stu_grade = 'P'"
    q10 = "SELECT count(Stu_grade) FROM Student where Stu_grade = 'SP'"
    q11 = "SELECT count(Stu_grade) FROM Student where Stu_grade = 'CP'"
    q12 = "SELECT count(Stu_grade) FROM Student where Stu_grade = 'F'"



    cur = con.cursor()
    cur.execute(q1)
    for row in cur:
        for i in row:
            i1 = round(i,2)
            print("the average mark for Assessment 1  :", i1 , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q2)
    for row in cur:
        for j in row:
            j1 = round(j,2)
            print("the average mark for Assessment 2  :", j1 , end="  ")
    print()
    
    cur = con.cursor()
    cur.execute(q3)
    for row in cur:
        for k in row:
            k1 = round(k,2)
            print("the average mark for Assessment 3 :", k1 , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q4)
    for row in cur:
        for l in row:
            l1 = round(l,2)
            print("the average mark for final mark  :", l1 , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q5)
    for row in cur:
        for m in row:
            m1 = round(m,1)
            print("the average grade point for all students in COMP101  :", m1 , end="  ")
    print()
 
    cur = con.cursor()
    cur.execute(q6)
    for row in cur:
        for a in row:
            print("the number of students who received a final grade letter HD :", a , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q7)
    for row in cur:
        for b in row:
            print("the number of students who received a final grade letter D :", b , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q8)
    for row in cur:
        for c in row:
            print("the number of students who received a final grade letter C :", c , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q9)
    for row in cur:
        for d in row:
            print("the number of students who received a final grade letter P :", d , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q10)
    for row in cur:
        for e in row:
            print("the number of students who received a final grade letter SP :", e , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q11)
    for row in cur:
        for f in row:
            print("the number of students who received a final grade letter CP :", f , end="  ")
    print()

    cur = con.cursor()
    cur.execute(q12)
    for row in cur:
        for g in row:
            print("the number of students who received a final grade letter F :", g , end="  ")
    print()

# main routinne
mainMenu()

