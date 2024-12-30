import sys

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



def use_inventory():

    print("Инвентарь:\n", characters_stats.character_backpack)

    inventory_choose = input("Введите название предмета для использования -> ")



def choose_action():

    print("Выберите локацию, куда отправитесь: ")
    print("Дом", "/ Лес", "/ Торговец")

    choose = input()
    choose = choose.lower()

    while choose != "лес" and choose != "дом" and choose != "торговец" and choose != "инвентарь":
        choose = input("\n" + "Вы пробормотали что-то под нос..." + "\n" +  "Выберите локацию, куда отправитесь: ")
        choose = choose.lower()


    if choose == "дом":
        print(rep_library.house_page)


    if choose == "лес":

        fight.forest_fight(rep_library.reps)


    if choose == "торговец":

        seller.use_seller()


    if choose == "инвентарь":

        use_inventory()



start_key = menu()
char_name = name_char()