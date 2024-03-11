from .receiving import ReceivingCommand
from .auto import AutomotiveCommand
from .industrial import IndustrialCommand
from .shipping import ShippingCommand
from .end import EndCommand

class CommandHandler:
    def __init__(self):
        self.commands = {
            'Receiving': ReceivingCommand(),
            'Automotive': AutomotiveCommand(),
            'Industrial': IndustrialCommand(),
            'Shipping': ShippingCommand(),
            'End': EndCommand()
        }

    def handle_command(self, command_key, *args, **kwargs):
        command = self.commands.get(command_key)
        if command:
            return command.execute(*args, **kwargs)
        else:
            return "Comando no reconocido."