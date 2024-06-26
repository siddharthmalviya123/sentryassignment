import sentry_sdk

sentry_sdk.init(
    dsn="https://53ec36894cbd28d92c5397edafce2eb9@o4507496060813312.ingest.us.sentry.io/4507496484110336",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

def example_function():
    try:
        #causing the exeption by our own
        1 / 0
    except Exception as e:
        #exceptional handling
        capture_exception(e)


example_function()

