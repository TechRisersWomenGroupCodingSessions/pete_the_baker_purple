from baker.baker import inc
from baker.baker import Baker

def test_answer():
    assert inc(3) == 5


def test_return_0():
    baker = Baker()
    recipe = {"flour": 500}
    ingredients = {"sugar": 500}
    return_value = baker.cakes(recipe,ingredients)
    assert return_value == 0


