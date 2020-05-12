"""Mohans first sensor"""
import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_NAME,
    TEMP_CELSIUS
)
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity

DEFAULT_NAME="example_sensor"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up certificate expiry sensor."""
    name = config.get(CONF_NAME)
    add_entities([MohanSensor(name)], True)
    

'''
async def async_setup_entry(hass, entry, async_add_entities):
    """Add cert-expiry entry."""
    name = entry.data[CONF_NAME]

    async_add_entities(
        [MohanSensor(name)], False,
    )
    return True
'''

class MohanSensor(Entity):
    """Implementation of the certificate expiry sensor."""

    def __init__(self, name):
        """Initialize the sensor."""
        self._name = name
        self._state = 23

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique id for the sensor."""
        return self._name

        
    @property
    def unit_of_measurement(self):
        """Return the unit this state is expressed in."""
        return TEMP_CELSIUS
    

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return "mdi:certificate"

    '''
    async def async_update(self):
        """Fetch the certificate information."""
        pass
    '''
'''
    @property
    def device_state_attributes(self):
        """Return additional sensor state attributes."""
        return {"is_valid": self._valid, "error": str(self._error)}
'''