
# 使用说明
---
我想写一个window小工具，但是我不会pyqt，于是我就用web技术栈搭建了一套python作为后端，vue作为前端，然后将前后端打包成exe直接运行的脚手架。
### 已经完成工作
- 前端vite、后端flask.前后端热加载，修改即生效
- 加密core文件夹下所有代码成.pyd形式，提高性能和防止解密
- 将自己的代码打包成egg压缩包，做好的工具发别人用时，不会看到满屏都是python文件
- 定义了文件层级规范、编码规范PEP8、静态代码检测推荐pylint、单元测试使用pytest库
### 调试开发
---
入口函数在`sample/main.py`里面，该启动程序启动时产生一个系统托盘，然后跳转到浏览器的前端主页面。托盘有两个菜单用于关闭程序和打开前端页面。
```
# 启动后端
python sample/main.py

# 打包成exe时
python bin/build.py

# 修改了核心文件后需要重新编译，因为默认优先是读取.pyd文件
python bin/build_core.py
```




