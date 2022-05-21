# id, name, buying price, quantity, selling price, profit"
from operator import itemgetter


array_of_product = []

print("Welcome to Find Your Products App")
print("You can input your products below and we'll give you some recommendations")
print("")
user_input = input("Do you want to continue? (Y/N): ")

while (user_input == 'Y'):
    product_name = input(
        f"Input your product's name: ")
    product_buy_price = int(
        input(f"Input your product's buying price: "))
    product_quantity = int(
        input(f"Input your product's quantity: "))
    product_sell_price = int(
        input(f"Input your product's selling price: "))
    product_profit = product_sell_price - product_buy_price
    array_of_product.append([len(array_of_product)+1, product_name,
                            product_buy_price, product_quantity, product_sell_price, product_profit])
    print("")
    user_input = input("Do you want to continue? (Y/N): ")

print("")

modal = int(input("Input your capital: "))
print("")

knapsack = []
for i in array_of_product:
    for j in range(i[3]):
        knapsack.append([i[1], i[2], i[5], float(i[5]/i[2])])

knapsack_sorted_by_weight = sorted(knapsack, key=itemgetter(1))
knapsack_sorted_by_profit = sorted(knapsack, key=itemgetter(2), reverse=True)
knapsack_sorted_by_density = sorted(knapsack, key=itemgetter(3), reverse=True)

greedy_by_profit = []
greedy_by_weight = []
greedy_by_density = []

expenditure_by_profit = 0
expenditure_by_weight = 0
expenditure_by_density = 0

income_by_profit = 0
income_by_weight = 0
income_by_density = 0

# greedy by profit


# greedy by weight

# greedy by density

print(knapsack_sorted_by_weight)
print(knapsack_sorted_by_profit)
print(knapsack_sorted_by_density)
