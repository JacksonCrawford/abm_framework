from model import SlimeModel

def main():
    model = SlimeModel(10, 10)

 
    counter = 0 
    for a in range(10):
        for b in range(50):
            model.step()
        model.export_env_to_csv(counter)
        model.export_agents_to_csv(counter)
        counter += 1

main()
