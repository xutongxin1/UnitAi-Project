class MPythonPin():
    def __init__(self,i:int,PinMode:str):
         return

    def write_digital(value):
        "IO引脚输出电平控制。value =1时输出高电平， value =0时输出低电平。"

    def read_digital(self):
        "返回该IO引脚电平值。1代表高电平，0代表低电平"

    def read_analog(self):
        "读取ADC并返回读取结果，返回的值将在0到4095之间。"

    def write_analog(duty: int, freq=1000):
        """设置输出PWM信号的占空比。

duty 0 ≤ duty ≤ 1023
freq PWM波频率,0 < freq ≤ 0x0001312D（十进制:0 < freq ≤ 78125）
"""


class PinMode():
    def OUT(self):
        return
    def IN(self):
        return

class mpythonEsp():
    class ntptime():
        def settime(timezone:str,server:str):
            """"
            授时函数
            时区，授时服务器
            """
            return



class mythonM():
    class mython():
        def sleep(s:int):
            "秒级延时"
            return

        def sleep_ms(ms:int):
            "毫秒级延时"
            return

        def sleep_us(us:int):
            "微秒级延时"
            return

class sound():
        def read(s:int):
            "板载麦克风"
            return
class light():
        def read(s:int):
            "板载光线传感"
            return
class rgb():
        def write(self):
            "生效板载rgb"
            return
class oled():
        def poweron(self):
            "开启屏幕"

        def poweroff(self):
            "关闭屏幕"

        def contrast(brightness:int)-> str:
            """调节屏幕亮度
            brightness 亮度,范围0~255"""

        def DispChar(s:str, x:int, y:int, mode):
            """oled屏显示文本。采用 Google Noto Sans CJK 开源无衬线字体字体，支持英文,简体中文繁体中文，日文和韩文语言。 当显示字符串超出显示屏宽度可自动换行。

返回(字符总像素点宽度,续接显示的x,y坐标)的二元组。

s -需要显示的文本。

x 、y -文本的左上角作为起点坐标。

mode - 设置文本模式,默认为TextMode.normal

TextMode.normal - 等于1 。普通模式,文本显示白色,背景为黑色。
TextMode.rev - 等于2 。反转模式,文本显示黑色,背景为白色。
TextMode.trans - 等于3 。透明模式,透明文本意味着文本被写在显示中已经可见的内容之上。不同之处在于，以前屏幕上的内容仍然可以看到，而对于normal，背景将被当前选择的背景颜色所替代。
TextMode.xor - 等于4 。XOR模式,如果背景是黑色的，效果与默认模式(normal模式)相同。如果背景为白色，则反转文本。
"""
        def show(self):
            "将frame缓存发送至oled显示。"

class wifi():
        def connectWiFi(ssid:str, password:str, timeout:int=10):
            """
            连接wifi网络

ssid -WiFi网络名称
password -WiFi密码
tiemout -链接超时,默认10秒
"""
        def disconnectWiFi(self):
            "断开wifi网络连接"
        def enable_APWiFi(essid:str, password:str, channel:int=10):
            """
            开启wifi的无线AP模式

essid - 创建WiFi网络名称
password - 密码
channel -设置wifi使用信道,channel 1~13
"""
        def disable_APWiFi(self):
            "关闭无线AP"


class mpythonH():
    class urequests():
        def close(self):
            """对连接的操作
            关闭socket。"""
        def content(self):
            """对连接的操作
            返回响应的内容，以字节为单位。"""
        def text(self):
            """对连接的操作
            以文本方式返回响应的内容，编码为unicode。"""
        def json(self):
            """对连接的操作
            返回响应的json编码内容并转为dict类型。"""

        def request(method, url, data, json, headers, params, files):
            """"对连接的操作
            向服务器发送HTTP请求。

method - 要使用的HTTP方法
url - 要发送的URL
data - 要附加到请求的正文。如果提供字典或元组列表，则将进行表单编码。
json - json用于附加到请求的主体。
headers - 要发送的标头字典。
params - 附加到URL的URL参数。如果提供字典或元组列表，则将进行表单编码。
files - 用于文件上传,类型为2元组,其中定义了文件名,文件路径和content类型。如下,{‘name’, (file directory,content-type)}
"""

        def head(url, **kw):
            """"
            发送HEAD请求,返回Response对象。

url - Request对象的URL
**kw - request方法的参数。
"""
        def get(url, **kw):
            """"
            发送GET请求,返回Response对象。

url - Request对象的URL
**kw - request方法的参数。
"""
        def post(url, **kw):
            """
            发送POST请求,返回Response对象。

url - Request对象的URL
**kw - request方法的参数。
"""
        def put(url, **kw):
            """
            发送PUT请求,返回Response对象。

url - Request对象的URL
**kw - request方法的参数。
"""
        def patch(url, **kw):
            """
            送PATCH请求,返回Response对象。

url - Request对象的URL
**kw - request方法的参数。
"""
        def delete(url, **kw):
            """
            发送DELETE请求。,返回Response对象。

url - Request对象的URL
**kw - request方法的参数。
"""
