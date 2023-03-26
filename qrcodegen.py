import qrcode
img = qrcode.make('Olá ser estranho que se encontra por aqui, esse foi meu primeiro qrcode gerado em python!\n')
img.save("Meu_primeiro_QrCode.png")