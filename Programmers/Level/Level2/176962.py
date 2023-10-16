def solution(plans):
    answer = []
    plan_list = []
    for plan in plans:
        minute = convertMinute(plan[1])
        plan_list.append([minute, plan[0], int(plan[2])])
    plan_list.sort(key=lambda x: x[0])
    wait = []
    for idx, plan in enumerate(plan_list):
        if idx == len(plan_list) - 1:
            break
        name, remain_time = plan[1], plan[2]
        cur_time = plan[0]
        next_time = plan_list[idx + 1][0]
        can_work_time = next_time - cur_time
        if can_work_time > remain_time:
            answer.append(name)
            middle_time = can_work_time - remain_time
            while middle_time and wait:
                wait_plan = wait.pop()
                wait_plan_remain = wait_plan[2]
                if wait_plan_remain > middle_time:
                    wait_plan[2] -= middle_time
                    middle_time = 0
                    wait.append(wait_plan)
                    break
                elif wait_plan_remain == middle_time:
                    answer.append(wait_plan[1])
                    middle_time = 0
                else:
                    answer.append(wait_plan[1])
                    middle_time -= wait_plan_remain
        elif can_work_time == remain_time:
            answer.append(name)
        else:
            plan[2] -= can_work_time
            wait.append(plan)

    answer.append(plan_list[-1][1])
    while wait:
        answer.append(wait.pop()[1])

    return answer


def convertMinute(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return hour * 60 + minute
