# OpenStreetMap Importance Heuristic

This repository is a quick and dirty proof of concept for a goal directed OpenStreetMap completion priorization.

In [this](https://media.ccc.de/v/fossgis2025-58025-openstreetmap-ist-doch-vollstandig) FOSSGIS 2025 Michael Reichert talked about how complete OpenStreetMap is and how to figure out where to go and what to map.

Instead of querying e.g. for surface tags randomly here I suggest using a routing engine based heuristic to find ways of high importance missing e.g. surface tags.

Here is how it works
1. We use a routing engine and do random queries, e.g. between cities or from one end of a city to the other end of a city
2. We count how often shortest paths go over specific ways, or rather pairs of OpenStreetMap nodes
3. We can now sort that list of ways or node pairs and rank it, as a heuristic of how important they are
4. We check if these ways all have surface tags, prioritizing top to bottom for highest impact

I don't know if anyone has done this before, this idea just came to me watching the talk and wondering if there are heuristics to prioritize by.


## Usage

Download OpenStreetMap .osm.pbf dataset

    make osm

Make it routable with the Open Source Routing Machine

    make osrm

Start up the routing API

    make api



## Note on alternative routes

Alternative routes are an amazing tool and often under-appreciated.
Specifically the `alternatives=n` feature [we implemented](https://www.openstreetmap.org/user/daniel-j-h/diary/44020) is very powerful for use cases.
For example: Generate many (tens, hundreds) plausible alternative routes, then post-process them based on domain-specific or real-time data, and then return a subset to the user.

You find this technique applicable in many domains
- In delivery-like use cases where breaks and delivery times and other real time data come into play to optimize ETAs
- In outdoor use cases where you could post-process many alternatives to rank them based on land use, think nature or forests


## License

Copyright © 2025 Daniel J. H.

Distributed under the MIT License (MIT).
