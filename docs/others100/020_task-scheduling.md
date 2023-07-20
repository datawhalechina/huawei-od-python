# 020_任务调度

## 题目描述

现有一个CPU和一些任务需要处理，已提前获知每个任务的任务D、优先级、所需执行时间和到达时间。
CPU同时只能运行一个任务，请编写一个任务调度程序，采用“可抢占优先权调度”调度算法进行任务调度，规则如下

* 如果一个任务到来时，CPU是空闲的，则CPU可以运行该任务直到任务执行完毕。但是如果运行中有一个更高优先级的任务到来，
  则CPU必须暂停当前任务去运行这个优先级更高的任务；
* 如果一个任务到来时，CPU正在运行一个比他优先级更高的任务时，信道大的任务必须等待：
* 当CPU空闲时，如果还有任务在等待，CPU会从这些任务中选择一个优先级最高的任务执行，相同优先级的任务选择到达时间最早
  的任务。

## 输入描述

输入有若干行，每一行有四个数字（均小于10^8），
分别为任务ID,任务优先级，执行时间和到达时间。
每个任务的任务D不同，优先级数字越大优先级越高，
并且相同优先级的任务不会同时到达。
输入的任务已按照到达时间从小到大排序，并且保证在任何时间，
处于等待的任务不超过10000个。

## 输出描述

按照任务执行结束的顺序

## 示例描述

### 示例一

**输入：**
```text
1 3 5 1
2 1 5 10
3 2 7 12
4 3 2 20
5 4 9 21
6 4 2 22
```

**输出：**
```text
1 6
3 19
5 30
6 32
4 33
2 35
```

## 解题思路

该算法实现了一种基于等级的简单调度算法：

1. 其中任务在任务列表中根据其开始时间以先进先出的顺序排队
2. 按照等级的高低顺序优先处
   理。
3. 该算法将任务添加到等待队列中，然后对等待队列进行排序，以获得最高级别的任务。

## 解题代码

```python
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
```

