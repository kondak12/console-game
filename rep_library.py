def beginning_scene_in_game(charname):
    print(input("Вы - " + charname + " отважный незнакомец, искатель приключений, который желает\n"
                                     "завоевать сердце прекрасной принцессы, придётся заморать руки, чтобы сделать это, ведь...\n"
                                     "Ужасный странно-череповатый дракон хочет сжечь принцессу до тла, чтобы получить золото всего королевства!\n"
                                     "Больше нет времени, нужно выдвигаться в путь..."))

beginning = ("\nПриветствую тебя незнакомец,\n"
             "эта игра создана специально для тебя. \n"
             "Для полного погружения в мою игру, \n"
             "советую тебе включить на фон плейлист Dark Fantasy. \n"
             "Приятной игры...  (Нажмите 'Enter')")

next_page = "Справка: чтобы переходить к следующему диалогу, просто нажмите 'Enter' "

act_1 = ("Вы вышли из дома, с этого момента и началось ваше путешествие...\n"
         "Акт 1: Рождение воина")

act_2 = ("\nВы ни в чём не сомневаясь покинули город, ступив на встречу своему страху и цели.\n"
         "Акт 2: Навстречу страху.\n")

act_2_action_1 = ("Шагая вперёд, с каждым шагом всё больше слышались крики ужаса из города.\n"
                  "С каждым новым шагом вы всё лучше видели как дракон уже кружит вокруг башни принцессы,\n"
                  "иногда пуская огненные шарики в лучников.")

def act_2_action_2(name):
    print(input("Ну же, " + name + ", соберись! Кто остановит это, если не такой смелый идиот как т.."))
    print(input("В ночи повиднелся огромный глаз, с подобием ведьмачьей шляпы на нём."))
    print(input("Что за чёрт..?"))
    print(input("Глаз.. Огромный глаз в шляпе..."))
    print(input("В миг глаз уставился на меня"))
    print("Бежать / Стоять")

def act_2_choose_stay():
    print(input("Глаз медленно подлетел и, осмотрев меня со всех сторон, сказал:"))
    print(input("'Человек, вижу ты спешишь, к чему такая спешка?'"))
    print("Выберите номер ответа:\n"
     "1. Привет глаз. Спешу вон в ту башню, где кружит дракон.\n"
     "2. Какое тебе дело? Хочешь сразиться?!\n")

def eye_answer_1():
    print(input("В ту башню.. Я погляжу, ты смелый малый."))
    print(input("Как раз для смельчаков вроде тебя у меня есть предложение..."))
    print(input("Я заберу у тебя здоровье, но дам тебе силы...\n"
                "Или же наоборот, возьму силы и дам здоровья, м?"))

eye_question_1 = ("1. -30 от макс. здоровья / +6 к урону\n"
                  "2. -6 урона / +30 к макс. здоровью\n"
                  "3. Прекратить сделку и идти дальше.")

def eye_question_choose_dmg(max_hp, min_dmg, max_dmg):
    print(input("\n'Сделка заключена, ПО ГЛАЗАМ!'"))
    print(input("Засияв, глаз мнгновенно исчез, оставив меня одного."))
    print(input("Чувствую небольшую слабость в теле, но прилив сил к рукам!"))
    print(input("Макс. здоровье - " + f"{max_hp}" + "   Урон - от " + f"{min_dmg}" + "  до " + f"{max_dmg}"))



home_page = "\nВы вошли в свой дом. 'Здравствуй, дом!'."

seller_page = "\nВы прибыли к торговцу. Он осмотрел вас со словами: 'Да, выглядишь не очень... Есть парочка товаров которые могут исправить это!'.\n"

forest_page = "\nВы прибыли в лес."



fight_choose = "Выберите действие: удар / инвентарь / бег\n"

# гаргулья
rep_forest_fight_1 = "\nКажется там что-то в кустах... 'на вас вылетела огромная гаргулья!' \nВ доле секунды вы думаете что сделать..."
rep_forest_fight_end_1 = "Вы сражались с гаргулией и страхом одновременно. Вы оказались сильнее, враг повержен...\n*lvl + 0.6*\n"
rep_forest_fight_coins_1 = "\nИз пасти гаргульи выпало 3 монеты, да уж, удачи тебе не занимать.\n + 3 монеты"

# кабан
rep_forest_fight_2 = "\nВы видите как на вашу тропинку вышел большой твердолобый кабан. \nНадо принять решение..."
rep_forest_fight_end_2 = "Вы убили кабана. Теперь можно и поживиться...\n*lvl + 0.4* \n*hp + 10*\n"
rep_forest_fight_coins_2 = "\nИз раны кабана выпали две монетки. Наверное он их когда-то съел...\n + 2 монеты"

# грибочек
rep_forest_fight_3 = "\nВы хотели пойти собрать грибов, как вдруг из под земли вылез разумный грибочек. \nВыглядит не очень то и опасным..."
rep_forest_fight_end_3 = "\nВы случайно убили гриб, наступив на него. А он мог бы стать добрым малым... \n*lvl + 0.2*\n"
rep_forest_fight_coins_3 = "\nПод шляпкой гриба виднеется золотая монета. Где он её нашёл?\n+ 1 монета"

# побег
rep_run = "Вы бежали с такой скоростью, что ни один великан бы не догнал вас!\nВы убежали с поля боя! \n*lvl - 0.3*\n"



reps = [rep_forest_fight_1, rep_forest_fight_2, rep_forest_fight_3]



seller_medvejevika = ["Медвежевика -> 'обычная ягода' -> лечит персонажа на 10 hp -> 3 золотых", "медвежевика",
                      "Сначала 3 золотых, парень.", "\nХм? медвежевика? Не проблема.\n", 3]

seller_sword_1 = ["Железный меч -> 'выкован руками торговца' -> увеличивает урон персонажа на 4 -> 8 золотых", "железный меч",
                  "Сперва 8 золотых!", "\nНужна обновка? Сейчас сделаю!\n", 8]

seller_cell_of_body_2 = ["Ячейка крепкости 2 -> 'медальон в виде сердца' -> увеличивает здоровье персонажа на 30 -> 10 золотых'", "ячейка крепкости 2",
                         "Сперва 10 золотых!", "\nАа, приглянулся медальончик?\n", 10]

bought_seller_sword_1 = "Взяв меч в руки, ты чувствуешь его тяжесть, чувствуешь что он - твой новый товарищ."

bought_cell_of_body_2 = ("Вы прикладываете ячейку к груди.. Через миг она исчезает.\n"
                            "Вы чувствуете твёрдость тела, которой не было раньше.")

seller_no_coins = "Здесь кажется не хватает, приходи как накопишь, парень...\n"



home_choose = "Отдохнуть / Снаряжение / Уйти"



rep_use_medvejevika = "На вкус очень сладкая, неплохо!\nЗдоровье персонажа -> "

