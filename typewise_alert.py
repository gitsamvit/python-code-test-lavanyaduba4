def classify_temperature_breach(coolingType, temperatureInC):
  coolingType_limits={'PASSIVE_COOLING':[15,35],'HI_ACTIVE_COOLING':[35,45],'MED_ACTIVE_COOLING':[20,40]}
  if temperatureInC < coolingType_limits[coolingType][0] :
    return 'TOO_LOW'
  if temperatureInC > coolingType_limits[coolingType][1] :
    return 'TOO_HIGH'
  return 'NORMAL'

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