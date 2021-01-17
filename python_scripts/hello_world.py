name = data.get("name", "world")
logger.info("Hello %s", name)
hass.bus.fire(name, {"wow": "from a Python script!"})