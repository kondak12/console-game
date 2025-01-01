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

        print("У вас", characters_stats.character_cell_of_body,
              "    Макс. здоровье ->", characters_stats.character_default_health, "\n")



    if choose_home == "уйти":
        print("Ещё увидимся, дом. Жди меня!\n")

    time.sleep(1.5)



def check_inventory():
    if characters_stats.character_inventory == [ ]:
        print("Инвентарь пуст.")

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

        while (inventory_choose != "медвежевика" and inventory_choose != "мед" and inventory_choose != "печеньерка"
                                                 and inventory_choose != "печ" and inventory_choose != "закрыть"):

            inventory_choose = input("Что же сделать -> ")
            inventory_choose = inventory_choose.lower()

        if inventory_choose == "медвежевика" or inventory_choose == "мед":
            use_medvejevika()

        if inventory_choose == "печеньерка" or inventory_choose ==  "печ":
            use_pechenierka()


def choose_fighter_rep(f_f, f_f_num, f_rep, f_param):
    if f_f == f_f_num:
        print(f_rep)
        print(f_param)



def choose_action():

    print("Выберите локацию, куда отправитесь: ")

    if characters_stats.character_default_lvl < 3:
        print("Дом / Лес / Торговец")
    else:
        print("Дом / Лес / Торговец / Тропа")

    choose = input()
    choose = choose.lower()

    choose_list = ["инвентарь", "торговец", "лес", "дом", "торг", "инв"]

    if characters_stats.character_default_lvl >= 3:
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
            return 1

        elif choose_begin_act_2 == "остаться":
            print("Ещё чутка потренеруюсь...\n")


    if choose == "инвентарь" or choose == "инв":

        use_inventory()



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



start_key = menu()
char_name = name_char()