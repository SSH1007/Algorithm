# 연도를 받아 윤년 월들, 혹은 평년 월들을 반환하는 함수
def getMonths(year):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    # 년도가 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않거나 400으로 나누어 떨어지면 윤년!
    if year%4==0 and year%100!=0 or year%400==0:
        months[1] = 29
    return months

# 1년 1월 1일부터 주어진 날짜까지의 일 수를 반환하는 함수
def getDays(year, month, day):
    # 총 일 수 초기값
    days = 0
    # 1년부터 (주어진 년도-1)년까지 반복
    for i in range(1,year):
        # 해당 년도의 월들을 반환
        months = getMonths(i)
        # 월마다의 일 수를 총 일 수에 더해준다
        for j in range(12):
            days += months[j]

    # 주어진 년도의 월들을 반환한다.
    months = getMonths(year)
    # 주어진 년도의 월들의 날짜 수들을 총 일 수에 더해준다.
    # (주어진 월(month)은 포함하지 않는다)
    for i in range(month-1):
        days += months[i]
    
    # 주어진 날짜의 일 수를 총 일 수에 더해준다.
    days += day

    # 총 일 수를 반환한다.
    return days

# 오늘의 날짜와 D-Day 날짜 받기
ty, tm, td = map(int, input().split())
dy, dm, dd = map(int, input().split())
# 오늘이 y년 m월 d일이고, D-day가 y+1000년 m월 d일과 같거나 늦다면 gg를 출력
if dy-ty>1000 or (dy-ty==1000 and dm>tm) or (dy-ty==1000 and dm==tm and dd>=td):
    print('gg')
# 아니면 D-{남은 일자}를 출력
else:
    print(f'D-{getDays(dy, dm, dd) - getDays(ty, tm, td)}')