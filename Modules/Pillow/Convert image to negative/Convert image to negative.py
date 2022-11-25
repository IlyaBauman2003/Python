from PIL import Image, ImageDraw, ImageFont
 
image = Image.open('Positive.jpg')

for i in range(0, image.size[0]-1):
    for j in range(0, image.size[1]-1):

        pixelColorVals = image.getpixel((i,j))
        
        redPixel = 255 - pixelColorVals[0]
        greenPixel = 255 - pixelColorVals[1]
        bluePixel = 255 - pixelColorVals[2]

        image.putpixel((i,j), (redPixel, greenPixel, bluePixel))

draw = ImageDraw.Draw(image, 'RGBA')
font_ = ImageFont.truetype("impact.ttf", 70)
draw.text((0, 0), "GOODNIGHT", fill = (40,0,0,15), font = font_)

image.save("Negativ.jpg")
