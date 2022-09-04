import math


def solution(fees, records):
    answer = []
    record_dict = {}
    record_flag = {}
    for record in records:
        record_arr = record.split(' ')
        prev = record_dict[record_arr[1]] if record_arr[1] in record_dict else 0
        time, flag = calculate_time(record_arr[0], record_arr[2])
        record_dict[record_arr[1]] = prev + time
        record_flag[record_arr[1]] = flag
    for key in record_flag:
        if record_flag[key] == 0:
            continue
        else:
            record_dict[key] = record_dict[key] + (23 * 60 + 59)
    sorted_record = sorted(record_dict.items())
    for record in sorted_record:
        answer.append(calculate_fee(fees, record[1]))

    return answer


def calculate_time(time, history):
    t = time.split(':')
    minutes = int(t[0]) * 60 + int(t[1])
    if history == 'IN':
        return minutes * (-1), 1
    else:
        return minutes, 0


def calculate_fee(fees, time):
    if time < fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]