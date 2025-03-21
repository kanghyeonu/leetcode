class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        book = defaultdict(list)
        recipeSet = set(recipes)
        supplySet = set(supplies)
        answer = []

        for r, ingredient in zip(recipes, ingredients):
            book[r] = ingredient

        def isPossible(recipe, check):
            if recipe in check:
                return False
            check.append(recipe)
            for ingredient in book[recipe]:    
                if ingredient not in supplySet:
                    if ingredient in recipeSet and not isPossible(ingredient, check):
                        return False
                    elif ingredient not in recipeSet:
                        return False

                    supplySet.add(ingredient)

            return True

        for r in recipes:
            if isPossible(r, []):
                answer.append(r)
                supplySet.add(r)

        return answer

        