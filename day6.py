inputs = [int(n) for n in open("day6.txt").read().splitlines()[0].split(',')]
days = 256

states = [0]*9
for input in inputs:
    states[input] += 1

for _ in range(0,days):
    newborns = states[0]
    for i in range(0,8):
        states[i] = states[i+1]
    states[6] += newborns
    states[8] = newborns
    
print(sum(states))