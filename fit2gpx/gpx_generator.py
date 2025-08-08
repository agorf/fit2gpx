import xml.etree.ElementTree as ET
from xml.dom import minidom

class GpxGenerator:
    def __init__(self, records, creator, activity_name):
        self.records = records
        self.creator = creator
        self.activity_name = activity_name

    def to_xml(self):
        gpx_attrs = {
            'version': '1.1',
            'creator': self.creator,
            'xmlns': 'http://www.topografix.com/GPX/1/1',
            'xmlns:gpxtpx': 'http://www.garmin.com/xmlschemas/TrackPointExtension/v1'
        }
        gpx = ET.Element('gpx', gpx_attrs)
        trk = ET.SubElement(gpx, 'trk')
        ET.SubElement(trk, 'name').text = self.activity_name
        trkseg = ET.SubElement(trk, 'trkseg')

        for record in self.records:
            self.__record_track_point(trkseg, record)

        return self.__pretty_print_xml(ET.tostring(gpx, 'utf-8'))

    def __record_track_point(self, trkseg, record):
        trkpt = ET.SubElement(trkseg, 'trkpt', lat=str(record.latitude), lon=str(record.longitude))

        self.__record_altitude(trkpt, record)
        self.__record_timestamp(trkpt, record)
        self.__record_extensions(trkpt, record)

    def __record_altitude(self, trkpt, record):
        if record.altitude is not None:
            ele = ET.SubElement(trkpt, 'ele')
            ele.text = str(record.altitude)

    def __record_timestamp(self, trkpt, record):
        if record.timestamp is not None:
            time = ET.SubElement(trkpt, 'time')
            time.text = record.timestamp.isoformat()

    def __record_extensions(self, trkpt, record):
        extensions = ET.SubElement(trkpt, 'extensions')

        self.__record_heart_rate(extensions, record)
        self.__record_cadence(extensions, record)

    def __record_heart_rate(self, extensions, record):
        if record.heart_rate is not None:
            hr = ET.SubElement(extensions, 'gpxtpx:hr')
            hr.text = str(record.heart_rate)

    def __record_cadence(self, extensions, record):
        if record.cadence is not None:
            cad = ET.SubElement(extensions, 'gpxtpx:cad')
            cad.text = str(record.cadence)

    def __pretty_print_xml(self, ugly_xml):
        return minidom.parseString(ugly_xml).toprettyxml(indent='  ')
