import os
import sys
from flask import Flask, render_template
from sample.route import user
from sample.util.config import web_ui_name

# 如果python版本是这个嵌入式版本，则说明是在egg打包中调用。否则是开发环境
# if sys.version == '3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]':
#     run_path = os.path.abspath('../../'+web_ui_name+'/dist')
# else:
#     run_path = os.path.abspath('../dist/')
run_path = os.path.abspath('../')
app = Flask(__name__, template_folder=run_path + 'dist',
            static_folder=run_path + 'dist/assets')


# 开启全局跨域
# CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/local_file_path')
def local_file_path():
    return run_path


# 将其他页面蓝图注册
app.register_blueprint(user.bp)


# 将所有的路由转发交给vue的路由，因此跳转到index界面
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    return render_template("index.html")


def run_web_app(debug: bool = False):
    app.run(host="127.0.0.1", port=8058, debug=debug)


if __name__ == '__main__':
    # 启动此程序后可以进行调试，接口会自动更新无需重启
    run_web_app(debug=True)
