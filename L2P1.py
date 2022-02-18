def bunkcoord(tup):
    x = tup // 8
    y = tup % 8
    return x, y


def createstate():
    return [[0 for j in range(8)] for i in range(8)]


def toaddtoqueue(src, state):
    possible = [(x, y) for x in [1, -1] for y in [2, -2]]
    possible += [(y, x) for x in [1, -1] for y in [2, -2]]
    queue_addendum = []
    for elem in possible:
        # print(src[0], elem[0])
        point = (src[0] + elem[0], src[1] + elem[1])
        if point[0] < 0 or point[0] > 7 or point[1] < 0 or point[1] > 7:
            continue
        if state[point[0]][point[1]] == 0:
            queue_addendum.append((src[0] + elem[0], src[1] + elem[1]))
            state[point[0]][point[1]] = state[src[0]][src[1]] + 1
    return queue_addendum


def solution(src, desc):
    if src == desc:
        return 0;
    state = createstate()
    src = bunkcoord(src)
    desc = bunkcoord(desc)
    #state[src[0]][src[1]] = 0
    queue = [src]
    for i in range(64):
        src = queue[0]
        newbatch = toaddtoqueue(src, state)
        queue += newbatch
        #print(newbatch)
        # print(queue)
        for elem in newbatch:
            if elem == desc:
                return state[src[0]][src[1]] + 1
        queue.pop(0)

print(solution(0,0))












