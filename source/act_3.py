from source import rep_library
from source import functions
from source import characters_stats
from source import fight


def act_3_actions():
    functions.clear_console()
    print(input(rep_library.act_3_beginning))

    act_3_action_1_num = rep_library.act_3_action_1()


    if act_3_action_1_num == "1":

        rep_library.act_3_action_1_choose_1()
        fight.fighting(2)


    elif act_3_action_1_num == "2":

        characters_stats.character_sword = rep_library.sword_3
        characters_stats.character_default_damage = [16, 20]
        rep_library.act_3_action_1_choose_2(characters_stats.character_dmg()[0], characters_stats.character_dmg()[1])


    functions.clear_console()
    act_3_action_2_choose = rep_library.act_3_action_2()

    if act_3_action_2_choose == "1":

        functions.clear_console()
        rep_library.act_3_action_2_choose_1_phase_1(functions.characters_stats.character_name)

        fight.fighting(3)

        if characters_stats.game_status == 0:
            functions.clear_console()
            rep_library.death_ending(characters_stats.character_name)

        else:
            act_3_action_2_choose_mid = rep_library.act_3_action_2_choose_1_phase_2_1()

            if act_3_action_2_choose_mid == "1":
                functions.clear_console()
                rep_library.mid_ending(characters_stats.character_name)

            elif act_3_action_2_choose == "2":
                functions.clear_console()
                rep_library.act_3_action_2_choose_1_phase_2_2()

                fight.fighting(4)

                if characters_stats.game_status == 0:
                    functions.clear_console()
                    rep_library.death_ending(characters_stats.character_name)
                    characters_stats.game_status = 2

                else:
                    rep_library.win_dragon()
                    characters_stats.game_status = 2

    elif act_3_action_2_choose == "2":
        rep_library.mid_ending(characters_stats.character_name)
        characters_stats.game_status = 2

    functions.base_game()