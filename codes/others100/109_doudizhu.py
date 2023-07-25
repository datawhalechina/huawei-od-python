graph = ["3","4","5","6","7","8","9","10","J","Q","K", "A"]
cards = {}
for card in graph:
	cards[card] = 4

def solveMethod(my, over):
	diff(cards, my)
	diff(cards, over)
	#print(cards)
	res = find(cards)
	print(res)


def diff(cards,string):
	for card in string.split("-"):
		if card in cards:
			cards[card] -= 1


def find(cards):
	res = "NO-CHAIN"

	l, r = 0 , 0 
	for i in range(0, len(graph)):
		card = graph[i]
		if cards[card] > 0:
				l = i
				while  i < len(graph) - 1 and cards[graph[i + 1]] > 0:
					i += 1

				r = i + 1

				if r - l > 5:
					res = "-".join(graph[l:r])


	return res

my = input()
over = input()
solveMethod(my,over)

