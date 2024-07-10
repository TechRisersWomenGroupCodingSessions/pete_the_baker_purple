from baker.baker import Baker


def test_missing_ingredients_return_0():
    baker = Baker()
    recipe = {"flour": 500}
    ingredients = {"sugar": 500}
    return_value = baker.cakes(recipe, ingredients)
    assert return_value == 0


def test_exact_amount_ingredients_return_1():
    baker = Baker()
    recipe = {"flour": 500}
    ingredients = {"flour": 500}
    return_value = baker.cakes(recipe, ingredients)
    assert return_value == 1;


def test_return_2():
    baker = Baker()
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    ingredients = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    return_value = baker.cakes(recipe, ingredients)
    assert return_value == 2;

def test_ingredient_present_amount_0_return_0():
    baker = Baker()
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    ingredients = {"flour": 0, "sugar": 1200, "eggs": 5, "milk": 200}
    return_value = baker.cakes(recipe, ingredients)
    assert return_value == 0;

def test_run_0cakesOneMoreTime():
    baker = Baker()
    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    ingredients = {"sugar": 500, "flour": 2000, "milk": 2000}
    return_value = baker.cakes(recipe, ingredients)
    assert return_value == 0;