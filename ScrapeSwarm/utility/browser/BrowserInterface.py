from abc import ABC, abstractmethod

class BrowserInterface(ABC):
    '''
    This abstract class contains methods related to Browser.
    '''

    @abstractmethod
    def get_browser(self):
        raise NotImplementedError("Select any browser before proceeding...")

    @abstractmethod
    def open_url(self, url: str):
        raise NotImplementedError("Method to open a given URL is not implemented")

    @abstractmethod
    def close_browser(self):
        raise NotImplementedError("Method to close the browser is not implemented")

    @abstractmethod
    def take_screenshot(self, file_path: str):
        raise NotImplementedError("Method to take a screenshot is not implemented")

    @abstractmethod
    def execute_script(self, script: str):
        raise NotImplementedError("Method to execute a JavaScript script is not implemented")
