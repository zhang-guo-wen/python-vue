import datetime
import os
import shutil
from pathlib import Path

# 项目路径，不可修改
run_path = os.path.abspath('..')
# 打包项目名称，默认当前项目名称
project_name = run_path[run_path.rindex('\\') + 1:]
# 编译生成的文件夹名称，默认当前项目`dist`下
build_file_name = 'dist'
# 排除的依赖文件，不打包
ignore_rely_name = []
# 前端项目名称
web_ui_project_name = 'vue3-ui'
# 前端项目路径
web_ui_file_path = run_path + '/' + web_ui_project_name
# 前端项目编译后的路径
web_ui_build_file_path = run_path + '/' + web_ui_project_name + '/dist'
# 是否开启编译打印详情
build_log_print = False


def del_old_build_file(file_list):
    """清除编译过程生成的文件"""
    for file_path in file_list:
        if Path(file_path).is_file():
            os.remove(file_path)
        elif Path(file_path).is_dir():
            shutil.rmtree(file_path)


def move_and_rename_file(source_file, target_file):
    """移动并命名文件"""
    if Path(source_file).is_file() and not Path(target_file).is_file():
        os.rename(source_file, target_file)
    elif Path(source_file).is_file() and Path(target_file).is_file():
        os.remove(source_file)


def created_build_file(build_file_path=run_path, project_name_=project_name, build_file_name_=build_file_name):
    """根据设定路径创建编译目录，清除旧的编译文件"""
    print(f'{datetime.datetime.now()}:{project_name_}正在编译，请勿中断。。。')
    print(f'{datetime.datetime.now()}:拷贝运行环境文件中。。。')
    dist_dir = Path(build_file_path + '/' + build_file_name_)
    if not dist_dir.exists() and not dist_dir.is_dir():
        os.mkdir(dist_dir)
    build_dir = Path(build_file_path + '/' + build_file_name_ + '/' + project_name_)
    if build_dir.exists():
        shutil.rmtree(build_dir)


def copy_runtime_file(build_file_path=run_path, project_name_=project_name, build_file_name_=build_file_name):
    """复制运行环境"""
    runtime_source = Path(build_file_path + '/docs/build_file/')
    if not runtime_source.is_dir():
        raise FileNotFoundError(build_file_path + '/docs/runtime 中的python运行环境文件被删除，无法编译')
    runtime_target = Path(build_file_path + '/' + build_file_name_ + '/' + project_name_ + '/')
    shutil.copytree(runtime_source, runtime_target)
    env_package_source = Path(build_file_path + '/venv/Lib/site-packages')
    if not env_package_source.exists():
        raise FileNotFoundError(
            build_file_path + '/venv/Lib/site-packages 虚拟机环境依赖没有找到，请使用虚拟机环境创建项目')
    env_package_target = Path(build_file_path + '/' + build_file_name_ + '/' + project_name_ + '/site-packages')
    shutil.copytree(env_package_source, env_package_target)


def del_runtime_rely(rely_name_list=ignore_rely_name):
    """删除不需要的依赖包，如测试，pip等等"""
    ...


def build_ui():
    """编译前端，并复制文件"""
    print(f'{datetime.datetime.now()}:开始编译前端项目。。。')
    command = 'cd ' + web_ui_file_path + ' & npm run build:prod'
    if not build_log_print:
        command = command + '>nul 2>nul'
    os.system(command)
    print(f'{datetime.datetime.now()}:复制前端dist文件中。。。')
    ui_source = Path(web_ui_build_file_path)
    if not ui_source.exists():
        raise FileNotFoundError(web_ui_build_file_path + '文件没有找到')
    ui_target = Path(run_path + '/dist/' + project_name + '/dist')
    shutil.copytree(ui_source, ui_target)


def build_encrypt_code():
    """加密核心代码,清除过程文件"""
    print(f'{datetime.datetime.now()}:加密核心代码,清除过程文件。。。')
    try:
        core_path = run_path + '/sample/core/'
        core_code_list = os.listdir(Path(run_path + '/sample/core'))
        for file_name in core_code_list:
            file_name = str(file_name)
            if file_name == '__init__.py':
                continue
            if Path(core_path + file_name).is_file() and file_name.endswith('.py'):
                # linux
                # command = f'cd {core_path} & easycython {file_name} >/dev/null 2>&1'
                command = f'cd {core_path} & easycython {file_name}'
                if not build_log_print:
                    command = command + '>nul 2>nul'
                os.system(command)
        del_old_build_file(['../sample/core/build'])
        for file_name in core_code_list:
            file_name = str(file_name)
            if file_name == '__init__.py' or file_name.endswith('.pyd'):
                continue
            # 清除加密核心core.py生成的中间文件，只保留.pyd文件
            c_build_list = ['../sample/core/' + file_name.replace('.py', '.c'),
                            '../sample/core/' + file_name.replace('.py', '.html')]
            del_old_build_file(c_build_list)
    except Exception as e:
        print(e)
        print('加密失败，可能是缺少环境。。。')


def zip_code(build_file_path=run_path, project_name_=project_name, build_file_name_=build_file_name):
    """打包文件成egg格式，排除core文件夹下面的.py文件和.pyc文件"""
    print(f'{datetime.datetime.now()}:执行setup.py文件，压缩python文件生成egg文件')
    core_code_list = os.listdir(Path(run_path + '/sample/core'))
    for file_name in core_code_list:
        file_name = str(file_name)
        if file_name == '__init__.py':
            continue
        if file_name.endswith('.py'):
            core_source = '../sample/core/' + file_name
            core_target = '../sample/core/' + file_name.replace('.py', "")
            # 排除core.py文件，因此重新命名一下
            move_and_rename_file(core_source, core_target)
    # 删除core的.pyc缓存文件不打包.虽然setup时好像会将.py编译成.pyc，但是没有.py不会编译成，.pyd也不能编译
    del_old_build_file([build_file_path + '/sample/core/__pycache__'])
    command = 'cd .. & python setup.py bdist_egg'
    if not build_log_print:
        command = command + '>nul 2>nul'
    os.system(command)
    # 清除生成的中间文件，将生成的文件移动到项目中，并且改名.
    del_old_build_file(['../build', '../' + project_name_ + '.egg-info'])
    core_code_list = os.listdir(Path(run_path + '/sample/core'))
    for file_name in core_code_list:
        file_name = str(file_name)
        if file_name.endswith('.pyd') or file_name.endswith('.py'):
            continue
        core_source = '../sample/core/' + file_name
        core_target = '../sample/core/' + file_name + '.py'
        # 排除core.py文件，因此重新命名一下
        move_and_rename_file(core_source, core_target)


def copy_egg_file(build_file_path=run_path, project_name_=project_name, build_file_name_=build_file_name):
    move_and_rename_file(build_file_path + '/' + build_file_name_ + '/' + project_name_ + '-1.0-py3.8.egg',
                         build_file_path + '/' + build_file_name_ + '/' + project_name_ + '/sample.egg')


if __name__ == '__main__':
    # 创建编译目录
    created_build_file()
    # 复制python运行环境
    copy_runtime_file()
    # 编译前端项目
    build_ui()
    # 将core加密，然后删除多余文件注意需要c++环境，需要安装easycython cpython
    build_encrypt_code()
    #
    zip_code()
    #
    copy_egg_file()
