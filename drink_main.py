from drink_machine import DrinkMachine
from drink_service import DrinkService


def main():
    dm_class = DrinkMachine()
    service = DrinkService(dm_class)
    service.run()
    # dm_class.add_drinking("奶茶",15,5)
    # print(dm_class.menu)
    # dm_class.add_drinking("奶茶",15,10)
    # print(dm_class.menu)
    # print(dm_class.buy_drinking("綠茶"))
    # print(dm_class.buy_drinking("奶茶"))
    # print(dm_class.menu)
    # print(dm_class.show_menu())

print(__name__)
if __name__ =="__main__":
    main()
