#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-26 16:13:15
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os

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

	cut_point.append(len(graph_rest)-1)
	for i  in range(1,len(cut_point)):
		l= cut_point[i]-cut_point[i-1]
		res_point1,res_point2=0,0

		if l >=5 and l > (res_point2-res_point1):
			res_point1,res_point2=cut_point[i-1],cut_point[i]

	#res_point1= -1 if res_point1 ==0 else res_point1
	res="NO-CHAIN" if res_point2==0 else "-".join(map(str,graph_rest[res_point1+1:res_point2+1]))

	return res


def solve_method(my, over):

	cards = {}
	for card in graph:
		cards[card] = 4
	for card in (my+"-"+over).split("-"):
		if card in cards:
			cards[card] -= 1
			if cards[card] == 0:
				 del cards[card]
	graph_rest=list(cards.keys())
	
	return find(graph_rest)



if __name__ == "__main__":
	my,over="3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A","4-5-6-7-8-8-8"
	assert solve_method(my,over) == "9-10-J-Q-K-A" 
	my,over="3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A","4-5-6-7-8-8-8"
	assert solve_method(my,over) == "9-10-J-Q-K-A" 
	my,over="3-3-3-3-8-8-8-8","K-K-K-K"
	assert solve_method(my,over) == "NO-CHAIN" 
	my,over="3-8","K-K"
	assert solve_method(my,over) == "3-4-5-6-7-8-9-10-J-Q-K-A"