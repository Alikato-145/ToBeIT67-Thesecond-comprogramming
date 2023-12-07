'''Hello <i>Judge'''

def main():
    sec = int(input())
    day = sec //86400
    sec = sec - day*86400
    hour = sec // 3600
    sec = sec - hour*3600
    minute = sec //60
    sec = sec - minute*60
    result_day = day > 1 and "days" or "day"
    result_hour = hour > 1 and "hours" or "hour"
    result_min = minute > 1 and "minutes" or "minute"
    result_sec = sec > 1 and "seconds." or "second."

    print(day,result_day,hour,result_hour,minute,result_min,sec,result_sec)
main()