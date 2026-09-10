# Rewrite this code as SEQUENTIAL
cart_total = 120
is_member - True
has_coupon = False
if is_member:
    if cart_total > 100:
        print("Member discount: 20% off + free shipping!")
    elif cart_total > 50:
        print("Member discount: 10% off!")
    else:
        print("Member discount: 5% off!")
else:
    if has_coupon:
        print("Coupon discount: 10% off!")
    elif cart_total > 100:
        print("Non-member discount: 5% off + free shipping!")
    else:
        print("No discounts availab.e Sign up for membership!")

# Sequential version (you can use if statements still, just no branching!)
cart_total = 120
is_member - True
has_coupon = False

if (cart_ total > 100 and is_member):
    print("Member discount: 20% off + free shipping!")
if (cart_total > 50 and is_member):
    print("Member discount: 10% off!")
if (is_member):
    print("Member discount: 5% off!")
if (has_coupon and not is_member):
    print("Coupon discount: 10% off!")
if (cart_total > 100 and not is_member):
    print("Non-member discount: 5% off + free shipping!")
if (cart_total < 100 and not is_member)
    print("No discounts available. Sign up for membership!")

# Slides answer
cart_total = 120
is_member - True
has_coupon = False

# Precompute possible conditions
member_and_cart_over_100 = is_member and (cart_total > 100)
member_and_cart_over_50 = is_member and (cart_total > 50)
member_and_cart_under_50 = is_member and (cart_total <= 50)

non_member_and_has_coupon = not is_member and has_coupon
non_member_and_cart_over_100 = not is_member and (cart_total > 100)
non_member_and_cart_under_100 = not is_member and (cart_total <= 100) and (not has_coupon)

if member_and_cart_over_100:
    print("Member discount: 20% off + free shipping!")
if member_and_cart_over_50:
    print("Member discount: 10% off!")
if member_and_cart_under_50:
    print("Member discount: 5% off!")
if non_member_and_has_coupon:
    print("Coupon discount: 10% off!")
if non_member_and_cart_over_100:
    print("Non-member discount: 5% off + free shipping!")
if non_member_and_cart_under_100:
    print("No discounts available. Sign up for membership!")

# Fully Looping Practice
cart_total = 120
is_member - True
has_coupon = False

# Define all discount rules as a list of dictionaries
discount_rules: [
    {"condition": lambda: is_member and cart_total > 100,
    "message": "Member discount: 20% off + free shipping!"},
    {"condition": lambda: is_member and cart_total > 50,
     "message": "Member discount: 10% off + free shipping!"},
    {"condition": lambda: is_member and cart_total <= 50,
     "message": "member discount: 5% off!"},
    {"condition": lambda: not is_member and has_coupon,
     "message": "Coupon discount: 10% off!"},
    {"condition": lambda: not is_member and cart_total > 100,
     "message": "Non-member discount: 5% off + free shipping!"},
    {"condition": lambda: not is_member and cart_total< 100,
     "message": "No discounts available. Sign up for membership!"}
]

# Loop over the rules and print the first applicable discount
for rule in discount_rules:
    if rule["condition"]():
        print(rule["message"])
        break # stop after the first matching rule