class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        closable = set()
        for f, s in prerequisites:
            if f in courses:
                courses[f].append(s)
            else:
                courses[f] = [s]

        def dfs(n, visited):
            if n in closable:
                return True 
            if n in visited:
                return False
            if n not in courses:
                return True
            visited.add(n)
            flag = True
            for prerec in courses[n]:
                flag &= dfs(prerec, visited)
            visited.remove(n)
            return flag

        for f, s in prerequisites:
            visited = set()
            if not dfs(f, visited):
                return False
            closable.add(f)
        return True

        
