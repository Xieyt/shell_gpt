from .app import main as main
from .app import entry_point as cli  # noqa: F401

import warnings
warnings.filterwarnings("ignore", category=UserWarning,
module="pydantic._internal._config")
