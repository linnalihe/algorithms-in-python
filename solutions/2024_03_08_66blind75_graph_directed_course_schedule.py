# https://leetcode.com/problems/course-schedule/description/
# all tests passed
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
        
    course_map = [[] for _ in range(numCourses)]
    for curr, prereq in prerequisites:
        course_map[curr].append(prereq)

    visited = [-1 for _ in range(numCourses)]
    arrived = [-1 for _ in range(numCourses)]
    departed = [-1 for _ in range(numCourses)]

    def dfs(c, ts):
        arrived[c] = ts
        ts+=1

        for p in course_map[c]:
            if visited[p] == -1:
                visited[p] = c
                if dfs(p, ts):
                    return True
            else:
                if departed[p] == -1:
                    return True
        departed[c] = ts
        ts+=1

        return False

    ts = 0
    for n in range(numCourses):
        if visited[n] == -1:
            if dfs(n, ts):
                return False
    return True