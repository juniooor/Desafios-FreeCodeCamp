categories = ['Food', 'Auto', 'Clothing']
chart = "percentage spent by category\n"
percentages = [10, 70, 30]

height = (len(max(categories, key=len)))
padded = [names.ljust(height) for names in categories]

for num in reversed(range(0, 110, 10)):
    chart += f"{str(num) + '|':>4}"
    for percent in percentages:
        if percent >= num:
            chart += " o "
        else: 
            chart += "   " 

    chart += ' \n'

chart += "    " + "-" *10 + '\n' 

for name in zip(*padded):
    chart += "     " + ('  '.join(name)) + '  \n'

print(chart.rstrip('\n'))

