import itertools
def solve_method(n,segment):
    segement = segment.split(" ")
    permutation_list = list(itertools.permutations(segement))
    permutation_list = list(set(["".join(i) for i in permutation_list]))
    permutation_list.sort()
    for item in permutation_list:
        print(item)

def main():
    n=int(input().strip())
    segment = input().strip()
    solve_method(n,segment)

if __name__ == '__main__':
    main()


