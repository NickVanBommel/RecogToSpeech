import speech_recognition as sr
import pyaudio

p = pyaudio.PyAudio()
#print(p.get_default_input_device_info())

while(1):
    r = sr.Recognizer()

    with sr.Microphone(device_index=0) as source:
        print("Say something!")
        audio = r.listen(source)
        print("end listen")

    BING_KEY = "7c6884d746204eb58efbd986f54b3d75" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        output=r.recognize_bing(audio, key=BING_KEY)
        print("Microsoft Bing Voice Recognition thinks you said " + output)
        if "take picture" in output:
            print("CaptureTask")
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))