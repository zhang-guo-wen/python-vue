"""
    启动web服务
    打开网页
    启动系统托盘
"""
import threading
import webbrowser
from sample.route.main import run_web_app
from sample.service.menu_service import create_menu
from sample.util import config

start = False


def start(debug=True):
    mul_web = threading.Thread(target=run_web_app, args=(debug,))
    mul_web.start()
    webbrowser.open(config.web_url)
    create_menu()
    mul_web.join()


start(False)
if __name__ == '__main__':
    start(True)
