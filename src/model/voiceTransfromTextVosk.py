# 使用 Vosk 进行语音识别
from vosk import Model, KaldiRecognizer
import wave
import json

model = Model("model")  # 需要下载 Vosk 模型
wf = wave.open(
    "/Users/xjk/Desktop/back-code-project/python-tool/src/store/voice/1121爱因斯坦_20241121T131535.574083_缩混.mp3",
    "rb",
)
rec = KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        print(result)  # 打印识别结果，包括时间戳

# 可以提取每个单词的时间戳
result = rec.FinalResult()
print(result)
