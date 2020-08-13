class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        if self.cents + deposit_cents < 100:
            self.cents += deposit_cents
            self.dollars += deposit_dollars
        else:
            dollars_in_cents = (self.cents + deposit_cents) // 100
            total_dollars = dollars_in_cents + deposit_dollars
            diff = (self.cents + deposit_cents) % 100
            self.dollars += total_dollars
            self.cents = diff



