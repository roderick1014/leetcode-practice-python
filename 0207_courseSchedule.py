# 0207 - Course Schedule

'''
    Question:
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
        You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        Return true if you can finish all courses. Otherwise, return false.
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # To solve the problem we can create a graph which doesn't consist the ring!
        course_graph = [[] for _ in range(numCourses)]
        traversed = [0 for _ in range(numCourses)]

        for course, condition in prerequisites:
            course_graph[course].append(condition)

        for index in range(numCourses):
            if not self.dfs(course_graph, traversed, index):
                return False
                    
        return True
    
    def dfs(self, course_graph, traversed, index):
        if traversed[index] == -1: # If the vertex is being traversed → ring/cycle happens.
            return False
        if traversed[index] == 1:  # If the vertex is done traversed.
            return True
        traversed[index] = -1      # 
        for idx in course_graph[index]:   # Check if ring/cycle happes.
            if not self.dfs(course_graph, traversed, idx):
                return False
        traversed[index] = 1       # If there's no ring in this iteration, set 1 as done of the traversed.
        
        return True
        
if __name__ == '__main__':
    numCourses = 5
    # prerequisites = [[0,1],[1,0]]
    prerequisites = [[1,4],[2,4],[3,1],[3,2]]
    sol = Solution()
    ans = sol.canFinish(numCourses, prerequisites)
    print(ans)