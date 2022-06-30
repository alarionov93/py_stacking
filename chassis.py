import RPi.GPIO as GPIO
import time

LF = 9
LR = 10
RF = 5
RR = 11

EL = 26
ER = 19
EF = 13
EB = 6

GPIO.setmode(GPIO.BCM)
GPIO.cleanup(EL)
GPIO.cleanup(ER)
GPIO.cleanup(EF)
GPIO.cleanup(EB)
GPIO.cleanup(LF)
GPIO.cleanup(LR)
GPIO.cleanup(RF)
GPIO.cleanup(RR)

GPIO.setup(EL, GPIO.OUT)
GPIO.setup(ER, GPIO.OUT)
GPIO.setup(EF, GPIO.OUT)
GPIO.setup(EB, GPIO.OUT)

GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LR, GPIO.OUT)
GPIO.setup(RF, GPIO.OUT)
GPIO.setup(RR, GPIO.OUT)

pwms = [
    GPIO.PWM(EL, 100),
    GPIO.PWM(ER, 100),
    GPIO.PWM(EF, 100),
    GPIO.PWM(EB, 100),
]

def pwm_values(function):
    def wrapper():
        # actions
        function()
        return wrapper

def go(t):
    st = 0
    values = [30,30,60,30]
    try:
        f = open('check_img.txt', 'r')
    except FileNotFoundError:
        print('File Not Found!')
    for pwm, val in zip(pwms, values):
        pwm.start(val)
    GPIO.output(LF,1)
    GPIO.output(LR,0)
    GPIO.output(RF,1)
    GPIO.output(RR,0)
    while 1:
        time.sleep(1)
        stat = f.read()
        if 'found' in stat:
            for pwm in pwms:
                pwm.stop()
            GPIO.output(LF,0)
            GPIO.output(LR,1)
            GPIO.output(RF,0)
            GPIO.output(RR,1)

    return st

def rgt(angle):
    st = 0
    return st

def fwd(spd):
    st = 0
    return st

def bck(spd):
    st = 0
    return st

go(100)

GPIO.cleanup(EL)
GPIO.cleanup(ER)
GPIO.cleanup(EF)
GPIO.cleanup(EB)
GPIO.cleanup(LF)
GPIO.cleanup(LR)
GPIO.cleanup(RF)
GPIO.cleanup(RR)