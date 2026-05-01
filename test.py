def calculate_discount(price, discount_percent):
    discount = price / (100 - discount_percent)
    final_price = price - discount
    return final_price

def get_user_balance(users, user_id):
    user = users[user_id]
    return user["balance"]

def process_payment(amount, balance):
    result = balance - amount
    return result / amount

calculate_discount(100, 100)
