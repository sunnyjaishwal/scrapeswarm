import random
import json
from urllib.parse import urlparse

class AntiBot:
    def __init__(self, config_path='configs/user_agents.json'):
        with open(config_path, 'r') as f:
            self.user_agents = json.load(f)
    
    def get_random_user_agent(self, os_type=None):
        """
        Get a random user agent, optionally filtered by OS type
        """
        if os_type:
            filtered_agents = [ua for ua in self.user_agents if os_type.lower() in ua.lower()]
            return random.choice(filtered_agents) if filtered_agents else random.choice(self.user_agents)
        return random.choice(self.user_agents)
    
    def rotate_user_agent(self, request):
        """
        Rotate user agent for a request
        """
        request.headers['User-Agent'] = self.get_random_user_agent()
        return request
    
    def handle_captcha(self, response):
        """
        Basic captcha detection and handling mechanism
        """
        if 'captcha' in response.body.decode().lower():
            # Implement captcha solving logic or skip
            return None
        return response

class ProxyManager:
    def __init__(self, config_path='configs/proxies.json'):
        with open(config_path, 'r') as f:
            self.proxies = json.load(f)
        
    def get_random_proxy(self):
        """
        Get a random proxy from the pool or from the json file
        """
        return random.choice(self.proxies) if self.proxies else None
    
    def validate_proxy(self, proxy):
        """
        Basic proxy validation
        """
        try:
            parsed = urlparse(proxy)
            return all([parsed.scheme, parsed.netloc])
        except Exception:
            return False