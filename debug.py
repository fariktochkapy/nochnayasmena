def wait():
    input("\nНажмите Enter...")

def sep():
    print("\n" + "=" * 50)

def clear():
    print("\n" * 50)

def save(text):
    with open("report.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

clear()

crisis_words = {"умру", "травят", "надоело", "суицид", "покончить", "закончилось", "больше", "не", "могу", "все", "кончено"}

emotional = 7
style = []
success = 0


lines = [
    "=" * 50,
    "НОЧНАЯ СМЕНА В CALL-ЦЕНТРЕ",
    "=" * 50,
    "Вы - оператор службы психологической поддержки.",
    "Ваша ночная смена (с 00:00 до 08:00).",
    f"Эмоциональный ресурс: {emotional}",
    "",
]

for line in lines:
    print(line)

wait()

save("=" * 50)
save("ОТЧЕТ О НОЧНОЙ СМЕНЕ")
save("=" * 50)
save(f"Начальный эмоциональный ресурс: {emotional}")

# =========== ЗВОНОК 1 ===========
clear()
print("00:47")
sep()
print("Абонент: Анна Петровна, 78 лет")
print("Ситуация: не может уснуть, чувствует одиночество")
sep()
save("\nЗВОНОК 1 - Анна Петровна")
print("\nАнна Петровна: 'Я не могу уснуть... Сын звонит редко...'")
sep()
print("Что делаем?:")
print("  А) Следовать протоколу (завершить через 10 минут)")
print("  Б) Нарушить протокол (выслушать полностью)")
sep()

choice = input("Ваш выбор (А или Б): ").upper()
sep()

if choice == "А":
    print("Вы: 'Постарайтесь выпить теплого молока...'")
    print("Вы завершили разговор по протоколу.")
    style.append("протокол")
    save("Выбор: Протокол")
    save("Ресурс не изменился")
elif choice == "Б":
    print("Вы: 'Расскажите мне о вашем сыне...'")
    print("\nАнна Петровна рассказывает...")
    print("\nВ конце: 'Спасибо, что выслушали.'")
    emotional -= 1
    style.append("эмпатия")
    success += 1
    save("Выбор: Эмпатия")
    save("Ресурс: -1")
else:
    print("Вы мешкаетесь, и следуете протоколу.")
    style.append("протокол")
    save("Выбор: Протокол")

print(f"\nРесурс: {emotional}")
wait()

# =========== ЗВОНОК 2 ===========
clear()
print("02:15")
sep()
print("Абонент: Алексей, 14-15 лет")
print("Ситуация: буллинг в школе и соцсетях")
sep()
save("\nЗВОНОК 2 - Алексей (буллинг)")

print("\nАлексей: 'Меня травят... Иногда хочется, чтобы все закончилось...'")
sep()

words = {"травят", 'закончилось', "школе"}
found = crisis_words.intersection(words)
if found:
    print(f"Кризисные слова: {', '.join(found)}")

    sep()

print("Что делаем?:")
print("  А) Действовать по протоколу (запросить данные)")
print("  Б) Работать на доверие (поискать поддержку)")
sep()

choice = input("Ваш выбор (А или Б): ").upper()
sep()

if choice == "А":
    print("Вы: 'Мне нужны твои данные для безопасности...'")
    print("\nАлексей: 'Нет...' *бросает трубку*")
    emotional -= 3
    save("Выбор: Протокол")
    save("Результат: Бросил трубку")
    save("Ресурс: -3")
elif choice == "Б":
    print("Вы: 'Давай подумаем, кто может помочь...'")
    sep()

    attempts = 3
    persuaded = False

    while attempts > 0 and not persuaded:
        print(f"Попыток: {attempts}")
        print("Какой подход?")
        print("1) Друзья  2) Учителя  3) Анонимно")
        print(style)
        try:
            sub = int(input("Ваш выбор (1-3): "))

            if sub == 1:
                print("\nВы: 'Есть друзья, которым можно рассказать?'")
                if "эмпатия" in style:
                    print("Алексей: 'Есть один друг... Может, расскажу.'")
                    persuaded = True
                    success += 1
                else:
                    print("Алексей: 'Нет друзей...'")
                    attempts -= 1

            elif sub == 2:
                print("\nВы: 'Может, учитель?'")
                print("Алекс: 'Классная руководительница...'")
                persuaded = True
                success += 1

            elif sub == 3:
                print("\nВы: 'Есть анонимные чаты...'")
                print("Алексей: 'Не хочу...' *бросает трубку*")
                emotional -= 2
                save("Выбор: Анонимно")
                save("Результат: Бросил трубку")
                save("Ресурс: -2")
                break
            else:
                print("Неверный выбор.")
                attempts -= 1
        except:
            print("\nВведите число 1-3.")
            attempts -= 1

    if persuaded:
        print("\nАлексей согласился на помощь!")
        style.append("эмпатия")
        save("Выбор: Работа на доверие")
        save("Результат: Согласился")
else:
    print("\nАлексей бросил трубку.")
    emotional -= 1
    save("Выбор: Неопределенный")
    save("Результат: Бросил трубку")

print(f"\nРесурс: {emotional}")
wait()

# =========== ЗВОНОК 3 ===========
clear()
print("04:30")
sep()
print("Абонент: Дмитрий, 40-45 лет")
print("Ситуация: ссора с женой, агрессия")
sep()
save("\nЗВОНОК 3 - Дмитрий (агрессия)")

print("\nДмитрий: 'Я сейчас вернусь и устрою скандал! Надоело все!'")
sep()
print("АБОНЕНТ В ГНЕВЕ")
print("Предложите 3 способа успокоиться:")
sep()

methods = [
    "Глубокое дыхание",
    "Прогулка 10 минут",
    "Вспомнить хорошее",
    "Выпить воды",
    "Посчитать до 20"
]
available = methods.copy()
tried = []
calmed = False

for attempt in range(1, 4):
    print(f"Попытка {attempt}:")
    for i, m in enumerate(available[:3], 1):
        print(f"  {i}) {m}")

    num = 0
    try:
        num = int(input("Ваш выбор (1-3):"))
        if 1 <= num <= 3:
            method = available[num - 1]
            tried.append(method)
            print(f"\nВы выбрали: '{method}'")

            if emotional >= 4:
                print("\nДмитрий: 'Ладно... попробую...'")
                calmed = True
                success += 1
                break
            elif attempt == 3:
                print("\nДмитрий: 'Надоело!' *бросает трубку*")
                emotional -= 2
    except:
        print("\nВыберите один из предложенных вариантов.")
        num = 0

    if available and num <= len(available):
        available.pop(num - 1)

sep()
if calmed:
    print("Успокоился!")
    style.append("эмпатия")
    save("Выбор: Методы успокоения")
    save(f"Методы: {tried}")
    save("Результат: Успокоился")
else:
    print("Не успокоился.")
    save("Выбор: Методы")
    save(f"Методы: {tried}")
    save("Результат: Не успокоили")

print(f"\nРесурс: {emotional}")
wait()

# =========== ЗВОНОК 4 ===========
clear()
print("06:50")
sep()
print("Абонент: Света, 19 года")
print("Ситуация: паника перед экзаменом")
sep()
save("\nЗВОНОК 4 - Света (экзамен)")
print("\nСвета: 'У меня через 3 часа экзамен...'")
sep()
print("ФИНАЛЬНЫЙ ЗВОНОК")
print("Что посоветуете?")
sep()

empathy = style.count("эмпатия")
protocol = style.count("протокол")

stats = {
    "звонков": 4,
    "эмпатия": empathy,
    "протокол": protocol,
    "успехи": success,
    "ресурс": emotional
}

print("Статистика:")
for k, v in stats.items():
    print(f"   {k}: {v}")
sep()

advice = []
if empathy >= protocol:
    advice = [
        "Спросить о чувствах",
        "Спросить о страхе провала",
        "Вспомнить прошлые успехи"
    ]
else:
    advice = [
        "Метод 5-4-3-2-1",
        "Квадратное дыхание",
        "Составить план"
    ]
if emotional < 3:
    advice.append("Просто выслушать")

print("Советы:")
for i, a in enumerate(advice, 1):
    print(f"{i}) {a}")
sep()

try:
    num = int(input("Выберите номер: "))
    if 1 <= num <= len(advice):
        print(f"\nВы выбрали: '{advice[num - 1]}'")
        sep()

        if emotional >= 5 and "эмпатия" in style:
            print("Света: 'Поняла... Пойду.'")
            ending = "Точка опоры"
            success += 1
        elif emotional < 2:
            print("Света: 'Не понимаете...' *бросила*")
            ending = "Выгорание"
        else:
            print("Света: 'Спасибо...'")
            ending = "Протокол выполнен"

        if success >= 3:
            ending = "Обратная связь"
    else:
        print("Света: 'Спасибо...'")
        ending = "Протокол выполнен"
except:
    print("Света благодарит.")
    ending = "Протокол выполнен"

stats["успехи"] = success
stats["ресурс"] = emotional
wait()

# =========== ФИНАЛ ===========
clear()
print("=" * 50)
print("КОНЕЦ СМЕНЫ: 08:00")
print("=" * 50)
print("\nВы кладете трубку...")
sep()
print(f"Концовка: {ending}")
sep()
print("Итог:")
for k, v in stats.items():
    print(f"   {k}: {v}")
sep()

endings = {
    "Точка опоры": "Вы измотаны, но работа имеет смысл.",
    "Выгорание": "Чувствуете опустошённость. Может, не ваша работа...",
    "Протокол выполнен": "Просто отработали смену. Завтра новый день.",
    "Обратная связь": "SMS: 'Слышала запись. Ты — прирождённый психолог.'"
}

print(endings[ending])
sep()

save("\n" + "=" * 50)
save("ИТОГИ СМЕНЫ")
save("=" * 50)
save(f"Концовка: {ending}")
save(f"Ресурс: {emotional}")
save(f"Успехи: {success}")
save(f"Статистика: {stats}")
save("\nСтиль работы:")
for i, s in enumerate(style, 1):
    save(f"Звонок {i}: {s}")

print("\nОтчет сохранен в 'report.txt'")
print("=" * 50)
print("\nСпасибо за игру!")
print("=" * 50)