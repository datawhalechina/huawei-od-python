def getWordDict(s)->list:
	# return LIST recording dict of String
	wd = [0] * 26 # Word Dictionary of 26 Chars
	for c in s:
		wd[ord(c) - ord('a')] += 1
	return wd

def solution(s1, s2, k):
	'''
	Compare Word Dict
	'''
	wd_s1 = getWordDict(s1)
	# first (len(s1) + k) substring
	wd_s2 = getWordDict(s2[:len(s1) + k])
	# matches at first index
	if wd_s1 <= wd_s2: # compare LIST of same size
		return 0
	else:
		for r in range(len(s1) + k, len(s2)): # new right BDRY(Boundary)
			l = r - (len(s1) + k) # old left BDRY
			rw, lw = s2[r], s2[l]
			wd_s2[ord(rw) - ord('a')] += 1
			wd_s2[ord(lw) - ord('a')] -= 1
			if wd_s1 <= wd_s2:
				return l + 1
		return -1 # failed

if __name__ == "__main__":
	s1, s2 = input(), input()
	k = int(input())
	print(solution(s1, s2, k))