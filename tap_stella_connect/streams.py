"""Stream type classes for tap-stella-connect."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_stella_connect.client import TapStellaConnectStream


class DataStream(TapStellaConnectStream):
    # Data Stream Schema Definition

    name = "data"
    path = "/data"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "request_created_at"

    schema = th.PropertiesList(
        th.Property("uuid", th.StringType),
        th.Property("sequence_id", th.IntegerType),
        th.Property("parent_uuid", th.StringType),
        th.Property("is_recovery", th.BooleanType),
        th.Property("branding", th.StringType),
        th.Property("channel", th.StringType),
        th.Property("ext_interaction_id", th.StringType),
        th.Property("external_url", th.StringType),
        th.Property("language", th.StringType),
        th.Property("survey_id", th.IntegerType),
        th.Property("survey_name", th.StringType),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("request_created_at", th.DateTimeType),
        th.Property("request_delivery_status", th.StringType),
        th.Property("request_sent_at", th.DateTimeType),
        th.Property("requested_via", th.StringType),
        th.Property("response_received_at", th.DateTimeType),
        th.Property("reward_eligible", th.BooleanType),
        th.Property("reward_name", th.StringType),
        th.Property("marketing", th.ObjectType(
            th.Property("custom_link_eligible", th.BooleanType),
            th.Property("custom_link_initiated", th.BooleanType),
            th.Property("facebook_follow_eligible", th.BooleanType),
            th.Property("facebook_follow_initiated", th.BooleanType),
            th.Property("facebook_share_eligible", th.BooleanType),
            th.Property("facebook_share_initiated", th.BooleanType),
            th.Property("twitter_follow_eligible", th.BooleanType),
            th.Property("twitter_follow_initiated", th.BooleanType),
            th.Property("twitter_share_eligible", th.BooleanType),
            th.Property("twitter_share_initiated", th.BooleanType),
        )),
        th.Property("employee", th.ObjectType(
            th.Property("custom_id", th.StringType),
            th.Property("email", th.StringType),
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
        )),
        th.Property("team_leader", th.ObjectType(
            th.Property("custom_id", th.StringType),
            th.Property("full_name", th.StringType),
        )),
        th.Property("customer", th.ObjectType(
            th.Property("custom_id", th.StringType),
            th.Property("email", th.StringType),
            th.Property("full_name", th.StringType),
        )),
        th.Property("custom_properties", th.CustomType({"type": ["object", "string", "integer"]})),
        th.Property("answers", th.CustomType({"type": ["object", "string", "integer"]})),
    ).to_dict()
