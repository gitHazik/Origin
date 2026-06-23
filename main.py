import gymnasium as gym
import envs.env  # This triggers the registration logic in env.py
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from utils.visualizer import plot_training_results
import os

# Create results directory if it doesn't exist
os.makedirs("results", exist_ok=True)
os.makedirs("models", exist_ok=True)

def train_and_visualize():
    # 1. Initialize and wrap the environment for monitoring[cite: 1]
    env = gym.make('KaemKaar-v0')
    env = Monitor(env)

    # 2. Instantiate the agent using PPO[cite: 1]
    # MlpPolicy is standard for this type of observation space[cite: 1]
    model = PPO("MlpPolicy", env, verbose=1)

    # 3. Train the agent[cite: 1]
    print("Training the Kaem Kaar scheduler...")
    model.learn(total_timesteps=10000)
    
    # 4. Save the brain for later use[cite: 1]
    model.save("models/kaem_agent")
    print("Model saved to models/kaem_agent")

    # 5. Extract rewards and visualize[cite: 1]
    rewards = env.get_episode_rewards()
    plot_training_results(rewards)

if __name__ == "__main__":
    train_and_visualize()