shop_list = {}

def add_user ():
    data = int(input("Сколько строк вы хотите внести?: "))
    for elem in range(0, data):
        user = input("Введите покупателя: ")
        product = input("Введите товар и количество: ")
        if user in shop_list:
            shop_list[user].append(product)
        else:
            shop_list[user] = [product]
    return shop_list

def output_shop_list():
    sort_shop_list = {}
    sorted_keys = sorted(shop_list.keys())
    for user in sorted_keys:
        sort_shop_list[user] = sorted(shop_list[user])
    return sort_shop_list

add_user()
output_shop_list()
print(output_shop_list())
