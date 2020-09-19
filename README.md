# selenium_jiayibao_auto

制作加一宝管理后台自动登录脚本

首先使用pytessreact识别验证码，由于识别成功率太低，更换百度OCR识别并登录成功

注：	1.安装pytessreact需要依赖tesseract，该插件可以使用brew安装（mac）
	2.百度OCR识别结果为字典形式，需要对结果进行提取，定位为['words_result'][0]['words']
	3.vs code使用blazmeter生成的脚本报错Unused variable ‘e’问题暂未解决，搜索说是安装的插件问题，待时间空余再处理
	4.识别验证码模块可单独出来，目前暂缓

<login>--2020.09.19
	完成自动登录的脚本封装与调用，将百度OCR识别分开，增加代码可读性