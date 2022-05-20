import qrcode
from PIL import Image

logo_link = 'LOGO' #logo link (PNG, JPG)

logo = Image.open(logo_link)

basewidth = 150

wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H)

url = 'URL' #enter a valid URL 

QRcode.add_data(url)

QRcode.make()

QRcolor = 'black'

QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

pos = ((QRimg.size[0] - logo.size[0]) // 2,
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

QRimg.save('NAME') #the name you want to save the code with
