""" Builder Pattern (create an object in multiple steps) """

MINI14 = '1.4GHz Mac mini'
"""
class AppleFactory:
    class MacMini14:
        def __init__(self) -> None:
            self.memory = 4
            self.hdd = 500
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = (f'Model: {MINI14}',
                    f'Memory: {self.memory}GB',
                    f'Hard Disk: {self.hdd}GB',
                    f'Graphics Card: {self.gpu}')
            return '\n'.join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            msg = f'{model} not found'
            print(msg)


if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)
"""

class Computer:
    def __init__(self, serial_number) -> None:
        self.serial_number = serial_number
        self.memory = 4
        self.hdd = 500
        self.gpu = 'Intel HD Graphics 5000'

    def __str__(self):
        info = (f'Model: {MINI14}',
                f'Memory: {self.memory}GB',
                f'Hard Disk: {self.hdd}GB',
                f'Graphics Card: {self.gpu}')
        return '\n'.join(info)

class ComputerBuilder:
    def __init__(self) -> None:
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount
    
    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self) -> None:
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (
            self.builder.configure_memory(memory),
            self.builder.configure_hdd(hdd),
            self.builder.configure_gpu(gpu)     
            )

        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, 
                                memory=8, 
                                gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print(computer)