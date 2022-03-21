import environment

def main():
#   Create an environment grid
    board = environment.grid(10, 10)

    board.export_env_to_csv(0)
    board.random_init(0, 9)

# Print the grid
#    board.print_grid()

#   Get an agent
    agent = board.get_agent(2, 2)
    agent = agent[0]
# Move that agent
    board.move_agent(agent, 1, 1)

#   Export agents' values to a csv
    board.export_agents_to_csv(0)

    griditer = iter(board)
#    print(next(myiter)[0].get_contents_at("value"))
 
    for x in range(board.size):
        agents = next(griditer)
        for ag in agents:
            print(ag.get_contents_at("value"), end=" ")
        print("")
       
    print(board.find("value", 2))

    print(board.find_all("value", 2))
#   Method to get neighbors from an agent  
#    print(board.get_neighbors(agent, False)) 

main()
