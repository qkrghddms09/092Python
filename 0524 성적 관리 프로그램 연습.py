#coding: euc-kr

def style():                                #���� �Լ�
    print()
    print("-"*40)
    print()


def form_score(a, b):                       #������ ����� �Լ�
    print("���� :", a)
    print("��� :", b)

def cnt_loop():
    while True:
        cnt = input("��� �Ͻðڽ��ϱ�?(y/n)")
    
        if cnt == "y" or cnt == "Y" or cnt == "��":
            return  1

        elif cnt == "n" or cnt == "N" or cnt == "��":
            return  0    

        else:
            print("�߸��� ��û�Դϴ�. �ٽ� �Է��� �ּ���")
            pass

def sub_name_append(sub_num):
    for i in range(sub_num):                #����� ��ŭ ������ �޴� for��
        #sub_name : ���� �̸��� �޴� ����
        sub_name = input("���� �̸��� �Է��ϼ���: ")
        list_sub_name.append(sub_name)      #���� �̸� ���� ����Ʈ�� ������ �߰�
    return list_sub_name


def std_data_list_append(std, sub_num):
    std_data_list_local = []
    for i in range(std):                    #�л��� ��ŭ �л��� �����͸� �޴� for��
        #1���� �л��� ���� �����͸� �����ϱ� ���� ����Ʈ, ���´� [�л��̸�, ����, ����, ����]
        std_data = []                       
        print(i+1, end="")                  
        std_name = input("��° �л� �̸� �Է� : ")
        std_data.append(std_name)
        for j in range(sub_num):            #����� ��ŭ �л��� ������ �޽��ϴ�.
            print("'", std_name, "'", "�л��� ", list_sub_name[j], "���� ���� : ", end ="")

            #���� ������ �޴� ����
            sub_score = int(input())        
            
            std_data.append(sub_score)      #1���� �л��� ���� �����͸� append

        std_data_list_local += [std_data]         #�л� ������ ����Ʈ��  �л� �����͸� ����Ʈ ���·� ����
                                            #['ȫ�浿', 70, 80, 90, ...] ����
    return std_data_list_local
        
def std_sum_and_avg(std, sub_num, std_data_list):
    #���� �л��� ���� ����� ���� for��
    for i in range(std):                    #�л� �� ��ŭ ������ : for��
        sum0 = 0
        avg0 = 0.0
        
        print()
        print("'", std_data_list[i][0], "'", "�л��� ����")
        
        for j in range(1, sub_num+1):           #���� �� ��ŭ ������
            sum0 += int(std_data_list[i][j])    #������  �л�_������_����Ʈ[0][1] ~ [1][1]
        
        avg0 = sum0/sub_num
        form_score(sum0, avg0)

        style()

def sub_sum_and_avg(sub_num, list_sub_name, std, std_data_list):
    #���� ������ ���� ����� ���� for��   
    for j in range(sub_num):                     #����� ��ŭ ������ for��
        sum01 = 0
        avg01 = 0.0
        
        print()
        print("'", list_sub_name[j], "'", "���� ��ü ������ ���")
            
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
        print("           ���� ���� ���α׷�")
        print("�� �л��� ������ ���, ���� ��ü ������ ����� ����մϴ�.")
        print("="*60)

        list_sub_name = []                      #���� �̸��� ��� ���� ����Ʈ
        std_data_list = []                      #�л��� �����͸� ��� ���� ����Ʈ

        #std : �л� ���� �޴� ����
        #sub_num : ���� ���� �޴� ����
        std = int(input("�л� ���� �Է��ϼ��� : "))
        sub_num = int(input("���� ���� �Է��ϼ��� : "))
        style()
        list_sub_name = sub_name_append(sub_num)
        style()        
        std_data_list = std_data_list_append(std, sub_num)
        style()
        #sum_list = ['���� �հ�']
        #avg_list = ['���� ���']

        std_sum_and_avg(std, sub_num, std_data_list)

        sub_sum_and_avg(sub_num, list_sub_name, std, std_data_list)
        
        style()      
        loop = cnt_loop()                        #while���� ���������� �Լ� ȣ��
