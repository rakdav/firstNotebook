def run():
    with open("hello.txt", "w") as file:
        file.write("hello world")

    print("Файл записан")