import paho.mqtt.client as mqtt
import time
import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(1), channels=1, rate=16000, output=True)
timeflag =0
HOST = "124.223.103.23"#树莓的MQTT服务器
PORT = 1883#树莓的MQTT服务器端口
def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 15)
    client.loop_forever()
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("ESP32_RECVER")#订阅两个语音
    client.subscribe("ESP32_SENDER")
    print("ready!")
 
def on_message(client, userdata, msg):
    stream.write(msg.payload)#接收到的语音信息直接写入到stream
    
 
if __name__ == '__main__':
    client_loop()