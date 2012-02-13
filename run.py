# enabel to run code in map-structure:
# >current map
#       - Domination-Game   [map]   - GIT-repository
#       - run.py            [file]  - this file
#       - agent.py          [file]  - Our agent
import os, sys
path, filename = os.path.split("../Domination-Game/domination")
sys.path.append(path)
defaultAgent = '../Domination-Game/domination/agent.py'

##### set agents
redAgent = 'agent.py'
blueAgent =  defaultAgent

##### code to run game
from domination import core, run

class MyScenario(run.Scenario):
    REPEATS = 10
    SETTINGS = core.Settings(max_steps=100)
MyScenario.test(redAgent, blueAgent)




