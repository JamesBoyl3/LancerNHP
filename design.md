[
# Lancer NHP Design

This document goes into detail on the design choices of the Lancer NHP.

## Agentic Environment

### Actions

The action list specifies every possible action and agent (player) can make. 

| Action ID | Action (human-readable) |
|-|-|
| 0 | Boost |
| 1 | Skirmish |
| 2 | Quick Tech |
| 3 | Invade |
| 4 | Lock on |
| 5 | Bolster |
| 6 | Scan |
| 7 | Ram |
| 8 | Grapple |
| 9 | Hide |
| 10 | Search |
| 11 | Activate System (Quick) | 
| 12 | Prepare |
| 13 | Eject | 
| 14 | Self-Destruct |
| 15 | Shut Down | 
| 16 | Barrage |
| 17 | Stabalise | 
| 18 | Full Tech |
| 19 | Disengage |
| 20 | Improvised attack |
| 21 | Activate Systems (Full) | 
| 22 | Boot Up |
| 23 | Mount |
| 24 | Dismount |
| 25 | Skill Check |
| 26 | Overcharge |
|| System specific free actions| (IMPLEMENTED LATER)
| 27 | Brace |
| 28 | Overwatch | 
| 29 | Preped Action |
|| System specific free actions| (IMPLEMENTED LATER)

*Note: The actions are grouped for efficient differention of quick-full-prepped-reactions*
*|||*
*|-|-|*
*| Quick Action | 0-15 |*
*| Full Action | |16-25|*
*| Free Action | 26 |*
*| Reaction | 27-30 |*

### Frame Tokens

Agents need data to operate on. The mech token has been designed to account for all the information they COULD get access to.

*Note: this is only defined for mechs as NHPs cannot engage in pilot-pilot combat. This may be changed later to represent mech-pilot combat.*

| Attribute index | Attribute |
| 0 | Structure |
| 1 | HP |
| 2 | Armour |
| 3 | Stress |
| 4 | Heat |
| 5 | Repair |
| 6 | Limited Bonus |
| 7 | Attack Bonus |
| 8 | Speed | 
| 9 | Evasion |
| 10 | Tech Attack |
| 11 | E-Defense |
| 12 | Sensors |
| 13 | Save | 

*Note: To improve performance the attributes will be scaled so that not one attibute dominate the networks predictions*

*Note: This will not always be visible to the NHP by masking the values (this is done as players do not have access to all this information all the time)*

### Gear Tokens

| Gear Index | Gear |
| 0 | Range |
| 1 | Damage |
| 2 | Damager type |
| 3 | Thermal type |

### System Tokens

*A list of every system in the game*

#### Mech Tokens

Mech tokens are a combination of the frame token, gear tokens, and system tokens. The flow can be found at (https://mermaid.ai/d/488da0b9-6dad-49d8-9d07-0d476dac13cf)

### Encoder Design

See [flow chart made on mermaid.ai](https://mermaid.ai/d/78d0cfce-9415-42dc-b488-4b8631a884a5)

## Agent (Neural Net) Design

