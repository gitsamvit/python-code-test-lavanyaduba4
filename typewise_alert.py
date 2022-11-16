def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = 0
  upperLimit = 0
  if coolingType == 'PASSIVE_COOLING':
    lowerLimit = 15
    upperLimit = 35
  elif coolingType == 'HI_ACTIVE_COOLING':
    lowerLimit = 35
    upperLimit = 45
  elif coolingType == 'MED_ACTIVE_COOLING':
    lowerLimit = 20
    upperLimit = 40
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    return send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    return send_to_email(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  return f'{header}, {breachType}'


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    return f'To: {recepient}\nHi, the temperature is too low'
  elif breachType == 'TOO_HIGH':
    return f'To: {recepient}\nHi, the temperature is too high'