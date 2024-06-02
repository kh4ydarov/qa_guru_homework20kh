import os
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene_in_action import utils
from pydantic import BaseModel


class Config(BaseModel):
    context: str
    remote_url: str = os.getenv('REMOTE_URL')
    device_name: str = os.getenv('DEVICE_NAME')
    appName: str = os.getenv('APP_NAME')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    app_bstack: str = os.getenv('APP')
    platformName: str = os.getenv('PLATFORM_NAME')
    platformVersion: str = os.getenv('PLATFORM_VERSION')
    load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env'))
    userName: str = os.getenv('USER_NAME')
    accessKey: str = os.getenv('ACCESS_KEY')
    app_local: str = os.getenv('APP_LOCAL')
    udid: str = os.getenv('UDID')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local_emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app_local', self.app_local)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_bstack)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Test_Wiki',
                    'buildName': 'Test_Wiki',
                    'sessionName': 'Test_Wiki',
                    'userName': self.userName,
                    'accessKey': self.accessKey,
                },
            )

        return options


config = Config(context="local_emulator")
