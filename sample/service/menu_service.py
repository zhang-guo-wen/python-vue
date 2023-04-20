import os
import webbrowser
import pystray
from PIL import Image, ImageDraw
from pystray import MenuItem
from sample.util import config


def on_closing():
    # 关闭程序，杀死进程
    # LINUX
    # os.kill(os.getpid(), signal.SIGKILL)
    pid = os.getpid()
    os.system('taskkill /f /pid %s' % + pid)


def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image


def on_exit(icon, item):
    icon.stop()
    on_closing()


def create_menu():
    menu = (MenuItem('打开界面', lambda: webbrowser.open(config.web_url)),
            MenuItem(text='退出', action=on_exit),)

    image = create_image(64, 64, 'black', 'white')
    # In order for the icon to be displayed, you must provide an icon

    icon = pystray.Icon("name", image, "", menu)
    icon.run()
