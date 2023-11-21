#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []

    genre_playtime = {key : 0 for key in set(genres)}
    genre_play = {key : [] for key in set(genres)}
    for genre, play, index in zip(genres, plays, range(len(genres))):
        genre_playtime[genre] += play
        genre_play[genre].append([play, index])
    
    for genre, playtime in sorted(genre_playtime.items(), key = lambda x: x[1], reverse = True):
        tmp = genre_play[genre]
        sorted_genre_play = sorted(tmp, key = lambda x: (x[0], -x[1]), reverse = True)
        if len(sorted_genre_play) == 1:
            answer.append(sorted_genre_play[0][1])
        else:
            answer.append(sorted_genre_play[0][1])
            answer.append(sorted_genre_play[1][1])

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
# %%
