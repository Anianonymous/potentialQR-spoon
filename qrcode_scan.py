import qrcode as qc
import pyttsx3 as p
seh=p.init()
inp=int(input('enter your kcet rank to seek admission in the college: '))
if inp<=2900:
    img=qc.make('https://www.dsce.edu.in/')
    img.save('dsce.png')
    seh.say('you will get admission at DSCE')
    seh.runAndWait()
elif 5000>inp>2900:
    img = qc.make('http://www.nmit.ac.in/')
    img.save('nmit.png')
    seh.say('you will get admission at NMIT')
    seh.runAndWait()
else:
    seh.say('you will get admission at other colleges')
    seh.runAndWait()
