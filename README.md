# Simulation code of the assignment:

## Prerequisites <a name="prerequisites"></a>
- **Python 3.12**
- **Jupyter Notebook**

To run the code, install the following packages with their specified versions:
***
You have to install: 
1. **ipykernel**  
   ```bash
   pip install ipykernel==6.29.5
   ```
2. **numpy**  
   ```bash
   pip install numpy==2.3.1
   ```
3. **cvxpy**  
   ```bash
   pip install cvxpy
   ```
4. **matplotlib**  
   ```bash
   pip install matplotlib==3.10.3
   ```
4. **seaborn**  
   ```bash
   pip install seaborn==0.13.2
   ```

***
## Code Files

### 1. `grid_world.py`
**Description**:  
Contains the definition of the two Grid Worlds used in:
- Part 1 (Basic RL methods)
- Part 2 (Monte Carlo methods)

---

### 2. `Part1.ipynb`
**Description**:  
Implements value function estimation and optimal policy determination using different methods.

**Value Function Estimation**:
- Explicit Bellman method
- Iterative Bellman method (under a uniform random policy)

**Optimal Policy Determination**:
- Bellman optimality equation
- Policy iteration  
- Value iteration

---

### 3. `Part2.ipynb`  
**Description**:  
Uses Monte Carlo methods to learn an optimal policy.

**Methods Implemented**:
- Monte Carlo with Exploring Starts
- ε-Soft Approaches
- Behaviour Policy with Importance Sampling