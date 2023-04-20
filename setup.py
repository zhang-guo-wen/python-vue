import os.path

from setuptools import setup, find_packages

run_path = os.path.abspath('.')
project_name = run_path[run_path.rindex('\\') + 1:]
# 将我们的代码打包成egg
setup(name=project_name,
      version='1.0',
      # 搜索所有的包，包含_init_.py文件的文件夹
      packages=find_packages(),
      # 将.pyd文件也打包进来
      package_data={
          '': ['*.pyd']
      },
      )
