import sounddevice as sd
sd.default.samplerate = 48000
sd.default.channels = 2
duration =3 #seconds
#need to use a python jack lib to create audio loopback
for i in range(6,10):
    soundArr = sd.rec(duration * sd.default.samplerate,dtype='float64',device=i)
    sd.wait()# block until recording is done 
    print(soundArr)
    
