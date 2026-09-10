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