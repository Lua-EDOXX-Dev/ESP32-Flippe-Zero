from PIL import Image

img = Image.open("TFTbootLogo.png").convert("RGB")

# Auf 240x280 bringen
img = img.resize((240, 280))

data = bytearray()

for r, g, b in img.getdata():
    rgb565 = ((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3)

    data.append((rgb565 >> 8) & 0xFF)
    data.append(rgb565 & 0xFF)

with open("boot.rgb565", "wb") as f:
    f.write(data)

print("Fertig:", len(data), "Bytes")