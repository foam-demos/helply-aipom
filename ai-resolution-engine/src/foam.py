import foam
from helply.config import FOAM_API_KEY, IS_PRODUCTION

foam.init(
    service_name="ai-resolution-engine",
    api_key=FOAM_API_KEY,
    environment="production" if IS_PRODUCTION else "development",
    enable_sql_instrumentation=True,
    enable_celery_instrumentation=True,
)