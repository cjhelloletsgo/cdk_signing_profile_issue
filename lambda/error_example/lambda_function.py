import json
import logging
from typing import Any

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: dict[str, Any], _context: Any):
    """Lambda handler"""
    logger.info("event: %s ", json.dumps(event))
    
    # Test change
