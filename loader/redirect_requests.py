from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host == "https://assets.checkra.in":
        flow.request.host = "http://192.168.1.89"
