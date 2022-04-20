from model import SlimeModel

def main():
    model = SlimeModel(10, 10)

    n_steps = 5000
    n_writes = 10
 
    counter = 0 
    # Number of times you 
    for a in range(n_writes):
        for b in range(int(n_steps / n_writes)):
            model.step()
        model.export_env_to_csv(counter)
        model.export_agents_to_csv(counter)
        counter += 1

main()
