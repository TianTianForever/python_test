#_*_coding:utf-8_*_
#author:tiantian
import requests
class youdao_date():
    def __init__(self,parm):
        self.form_data = {}
        self.form_data['type'] = 'AUTO'
        self.form_data['i'] = parm
        self.form_data['doctype'] = 'json'
        self.form_data['keyfrom'] = 'fanyi.web'
        self.form_data['ue'] = 'UTF-8'
        self.form_data['action'] = 'FY_BY_CLICKBUTTON'
        self.form_data['typoResult'] = 'true'
    def translate(self):
        r = requests.get('http://fanyi.youdao.com/translate',params = self.form_data)
        # get json date
        target = r.json()
        target = target['translateResult'][0][0]
        print("%s --> %s"%(target['src'],target['tgt']))

if __name__ == '__main__':
     content = input("请输入要翻译的内容：")
     youdao_translate = youdao_date(content)
     youdao_translate.translate()
#123
