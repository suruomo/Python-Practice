from PIL import Image, ImageDraw, ImageFont


# 将你的QQ头像（或者微博头像）右上角加上红色的数字，可以微信未读信息数量那种提示效果。
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=150)
    fillcolor = "#ff0000"
    width, height = img.size
    # 在图片右上角添加’99‘水印
    draw.text((width - 200, 50), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')
    return 0


# 程序入口
if __name__ == '__main__':
    image = Image.open('F:\图片\朱一龙镇魂高清4K壁纸_彼岸图网.jpg')
    add_num(image)
    image.show()
