from abc import ABC, abstractmethod

class BrowserInterface(ABC):
    """
    BrowserInterface is an abstract base class that defines the interface for browser-related operations.
    Methods
    -------
    get_browser():
        Abstract method to get the browser instance. Must be implemented by subclasses.
    open_url(url: str):
        Abstract method to open a given URL in the browser. Must be implemented by subclasses.
    close_browser():
        Abstract method to close the browser. Must be implemented by subclasses.
    take_screenshot(file_path: str):
        Abstract method to take a screenshot of the current browser window and save it to the specified file path. Must be implemented by subclasses.
    execute_script(script: str):
        Abstract method to execute a JavaScript script in the context of the current browser window. Must be implemented by subclasses.
    """
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
