import sys
import os
import time
import random
from itertools import count

from source import characters_stats
from source import rep_library
from source import fight
from source import seller
from source import act_2
from source import act_3


def name_char():
    characters_stats.character_name = input("Введите имя персонажа >> ")

    while characters_stats.character_name.isdigit() or characters_stats.character_name == "":
        clear_console()
        characters_stats.character_name = input("Это точно имя? Попробуйте ещё раз >> ")



def game_menu(act_number):
    print("\n1 *----- ПРОДОЛЖИТЬ -----> 1\n"
          "2 *--- СОХРАНИТЬ ИГРУ ---> 2\n"
          "3 *---- ГЛАВНОЕ МЕНЮ ----> 3\n"
          "4 *------- ВЫЙТИ --------> 4\n")

    game_menu_choose = input("Введите номер команды -> ")
    game_menu_choose = str(game_menu_choose)

    game_menu_choose_list = ["1", "2", "3", "4"]

    while game_menu_choose not in game_menu_choose_list:
        game_menu_choose = input("Неизвестная номер команды. Повторите ввод -> ")
        game_menu_choose = game_menu_choose.lower()


    if game_menu_choose == "2":
        save_game()

        print("\nИгра сохранена!")


    if game_menu_choose == "3":
        base_game()


    if game_menu_choose == "4":
        sys.exit()



def save_game():
    with open("source/save_game.txt", "w") as save_game_file:
        save_game_file.write(f"{characters_stats.character_name}" + "\n" +
                             f"{characters_stats.character_health}" + "\n" +
                             f"{characters_stats.character_default_health}" + "\n" +
                             f"{characters_stats.character_default_lvl}" + "\n" +
                             f"{characters_stats.character_dmg()[0]}" + "\n" +
                             f"{characters_stats.character_dmg()[1]}" + "\n" +
                             f"{characters_stats.character_sword}" + "\n" +
                             f"{characters_stats.character_cell_of_body}" + "\n" +
                             f"{characters_stats.character_coins}" + "\n" +
                             f"{characters_stats.character_inventory}" + "\n" +
                             f"{characters_stats.seller_triggers[0]}" + "\n" +
                             f"{characters_stats.seller_triggers[1]}" + "\n" +
                             f"{characters_stats.save_number}")



def load_game():
    clear_console()
    with open("source/save_game.txt", "r") as save_game_file:

        save_game_file = save_game_file.read()

        save_game_file = save_game_file.split("\n")

        characters_stats.character_name = save_game_file[0]
        characters_stats.character_health = int(save_game_file[1])
        characters_stats.character_default_health = int(save_game_file[2])
        characters_stats.character_default_lvl = float(save_game_file[3])
        characters_stats.character_dmg()[0] = int(save_game_file[4])
        characters_stats.character_dmg()[1] = int(save_game_file[5])
        characters_stats.character_sword = f"{save_game_file[6]}"
        characters_stats.character_cell_of_body = f"{save_game_file[7]}"
        characters_stats.character_coins = int(save_game_file[8])
        characters_stats.character_inventory = [save_game_file[9]]
        characters_stats.seller_triggers[0] = int(save_game_file[10])
        characters_stats.seller_triggers[1] = int(save_game_file[11])
        characters_stats.save_number = int(save_game_file[12])

    if characters_stats.save_number == 1:
        print("Вы остановились в 1 акте игры.")
    elif characters_stats.save_number == 2:
        print("Вы остановились во 2 акте игры.")
    elif characters_stats.save_number == 3:
        print("Вы остановились в 3 акте игры.")
    print()


def reference():
    clear_console()
    print(rep_library.call_reference)

    ref_enter = input("Введите номер пункта >> ")
    ref_enter = str(ref_enter)

    while ref_enter not in rep_library.reference_list:
        ref_enter = input("Неизвестный пункт. Повторите попытку >> ")
        ref_enter = str(ref_enter)

    if ref_enter == "1":
        print(input(rep_library.call_reference_suj))

    if ref_enter == "2":
        print(input(rep_library.call_reference_lvl))

    if ref_enter == "3":
        print(input(rep_library.call_reference_inventory))

    if ref_enter == "4":
        print(input(rep_library.call_reference_refs))

    if ref_enter == "5":
        print(input(rep_library.call_reference_dialogues))

    if ref_enter == "6":
        print(input(rep_library.call_reference_advice))



def menu():
    clear_console()
    print(rep_library.art)

    enter_list = ["1", "2", "3"]
    print("\n            1 <----- НОВАЯ ИГРА -----> 1\n"
          "           2 <------ ПРОДОЛЖИТЬ ------> 2\n"
          "            3 <------- ВЫХОД --------> 3\n")

    enter = input("Введите номер команды >> ")
    enter = str(enter)

    while enter not in enter_list:
        enter = input("\nНеизвестная команда!\nВведите команду >> ")
        enter = str(enter)


    if enter == "1":
        name_char()
        beginning_actions()
        enter = 1


    if enter == "2":
        load_game()
        acts_playing()


    if enter == "3":
        clear_console()
        sys.exit()

    return enter


def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:                # Linux/MacOS
        os.system('clear')


def typing_effect(text, delay=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return ""


def autosave_question():
    clear_console()
    save_trigger = input("\nХотите сохранить текущий прогресс?\nДа / Нет\nВыбор >> ")

    while save_trigger.lower() != "нет" and save_trigger.lower() != "да":
        save_trigger = input("\nХотите сохранить текущий прогресс?\nДа / Нет\nВыбор >> ")
        save_trigger = save_trigger.lower()

    if save_trigger == "да":
        save_game()



def beginning_actions():
    clear_console()
    print(input(rep_library.beginning))
    print(input(rep_library.next_page))
    print(input(rep_library.reference_in_beginning))
    rep_library.beginning_scene_in_game(characters_stats.character_name)
    clear_console()
    print(input(rep_library.act_1))



def go_home():
    clear_console()
    print(rep_library.home_page)
    print(rep_library.home_choose)

    choose_home = input()
    home_list = ["1", "2", "3", "справка"]

    while choose_home.lower() not in home_list:
        print("Непонятные мысли лезут в голову, что это?")
        choose_home = input("Надо подумать снова -> ")

    if choose_home.lower() == "справка":   # справка
        clear_console()
        reference()

    if choose_home.lower() == "1":
        clear_console()
        print("Пора бы отдохнуть... 'Вы заснули'.")

        typing_effect("Z... Z... z...", 0.3)

        characters_stats.character_health = characters_stats.character_default_health
        print("\nВы отдохнули. Здоровье восстановлено.")


    if choose_home == "2":
        clear_console()
        print("У вас", characters_stats.character_sword, "    Мин. урон ->", characters_stats.character_dmg()[0] + characters_stats.character_lvl,
              " /  Макс. урон ->", characters_stats.character_dmg()[1])

        print("У вас", characters_stats.character_cell_of_body,
              "    Макс. здоровье ->", characters_stats.character_default_health, "\n")

        time.sleep(2.5)


    if choose_home == "3":
        clear_console()
        print("Ещё увидимся, дом. Жди меня!\n")

    time.sleep(1.5)
    clear_console()



def check_inventory():
    clear_console()
    if len(characters_stats.character_inventory) == 0:
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
    clear_console()
    characters_stats.character_inventory.remove("медвежевика")
    characters_stats.character_health += 15

    print(input("Вы съели ягоду. +15 Здоровья"))

    if characters_stats.character_health > characters_stats.character_default_health:
        characters_stats.character_health = characters_stats.character_default_health

    print(input("Здоровье персонажа -> " + f"{characters_stats.character_health}"))



def use_pechenierka():
    clear_console()
    characters_stats.character_inventory.remove("печеньерка")
    characters_stats.character_health += 30

    print(input("Вы съели печеньерку. +30 Здоровья"))

    if characters_stats.character_health > characters_stats.character_default_health:
        characters_stats.character_health = characters_stats.character_default_health

    print(input("Здоровье персонажа -> " + f"{characters_stats.character_health}"))



def use_inventory():
    clear_console()
    check_inventory()

    if len(characters_stats.character_inventory) == 0:
        inventory_choose = input("Введите 'закрыть' чтобы закрыть инвентарь.\nВведите название предмета для использования -> ")
        inventory_choose = inventory_choose.lower()

        character_inventory_list = ["медвежевика", "мед", "печеньерка", "печ", "закрыть", "справка"]

        while inventory_choose not in character_inventory_list:

            inventory_choose = input("Что же сделать -> ")
            inventory_choose = inventory_choose.lower()

        if inventory_choose == "справка":  # справка
            clear_console()
            reference()

        if inventory_choose == "медвежевика" or inventory_choose == "мед":
            clear_console()
            use_medvejevika()

        if inventory_choose == "печеньерка" or inventory_choose ==  "печ":
            clear_console()
            use_pechenierka()



def choose_fighter_rep(f_f, f_f_num, f_rep, f_param):
    if f_f == f_f_num:
        print(f_rep)
        print(f_param)



def act_1():
    while characters_stats.game_status != 0:
        print("Выберите локацию, куда отправитесь: ")

        if int(characters_stats.character_default_lvl) < 3:
            print("1 Дом / 2 Лес / 3 Торговец // 4 Меню")
        else:
            print("1 Дом / 2 Лес / 3 Торговец / Тропа // 4 Меню")

        choose = input()
        choose = choose.lower()

        choose_list = ["1", "2", "3", "4", "инвентарь", "инв", "справка"]

        if int(characters_stats.character_default_lvl) >= 3:
            choose_list.append("тропа")

        while choose not in choose_list:
            choose = input("\n" + "Вы пробормотали что-то под нос..." + "\n" +  "Выберите локацию, куда отправитесь: ")
            choose = choose.lower()


        if choose == "1":
            go_home()


        if choose == "2":
            clear_console()
            fight.fighting(0)


        if choose == "3":
            clear_console()
            seller.use_seller()


        if choose == "тропа" and characters_stats.character_default_lvl >= 3:
            clear_console()
            rep_library.act_2_recomendations()

            choose_begin_act_2 = input("Хмм.. -> ")
            choose_begin_act_2 = choose_begin_act_2.lower()

            while choose_begin_act_2 != "1" and choose_begin_act_2 != "2":
                choose_begin_act_2 = input("Хмммм.. -> ")
                choose_begin_act_2 = choose_begin_act_2.lower()


            if choose_begin_act_2 == "1":
                clear_console()
                characters_stats.save_number = 2

                autosave_question()

                break


            elif choose_begin_act_2 == "остаться":
                clear_console()
                print("Ещё чутка потренеруюсь...\n")


        if choose == "инвентарь" or choose == "инв":

            use_inventory()


        if choose == "справка":   # справка

            reference()


        if choose == "4":
            game_menu(1)



def seller_choice(sell_item, item_name, phrase_before_sell, phrase_item):

    print(phrase_item)

    time.sleep(1.5)

    print(phrase_before_sell)

    if characters_stats.character_coins >= sell_item:
        item_name = item_name.lower()
        if item_name != rep_library.sword_1 and item_name != f"{rep_library.cell_of_body_2}":
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
    if characters_stats.save_number == 1:
        act_1()

    if characters_stats.save_number == 2:
        if characters_stats.game_status != 0:
            act_2.act_2_actions()

    if characters_stats.save_number == 3:
        if characters_stats.game_status != 0:
            act_3.act_3_actions()



def base_game():
    menu_trigger = menu()

    if menu_trigger == 1:
        acts_playing()