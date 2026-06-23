import matplotlib.pyplot as plt

def plot_training_results(rewards):
    """Plots the episode rewards over time."""
    plt.figure(figsize=(10, 5))
    plt.plot(rewards)
    plt.title("Agent Training Progress: Episode Rewards")
    plt.xlabel("Episode")
    plt.ylabel("Mean Reward")
    plt.grid(True)
    plt.savefig("results/training_progress.png")
    print("Graph saved to results/training_progress.png")