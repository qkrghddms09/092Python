#coding: euc-kr

def style():                                #서식 함수
    print()
    print("-"*40)
    print()


def form_score(a, b):                       #서식을 만드는 함수
    print("총점 :", a)
    print("평균 :", b)

def cnt_loop():
    while True:
        cnt = input("계속 하시겠습니까?(y/n)")
    
        if cnt == "y" or cnt == "Y" or cnt == "ㅛ":
            return  1

        elif cnt == "n" or cnt == "N" or cnt == "ㅜ":
            return  0    

        else:
            print("잘못된 요청입니다. 다시 입력해 주세요")
            pass

def sub_name_append(sub_num):
    for i in range(sub_num):                #과목수 만큼 과목을 받는 for문
        #sub_name : 과목 이름을 받는 변수
        sub_name = input("과목 이름을 입력하세요: ")
        list_sub_name.append(sub_name)      #과목 이름 모음 리스트에 과목을 추가
    return list_sub_name


def std_data_list_append(std, sub_num):
    std_data_list_local = []
    for i in range(std):                    #학생수 만큼 학생의 데이터를 받는 for문
        #1명의 학생에 대한 데이터를 축적하기 위한 리스트, 형태는 [학생이름, 점수, 점수, 점수]
        std_data = []                       
        print(i+1, end="")                  
        std_name = input("번째 학생 이름 입력 : ")
        std_data.append(std_name)
        for j in range(sub_num):            #과목수 만큼 학생의 성적을 받습니다.
            print("'", std_name, "'", "학생의 ", list_sub_name[j], "과목 성적 : ", end ="")

            #과목 점수를 받는 변수
            sub_score = int(input())        
            
            std_data.append(sub_score)      #1명의 학생에 대한 데이터를 append

        std_data_list_local += [std_data]         #학생 데이터 리스트에  학생 데이터를 리스트 형태로 축적
                                            #['홍길동', 70, 80, 90, ...] 형태
    return std_data_list_local
        
def std_sum_and_avg(std, sub_num, std_data_list):
    #각각 학생의 성적 평균을 내는 for문
    for i in range(std):                    #학생 수 만큼 돌려라 : for문
        sum0 = 0
        avg0 = 0.0
        
        print()
        print("'", std_data_list[i][0], "'", "학생의 성적")
        
        for j in range(1, sub_num+1):           #과목 수 만큼 돌려라
            sum0 += int(std_data_list[i][j])    #접근은  학생_데이터_리스트[0][1] ~ [1][1]
        
        avg0 = sum0/sub_num
        form_score(sum0, avg0)

        style()

def sub_sum_and_avg(sub_num, list_sub_name, std, std_data_list):
    #각각 과목의 성적 평균을 내는 for문   
    for j in range(sub_num):                     #과목수 만큼 돌리는 for문
        sum01 = 0
        avg01 = 0.0
        
        print()
        print("'", list_sub_name[j], "'", "과목 전체 총점과 평균")
            
        for k in range(std):
            sum01 += int(std_data_list[k][j+1])
             
        avg01 = sum01/std
        form_score(sum01, avg01)
                   
        style()
    

if __name__ == "__main__":       
    loop=1
    while loop:
        print()
        print("="*60)
        print("           성적 관리 프로그램")
        print("각 학생당 총점과 평균, 과목별 전체 총점과 평균을 계산합니다.")
        print("="*60)

        list_sub_name = []                      #과목 이름을 모아 놓은 리스트
        std_data_list = []                      #학생의 데이터를 모아 놓은 리스트

        #std : 학생 수를 받는 변수
        #sub_num : 과목 수를 받는 변수
        std = int(input("학생 수를 입력하세요 : "))
        sub_num = int(input("과목 수를 입력하세요 : "))
        style()
        list_sub_name = sub_name_append(sub_num)
        style()        
        std_data_list = std_data_list_append(std, sub_num)
        style()
        #sum_list = ['과목 합계']
        #avg_list = ['과목 평균']

        std_sum_and_avg(std, sub_num, std_data_list)

        sub_sum_and_avg(sub_num, list_sub_name, std, std_data_list)
        
        style()      
        loop = cnt_loop()                        #while문을 빠져나가는 함수 호출
