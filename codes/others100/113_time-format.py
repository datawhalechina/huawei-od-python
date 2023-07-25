from typing import List


def main() -> None :
	n = int(input())
	times = [input() for _ in range(n)]
	solve_method(times)


def solve_method(times : List[str]) -> None:
	sorted_times = sorted(times, key=get_time)
	for t in sorted_times:
		print(t)



def get_time(time_str: str) -> int:
	h = int(time_str.split(':')[0])
	m = int(time_str.split(':' )[1])
	s = int(time_str.split(':')[-1].split('.')[0])
	n = int(time_str.split(':')[-1].split('.')[1])
	return h *60 * 60 * 1000 + m * 60 *1000 + s * 1000 +n


if __name__ == '__main__':
	main()