from __future__ import annotations

import sys
import jwt
from datetime import datetime
from typing import Any, Iterable

import requests
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


if sys.version_info >= (3, 8):
    from functools import cached_property
else:
    from cached_property import cached_property



class TapStellaConnectStream(RESTStream):
    """TapStellaConnect stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://api.stellaconnect.net/v2"

    records_jsonpath = "$[*]"  

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Any:
       
        next_page_token = None
        data = response.json()
        if len(data)>0:
            #Pagination is calculated by sequence_id
            next_page_token = data[-1].get("sequence_id")

        return next_page_token

    @property
    def http_headers(self) -> dict:
        headers = {}

        #make the JWT for process
        # timestamp = datetime.now()
        # iat = datetime.fromtimestamp(timestamp, timezone.utc)
        jwt_to_use = jwt.encode({"iss": "Hotglue Tap", "iat": datetime.now()}, self.config['api_secret'], algorithm="HS256")

        headers["Authorization"] = jwt_to_use
        headers["x-api-key"] = self.config["api_key"]
        
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        else:
            headers["User-Agent"] = "hotglue_dummy_agent"
        return headers
    
    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ANN401
    ):

        params: dict = {}
        if self.replication_key:
            params['created_at_gte'] = self.config['start_date']
        params["limit"] = self._page_size
        if next_page_token:
            params['after'] = next_page_token
        return params

