# coding:utf-8
import sys
task_list = []
while True:
    line = sys.stdin.readline()#从标准输入读取一行
    if not line:
        break
    task_list.append([int(x) for x in line.split(" ")])#将读取的行转换为整数列表并添加到任务列表中
time = 0 #初始化时间为0
waiting_list=[] #初始化等待列表为空
while len(task_list)>0:#只要任务列表不为空就继续执行
    current_task=next((task for task in task_list if task[3]==time),None) #获取当前时间的任务
    if current_task is not None:#如果有当前时间的任务
        waiting_list.append(current_task)#将任务添加到等待列表中
        waiting_List=sorted(waiting_List,key=lambda x: -x[1])#按照优先级对等待列表进行排序
        current_task=waiting_List[0]#获取优先级最高的任务
    else:
        if len(waiting_List)!=0:#如果没有当前时间的任务但等待表不为空
            current_task=waiting_List[0]#获取优先级最高的任务
    if current_task is not None:#如果有任务
        current_task[2]-=1#执行任务
        if current_task[2]==0 :#如果任务执行完毕
            print(str(current_task[0])+""+str(time+1))#输出任务编号和完成时间
            task_list.remove(current_task)#从任务列表中移除任务
            waiting_List.remove(current_task)#从等待表中移除任务
    time +=1 #时间加1