
def process_list_items(items: list[str]):
    for item in items:
        print(item.title() + " is a fruit. And " + item.capitalize() + " is delicious.")

process_list_items(["apple", "banana", "cherry"])

def process_tuple_and_set(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

print(process_tuple_and_set((1, 2, "three"), {b'four', b'five', b'six'}))

def process_dict_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name, item_price)

process_dict_items({"apple": 0.99, "banana": 0.59, "cherry": 2.99})


def process_union_item(item: int | str):
    print(item)

process_union_item(42)
process_union_item("Hello, World!")


def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

say_hi("Alice")
say_hi()