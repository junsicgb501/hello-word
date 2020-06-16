answer="go"
student_list=[ ]
score_list=[ ]
while answer=="go":
    id=input("학번:")
    student_list.append(id)
    name=input("이름:")
    student_list.append(name)
    a1=input("수강과목1:")
    student_list.append(a1)
    a2=input("수강과목2:")
    student_list.append(a2)
    a3=input("수강과목3:")
    student_list.append(a3)

    score_list.append(id)
    score_list.append(name)
    a1=input(a1+"성적을 입력하세요:")
    score_list.append(a1)
    a2=input(a2+"성적을 입력하세요:")
    score_list.append(a2)
    a3=input(a3+"성적을 입력하세요:")
    score_list.append(a3)
    print("=======================")
    print("학번:"+"이름:"+a1+a2+a3)
    print("=======================")
    print(score_list)
    print("=======================")
    answer=input("프로그램 계속(go), 종료(end):")
