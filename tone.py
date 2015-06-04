import math
from pyb import DAC, micros, elapsed_micros

def tone1(freq):
    t0 = micros()
    dac = DAC(1)
    while True:
        theta = 2*math.pi*float(elapsed_micros(t0))*freq/1e6
        fv = math.sin(theta)
        v = int(126.0 * fv) + 127
        #print("Theta %f, sin %f, scaled %d" % (theta, fv, v))
        #delay(100)
        dac.write(v)

def tone2(freq):
    t0 = micros()
    dac = DAC(1)
    omega = 2 * math.pi * freq / 1e6
    while True:
        theta = omega*float(elapsed_micros(t0))
        fv = math.sin(theta)
        v = int(126.0 * fv) + 127
        #print("Theta %f, sin %f, scaled %d" % (theta, fv, v))
        #delay(100)
        dac.write(v)

def tone3(freq, l_buf=256):
    dac = DAC(1)
    dtheta = 2 * math.pi / l_buf
    scale = lambda fv: int(126.0 * fv) + 127
    buf = bytearray(scale(math.sin(dtheta*t)) for t in range(l_buf))
    dac.write_timed(buf, freq * l_buf, mode=DAC.CIRCULAR)

def tone4(freq, l_buf=256):
    dac = DAC(1)
    dtheta = 2 * math.pi / l_buf
    scale = lambda fv: int(123 * fv) + 127
    buf = bytearray(scale(math.sin(dtheta*t)) for t in range(l_buf))
    dac.write_timed(buf, freq * l_buf, mode=DAC.CIRCULAR)

def tone5(freq, wavefun=lambda x: math.sin(2.0*math.pi*x), l_buf=256):
    dac = DAC(1)
    dt = 1.0 / l_buf
    scale = lambda fv: int(123 * fv) + 127
    buf = bytearray(scale(wavefun(t*dt)) for t in range(l_buf))
    dac.write_timed(buf, freq * l_buf, mode=DAC.CIRCULAR)

def tone6(freq, wavefun=lambda x: math.sin(2.0*math.pi*x), l_buf=256, dacnum=1):
    dac = DAC(dacnum)
    dt = 1.0 / l_buf
    scale = lambda fv: int(123 * fv) + 127
    buf = bytearray(scale(wavefun(t*dt)) for t in range(l_buf))
    dac.write_timed(buf, freq * l_buf, mode=DAC.CIRCULAR)
