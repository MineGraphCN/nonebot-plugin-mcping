import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="nonebot-plugin-mcping",  # 项目名称，保证它的唯一性，不要跟已存在的包名冲突即可
    version="0.0.1",  # 程序版本
    author="17TheWord",  # 项目作者
    author_email="17theword@gmail.com",  # 作者邮件
    description="基于NoneBot的查询MineCraft服务器状态并返回图片的插件",  # 项目的一句话描述
    long_description=long_description,  # 加长版描述？
    long_description_content_type="text/markdown",  # 描述使用Markdown
    url="https://github.com/17TheWord/nonebot-plugin-mcping",  # 项目地址
    packages=setuptools.find_packages(),  # 无需修改
    classifiers=[
        "Programming Language :: Python :: 3.9",  # 使用Python3.10
        "License :: OSI Approved :: GNU Affero General Public License v3",  # 开源协议
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'nonebot2>=2.0.0rc3',
        'nonebot-adapter-onebot>=2.1.1',
        'nonebot-plugin-guild-patch>=0.2.0',
        'mcstatus>=10.0.0',
        'pillow>=9.4.0'
    ],
)
