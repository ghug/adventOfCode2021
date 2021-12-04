lines = open("a.txt").read().splitlines()
nums = lines[0].split(',')

boards = ' '.join(lines[1:]).split()
boards = [int(n) for n in boards]

def runPlay(n):
    for i in range(0,len(boards)):
        if int(boards[i]) == int(n):
            boards[i] = -1

def checkBoard(arr):
    for n in range(0,5):
        if sum(arr[n*5:n*5+5]) == -5 or sum(arr[n:25:5]) == -5:
            return True

# added ids for part 2
ids = set([int(n) for n in range(100)])

for num in nums:
    runPlay(num)
    for i in range(0,len(boards),25):
        if int(i/25) in ids:
            if checkBoard(boards[i:i+25]):
                s = 0
                for l in boards[i:i+25]:
                    if l != -1:
                        s += l
                ## part 1:
                # print(int(s)*int(num))
                # exit()
                if len(ids) == 1:
                    print(int(s)*int(num))
                    exit()
                else:
                    ids.discard(i/25)