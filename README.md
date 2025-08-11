# fit2gpx

Convert Garmin `.fit` files to `.gpx`

Features:

- Support bulk-conversion (one or more files)
- Preserve location (latitude, longitude), time and altitude
- Preserve heart rate and cadence extensions
- Name GPX file to follow Garmin's original naming of `<time>-<location>-<activity_type>.gpx`

## Install

Get the source:

    git clone https://github.com/agorf/fit2gpx.git
    cd fit2gpx

Install it in your machine:

    python -m venv .venv
    source .venv/bin/activate
    pip install .

Note: Requires Python ≥ 3.8. Dependencies (installed automatically): `fitdecode`, `geopy`.

You can also use Docker:

    docker build -t fit2gpx .

See _Usage_ section on how to run it with Docker.

## Usage

Convert a single file in the current directory:

    fit2gpx 19608508047_ACTIVITY.fit

Example output:

    19608508047_ACTIVITY.fit -> 2025-07-02T04:39:39+00:00-argithea-mountaineering.gpx

Note: Each `.gpx` file is written under the same directory as its corresponding `.fit` file.

With Docker:

    docker run --rm -v .:/work fit2gpx 19608508047_ACTIVITY.fit

Convert all files in the current directory:

    fit2gpx *.fit

With Docker:

    docker run --rm -v .:/work fit2gpx *.fit

## License

[MIT](https://github.com/agorf/fit2gpx/blob/main/LICENSE)

## Author

[Angelos Orfanakos](https://angelos.dev/)
