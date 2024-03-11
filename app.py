from aiohttp import web
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    BotFrameworkAdapter,
)
from botbuilder.schema import Activity

from gbot import Gbot  # Ajusta la ruta de importación según tu estructura de proyecto

# Configura el bot
# APP_ID = '5e6f36ee-18d3-4d33-8f8f-4e08c5e1c977'  # Tu Microsoft App ID
# APP_PASSWORD = 'a97a69c7-98b6-4068-9b17-12444e73c867'  # Tu Microsoft App Password
APP_ID = ''  # Tu Microsoft App ID
APP_PASSWORD = ''  # Tu Microsoft App Password
SETTINGS = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)

# Crea la instancia de tu bot
GBOT = Gbot()

# Define el endpoint del bot
async def messages(req: web.Request) -> web.Response:
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return web.Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    try:
        await ADAPTER.process_activity(activity, auth_header, GBOT.on_turn)
        return web.Response(status=201)
    except Exception as e:
        raise e

APP = web.Application()
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    try:
        web.run_app(APP, host="10.112.254.84", port=3978)
    except Exception as e:
        raise e
