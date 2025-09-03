import math


def main():
    testCase1()
    testCase2()
    testCase3()
    testCase4()

def circleArrayRadiusSort(inputArray):
    sortedArray = []
    tempArray = inputArray.copy()
    while tempArray:
        minTuple = tempArray[0]
        for tuple in tempArray:
            if tuple[-1] < minTuple[-1]:
                minTuple = tuple
        sortedArray.append(minTuple)
        tempArray.remove(minTuple)
    return sortedArray

def intersectChecker(inputArray):
    n = len(inputArray)
    adjListOfCircles = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if circlesIntersect(inputArray[i], inputArray[j]):
                adjListOfCircles[i].append(j)
                adjListOfCircles[j].append(i)
    visited = [False] * n

    def dfsForCircles(u):
        visited[u] = True
        for v in adjListOfCircles[u]:
            if not visited[v]:
                dfsForCircles(v)
    dfsForCircles(0)
    return all(visited)

def circlesIntersect(circle1, circle2):
    distance = math.sqrt((circle1[0] - circle2[0]) ** 2 + (circle1[1] - circle2[1]) ** 2)
    return distance <= circle1[2] + circle2[2]

def testCase1():
    input1 = (1,3,0.7)
    input2 = (2,3,0.4)
    input3 = (3,3,0.9)

    circleList = [input1, input2, input3]
    sortedList = circleArrayRadiusSort(circleList)
    print(circleArrayRadiusSort(circleList))
    print(intersectChecker(sortedList))

def testCase2():
    input1 = (1.5,1.5,1.3)
    input2 = (4,4,0.7)

    circleList = [input1, input2]
    sortedList = circleArrayRadiusSort(circleList)
    print(circleArrayRadiusSort(circleList))
    print(intersectChecker(sortedList))

def testCase3():
    input1 = (0.5,0.5,0.5)
    input2 = (1.5,1.5,1.1)
    input3 = (0.7,0.7,0.4)
    input4 = (4,4,0.7)

    circleList = [input1, input2, input3, input4]
    sortedList = circleArrayRadiusSort(circleList)
    print(circleArrayRadiusSort(circleList))
    print(intersectChecker(sortedList))

def testCase4():
    input1 = (0.5,0.5,0.5)
    input2 = (1.5,1.5,1.1)
    input3 = (3.5,3.5,0.8)
    input4 = (4,4,0.7)

    circleList = [input1, input2, input3, input4]
    sortedList = circleArrayRadiusSort(circleList)
    print(circleArrayRadiusSort(circleList))
    print(intersectChecker(sortedList))

if __name__ == "__main__":
    main()