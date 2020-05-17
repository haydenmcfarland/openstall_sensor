from openstall_sensor.configuration import configure
from openstall_sensor.constants import API_URL, PIR_PIN, SLEEP, ERROR_QUERY
from openstall_sensor.graphql.mutations import MUTATION_MOTION
import requests
import RPi.GPIO as GPIO
import time

DEBUG = True


def execute_query(query):
    request = requests.post(API_URL, json={'query': query})
    if request.status_code != 200:
        raise Exception(ERROR_QUERY.format(request.status_code, query))
    return request.json()


# FIXME: we need to have the server determine the sensor ID on initialization
SENSOR_ID = 1


def motion(PIR_PIN):
    result = execute_query(MUTATION_MOTION.format(SENSOR_ID))
    if DEBUG:
        print(result)


def run():
    try:
        configure(GPIO)
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motion)
        while True:
            print('...')
            time.sleep(SLEEP)
    except KeyboardInterrupt:
        GPIO.cleanup()
