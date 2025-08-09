# fit2gpx

Convert Garmin `.fit` files to `.gpx`, preserving location, time, altitude, heart rate and cadence (extensions)

## Install

From source:

    git clone https://github.com/agorf/fit2gpx.git
    cd fit2gpx
    python -m venv .venv
    source .venv/bin/activate
    pip install .

Note: Requires Python ≥ 3.8. Dependencies (installed automatically): `fitdecode`, `geopy`.

## Usage

Convert one or more `.fit` files. Each `.gpx` is written next to its input file (same basename):

    fit2gpx activity1.fit activity2.fit

Example output:

    activity1.fit -> activity1.gpx
    activity2.fit -> activity2.gpx

If a file has no track data, you’ll see:

    activity.fit -> no data

## License

[MIT](https://github.com/agorf/fit2gpx/blob/main/LICENSE)

## Author

[Angelos Orfanakos](https://angelos.dev/)
