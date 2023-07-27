#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-26 22:50:13
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

graph = ["3","4","5","6","7","8","9","10","J","Q","K", "A"]
#给牌按顺序标记 以便于后面找连续的牌
graph_num={}
for i in range(len(graph)):
	graph_num[graph[i]] = i
def find(graph_rest): 
	#记录不连续的位置
	cut_point=[-1]
	for i in range(len(graph_rest)-1):
		if  graph_num[graph_rest[i+1]]-graph_num[graph_rest[i]]>1:
			cut_point.append(i)
	res=[]
	cut_point.append(len(graph_rest)-1)
	for i  in range(1,len(cut_point)):
		l= cut_point[i]-cut_point[i-1]
		res_point1,res_point2=0,0

		if l >=5 :
			res_point1,res_point2=cut_point[i-1],cut_point[i]
			#res_point1= -1 if res_point1 ==0 else res_point1
			if res_point2!=0:
				res.append(" ".join(map(str,graph_rest[res_point1+1:res_point2+1])))

	return res


def solve_method(s):
	s=s.split(" ")
	s1=[]
	for i in graph:
		s1.append(s.count(i))
	maxcount=max(s1)
	checklist=[]
	for i in range(maxcount):
		sub_checklist=[]
		for j in  range(len(s1)):
			if s1[j] >0 :
				sub_checklist.append(graph[j])
				s1[j]-=1

		checklist.append(sub_checklist)

	result=[]
	
	for  i in checklist:
		result.extend(find(i))
	
	if len(result)==0:
		result=["No"]
	else:
		result.sort(key=lambda x :  graph_num[x[0]] if x!='10' else graph_num['10'])
	return result


if __name__ == "__main__":
	
	assert solve_method("2 9 J 10 3 4 K A 7 Q A 5 6") == ['3 4 5 6 7', '9 10 J Q K A']
	assert solve_method("2 9 J 2 3 4 K A 7 9 A 5 6") == ['3 4 5 6 7']
	assert solve_method("2 9 9 9 3 4 K A 10 Q A 5 6") == ['No']