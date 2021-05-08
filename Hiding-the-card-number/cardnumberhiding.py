def card_hide(card): # defining a function to hide a given credit card number
    card = list(card)
    first12 = card[:12]
    last4 = card[12:]
    first12_afterchange = []
    for i in first12:
        first12_afterchange.append("*")
    
    card = first12_afterchange + last4
    return card
def tostring(alist):
    str = ""
    return (str.join(alist))
print(tostring(card_hide("1234567890123456")))
