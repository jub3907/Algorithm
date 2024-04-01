#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/17683

def time_c(t):		# 시간계산
    return int(t.split(':')[0])*60 + int(t.split(':')[1])

def change(x):		# #음 치환
    exc = {'C#':'1','D#':'2', 'F#':'3', 'G#':'4', 'A#':'5'}
    for k, v in exc.items():
        x = x.replace(k, v)
    return x

def solution(m, musicinfos):
    answer = []
    for info in musicinfos:
        info = info.split(',')
        info[3] = change(info[3])
        T = time_c(info[1]) - time_c(info[0])	# 시간계산
        
        if T >= len(info[3]):	# 시간이 길이보다 길면
            M = info[3] * (T//len(info[3])) + info[3][:T%len(info[3])]
        else:					# 시간이 길이보다 짧으면
            M = info[3][:T]
        
        if change(m) in M:		# 들은음이 있으면
            answer.append([T, info[2]])
        
    if len(answer) == 0:
        return '(None)'
    else:
        return sorted(answer, key=lambda x: -x[0])[0][1]
    
#%%
def replace(string):
    return string.replace('A#', 'H').replace('B#', 'I').replace('C#', 'J').replace('D#', 'K').replace('F#', 'L').replace('G#', 'N')

def solution(m, musicinfos):
    answer = '(None)'
    m = replace(m)
    max_time = 0
    
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start = start.split(':')
        end = end.split(':')

        time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])
        melody = replace(melody)

        melody = melody * (time // len(melody)) + melody[0:time % len(melody)]

        if m in melody and time > max_time:
            max_time = time
            answer = title
    return answer