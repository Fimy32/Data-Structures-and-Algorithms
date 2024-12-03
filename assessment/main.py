import menu


def run():
    menu.current = 0
    print("Enter the arrow keys to navigate the menu, and enter Y to confirm option.")
    while menu.menu():
        pass
    print("Completed")

run()