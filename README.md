# NumRecog
## github地址：

https://github.com/CHNVincent/NumRecog.git

## 调用方法示例：
pip install  NumRecog

from NumRecog import model.py,model_inference.py

classifier = MyImageClassifier(device='cpu')   #类的实例化

result = classifier.predict('mnist_test_3.png')   #输入需要识别的数字图片地址，获得识别结果

print(f'预测数字: {result}')                                #输出识别结果


## 项目的打包：
python setup.py sdist:

这个命令用于创建一个源代码分发包（source distribution）。它会将你的项目源代码以及所有必需的文件打包成一个压缩文件（通常是 .tar.gz 或 .zip 文件），这样其他人就可以通过这个包来安装你的项目。这在分发源代码或者在PyPI上发布你的项目时非常有用。
