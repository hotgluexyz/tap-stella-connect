"""TapStellaConnect tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_stella_connect import streams


class TapTapStellaConnect(Tap):
    """TapStellaConnect tap class."""

    name = "tap-stella-connect"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_secret",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="Project IDs to replicate",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync")
    ).to_dict()

    def discover_streams(self) -> list[streams.TapStellaConnectStream]:
        return [
            streams.DataStream(self)
        ]


if __name__ == "__main__":
    TapTapStellaConnect.cli()
