from rembg import remove
from PIL import Image
input_path = 'OIP.jpg'
output_path = 'JonSnow.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open("JonSnow.png")