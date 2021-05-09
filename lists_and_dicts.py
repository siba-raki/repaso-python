def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname" : "Santiago", "lastame": "Ibarra"}

    super_list = [
        {"firstname" : "Santiago", "lastame": "Ibarra"},
        {"firstname" : "Jose", "lastame": "Torres"},
        {"firstname" : "Matias", "lastame": "Matrines"},
        {"firstname" : "Diego", "lastame": "Torres"},
        {"firstname" : "Anduin", "lastame": "Rios"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 6, 8],
        "float_nums": [1.2, 4.4, 5.6]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i)

if __name__ == '__main__':
    run()