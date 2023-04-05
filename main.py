import requests
import re
import os
import json

defaultFileName = 1     #默认文件夹名

def BaiDuwk_getInfo():
    """获取爬虫必要信息，得到网址及创建本地文件夹"""
    url = input("  爬取百度文库  请输入要爬取的网站：")
    #设定文件夹名
    file = input('  python将创建存储文件夹，请输入文件夹名\n（按下“Enter"键，系统将按默认名创建')
    if file == None :
        file = defaultFileName
    #创建文件夹
    BaiDuwk_path = os.getcwd ()
    BaiDuwk_filePath = BaiDuwk_path + f'\\{file}'
    if not os.path.exists (BaiDuwk_filePath):  # 如果pic文件夹不存在 创建
        os.mkdir (BaiDuwk_filePath)
    return url, file


if __name__ == '__main__':
    url,file = BaiDuwk_getInfo()
    getgoodgrades


