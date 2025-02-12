from datetime import datetime, timedelta

class Site:
    def __init__(self, site):
        self.site = site

    def get_site(self):
        return self.site

    def set_site(self, site):
        self.site = site

class Cookie(Site):
    def __init__(self, site, data, duration_minutes):
        super().__init__(site)
        self.data = data
        self.creation_time = datetime.now()
        self.expiry_time = self.creation_time + timedelta(minutes=duration_minutes)

    def is_expired(self):
        return datetime.now() > self.expiry_time

    def __repr__(self):
        return f"Cookie(site={self.site}, data={self.data}, creation_time={self.creation_time}, expiry_time={self.expiry_time})"
    
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_creation_time(self):
        return self.creation_time

    def set_creation_time(self, creation_time):
        self.creation_time = creation_time
        self.expiry_time = self.creation_time + timedelta(minutes=(self.expiry_time - self.creation_time).total_seconds() / 60)

    def get_expiry_time(self):
        return self.expiry_time

    def set_expiry_time(self, expiry_time):
        self.expiry_time = expiry_time

    @staticmethod
    def get_valid_cookies(cookies, site_id=None):
        """
        Get valid cookies from the list of cookies.

        This method filters out expired cookies and, if a site_id is provided, 
        it also filters cookies that belong to the specified site.

        Args:
            cookies (list): A list of cookie objects.
            site_id (str, optional): The site ID to filter cookies by. Defaults to None.

        Returns:
            list: A list of valid cookie objects.
        """
        if site_id:
            return [cookie for cookie in cookies if not cookie.is_expired() and cookie.get_site() == site_id]
        return [cookie for cookie in cookies if not cookie.is_expired()]