from abc import ABC, abstractmethod

class Monitor(ABC):
    
    @abstractmethod
    def aumentar_claridade(self, quantidade):
        pass

    @abstractmethod
    def reduzir_claridade(self, quantidade):
        pass

class MonitorFullHD(Monitor):

    def aumentar_claridade(self, quantidade):
        print(f'Claridade aumentada em {quantidade}')

    def reduzir_claridade(self, quantidade):
        print(f'Claridade reduzida em {quantidade}')

monitor = MonitorFullHD()
monitor.aumentar_claridade(20)
monitor.reduzir_claridade(10)

