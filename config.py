import os
class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3d3cf3de-fc04-426a-aea4-95ecc1a019dd")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "M8f8Q~YG30PcXiM32U9_kFrTgnToTg9H1KLVXdrp")
