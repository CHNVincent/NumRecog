from setuptools import setup, find_packages

setup(
    name='NumRecog',  # 包名
    version='1.0',      # 版本号
    packages=find_packages(),  # 自动查找包
    include_package_data=True,  # 包含非代码文件
    install_requires=[          # 依赖项
        'torch',
        'torchvision',
        'Pillow',
        'numpy'
    ],
    description='手写数字的神经网络识别程序',  # 描述
    author='Vincent 参考知识星球',  # 作者
    author_email='your.email@example.com',  # 作者邮箱
    url='https://github.com/yourusername/my_package',  # 项目地址
    classifiers=[  # 分类信息
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # Python 版本要求
)
