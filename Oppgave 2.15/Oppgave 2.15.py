import time

def posisjon(t, v0=0, a=0): # funksjon som regner ut posision medtid (t), startfart (v0) og akselerasjonen (a) gitt
    s = v0*t + 0.5*a*t**2 # posisjonen etter tid t
    return s # sender tilbake resultatet
# 45-graders kast
vx0 = 10 # startfart i x-retning (i m/s)
vy0 = 10 # startfart i y-retning (i m/s)
ay = -9.81 # (tyngde)akselerasjon i y-retning (nedover)
tid = 0
tid_steg = 0.1 #
sx = 0
sy = 0
# while-løkka
while sy >= 0: # Vi holder på til ballen har nådd bakken
    sx = posisjon(tid, vx0) # Ingen akselerasjon i x-retning)
    sy = posisjon(tid, vy0, ay) # I y-retning har vi tyngdeakselerasjonen nedover.)
    print("tid: %4.2f" % tid, "s x-posisjon: %5.4f"% sx, "m y-posisjon: %5.4f" % sy,"m") # uformatert print
    #print("tid: %4.2f s x-posisjon: %5.1f m y-posisjon: %5.2f m" %(tid, sx, sy)) # formatert print
    tid = tid + tid_steg # oppdatering av tidsvariabelen
    time.sleep(tid_steg) # denne funksjon stopper Python i tid_steg (0.1) sekunder.
    print("tid: %4.2f s x-posisjon: %5.4f m y-posisjon: %5.4f m" %(tid, sx, sy) )