from typing import Any

from opensearchpy import OpenSearch


def create_opensearch_client(credentials: dict[str, Any]) -> OpenSearch:
    _e = credentials["endpoint"]
    endpoint = [i.strip() for i in _e.split(',') if i.strip()]

    user = credentials["user"]
    password = credentials["password"]

    client = OpenSearch(
        hosts=endpoint,
        http_compress=True,  # enables gzip compression for request bodies
        http_auth=(user, password),
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )
    return client