game_status = 1             # обозначения статуса игры: 2 - игра пройдена; 1 - персонаж жив; 0 - персонаж мёртв;

character_default_health = 100
character_health = 100
character_cell_of_body = 1

character_default_lvl = 1
character_lvl = int(character_default_lvl // 2)

character_sword = "Деревянный меч"
character_damage = [8 + character_lvl, 12 + character_lvl]

character_coins = 100

character_inventory = []
character_key_inventory = []