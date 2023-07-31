def solve_method(M, scores):
    min_scores = []
    for i in range(len(scores)-M+1):
        min_score = scores[i]
        for j in range(1, M):
            min_score = min(min_score, scores[i+j])
        min_scores.append(min_score)
    return ','.join(map(str, min_scores))

if __name__ == "__main__":
    # 3
    # 12,3,8,6,5
    M = int(input())
    scores = list(map(int, input().split(',')))
    print(solve_method(M, scores))

    assert solve_method(3, [12,3,8,6,5]) == "3,3,5"