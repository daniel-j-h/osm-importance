#!/usr/bin/env python3

import sys
import json
import math
import string
import random
import urllib.request
import collections


API = string.Template("http://127.0.0.1:5001/route/v1/biking/$locations?overview=false&generate_hints=false&alternatives=$alternatives&annotations=nodes")


# point moving on a circle around a location with a radius in km
def point_on_circle(location, radius, ratio):
    assert radius > 0
    assert 0 <= ratio <= 1

    EARTH_MEAN_RADIUS = 6371.004

    lng = math.radians(location[0])
    lat = math.radians(location[1])

    angle = ratio * 2 * math.pi

    offset = radius / EARTH_MEAN_RADIUS

    lng = lng + math.atan2(math.sin(angle) * math.sin(offset) * math.cos(lat),
                           math.cos(offset) - math.sin(lat) * math.sin(lat))

    lat = math.asin(math.sin(lat) * math.cos(offset) +
                    math.cos(lat) * math.sin(offset) * math.cos(angle))

    return math.degrees(lng), math.degrees(lat)


# two opposing points moving on a circle around a location with a radius in km
def points_on_circle(location, radius, ratio):
    source = point_on_circle(location, radius, ratio)
    target = point_on_circle(location, radius, (ratio + 0.5) % 1.0)
    return source, target


def main():
    berlin = 13.394, 52.515

    counts = collections.Counter()

    n = 1000

    for i in range(n):
        source, target = points_on_circle(berlin, radius=15, ratio=(i / n))

        locations = f"{source[0]},{source[1]};{target[0]},{target[1]}"

        url = API.substitute(locations=locations, alternatives=10)

        # Note: does not support keep-alive, ineff. but fine for now
        with urllib.request.urlopen(url) as f:
            if f.status != 200:
                continue

            body = f.read()
            res = json.loads(body)

            if res["code"].lower() != "ok":
                continue

            for routes in res["routes"]:
                leg = routes["legs"][0]
                annotation = leg["annotation"]
                nodes = annotation["nodes"]

                for (a, b) in zip(nodes, nodes[1:]):
                    counts[(a, b)] += 1

    for (a, b), count in counts.most_common(10000):
        print(f"{a},{b},{count}")


if __name__ == "__main__":
    main()
