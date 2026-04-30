from datetime import datetime
while True:
    print("1-добавить 2-все 3-5 4-выход")
    a = input("Выбор: ")
    if a == "1":
        t = input("Текст: ")
        if t:
            f = open("diary.txt", "a")
            f.write("[" + datetime.now().strftime("%Y-%m-%d %H:%M") + "] " + t + "\n")
            f.close()
    if a == "2":
        f = open("diary.txt", "r")
        print(f.read())
        f.close()
    if a == "3":
        f = open("diary.txt", "r")
        lines = f.readlines()
        f.close()
        for line in lines[-5:]:
            print(line)
    if a == "4":
        break
