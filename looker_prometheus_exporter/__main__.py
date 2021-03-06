import os
import logging

from prometheus_client import start_http_server

from looker_prometheus_exporter.looker_metric_fetcher import LookerMetricFetcher

if __name__ == '__main__':
    client_id = os.getenv("LOOKER_CLIENT_ID")
    client_secret = os.getenv("LOOKER_CLIENT_SECRET")
    dashboard_id = os.getenv("LOOKER_DASHBOARD_ID")
    looker_base_url = os.getenv("LOOKER_BASE_URL")
    port = int(os.getenv("LOOKER_EXPORTER_PORT", 8000))

    lmf = LookerMetricFetcher(
        client_id=client_id, client_secret=client_secret, looker_base_url=looker_base_url, dashboard_id=dashboard_id
    )

    logging.info("Starting Prometheus server on port {}".format(port))
    start_http_server(port)

    logging.info("Starting to fetch Looker performance data")
    lmf.observe()
