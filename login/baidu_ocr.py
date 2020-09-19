# encoding:utf-8
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '22686391'
API_KEY = 'dLnEqSjPvOvoXImzXkfcSGMc'
SECRET_KEY = 'G9t50Q46x0ANCALgGD9BepkCCGE1T48Z'
def baid_ocr_to_text():
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)#调用个人账号信息

    def get_file_content(filePath):#定位图片位置
        with open('./code/vcode.png', 'rb') as fp:
            return fp.read()
    image = get_file_content('example.jpg')

    """ 调用通用文字识别, 图片参数为本地图片 """
    text = client.basicGeneral(image)#识别图片信息装入text
    code = text['words_result'][0]['words']
    return code

if __name__ == "__main__":
    baid_ocr_to_text()

