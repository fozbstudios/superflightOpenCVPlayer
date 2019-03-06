import sounddevice as sd
import time 
sd.default.samplerate = 48000
sd.default.channels = 2
duration =3 #seconds
# todo
    #rember default source
    # sample all sources
    # let user pivck new default
    # reset default back via pulse
soundArr = sd.rec(duration * sd.default.samplerate,dtype='float64',device=8)
sd.wait()# block until recording is done 
print(soundArr)
print("playing in 10!")
time.sleep(10)
while True:
    print("playing")
    sd.play(soundArr,device=8)
    sd.wait()
