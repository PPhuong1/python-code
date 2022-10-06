def input_from_user():
    first=[]
    while True:
        inputs=input("Exam points and exercises completed: ")
        if inputs!="":
            sep=inputs.split(' ')
            for i in sep:
                first.append(i)
        else:
            break
    print ("Statistics:")
    return first

def total_point(first):
    exam=[]
    exer=[]
    for i in range(0,len(first)):
        if i%2==0 :
            exam.append(first[i])
       
        elif i%2 !=0:
            exer.append(int(first[i])*0.1)
    result=[]
    for i in range(len(exam)):
        result.append(int(exam[i])+int(exer[i]))
    return result

def grade(first:list):
    final_total_score=total_point(first)
    exam=[]
    for i in range(0,len(first)):
        if i%2==0 :
            exam.append(int(first[i]))
       
    final_grade=[]
    for i in range(len(final_total_score)):
        if final_total_score[i] <=14 or exam[i]<10:
            i=0
            final_grade.append(i)          
        elif final_total_score[i] <=17:
            i=1
            final_grade.append(i)
        elif final_total_score[i] <=20:
            i=2
            final_grade.append(i)
        elif final_total_score[i]<=23:
            i=3
            final_grade.append(i)
        elif final_total_score[i]<=27:
            i=4
            final_grade.append(i)
        else:
            i=5
            final_grade.append(i)
    return final_grade

def avera (result:list):
    return f"Points average: {sum(result)/len(result)}"

def pass_score(score:list):
    pass_score=[]
    for i in score:
        if i>0:
            pass_score.append(i)
      
    pass_per=round(((len(pass_score)/len(score) )*100),1)
    return f"Pass percentage: {pass_per}"

def distribution(total_scr:list):
    print("Grade distribution:")
    for i in range(5,-1,-1):
        dis=(total_scr.count(i))* "*"
        print( f"{i}: {dis}")



input1= input_from_user()
sep1=total_point(input1)
total_scr=grade(input1)
a=avera(sep1)
print(a)
b=pass_score(total_scr)
print(b)
c=distribution(total_scr)

