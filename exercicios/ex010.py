print('bitcoin quote')
usdt = float(input('how many usdt do you have in your wallet now ?'))

btc = 64384  # ideal seria uma api em tempo real com preço do bitcoin

b = usdt/btc

print('you will get {}btc for this price, bro :) see you soon cowboy'.format(b))


