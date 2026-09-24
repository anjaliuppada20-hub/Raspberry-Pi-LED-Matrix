```python
import RPi.GPIO as GPIO
import time

# --------------------------------
# Raspberry Pi LED Matrix
# --------------------------------

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 8 row pins
ROWS = [5, 6, 13, 19, 26, 16, 20, 21]

# 8 column pins
COLS = [12, 25, 24, 23, 18, 17, 27, 22]

# Setup GPIO pins
for pin in ROWS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

for pin in COLS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


# ------------------------
```

