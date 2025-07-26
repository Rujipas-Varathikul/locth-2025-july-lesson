"""This programe will calculate the price of grocery from the amount inputed"""

pork_price = 100
basil_price = 100
pad_thai_price = 600
water_price = 10

# input => numbers of products, output => total price
num_pork = int(input('Enter number of pork you want to buy: '))
num_basil = int(input('Enter number of basil you want to buy: '))
num_pad_thai = int(input('Enter number of dishes Pad Thai you want to buy: '))
num_water = int(input('Enter number of water bottles you want to buy: '))

# 1140
total_price = pork_price*num_pork + basil_price*num_basil \
                + pad_thai_price*num_pad_thai + water_price*num_water

print('You need to pay', total_price, 'Bahts.')
