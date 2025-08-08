import fitdecode

from .frame_record import FrameRecord
from .point_location import PointLocation

class FitData:
    def __init__(self, fit):
        self.records = []
        self.analyze(fit)

    def analyze(self, fit):
        for frame in fit:
            if not isinstance(frame, fitdecode.FitDataMessage):
                continue

            if frame.name == 'session':
                self.sport = frame.get_value('sport')
                continue

            if frame.name != 'record':
                continue

            record = FrameRecord(frame)

            if record.is_valid:
                self.records.append(record)

        if self.records:
            record = self.records[0]
            self.area = PointLocation(record.longitude, record.latitude).name
            self.timestamp = record.timestamp
