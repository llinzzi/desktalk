#ifndef _AUDIOMQTT_
#define _AUDIOMQTT_

#include <PubSubClient.h>
#include <WiFi.h>
#include "IISAudio.h"
extern PubSubClient client;

#define SENDER  1 

#if SENDER

#define LOCALTOPIC "ESP32_SENDER"
#define PUBTOPIC   "ESP32_RECVER"

#else

#define LOCALTOPIC "ESP32_RECVER"
#define PUBTOPIC   "ESP32_SENDER"

#endif

extern bool sendOver;//发送完成标志位
extern bool recOver;//接受完成标志位
extern bool speakOut;//0代表对外讲话，1代表收听

void callback(char* topic, byte* payload, unsigned int length);
void reconnect() ;
void sendData(const uint8_t  *data, uint16_t len);

#endif
