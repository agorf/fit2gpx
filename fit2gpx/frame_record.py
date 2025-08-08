class FrameRecord:
    def __init__(self, frame):
        self.frame = frame

    @property
    def longitude(self):
        lon = self.frame.get_value('position_long', fallback=None)

        if lon:
            return self.__semicircles_to_degrees(lon)

    @property
    def latitude(self):
        lat = self.frame.get_value('position_lat', fallback=None)

        if lat:
            return self.__semicircles_to_degrees(lat)

    @property
    def altitude(self):
        return self.frame.get_value('enhanced_altitude', fallback=None) or self.frame.get_value('altitude', fallback=None)

    @property
    def timestamp(self):
        return self.frame.get_value('timestamp')

    @property
    def heart_rate(self):
        return self.frame.get_value('heart_rate', fallback=None)

    @property
    def cadence(self):
        return self.frame.get_value('cadence', fallback=None)

    @property
    def is_valid(self):
        return self.longitude is not None and self.latitude is not None

    def __semicircles_to_degrees(self, semicircles):
        return semicircles * (180.0 / 2**31)
