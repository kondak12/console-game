import sys

import time

import random

import characters_stats

import rep_library

import fight

import seller

import act_2

import act_3



def name_char():
    characters_stats.character_name = input("Введите имя персонажа >> ")

    while characters_stats.character_name.isdigit() or characters_stats.character_name == "":
        characters_stats.character_name = input("Это точно имя? Попробуй ещё раз, дружок >> ")



def game_menu(act_number):
    print("\n*----- ПРОДОЛЖИТЬ ----->\n"
          "*--- СОХРАНИТЬ ИГРУ --->\n"
          "*---- ГЛАВНОЕ МЕНЮ ---->\n"
          "*------- ВЫЙТИ -------->\n")

    game_menu_choose = input("Введите команду -> ")
    game_menu_choose = game_menu_choose.lower()

    game_menu_choose_list = ["продолжить", "прод", "сохранить иру" ,
                             "сохранить" , "сохр" , "главное меню",
                             "главное" , "глав" , "выйти"]

    while game_menu_choose not in game_menu_choose_list:
        game_menu_choose = input("Неизвестная команда. Введите команду -> ")
        game_menu_choose = game_menu_choose.lower()


    if game_menu_choose == "сохранить игру" or game_menu_choose == "сохранить" or game_menu_choose == "сохр":
        save_game(characters_stats.character_name, characters_stats.character_health,
                  characters_stats.character_default_health, characters_stats.character_default_lvl,
                  characters_stats.character_dmg()[0], characters_stats.character_dmg()[1],
                  characters_stats.character_sword, characters_stats.character_cell_of_body,
                  characters_stats.character_coins, characters_stats.character_inventory,
                  characters_stats.seller_triggers[0], characters_stats.seller_triggers[1], act_number)

        print("\nИгра сохранена!")


    if game_menu_choose == "главное меню" or game_menu_choose == "главное" or game_menu_choose == "глав":
        base_game()


    if game_menu_choose == "выйти":
        sys.exit()



def save_game(name, hp, d_hp, d_lvl, d_dmg_0, d_dmg_1, sword_name, body_cell, coins, inv, sel_sw, sel_body_cell, act_number):
    with open("save_game.txt", "w") as save_game_file:
        save_game_file.write(f"{name}" + "\n" +
                             f"{hp}" + "\n" +
                             f"{d_hp}" + "\n" +
                             f"{d_lvl}" + "\n" +
                             f"{d_dmg_0}" + "\n" +
                             f"{d_dmg_1}" + "\n" +
                             f"{sword_name}" + "\n" +
                             f"{body_cell}" + "\n" +
                             f"{coins}" + "\n" +
                             f"{inv}" + "\n" +
                             f"{sel_sw}" + "\n" +
                             f"{sel_body_cell}" + "\n" +
                             f"{act_number}")



def load_game():
    with open("save_game.txt", "r") as save_game_file:

        save_game_file = save_game_file.read()

        save_game_file = save_game_file.split("\n")

        characters_stats.character_name = save_game_file[0]
        characters_stats.character_health = int(save_game_file[1])
        characters_stats.character_default_health = f"{save_game_file[2]}"
        characters_stats.character_default_lvl = save_game_file[3]
        characters_stats.character_dmg()[0] = f"{save_game_file[4]}"
        characters_stats.character_dmg()[1] = f"{save_game_file[5]}"
        characters_stats.character_sword = f"{save_game_file[6]}"
        characters_stats.character_cell_of_body = f"{save_game_file[7]}"
        characters_stats.character_coins = f"{save_game_file[8]}"
        characters_stats.character_inventory = f"{save_game_file[9]}"
        characters_stats.seller_triggers[0] = f"{save_game_file[10]}"
        characters_stats.seller_triggers[1] = f"{save_game_file[11]}"
        characters_stats.save_number = f"{save_game_file[12]}"



def reference():

    print(rep_library.call_reference)

    ref_enter = input("Введите название пункта >> ")
    ref_enter = ref_enter.lower()

    while ref_enter not in rep_library.reference_list:
        ref_enter = input("Неизвестный пункт. Повторите попытку >> ")
        ref_enter = ref_enter.lower()

    if ref_enter == "сюжет":
        print(input(rep_library.call_reference_suj))

    if ref_enter == "уровень":
        print(input(rep_library.call_reference_lvl))

    if ref_enter == "инвентарь" or ref_enter == "инв":
        print(input(rep_library.call_reference_inventory))

    if ref_enter == "управление" or ref_enter == "упр":
        print(input(rep_library.call_reference_refs))

    if ref_enter == "диалоги":
        print(input(rep_library.call_reference_dialogues))

    if ref_enter == "совет":
        print(input(rep_library.call_reference_advice))



def menu():
    print(rep_library.art)

    print("\n            <----- НОВАЯ ИГРА ----->\n"
          "           <------ ПРОДОЛЖИТЬ ------>\n"
          "            <------- ВЫХОД -------->\n")

    enter = input("Введите команду >> ")
    enter = enter.lower()

    while enter != "новая игра" and enter != "новая" and enter != "продолжить" and enter != "прод" and enter != "выход":
        enter = input("\nНеизвестная команда!\nВведите команду >> ")
        enter = enter.lower()


    if enter == "новая игра" or enter == "новая":
        name_char()
        beginning_actions()
        enter = 1


    if enter == "продолжить" or enter == "прод":
        load_game()
        acts_playing()


    if enter == "выход":
        sys.exit()

    return enter



def autosave_question(act_num):
    save_trigger = input("\nХотите сохранить текущий прогресс?\nДа / Нет\nВыбор >> ")

    while save_trigger.lower() != "нет" and save_trigger != "да":
        save_trigger = input("\nХотите сохранить текущий прогресс?\nДа / Нет\nВыбор >> ")
        save_trigger = save_trigger.lower()

    if save_trigger == "да":
        save_game(characters_stats.character_name, characters_stats.character_health,
                  characters_stats.character_default_health, characters_stats.character_default_lvl,
                  characters_stats.character_dmg()[0], characters_stats.character_dmg()[1],
                  characters_stats.character_sword, characters_stats.character_cell_of_body,
                  characters_stats.character_coins, characters_stats.character_inventory,
                  characters_stats.seller_triggers[0], characters_stats.seller_triggers[1], act_num)



def beginning_actions():

    print(input(rep_library.beginning))

    print(input(rep_library.next_page))

    print(input(rep_library.reference_in_beginning))

    rep_library.beginning_scene_in_game(characters_stats.character_name)

    print(input(rep_library.act_1))



def go_home():
    print(rep_library.home_page)
    print(rep_library.home_choose)

    choose_home = input()

    while choose_home.lower() != "уйти" and choose_home.lower() != "отдохнуть" and choose_home.lower() != "снаряжение":
        print("Непонятные мысли лезут в голову, что это?")
        choose_home = input("Надо подумать снова -> ")

    if choose_home.lower() == "справка":   # справка
        reference()

    if choose_home.lower() == "отдохнуть":
        print("Пора бы отдохнуть... 'Вы заснули'.")

        print(input("Z... Z... z..."))

        time.sleep(1)

        characters_stats.character_health = characters_stats.character_default_health
        print("\n\nВы отдохнули. Здоровье восстановлено.")


    if choose_home == "снаряжение":
        print("У вас", characters_stats.character_sword, "    Мин. урон ->", characters_stats.character_dmg()[0] + characters_stats.character_lvl,
              " /  Макс. урон ->", characters_stats.character_dmg()[1])

        print("У вас", characters_stats.character_cell_of_body,
              "    Макс. здоровье ->", characters_stats.character_default_health, "\n")



    if choose_home == "уйти":
        print("Ещё увидимся, дом. Жди меня!\n")

    time.sleep(1.5)



def check_inventory():
    if characters_stats.character_inventory == [ ]:
        print("\nИнвентарь пуст.")

    else:
        print("Инвентарь:")

        count = -1

        for i in characters_stats.character_inventory:
            count += 1

            print()

            for j in i:
                if j == characters_stats.character_inventory[count][0]:
                    j = j.upper()

                if j != "'" and j != "[" and j != "]":
                    print(j, end="")

    print("\nУ вас", characters_stats.character_coins, "монет.\n")

    time.sleep(1.5)



def use_medvejevika():
    characters_stats.character_inventory.remove("медвежевика")
    characters_stats.character_health += 15

    print(input("Вы съели ягоду. +15 Здоровья"))

    if characters_stats.character_health > characters_stats.character_default_health:
        characters_stats.character_health = characters_stats.character_default_health

    print(input("Здоровье персонажа -> " + f"{characters_stats.character_health}"))



def use_pechenierka():
    characters_stats.character_inventory.remove("печеньерка")
    characters_stats.character_health += 30

    print(input("Вы съели печеньерку. +30 Здоровья"))

    if characters_stats.character_health > characters_stats.character_default_health:
        characters_stats.character_health = characters_stats.character_default_health

    print(input("Здоровье персонажа -> " + f"{characters_stats.character_health}"))



def use_inventory():

    check_inventory()

    if characters_stats.character_inventory != [ ]:
        inventory_choose = input("Введите 'закрыть' чтобы закрыть инвентарь.\nВведите название предмета для использования -> ")
        inventory_choose = inventory_choose.lower()

        character_inventory_list = ["медвежевика", "мед", "печеньерка", "печ", "закрыть", "справка"]

        while inventory_choose not in character_inventory_list:

            inventory_choose = input("Что же сделать -> ")
            inventory_choose = inventory_choose.lower()

        if inventory_choose == "справка":  # справка
            reference()

        if inventory_choose == "медвежевика" or inventory_choose == "мед":
            use_medvejevika()

        if inventory_choose == "печеньерка" or inventory_choose ==  "печ":
            use_pechenierka()



def choose_fighter_rep(f_f, f_f_num, f_rep, f_param):
    if f_f == f_f_num:
        print(f_rep)
        print(f_param)



def act_1():
    while characters_stats.game_status != 0:

        print("Выберите локацию, куда отправитесь: ")

        if int(characters_stats.character_default_lvl) < 3:
            print("Дом / Лес / Торговец // Меню")
        else:
            print("Дом / Лес / Торговец / Тропа // Меню")

        choose = input()
        choose = choose.lower()

        choose_list = ["инвентарь", "торговец", "лес", "дом", "торг", "инв", "справка", "меню"]

        if int(characters_stats.character_default_lvl) >= 3:
            choose_list.append("тропа")

        while choose not in choose_list:
            choose = input("\n" + "Вы пробормотали что-то под нос..." + "\n" +  "Выберите локацию, куда отправитесь: ")
            choose = choose.lower()


        if choose == "дом":
            go_home()


        if choose == "лес":
            fight.fighting(0)


        if choose == "торговец" or choose == "торг":
            seller.use_seller()


        if choose == "тропа" and characters_stats.character_default_lvl >= 3:
            rep_library.act_2_recomendations()

            choose_begin_act_2 = input("Хмм.. -> ")
            choose_begin_act_2 = choose_begin_act_2.lower()

            while choose_begin_act_2 != "идти" and choose_begin_act_2 != "остаться":
                choose_begin_act_2 = input("Хмммм.. -> ")
                choose_begin_act_2 = choose_begin_act_2.lower()


            if choose_begin_act_2 == "идти":
                characters_stats.save_number = 2

                autosave_question(characters_stats.save_number)

                break


            elif choose_begin_act_2 == "остаться":
                print("Ещё чутка потренеруюсь...\n")


        if choose == "инвентарь" or choose == "инв":

            use_inventory()


        if choose == "справка":   # справка

            reference()


        if choose == "меню":
            game_menu(1)



def seller_choise(sell_item, item_name, phrase_before_sell, phrase_item):

    print(phrase_item)

    time.sleep(1.5)

    print(phrase_before_sell)

    if characters_stats.character_coins >= sell_item:
        item_name = item_name.lower()
        if item_name != "железный меч" and item_name != "ячейка крепкости 2":
            characters_stats.character_inventory.append(item_name)

        characters_stats.character_coins -= sell_item

        time.sleep(1.5)

        print("Теперь забирай.\n")

        time.sleep(1.5)


    elif characters_stats.character_coins < sell_item:

        time.sleep(1.5)

        print(rep_library.seller_no_coins)

        time.sleep(1.5)



def chance(chance_number):
    r = random.randint(1, 100)
    if r <= chance_number:
        return True
    else:
        return False



def acts_playing():
    if int(characters_stats.save_number) == 1:
        act_1()

    if int(characters_stats.save_number) == 2:
        if int(characters_stats.game_status) != 0:
            act_2.act_2_actions()

    if int(characters_stats.save_number) == 3:
        if characters_stats.game_status != 0:
            act_3.act_3_actions()



def base_game():
    menu_trigger = menu()

    if menu_trigger == 1:
        acts_playing()