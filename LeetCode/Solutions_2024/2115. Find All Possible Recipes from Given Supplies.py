from functools import cache


class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:

        # hash for faster check is_member:

        supplies = set(supplies)

        # dict: name : ingredient list
        recepie_ingredients = {}
        for i, name in enumerate(recipes):
            recepie_ingredients[name] = ingredients[i]

        @cache
        def can_create(name: str) -> bool:
            nonlocal recepie_ingredients, supplies, visited

            if name in visited:
                return False
            visited.add(name)

            if name in supplies:
                return True

            if name not in recepie_ingredients:
                # there is no recipe for this name and it is not in supplies, so it is impossible to create.
                return False

            return not any(x not in supplies and not can_create(x) for x in recepie_ingredients[name])

        answer = []
        visited = set()
        for name in recipes:
            if can_create(name):
                answer.append(name)
        return answer


if __name__ == "__main__":
    ingredients = [["yeast", "flour"]]
    supplies = ["yeast"]
    recipes = ["bread"]
    print(Solution().findAllRecipes(recipes, ingredients, supplies))
