# Pygame Spring Jam 2024
##  CONTROLS
    Hold F for a sawed-off shotgun effect/ flamethrower, shoots particles in a cone shape (0.02 damage per particle), drains mana
    Press SHIFT for a dodge - arrests your momentum and doubles fire rate until you move, invincibility for 0.25 seconds
    Hold LEFTCLICK for a generic bullet (deals 1 damage)
    Hold RIGHTCLICK for a bomb, releases particles on impact (deals 1 damage)
    Press R for a shockwave, stops any bullets and confuses enemies for 0.5 seconds. Costs 25 mana
    When you accumulate enough damage to switch, press Q

## MECHANICS
    This is a top-down shooter with endless waves.
    Aim using the mouse pointer.
    Enemies spawn based on the state you are in (either hot or cold)
    Your bullets change based on the state you are in.
    If the enemy and the bullets have different states, damage dealt is doubled.
    Combine a hot and cold particle to make steam - stuns enemies and makes them unable to move.
    Accumulate damage dealt to perform a switch in temperature - also grants a full heal.
    When wave increments, gain a full heal.

## UI 
    Every enemy has a healthbar above them.
    Your mana bar is below you - when it drops to 0 all spells are disabled and it regenerates back. When it is full spells are enabled.
    Dealt damage accumulated is displayed in the bar at the top right - when it is full a switch can be performed.




    
    