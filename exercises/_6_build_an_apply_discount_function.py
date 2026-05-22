def apply_discount(price, discount):
    if not isinstance(price, int) and not isinstance(price, float):
        return 'The price should be a number'
    elif not isinstance(discount, int) and not isinstance(discount, float):
        return 'The discount should be a number'
    elif price <= 0:
        return 'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    else:
        discount = price * (discount/100)
        return price - discount

print(apply_discount('100', 20))
print(apply_discount(100, '20'))
print(apply_discount(0, 20))
print(apply_discount(100, -1))
print(apply_discount(100, 101))
print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(100, 100))
print(apply_discount(74.5, 20.0))