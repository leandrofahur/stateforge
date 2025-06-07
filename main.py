from transitions import Machine

class TraffiqLight:
    states = ['green', 'yellow', 'red']
    transitions = [{
        'trigger': 'go',
        'source': 'red',
        'dest': 'green'
    }, {
        'trigger': 'prepare_to_stop',
        'source': 'green',
        'dest': 'yellow'
    }, {
        'trigger': 'stop',
        'source': 'yellow',
        'dest': 'red'
    }]

    def __init__(self):
        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial='red')



traffiq = TraffiqLight()
print(traffiq)
traffiq.go()
print(f"After go(): {traffiq.state}")
traffiq.prepare_to_stop()
print(f"After prepare_to_stop(): {traffiq.state}")
traffiq.stop()
print(f"After stop(): {traffiq.state}")

print('State: ', traffiq.state)





