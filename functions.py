import sys

import time

import random

import characters_stats

import rep_library

import fight

import seller


def menu():
    print()
    print("СТАРТ /", "ВЫХОД", "\n")

    enter = input("Введите команду >> ")
    enter = enter.lower()

    while enter != "старт" and enter != "выход":
        enter = input("\n" + "Хороший выбор! Повторите попытку." + "\n" + "Введите команду >> ")
        enter = enter.lower()

    if enter == "выход":
        sys.exit()

    return enter



def name_char():
    name = input("Введите имя персонажа >> ")

    if name.isdigit() or name == " ":
        name = input("Это точно имя? Попробуй ещё раз, дружок >> ")

    return name



def beginning_actions():

    print(input(rep_library.beginning))

    print(input(rep_library.next_page))

    rep_library.beginning_scene_in_game(char_name)

    print(input(rep_library.act_1))



def go_home():
    print(rep_library.home_page)

    choose_home = ""
    print(rep_library.home_choose)

    choose_home = input()

    while choose_home != "уйти" and choose_home != "отдохнуть" and choose_home != "снаряжение":
        print("Непонятные мысли лезут в голову, что это?")
        choose_home = input("Надо подумать снова -> ")


    if choose_home == "отдохнуть":
        print("Пора бы отдохнуть... 'Вы заснули'.")

        for i in "Z... Z... z...":
            time.sleep(0.3)
            print(i, end="")

        time.sleep(1.5)

        characters_stats.character_health = characters_stats.character_default_health
        print("\n\nВы отдохнули. Здоровье восстановлено.")


    if choose_home == "снаряжение":
        print("У вас", characters_stats.character_sword, "    Мин. урон ->", characters_stats.character_damage[0],
              " /  Макс. урон ->", characters_stats.character_damage[1])
        print("Ячейка крепкости тела ->", characters_stats.character_cell_of_body,
              "    Макс. здоровье ->", characters_stats.character_default_health, "\n")


    if choose_home == "уйти":
        print("Ещё увидимся, дом. Жди меня!\n")

    time.sleep(1.5)



def check_inventory():
    if characters_stats.character_inventory == [ ]:
        print("Инвентарь пуст.\n")

    else:
        print("Инвентарь:")

        count = -1

        for i in characters_stats.character_inventory:
            count += 1

            if count != 0:
                print()

            for j in i:
                if j == characters_stats.character_inventory[count][0]:
                    j = j.upper()

                if j != "'" and j != "[" and j != "]":
                    print(j, end="")



def use_inventory():
    check_inventory()

    if characters_stats.character_inventory != [ ]:
        inventory_choose = input("\n\nВведите название предмета для использования -> ")



def choose_action():

    print("Выберите локацию, куда отправитесь: ")
    print("Дом", "/ Лес", "/ Торговец")

    choose = input()
    choose = choose.lower()

    choose_list = ["инвентарь", "торговец", "лес", "дом", "торг", "инв"]

    while choose not in choose_list:
        choose = input("\n" + "Вы пробормотали что-то под нос..." + "\n" +  "Выберите локацию, куда отправитесь: ")
        choose = choose.lower()


    if choose == "дом":
        go_home()


    if choose == "лес":

        fight.forest_fight(rep_library.reps)


    if choose == "торговец" or choose == "торг":

        seller.use_seller()


    if choose == "инвентарь" or choose == "инв":

        use_inventory()



def seller_choise(sell_item, item_name, phrase_before_sell, phrase_item):

    print(phrase_item)

    time.sleep(3)

    print(phrase_before_sell)

    if characters_stats.character_coins >= sell_item:
        characters_stats.character_inventory.append(item_name)
        characters_stats.character_coins -= sell_item

        time.sleep(3)

        print("Теперь забирай.\n")

        time.sleep(2)


    elif characters_stats.character_coins < sell_item:

        time.sleep(3)

        print(rep_library.seller_no_coins)

        time.sleep(2)



def chance(chance_number):
    r = random.randint(1, 100)
    if r <= chance_number:
        return True
    else:
        return False



start_key = menu()
char_name = name_char()