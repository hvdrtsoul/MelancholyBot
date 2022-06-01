from PIL import Image

image_to_send = Image.new("RGBA", (400, 100))
icon_to_insert = Image.open("icons/01d.png")

image_to_send.paste(icon_to_insert)
image_to_send.save("tmp.png")
