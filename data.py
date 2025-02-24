from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class DataBan:
    bun_name = 'Флюоресцентная булка R2-D3'
    bun_price = 2510

class DataIngredient:
    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус Spicy-X'
    sauce_price = 90

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Мясо бессмертных моллюсков Protostomia'
    filling_price = 1337

    burger_final_cost = 2510*2 + 90 + 1337