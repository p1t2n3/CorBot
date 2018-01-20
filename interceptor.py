"""
This inline script can be used to dump flows as HAR files.
"""


import json
import base64
import zlib
import os

from datetime import datetime
from datetime import timezone

import mitmproxy

from mitmproxy import version
from mitmproxy import ctx
from mitmproxy.utils import strutils
from mitmproxy.net.http import cookies

# global env
currentCookies = []

# A list of server seen till now is maintained so we can avoid
# using 'connect' time for entries that use an existing connection.
SERVERS_SEEN = set()


def load(l):
    l.add_option(
        "hardump", str, "", "HAR dump path.",
    )





def response(flow):
    """
       Called when a server response has been received.
    """
    # Response body size and encoding
    #main variable
    response_body = flow.response.content
    url = flow.request.url
    current_cookies = format_request_cookies(flow.request.cookies.fields)
    print("Current response value:")
    if('getFieldBossHelpRequests' in url):
        # Renew cookies everytime load list
        currentCookies = current_cookies

        # print(response_body)
        print(url)
        print(current_cookies)




def format_cookies(cookie_list):
    rv = []

    for name, value, attrs in cookie_list:
        cookie_har = {
            "name": name,
            "value": value,
        }

        # HAR only needs some attributes
        for key in ["path", "domain", "comment"]:
            if key in attrs:
                cookie_har[key] = attrs[key]

        # These keys need to be boolean!
        for key in ["httpOnly", "secure"]:
            cookie_har[key] = bool(key in attrs)

        # Expiration time needs to be formatted
        expire_ts = cookies.get_expiration_ts(attrs)
        if expire_ts is not None:
            cookie_har["expires"] = datetime.fromtimestamp(expire_ts, timezone.utc).isoformat()

        rv.append(cookie_har)

    return rv


def format_request_cookies(fields):
    return format_cookies(cookies.group_cookies(fields))


def format_response_cookies(fields):
    return format_cookies((c[0], c[1][0], c[1][1]) for c in fields)


def name_value(obj):
    """
        Convert (key, value) pairs to HAR format.
    """
    return [{"name": k, "value": v} for k, v in obj.items()]
