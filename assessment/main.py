import menu


def run():
    menu.current = 0
    while menu.menu():
        pass
    print("Completed")

run()