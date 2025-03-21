#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        s = set(supplies)
        r = set(recipes)
        g = defaultdict(list)
        cache = {}
        answer = []

        for index, recipe in enumerate(recipes):
            for ingredient in ingredients[index]:
                g[recipe].append(ingredient)

        def isPossible(recipe):
            queue = deque()
            visited = set()
            queue.append(recipe)
            visited.add(recipe)
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in g[node]:
                        if neighbor in visited:
                            cache[recipe] = False
                            return False
                        if neighbor not in s:
                            if neighbor not in r:
                                cache[recipe] = False
                                return False
                            else:
                                if neighbor in cache:
                                    if not cache[neighbor]:
                                        cache[recipe] = False
                                        return False
                                else:
                                    queue.append(neighbor)
                                    visited.add(recipe)
                            
            cache[recipe] = True
            return True

        for recipe in recipes:
            if isPossible(recipe):
                answer.append(recipe)

        return answer
# @lc code=end

