import simpy
import random
import numpy as np
import matplotlib.pyplot as plt

# Параметри
RANDOM_SEED = 42
LAMBDA = 2.5
N_ENTITY = 100

random.seed(RANDOM_SEED)

# Статистика
waiting_times = []
service_times = []
system_times = []

queue_lengths = {1: [], 2: [], 3: []}
queue_times = {1: [], 2: [], 3: []}

resource_busy_time = [0, 0, 0]

# Сутність
def entity(env, name, priority, resources):
    arrival_time = env.now

    for i, res in enumerate(resources):
        # Фіксуємо довжину черги
        queue_lengths[i+1].append(len(res.queue))
        queue_times[i+1].append(env.now)

        wait_start = env.now

        with res.request(priority=priority) as request:
            yield request

            # Час очікування
            waiting_times.append(env.now - wait_start)

            # Час обслуговування залежить від пріоритету
            if priority == 1:
                duration = random.uniform(2, 4)
            elif priority == 2:
                duration = random.uniform(3, 5)
            else:
                duration = random.uniform(4, 6)

            yield env.timeout(duration)

            service_times.append(duration)
            resource_busy_time[i] += duration

    system_times.append(env.now - arrival_time)

# Генератор заявок
def arrival_generator(env, resources):
    for i in range(N_ENTITY):
        yield env.timeout(random.expovariate(LAMBDA))

        priority = random.choices([1, 2, 3], weights=[0.3, 0.4, 0.3])[0]
        env.process(entity(env, f"Ent_{i}", priority, resources))

# Запуск моделювання
env = simpy.Environment()

resources = [
    simpy.PriorityResource(env, capacity=2),
    simpy.PriorityResource(env, capacity=3),
    simpy.PriorityResource(env, capacity=2)
]

env.process(arrival_generator(env, resources))
env.run()

# Метрики
avg_wait = np.mean(waiting_times)
avg_system = np.mean(system_times)
avg_service = np.mean(service_times)
throughput = N_ENTITY / env.now

total_capacity = sum([2, 3, 2])
utilization = sum(resource_busy_time) / (env.now * total_capacity)

# Вивід результатів
print("=== РЕЗУЛЬТАТИ ===")
print(f"Середній час очікування: {avg_wait:.2f}")
print(f"Середній час у системі: {avg_system:.2f}")
print(f"Середній час обслуговування: {avg_service:.2f}")
print(f"Пропускна здатність: {throughput:.2f}")
print(f"Завантаження системи: {utilization:.2f}")

# Графіки

# 1. Waiting time
plt.figure()
plt.hist(waiting_times, bins=20)
plt.title("Розподіл часу очікування")
plt.xlabel("Час")
plt.ylabel("Кількість")
plt.show()

# 2. System time
plt.figure()
plt.hist(system_times, bins=20)
plt.title("Розподіл часу в системі")
plt.xlabel("Час")
plt.ylabel("Кількість")
plt.show()

# 3. Queue lengths
plt.figure()
for i in range(1, 4):
    plt.plot(queue_times[i], queue_lengths[i], label=f"Фаза {i}")

plt.title("Довжина черги по фазах")
plt.xlabel("Час")
plt.ylabel("Довжина черги")
plt.legend()
plt.show()
