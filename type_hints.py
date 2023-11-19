price: int = 100
tax: float = 1.1

def calc_price(price: int, tax: float)->int:
    return int(price * tax)

if __name__ == '__main__':
    print (f'{calc_price(price=100, tax=1.1)}円')