import time
import logging
from collections import deque
from . import constants as const

class RateLimiter:
    def __init__(self):
        self.requests = deque(maxlen=const.MAX_REQUESTS_PER_MINUTE)
        self.logger = logging.getLogger('RateLimiter')

    def wait_if_needed(self):
        """
        Check if we need to wait before making another request to avoid rate limiting
        """
        now = time.time()
        
        # Remove requests older than the window
        while self.requests and self.requests[0] < now - const.REQUEST_WINDOW:
            self.requests.popleft()
        
        # If we've made maximum requests within the window, wait
        if len(self.requests) >= const.MAX_REQUESTS_PER_MINUTE:
            wait_time = self.requests[0] + const.REQUEST_WINDOW - now
            if wait_time > 0:
                self.logger.info(f'Rate limit reached. Waiting {wait_time:.2f} seconds...')
                time.sleep(wait_time)
        
        # Add small delay between requests regardless
        time.sleep(const.RATE_LIMIT_DELAY)
        
        # Record this request
        self.requests.append(now)

    def clear_history(self):
        """Clear request history"""
        self.requests.clear()