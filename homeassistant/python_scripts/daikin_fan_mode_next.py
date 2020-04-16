service_data = {"entity_id": "counter.daikin_fan_mode"}
isLastState = hass.states.get("counter.daikin_fan_mode").state
if isLastState == "4":
  hass.services.call("counter","reset",service_data, False)
else:
  hass.services.call("counter","increment",service_data, False)