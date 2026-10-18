# Project Summary: Metropolis Command Core

**Project Name:** Metropolis Command Core (Smart City Dashboard)  
**Built For:** Cognizant – IIIT Raichur AI Hackathon  

---

## 1. The Big Problem We Are Solving

Imagine a heavy storm hits a city. Lightning strikes a power station, and the power goes out. Because the power is out, the city's water pumps stop working. Because the pumps stop, a major road tunnel floods. Because the tunnel is flooded, a massive traffic jam happens. Finally, an ambulance gets stuck in that traffic jam. 

This is called a **domino effect**. 

In the real world, cities struggle to handle domino effects because every department works in its own bubble. The Power Company, the Water Department, the Traffic Police, and the Hospitals all have their own separate computer screens. When a disaster happens, human operators have to make frantic phone calls to figure out what is going on. It is too slow, and mistakes happen.

## 2. Our Solution: A Smart City Brain

We built the **Metropolis Command Core**. It is a single, smart computer system that watches over the whole city. 

Instead of using just one AI that might get confused by too much information, we built a team of **37 different AI assistants** that talk to each other instantly. Using Cognizant's Neuro AI tools, we organized these AI assistants into a strict chain of command, just like a real-life emergency response team.

### How the AI Team is Organized (The 3 Levels)

We split our 37 AI assistants into three levels so they stay focused and don't get overwhelmed:

**Level 1: The Chief Commander (1 AI)**
This is the "Boss." When you type a problem into the computer (like "There is a flood in Zone C"), you are talking to the Commander. The Commander doesn't guess the details; it figures out which departments need to be involved and gives them orders.

**Level 2: The Department Heads (12 AIs)**
These AIs act like city managers. We have one for Traffic, one for Power, one for Water, one for Emergency Services, and so on. When the Commander gives an order, the Department Head figures out what their specific team needs to do.

**Level 3: The Field Workers (24 AIs)**
These are the experts on the ground. Every Department Head manages two specific workers. For example, the Traffic Head manages one AI that checks stoplights and another AI that reroutes buses. These worker AIs look at the actual numbers—like water depth, traffic speed, or power levels—and report back to their boss.

## 3. How the System Makes Smart Decisions

To make sure the AIs work together perfectly, we gave them two very important rules:

### Rule 1: Catch the Domino Effect
The system is programmed to know how the city connects. If the weather AI reports heavy rain, the system automatically warns the water AI to check the drains, and the traffic AI to watch out for flooded roads. It sees the big picture.

### Rule 2: Strict Priorities (Who Wins an Argument?)
Sometimes, two departments want the same thing. For example, the Traffic AI might want to use a bridge to fix a traffic jam, but the Emergency AI needs that same bridge cleared for an ambulance. We programmed the system with a strict priority list:

1. **Life Safety comes first** (Ambulances, hospitals, rescues).
2. **Critical Infrastructure is second** (Power grids, water supply).
3. **Traffic is third** (Keeping cars moving).
4. **Citizen Convenience is last** (Fixing potholes, garbage collection).

Because of this rule, the AI will always stop regular traffic to let the ambulance through without hesitation.

## 4. A Standard City Map

If you have 37 AIs talking to each other, they need to look at the same map. We built a standard digital map with 6 zones (Zone A to Zone F). Everyone uses the exact same names. If the Power AI says "Substation 4 in Zone B is down," the Water AI instantly knows that its pumps in that same area are in trouble. 

## 5. What the System Actually Outputs

When an emergency happens, the Chief Commander AI finishes gathering all the reports and gives the human operator two things:

1. **A Simple Written Report:** A very clear, bulleted summary telling the mayor or city manager exactly what happened, what the domino effects are, and an action plan on how to fix it with time estimates.
2. **Dashboard Data (JSON Code):** A block of perfectly formatted computer data that automatically updates the visual dials, maps, and warning lights on the city's command center screens. 

**In short:** We built a highly organized team of AI agents that can see a city's problems, stop disasters from spreading, and make life-saving decisions in seconds.