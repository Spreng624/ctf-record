from PIL import Image, ImageDraw, ImageFont

# 创建一个新的白色背景图片
img = Image.new("RGB", (400, 200), color=(255, 255, 255))


# 保存图片为JPG格式
img.save("file_size_image.jpg", "JPEG")
