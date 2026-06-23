import gymnasium as gym
from gymnasium import spaces
import numpy as np
from gymnasium.envs.registration import register

# so this is the environment for the Kaem Kaar backend simulator.
# I'm modeling the traffic as a stochastic process because real life is messy.
class KaemKaarEnv(gym.Env):
    metadata = {'render_modes': ['human']}

    def __init__(self):
        super(KaemKaarEnv, self).__init__()
        
        # Action space: 0=Do nothing, 1=Scale Up, 2=Scale Down, 3=Throttle
        self.action_space = spaces.Discrete(4)
        
        # State: [cpu_load, request_queue, active_nodes, time_of_day]
        # Using 0-100 for CPU, arbitrary units for queue, etc.
        self.observation_space = spaces.Box(
            low=0, high=100, shape=(4,), dtype=np.float32
        )
        
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        # Starting point: Low load, no queue, 1 node running.
        self.state = np.array([10.0, 0.0, 1.0, 0.0], dtype=np.float32)
        return self.state, {}

    def step(self, action):
        # Time passes (just incrementing the hour)
        self.state[3] = (self.state[3] + 0.1) % 24
        
        # Action logic - basically telling the infrastructure what to do
        if action == 1: 
            self.state[2] += 1 # Spin up a new container
        elif action == 2: 
            self.state[2] = max(1, self.state[2] - 1) # Kill a container
        elif action == 3:
            self.state[1] *= 0.5 # Throttling traffic (dumping requests)
        
        # Traffic spikes (Poisson arrival simulator)
        # If it's peak time, traffic is way higher
        traffic_intensity = 10 if 8 <= self.state[3] <= 20 else 2
        self.state[1] += np.random.poisson(traffic_intensity)
        
        # CPU load depends on requests / available nodes
        self.state[0] = min(100, (self.state[1] / (self.state[2] + 0.1)) * 5)
        
        # The Reward: Balancing speed vs. money. 
        # Latency is basically CPU load here.
        latency_penalty = self.state[0] * 0.5
        cost_penalty = self.state[2] * 2.0
        reward = -(latency_penalty + cost_penalty)
        
        # Keep it running until things explode (or just arbitrary truncation)
        terminated = False
        truncated = False
        
        return self.state, reward, terminated, truncated, {}

# Registering this so I can call it like gym.make('KaemKaar-v0')
register(
    id='KaemKaar-v0',
    entry_point='envs.env:KaemKaarEnv',
)