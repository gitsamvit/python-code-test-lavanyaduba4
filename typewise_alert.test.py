import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_check_and_alert_to_controller(self):
    batteryChar={}
    batteryChar['coolingType'] = "HI_ACTIVE_COOLING"
    output= "65261, TOO_HIGH"
    print(typewise_alert.check_and_alert("TO_CONTROLLER",batteryChar,47))
    self.assertTrue(typewise_alert.check_and_alert("TO_CONTROLLER",batteryChar,47) == output)

  def test_check_and_alert_to_email_to_high(self):
    batteryChar={}
    batteryChar['coolingType'] = "MED_ACTIVE_COOLING"
    output= "To: a.b@c.com\nHi, the temperature is too high"
    self.assertTrue(typewise_alert.check_and_alert("TO_EMAIL",batteryChar,47) == output)

  def test_check_and_alert_to_email_to_low(self):
    batteryChar={}
    batteryChar['coolingType'] = "PASSIVE_COOLING"
    output= "To: a.b@c.com\nHi, the temperature is too low"
    self.assertTrue(typewise_alert.check_and_alert("TO_EMAIL",batteryChar,12) == output)  

  def test_check_and_alert_to_email_normal(self):
    batteryChar={}
    batteryChar['coolingType'] = "PASSIVE_COOLING"
    self.assertTrue(typewise_alert.check_and_alert("TO_EMAIL",batteryChar,17) == None)        


if __name__ == '__main__':
  unittest.main()
