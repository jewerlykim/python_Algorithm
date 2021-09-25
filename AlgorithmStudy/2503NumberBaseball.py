import sys
from itertools import permutations

sys.stdin = open("AlgorithmStudy/2503.txt", 'r')

question_times = int(sys.stdin.readline())

answer_hints = list()


def get_hints(question_times):
    for _ in range(question_times):
        hint_num, strikes, balls = map(int, sys.stdin.readline().split())
        answer_hints.append((hint_num, strikes, balls))


get_hints(question_times=question_times)

candidate_numbers = list()


def init_candidate():
    one_to_nine = list()
    for i in range(1, 10, 1):
        one_to_nine.append(i)
    candidate_numbers.extend(list(permutations(one_to_nine, 3)))


init_candidate()


def compare_numbers(candidates, hints, depth):
    new_candidates = list()
    hint_num, strikes, balls = hints
    using_hint = str(hint_num)
    for candidate_num in candidates:
        strike_counts, ball_counts = 0, 0
        for i in range(3):
            if int(using_hint[i]) in candidate_num:
                if int(using_hint[i]) == candidate_num[i]:
                    strike_counts += 1
                else:
                    ball_counts += 1
        if (strike_counts, ball_counts) == (strikes, balls):
            new_candidates.append(candidate_num)
    if depth < question_times - 1:
        depth += 1
        return compare_numbers(new_candidates, answer_hints[depth], depth)
    else:
        return len(new_candidates)

print(compare_numbers(candidate_numbers, answer_hints[0], 0))
