from os.path import basename
from sys import argv

import fitdecode

from .fit_data import FitData
from .gpx_generator import GpxGenerator

class FitConverter:
    def __init__(self, fit_path):
        self.fit_path = fit_path

    def convert(self):
        with fitdecode.FitReader(self.fit_path) as fit:
            print(f"{self.fit_path} -> ", end='')

            data = FitData(fit)

            if data.records:
                with open(self.__gpx_filename(data), 'w') as f:
                    creator = f"{basename(argv[0])} {basename(self.fit_path)}"
                    activity_name = f"{data.area} {data.sport}"
                    f.write(GpxGenerator(data.records, creator, activity_name).to_xml())
                    print(f.name)
            else:
                print('no data')

    def __gpx_filename(self, data):
        return f"{data.timestamp.isoformat()}-{self.__slugify(data.area)}-{data.sport.lower()}.gpx"

    def __slugify(self, text):
        text = text.lower().replace(' ', '_')

        # Convert Greek to Greeklish
        trans_table = str.maketrans('αάβγδεέζηήιίϊΐκλμνοόπρσςτυύϋΰφχωώ', 'aavgdeeziiiiiiklmnooprsstyyyyfxoo')
        slug = text.translate(trans_table).replace('θ', 'th').replace('ξ', 'ks').replace('ψ', 'ps')

        return slug

