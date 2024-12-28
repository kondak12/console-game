import sys

import characters_stats

import fight

import code_library

import seller


def mmenu():
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



start_key = mmenu()
char_name = name_char()


print(input(code_library.beginning))

print(input(code_library.next_page))

print(input(code_library.beginning_scene_in_game))

print(input(code_library.act_1))



def choose_action():

    print("Выберите локацию, куда отправитесь: ")
    print("Дом", "Лес", "Торговец")

    choose = input()
    choose = choose.lower()

    while choose != "лес" and choose != "дом" and choose != "торговец":
        choose = input("\n" + "Вы пробормотали что-то под нос..." + "\n" +  "Выберите локацию, куда отправитесь: ")
        choose = choose.lower()


    if choose == "дом":
        print(code_library.house_page)


    if choose == "лес":
        print(code_library.forest_page)

        fight.forest_fight(code_library.reps)


    if choose == "торговец":
        print(code_library.seller_page)

        seller.use_seller()



while characters_stats.game_status != 0:

    choose_action()