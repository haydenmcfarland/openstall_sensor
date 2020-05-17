MUTATION_MOTION = """
mutation {{
  motionDetected(sensorId: {}) {{
    result
  }}
}}
"""

MUTATION_PING = """
mutation {{
  ping(sensorId: {}) {{
    result
  }}
}}
"""

MUTATION_SENSOR_INIT = """
mutation {
  sensorInit() {
    result
  }
}
"""