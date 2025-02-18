from source import rep_library


game_status = 1             # обозначения статуса игры: 2 - игра пройдена; 1 - персонаж жив; 0 - персонаж мёртв;
save_number = 1

character_name = None

character_cell_of_body = f"{rep_library.cell_of_body_1}"
character_default_health = 100
character_health = 100

character_default_lvl = 1
character_lvl = int(character_default_lvl // 2)

character_sword = f"{rep_library.sword_1}"
character_default_damage = [8, 12]

def character_dmg():
    return [character_default_damage[0] + character_lvl, character_default_damage[1] + character_lvl]

character_coins = 100
seller_triggers = [1, 1]

character_inventory = []