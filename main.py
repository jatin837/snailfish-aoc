# snailfishes = ['[1,1]','[2,2]', '[3,3]', '[4,4]']
from collections import deque

snailfishes = ['[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]']
initial_fish = snailfishes[0]

stack = list()

for c in initial_fish:
    if c == '[':
        stack.append(c)
    if c == ']':
        stack.pop()


for fish in snailfishes[1:]:
    fish = '[' + initial_fish + ','+ fish + ']'
    initial_fish = fish
    print(fish)

split = lambda x : [x//2, x - x//2]
