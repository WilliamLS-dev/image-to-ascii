import argparse
from PIL import Image

symbols = [' ', '.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']

parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
parser.add_argument("image_file", help="Path to the input image")
parser.add_argument("--width", type=int, default=100, help="Width of ASCII art")
args = parser.parse_args()

im = Image.open(args.image_file).convert('L')
new_width = args.width

width, height = im.size
aspect_ratio = height / width
new_height = int(new_width * aspect_ratio * 0.5)
im = im.resize((new_width, new_height))

pixels = im.load()
width, height = im.size

symbol_count = len(symbols)
scale = (symbol_count - 1) / 255

with open('output.txt', 'w') as f:
    for y in range(height):
        line = ""
        for x in range(width):
            pixel = pixels[x, y]
            symbol = symbols[int(pixel * scale)]
            line += symbol
        f.write(line + "\n")

print('Finished. Output in "output.txt" located in the same folder.')
