import heapq

def solution(endingTime, jobs):
    answer = []
    realtime_queue = []
    current_time = 0
    for i in range(len(jobs)):
        number, enter, valid, work_time = jobs[i][0], jobs[i][1], jobs[i][2], jobs[i][3]
        heapq.heappush(realtime_queue, (enter, number, valid, work_time))
    
    while realtime_queue:
        enter, number, valid, work_time = heapq.heappop(realtime_queue)
        if valid < current_time:
            continue
        if current_time < enter:
            current_time = enter
        current_time += work_time
        if current_time <= valid and current_time <= endingTime:
            answer.append(number)

    return answer


solution(0, [[1, 10, 20, 4], [2, 12, 20, 2]])