import qrcode

meu_qrcode = qrcode.make({
    'itemId': '63eb1b8a-8b4e-11ee-b9d1-0242ac120002\n',
    'product': 'Maionese Hellmans NBA edition',
    'expiration': '23/04/2024',
    'position': 'A3.3'
})

# Mudar nome
meu_qrcode.save("A3.png")