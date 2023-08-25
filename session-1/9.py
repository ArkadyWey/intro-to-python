# 9. If statements 
stock_price = 10.1

if 0<=stock_price<=5:
    print("Stock is cheap. Buy it!!!") # note the indent - code gets ignored if boolean after if is False
elif 5<stock_price<=10: 
    print("Stock is neither cheap nor expensive. Hold it")
else: 
    print("Stock is expensive. Sell it!!!")