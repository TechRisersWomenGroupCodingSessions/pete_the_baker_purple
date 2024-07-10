from baker.baker import Baker

def test_return_0():
    baker = Baker()
    recipe = {"flour": 500}
    ingredients = {"sugar": 500}
    return_value = baker.cakes(recipe,ingredients)
    assert return_value == 0

def test_return_1():
    baker = Baker()
    recipe = {"flour": 500}
    ingredients = {"flour": 500}
    return_value = baker.cakes(recipe, ingredients)
    assert return_value == 1;

def test_run_2():
    baker = Baker()
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    ingredients = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    return_value = baker.cakes(recipe, ingredients)
    assert return_value == 2;


