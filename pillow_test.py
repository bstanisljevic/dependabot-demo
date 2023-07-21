import PIL
from PIL import Image, ImageFont, ImageDraw

# Function to use ImageFont.getsize(), which got deprecated in Pillow 10.0.0
def get_text_size(text, font_path, font_size):
    font = ImageFont.truetype(font_path, font_size)
    size = font.getsize(text)
    return size


font_path = "NITEMARE.TTF"
font_size = 24
text = "Hello, Pillow!"

text_size = get_text_size(text, font_path, font_size)
print(f"The size of the text '{text}' is: {text_size}")
