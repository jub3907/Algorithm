#%%
# https://www.acmicpc.net/problem/2581
start = int(input())
end = int(input())

primes = []
for num in range(start, end+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  
            if num % i == 0:
                error += 1
                break  
        if error == 0:
            primes.append(num) 
            
if len(primes) > 0 :
    print(sum(primes))
    print(min(primes))
else:
    print(-1)