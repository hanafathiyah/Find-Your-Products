from operator import itemgetter


def printresult(arrayofresult):
    display = []
    cnt = 0
    if(len(arrayofresult) >= 0):
        display.append([1, arrayofresult[0][0]])
        for i in range(1, len(arrayofresult)):
            if(arrayofresult[i] == arrayofresult[i-1]):
                display[len(display)-1][0] += 1
            else:
                display.append([1, arrayofresult[i][0], arrayofresult[i][1]])
    else:
        print("There's no product you can sell")

    print("Result:")
    for i in display:
        print(str(i[0])+"x"+" "+str(i[1])+" " +
              str('{:,}'.format(i[2]).replace(",", ".")))


# Inisialisasi Array Kosong
array_of_product = []
greedy_by_profit = []
greedy_by_weight = []
greedy_by_density = []
knapsack = []

print("Welcome to Find Your Products App")
print("You can input your products below and we'll give you some recommendations")
print("")

# Modal atau capital digunakan sebagai penanda kapasitas pada integer knapsack
modal = int(input("Input your capital: "))
print("")

user_input = input("Do you want to continue? (Y/N): ")

while (user_input == 'Y'):
    product_name = input(
        f"Input your product's name: ")
    # product_buy_price digunakan sebagai penanda weight pada integer knapsack
    product_buy_price = int(
        input(f"Input your product's buying price: "))
    product_quantity = int(
        input(f"Input your product's quantity: "))
    product_sell_price = int(
        input(f"Input your product's selling price: "))
    # product_profit digunakan sebagai penanda profit pada integer knapsack
    product_profit = product_sell_price - product_buy_price

    array_of_product.append([len(array_of_product)+1, product_name,
                            product_buy_price, product_quantity, product_sell_price, product_profit])
    print("")

    user_input = input("Do you want to continue? (Y/N): ")

print("")

# i[0]: id, i[1]: name, i[2]: buying price, i[3]: quantity, i[4]: selling price, i[5]: profit
for i in array_of_product:
    for j in range(i[3]):
        # append name, buying price (as weight), profit (as profit), and i[5]/i[2] as density
        knapsack.append([i[1], i[2], i[5], float(i[5]/i[2])])

# heuristik: greedy berdasarkan weight, profit, dan density

# weight terurut membesar
knapsack_sorted_by_weight = sorted(knapsack, key=itemgetter(1))
# profit terururut mengecil
knapsack_sorted_by_profit = sorted(knapsack, key=itemgetter(2), reverse=True)
# density terurut mengecil
knapsack_sorted_by_density = sorted(knapsack, key=itemgetter(3), reverse=True)

# greedy by profit
loop = 0
total = 0
while (loop < len(knapsack_sorted_by_profit)):
    if(total + knapsack_sorted_by_profit[loop][1] <= modal):
        # append digunakan untuk mengganti nilai 0 dan 1 pada objek
        greedy_by_profit.append(knapsack_sorted_by_profit[loop])
        total += knapsack_sorted_by_profit[loop][1]
    loop += 1

# greedy by weight
loop = 0
total = 0
while (loop < len(knapsack_sorted_by_weight)):
    if(total + knapsack_sorted_by_weight[loop][1] <= modal):
        # append digunakan untuk mengganti nilai 0 dan 1 pada objek
        greedy_by_weight.append(knapsack_sorted_by_weight[loop])
        total += knapsack_sorted_by_weight[loop][1]
    loop += 1

# greedy by density
loop = 0
total = 0
while (loop < len(knapsack_sorted_by_density)):
    if(total + knapsack_sorted_by_density[loop][1] <= modal):
        # append digunakan untuk mengganti nilai 0 dan 1 pada objek
        greedy_by_density.append(knapsack_sorted_by_density[loop])
        total += knapsack_sorted_by_density[loop][1]
    loop += 1

printresult(greedy_by_profit)
