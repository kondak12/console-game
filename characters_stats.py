game_status = 1             # обозначения статуса игры: 2 - игра пройдена; 1 - персонаж жив; 0 - персонаж мёртв;
act_2_trigger = 0

character_default_health = 100
character_health = 100
character_cell_of_body = "Ячейка крепкости тела 1"

character_default_lvl = 1
character_lvl = int(character_default_lvl // 2)

character_sword = "Деревянный меч"
character_default_damage = [8, 12]

def character_dmg():
    return [character_default_damage[0] + character_lvl, character_default_damage[1] + character_lvl]

character_coins = 3

character_inventory = []
character_key_inventory = []