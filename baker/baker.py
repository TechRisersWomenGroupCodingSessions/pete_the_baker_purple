class Baker:
    def cakes(self, ingredients, recipe):
        for item_in_recipe in recipe:
            if item_in_recipe not in ingredients:
                return 0
        return 1
