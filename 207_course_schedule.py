from collections import defaultdict, deque
from typing import List


class Courses:
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        first_courses = set([i for i in range(0, numCourses)])
        from_course_to_pre_num = defaultdict(int)
        from_pre_to_course = defaultdict(list)
        for course, pre in prerequisites:
            from_course_to_pre_num[course] += 1
            from_pre_to_course[pre].append(course)
            first_courses.discard(course)
        
        queue = deque(list(first_courses))
        visited = set()
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            for next_course in from_pre_to_course[cur]:
                if next_course in visited:
                    continue
                from_course_to_pre_num[next_course] -= 1
                if from_course_to_pre_num[next_course] == 0:
                    queue.append(next_course)
        
        return len(visited) == numCourses
