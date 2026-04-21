import simpy
import random
import matplotlib.pyplot as plt

# Параметри варіанту 12 (модифіковані)
ARRIVAL_RATE = 6  # Збільшено вдвічі
NUM_SERVERS = 75   # Для стаціонарного режиму
PROBABILITIES = {1: 0.7, 2: 0.3} # Типи сутностей
TIME_SERVICING = {1: 12.0, 2: 6.0}
MAX_WAIT_TIME = 50 # Обмеження часу очікування

time_stamps = []
length_queue = []

def entity(env, name, server, ent_type):
    arrival_time = env.now
    
    # Завдання 6: Обмеження часу очікування
    with server.request() as request:
        results = yield request | env.timeout(MAX_WAIT_TIME)
        
        if request in results:
            wait_time = env.now - arrival_time
            # Моделювання обслуговування
            service_time = random.expovariate(1.0 / TIME_SERVICING[ent_type])
            yield env.timeout(service_time)
        else:
            print(f"Сутність {name} (Тип {ent_type}) пішла через довге очікування")

def monitor(env, server):
    while True:
        time_stamps.append(env.now)
        length_queue.append(len(server.queue))
        yield env.timeout(1)

def arrival_generator(env, server):
    i = 0
    while True:
        yield env.timeout(random.expovariate(ARRIVAL_RATE))
        i += 1
        # Генерування типу сутності
        ent_type = random.choices(list(PROBABILITIES.keys()), weights=PROBABILITIES.values())[0]
        env.process(entity(env, i, server, ent_type))

env = simpy.Environment()
server = simpy.Resource(env, capacity=NUM_SERVERS)
env.process(arrival_generator(env, server))
env.process(monitor(env, server))
env.run(until=500)

# Візуалізація (Завдання 2.25-2.33)
plt.figure(figsize=(10, 5))
plt.plot(time_stamps, length_queue, label='Довжина черги')
plt.xlabel('Час (секунди)')
plt.ylabel('Довжина черги')
plt.title('Зміна довжини черги (Варіант 12, n=75)')
plt.grid()
plt.show()
