DOMAIN = "mohan_helloworld"

async def async_setup(hass, config):
    hass.states.async_set("mohan_helloworld.world", "Hello World")
    # Return boolean to indicate that initialization was successful.
    return True