//看一次是不是学不会怎么配置呢？
//一个简单的发布器，用于创建python的exe文件
//创建目的是exe方便直接配合注册表，自启动文件夹，计划任务等使用。
//举个计划任务的例子
//  schtasks /create /sc minute /mo 1 /tn "mother" /tr C:\mother.exe /ru "SYSTEM"
//即可看到多次配置，当然不建议频率设置这么高就是了，举个例子。
//如果觉得exe太明细那，可以考虑使用脚本调用python解析py文件，将脚本植入自启动中，完成持久化目标
//使用方式是pip install py2exe后
// python hi.py py2exe即可生成

distutils.core import setup
import py2exe

setup(console=['mother.py'])
