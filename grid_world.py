import numpy as np

def find_grid_position(arr, tar):
    """ 
    function used to find the row and column of an element in the 2d matrix (only for searching unique element)
    Input:
        arr (2d array) - the Gridworld map
        tar (char) - character needed to be found, e.g., 'R'
    Output:
        (i, row.index(tar)) - row and column of the input character on the map
    """
    try:
        for i, row in enumerate(arr):
            if tar in row:
                return (i, row.index(tar)) # return the index of the row (i) and column (row.index(tar))
    except ValueError:
        raise ValueError("Invalid Grid Value!") # if not found, raise the error
        

# Grid World Definition for Part 1
class Grid_1:

    def __init__(self):
        # set up parameters
        self.number_of_rows = 5
        self.number_of_columns = 5
        self.number_of_states = self.number_of_rows * self.number_of_columns
        self.number_of_actions = 4

        # Actions that agent can take
        #                      left      down      right     up
        self.action =       [ [0, -1],  [1, 0],   [0, 1],   [-1, 0]]
        self.action_text =  ['←', '↓', '→', '↑']

        # Gridworld map
        #             0   1   2   3   4
        self.map = [['W','B','W','W','G'], # 0          map[0][4] = 'G'
                    ['W','W','W','W','W'], # 1
                    ['W','W','W','W','W'], # 2      
                    ['W','W','R','W','W'], # 3          map[3][2] = 'R'
                    ['W','W','W','W','Y']] # 4

        '''
        Moddel structure: number of states by number of actions by n by 4 array
        For one state s and action a, there are n possibilities for transiting to different next state s_,
        each grid position composed of (p, s_, r, t):
            p  - transition probability from (s,a) to (s_)
            s_ - next state
            r  - reward of the transition from (s,a) to (s_)
            t  - terminal information, a bool value, True/False
        The model is used to store the transition probabilities, next states, rewards, and terminal states
        for each state-action pair.
        '''
        self.model = [[[] for _ in range(self.number_of_actions)] for _ in range(self.number_of_states)]
        for s in range(self.number_of_states):
            for a in range(self.number_of_actions):
                # Calculate the place on the grid based on the number of the state
                row, col = np.divmod(s,self.number_of_rows)
                # Determine the action to be taken
                act = self.action[a]
                # Calculate the new positions after taking the action
                row_, col_ = row + act[0], col + act[1]
                # Calculate the new state number based on the new positions
                state_ = row_ * self.number_of_rows + col_

                # White, Red, Yellow Sate Dynamics
                # if the current state is White, Red, or Yellow
                if self.map[row][col] == 'W' or self.map[row][col] == 'R' or self.map[row][col] == 'Y':
                    # if the new position is out of the grid, stay in the same state and get -0.5 reward
                    if (row_ < 0) or (col_ < 0) or (row_ > self.number_of_rows - 1) or (col_ > self.number_of_columns - 1):
                        self.model[s][a].append([1.0, s, -0.5])
                    # if the new state is terminal state, stay in the same state and get 0 reward
                    else:
                        self.model[s][a].append([1.0, state_, 0.0])

                # Blue Sate Dynamics
                elif self.map[row][col] == 'B':
                    # If the current state is Blue, jump to Red
                    row_, col_ = find_grid_position(self.map, 'R')
                    # Calculate the state number based on the place on the map
                    state_ = row_ * self.number_of_rows + col_
                    # Append the transition to the model with a probability of 1.0 and a reward of 5.0
                    self.model[s][a].append([1.0, state_, 5.0])

                # Green Sate Dynamics
                elif self.map[row][col] == 'G':  # if G, jump to R or Y
                    # If the current state is Green, jump to Red or Yellow
                    row_, col_ = find_grid_position(self.map, 'R')
                    # Calculate the state number based on the place on the map
                    state_ = row_ * self.number_of_rows + col_
                    # Append the transition to the model with a probability of 0.5 and a reward of 2.5
                    self.model[s][a].append([0.5, state_, 2.5])
                    # If the current state is Green, jump to Yellow
                    row_, col_ = find_grid_position(self.map, 'Y')
                    # Calculate the  state number based on the place on the map
                    state_ = row_ * self.number_of_rows + col_
                    # Append the transition to the model with a probability of 0.5 and a reward of 2.5
                    self.model[s][a].append([0.5, state_, 2.5])

                else:
                    raise ValueError("Invalid map value!")



# Grid World Definition for Part 2
class Grid_2:

    def __init__(self):
        # set up parameters
        self.number_of_rows = 5
        self.number_of_columns = 5
        self.number_of_states = self.number_of_rows * self.number_of_columns
        self.number_of_actions = 4

        # Actions that agent can take
        self.action =       [ [0, -1],  [1, 0],   [0, 1],   [-1, 0]]
        self.action_text =  ['←', '↓', '→', '↑']

        # Gridworld map
        #             0   1   2   3   4
        self.map = [['W','B','W','W','G'], # 0          map[0][4] = 'G'
                    ['W','W','W','W','W'], # 1
                    ['T','W','W','W','T'], # 2      
                    ['W','W','W','W','W'], # 3
                    ['T','W','R','W','Y']] # 4          map[4][2] = 'R'
        
        
        '''
        Moddel structure: number of states by number of actions by n by 4 array
        For one state s and action a, there are n possibilities for transiting to different next state s_,
        each grid position composed of (p, s_, r, t):
            p  - transition probability from (s,a) to (s_)   ### sum of the n p equals 1
            s_ - next state
            r  - reward of the transition from (s,a) to (s_)
            t  - terminal information, a bool value, True/False
        The model is used to store the transition probabilities, next states, rewards, and terminal states
        for each state-action pair.
        '''
        self.model = [[[] for _ in range(self.number_of_actions)] for _ in range(self.number_of_states)]
        for s in range(self.number_of_states):
            for a in range(self.number_of_actions):
                # Calculate the place on the grid based on the number of the state
                row, col = np.divmod(s,self.number_of_rows)
                # Determine the action to be taken
                act = self.action[a]
                # Calculate the new positions after taking the action
                row_, col_ = row + act[0], col + act[1]
                # Calculate the new state number based on the new positions
                state_ = row_ * self.number_of_rows + col_

                # Blue State Dynamics
                if self.map[row][col] == 'B':
                    # If the current state is Blue, jump to Red
                    row_, col_ = find_grid_position(self.map, 'R')
                    # Calculate the state number based on the place on the map
                    state_ = row_ * self.number_of_rows + col_
                    # Append the transition to the model with a probability of 1.0 and a reward of 5.0
                    self.model[s][a].append([1.0, state_, 5.0, False])

                # Green State Dynamics
                elif self.map[row][col] == 'G':
                    # If the current state is Green, jump to Red or Yellow
                    row_, col_ = find_grid_position(self.map, 'R')
                    # Calculate the state number based on the place on the map
                    state_ = row_ * self.number_of_rows + col_
                    # Append the transition to the model with a probability of 0.5 and a reward of 2.5
                    self.model[s][a].append([0.5, state_, 2.5, False])
                    # If the current state is Green, jump to Yellow
                    row_, col_ = find_grid_position(self.map, 'Y')
                    # Calculate the state number based on the place on the map
                    state_ = row_ * self.number_of_rows + col_
                    # Append the transition to the model with a probability of 0.5 and a reward of 2.5
                    self.model[s][a].append([0.5, state_, 2.5, False])

                # White, Red, Yellow Sate Dynamics
                elif self.map[row][col] == 'W' or self.map[row][col] == 'R' or self.map[row][col] == 'Y':
                    if (row_ < 0) or (col_ < 0) or (row_ > self.number_of_rows - 1) or (col_ > self.number_of_columns - 1):
                        # if the new position is out of the grid, stay in the same state and get -0.5 reward
                        self.model[s][a].append([1.0, s, -0.5, False])
                    # if the new state is terminal state, stay in the same state and get 0 reward
                    elif self.map[row_][col_] == 'T':
                        self.model[s][a].append([1.0, state_, 0.0, True])
                    # otherwise, stay in the new state and get -0.2 reward
                    else:
                        self.model[s][a].append([1.0, state_, -0.2, False])

                # Terminal (Black) State Dynamics
                elif self.map[row][col] == 'T':
                    # If the current state is Terminal, stay in the same state and get 0 reward
                    self.model[s][a].append([1.0, s, 0.0, True])

                else:
                    raise ValueError("Invalid map value!")