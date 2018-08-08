# ...
DOMAIN = "ch_weather"


def setup(hass, config):
    """Setup the ch_weather component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('ch_weather.Temperature', 'test')

    # Return boolean to indicate that initialization was successfully.
    return True
