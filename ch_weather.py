DOMAIN = 'ch_weather'

def setup(hass, config):
    hass.states.set('Meteo.Temperature', 'Warm')

    return True
