class Category:

    def __init__(self, category):
        self.category = category
        self.total = 0
        self.ledger = []

    def __repr__(self):
        string = self.category.center(30, '*') + '\n'

        for item in self.ledger:
            amount = '%.2f' %item['amount']
            desc = (item['description'][:29 - (len(amount))] + ' ') if len(item['description']) > 29 - (len(amount)) else item['description']
            spaces = " " * (30 - (len(desc) + len(amount)))
            string += (desc + spaces + amount) + '\n'
            total = '%.2f' %self.total

        return string + "Total: " + total

    def deposit(self, amount, description = ""): #função para fazer o deposito de dinheiro
        self.total += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""): #função para registrar gastos
        if self.check_funds(amount):
            self.total -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self): #funcao para obter saldo
        return self.total

    def transfer(self, amount, instance):
        if self.check_funds(amount):
            self.total -= amount
            self.ledger.append({'amount': -amount, 'description': "Transfer to " + instance.category})
            instance.total += amount
            instance.ledger.append({'amount': amount, 'description': "Transfer from " + self.category})
            return True
        else:
            return False

    def check_funds(self, amount): #função para evitar que o usuario gaste mais do que possui
        if amount <= self.total:
            return True
        else:
            return False


def create_spend_chart(categories):
# colocar nomes de categorias em uma lista
    names_list = []
    withd_list = []
    for category in categories:
        names = category.category                               
        names_list.append(names)                                
        height = (len(max(names_list, key=len)))
        padded = [word.ljust(height) for word in names_list]    

# Obtenha porcentagens, coloque em uma lista
        w_total = 0
        for item in category.ledger:
            amount = item['amount']
            if amount < 0:
                w_total += amount    
        withd_list.append(w_total)
    total = int(round(sum(withd_list)))
    percentages = []
    for x in withd_list:
        per = x * 100 / total
        per = round(per//10)*10         
        percentages.append(per)            

# construindo o grafico
    chart = "Percentage spent by category\n"
    for x in reversed(range(0, 110, 10)):
        chart += f"{str(x) + '|':>4}"
        for percent in percentages:
          if percent >= x:
            chart += " o " 
          else:
            chart += "   "
        chart += ' \n'
    chart += "    " + ("-" * ((len(names_list) + 2) * 2)) + '\n'         

    for row in zip(*padded):
        chart += ('     ' + '  '.join(row)) + '  \n'

    return chart.rstrip("\n")