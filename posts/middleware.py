import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

class SentryAPIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        sentry_sdk.init(
            dsn="https://56201d8459e4d0503ac2a9ac474887ae@o4506044240560128.ingest.sentry.io/4506044242460672",
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            traces_sample_rate=1.0,
            # Set profiles_sample_rate to 1.0 to profile 100%
            # of sampled transactions.
            # We recommend adjusting this value in production.
            profiles_sample_rate=1.0,
            )

    def __call__(self, request):
        # Process request if needed
        response = self.get_response(request)
        # Process response
        self.capture_api_logs(request, response)
        return response

    def capture_api_logs(self, request, response):
        # Capture logs for API requests
        if request.path.startswith('/api/'):
            data = {
                'method': request.method,
                'path': request.path,
                'status_code': response.status_code,
            }

            if response.status_code >= 400:
                sentry_sdk.capture_message(f"API Request Error: {data}")
            else:
                sentry_sdk.capture_message(f"API Request Success: {data}")

