from openstall_sensor.constants import PIR_PIN


def configure(GPIO):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)
