# OpenStreetMap Importance Heuristic

This repository is a proof of concept for a goal directed OpenStreetMap completion heuristic.

In [this](https://media.ccc.de/v/fossgis2025-58025-openstreetmap-ist-doch-vollstandig) FOSSGIS 2025 talk Michael Reichert showed how complete OpenStreetMap is and how to figure out where to go and what to map best.
Instead of querying e.g. for surface tags randomly here I suggest using a routing engine based heuristic to find ways of high importance missing e.g. surface tags.

Here is how it works
1. We use a routing engine and do queries, e.g. between cities or from one end of a city to the other
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

From here on use the Python scripts to run shortest path queries and to analyze.


## Note on Alternative Routes

Alternative routes are an amazing tool and often under-appreciated.
We use alternative routes in this project to generate many reasonable alternatives people might use when navigating e.g. within a city.

The `alternatives=n` feature [we implemented](https://www.openstreetmap.org/user/daniel-j-h/diary/44020) is very powerful for these use cases.
For example: Generate many (tens, hundreds) plausible alternative routes, then post-process them based on domain-specific or real-time data, and then return a subset to the user.

You find this technique applicable in many domains
- Post-process many alternatives to adjust ETAs with real-time or domain specific information
- Post-process many alternatives to rank them based on variety, land use e.g. percentage of forest paths


## License

Copyright © 2025 Daniel J. H.

Distributed under the MIT License (MIT).
