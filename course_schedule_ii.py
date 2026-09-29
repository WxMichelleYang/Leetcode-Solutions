from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        nextCourses = [[] for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]
        
        for p in prerequisites:
            fromCourse = p[1]
            toCourse = p[0]
            nextCourses[fromCourse].append(toCourse)
            inDegree[toCourse] += 1
            
        dq = deque(i for i in range(numCourses) if inDegree[i] == 0)
        ret = []
        while dq:
            curFrom = dq.popleft()
            ret.append(curFrom)
            for curTo in nextCourses[curFrom]:
                inDegree[curTo] -= 1
                if inDegree[curTo] == 0:
                    dq.append(curTo)
        if len(ret) < numCourses:
            return []
        return ret


# build a directed graph from the input course ids and the prerequisite relations
# node -> course 
# A -> B, A is the prerequisite course
# inDegree to store the number of prerequisite courses of a course A
# and we further traverse this directed graph using BFS 
# If a course's indegree is zero, it means all its prerequisite courses are finished.
# We first select all the courses with 0 inDegree and put them into the queue,

# 1.Fetch a course from the queue, and put it in the result list ret, 
# 2. for every neigbour of this course, its indegree decrease 1; so if we find a neighbour's indegree
# becomes zero, we add it to the queue; 

# Repeat this process till the queue is null
# Finally, if the length of ret is smaller than the number of courses, it mean there are cycles in the graph;
# we will return a null list; otherwise return ret;   
