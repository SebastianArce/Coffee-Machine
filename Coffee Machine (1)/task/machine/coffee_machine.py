class CoffeeMachine:
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def progress(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy":
                self.action_buy()
            elif action == "take":
                self.action_take()
            elif action == "fill":
                self.action_fill()
            elif action == "remaining":
                self.print_supplies()
            elif action == "exit":
                break

    def print_supplies(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("{} of money".format(self.money))

    def action_fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def action_take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def make_coffee(self, water, beans, money, milk=0):
        if self.water >= water and self.beans >= beans and self.cups > 0 and self.milk >= milk:
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= 1
            self.money += money
            print("I have enough resources, making you a coffee!")
        elif self.water < water:
            print("Sorry, not enough water!")
        elif self.milk < milk:
            print("Sorry, not enough milk")
        elif self.beans < beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups == 0:
            print("Sorry, not enough disposable cups!")

    def action_buy(self):
        type_coffee = input(
            "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if type_coffee == "1":
            self.make_coffee(250, 16, 4)
        elif type_coffee == "2":
            self.make_coffee(350, 20, 7, 75)
        elif type_coffee == "3":
            self.make_coffee(200, 12, 6, 100)
        elif type_coffee == "back":
            return


machine = CoffeeMachine()
machine.progress()

