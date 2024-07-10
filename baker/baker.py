class Baker:
    def cakes(self, recipe, ingredients):
        min_amount = 0
        for item_in_recipe in recipe:
            if item_in_recipe not in ingredients:
                return 0
            # in the ingredients
            recipe_value = recipe.get(item_in_recipe)
            ingredient_value = ingredients.get(item_in_recipe)

            amount = round(ingredient_value / recipe_value)

            if min_amount == 0 or min_amount > amount:
                min_amount = amount
        return min_amount