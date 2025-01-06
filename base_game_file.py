import act_2

import act_3

import characters_stats

import functions



functions.beginning_actions()


while characters_stats.game_status != 0 and characters_stats.act_2_trigger != 1:

    functions.auto_save_game(functions.char_name, characters_stats.character_health, characters_stats.character_default_lvl,
                             characters_stats.character_dmg()[0], characters_stats.character_dmg()[1],
                             characters_stats.character_sword, characters_stats.character_cell_of_body,
                             characters_stats.character_coins, characters_stats.character_inventory,
                             characters_stats.character_key_inventory, 1, 1)

    act_2_trigger = functions.choose_action()


if characters_stats.act_2_trigger == 1:

    act_2.act_2_actions()


if characters_stats.game_status != 0:

    act_3.act_3_actions()



if __name__ == "main":
    functions.beginning_actions()