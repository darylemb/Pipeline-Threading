import threading 
import alsaaudio
import queue
#Datos
fs=8000
N=170
def  Reproductor(q2):
	if q.qsize()>=3: 
		while True:
			audio=q.get()
			player.write(audio)

#Grabadora de audio
recorder=alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL, 'sysdefault:CARD=1') #Para debian
recorder.setchannels(1)
recorder.setrate(fs)
recorder.setformat(alsaaudio.PCM_FORMAT_S16_LE)
recorder.setperiodsize(N)

#Reproductor de audio
player=alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, alsaaudio.PCM_NORMAL, 'sysdefault:CARD=1') #Para debian
player.setchannels(1)
player.setrate(fs)
player.setformat(alsaaudio.PCM_FORMAT_S16_LE)
player.setperiodsize(N)

q=queue.Queue() 

for k in range(1000):
	print ("Grabando...")
	length,strBuff=recorder.read()
	q.put(strBuff)
	t= threading.Thread(target=Reproductor,args=(q,))  
	t.start()
