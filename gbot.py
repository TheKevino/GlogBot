from botbuilder.core import ActivityHandler, TurnContext, MessageFactory
from nlp.interpreter import Interpreter  # Ajusta la ruta de importación según tu estructura de proyecto

class Gbot(ActivityHandler):
    def __init__(self):
        self.interpreter = Interpreter()

    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text
        area = self.interpreter.interpret(user_input)

        if area is not None:
            response_message = f"Has sido enviado al área: {area}"
        else:
            response_message = "No se pudo determinar el área. Por favor, intenta ser más específico."
        
        await turn_context.send_activity(MessageFactory.text(response_message))
