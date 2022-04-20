# ABM Framework
***

## Model Breakdown

There are three main components to the ABM:

- The grid (a custom object with an underlying 2D array)

- The environment cells (a custom object)

- The agents (a custom object)

### Grid Methods

- Initialization -> Requires width and height parameters

- get_agent(x, y) -> Returns a list of agents at argued coordinates

- get_cell(x, y) -> Returns the env_cell at the argued coordinates

- get_n_cells() -> Returns number of cells in the grid

- move_agent(agent, target_x, target_y) -> Moves argued agent to to target coordinates

- get_neighbors(agent, moore) -> Gets argued agents' neighbors. Defaults to von neumann unless moore is specified as True

- find(param, value) -> Finds a parameter and value in the grid, returns it

- find_at(param, value) -> Finds all parameters and values in the grid, returns them

- print_grid() -> Prints the grid in the terminal

- export_env_to_csv(iteration) -> Exports grid in current state to csv with filename ```output/environment/enviornment_(iteration)```

- export_agents_to_csv(iteration) -> Exports agents on grid in current state to csv with filename ```output/agents/agents_(iteration)```

- random_init(low_bound, up_bound) -> Randomly generates agent values on grid, one agent per cell

### Env_Cell Methods

- Initialization -> Requires coordinates and value parameters (Handled automatically in grid)

- get_value() -> Returns value of object

- get_agents() -> Returns agent present on top of cell

- add_value(amount) -> Adds argued value to object's value

- add_agent(agent) -> Adds an agent on top of cell

### Agent Methods

- Initialization -> Requires coordinates

- get_contents() -> Returns dictionary of contents

- get_contents_at(key) -> Returns value of key from contents dictionary

- set_contents(key, value) -> Adds or updates value in contents dictionary

- add_content(key, increase) -> Increases value at key in contents dictionary by increase parameter

- set_pos(new_x, new_y) -> Changes internal coordinates (NOTE: Does not update placement on grid)

- move_left() -> Change internal coordinates by one to the left

- move_right() -> Change internal coordinates by one to the right

- move_down() -> Change internal coordinates by one downwards

- move_up() -> Change internal coordinates by one upwards
