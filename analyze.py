#!/usr/bin/env python3

import sys
import csv

import osmium


# https://docs.osmcode.org/pyosmium/latest/
class Handler(osmium.SimpleHandler):
    def __init__(self, segments):
        super().__init__()
        self.segments = segments

    def way(self, w):
        if w.is_closed():
            return

        if not "highway" in w.tags:
            return

        noderefs = list(w.nodes)

        segments = [(noderefs[i].ref, noderefs[i + 1].ref)
                    for i in range(len(noderefs) - 1)]

        if not any(segment in self.segments for segment in segments):
            return

        wid = w.positive_id()

        if "surface" not in w.tags:
            print(f"https://www.openstreetmap.org/way/{wid}")


def main():
    if len(sys.argv) != 3:
        sys.exit(f"{sys.argv[0]} map.osm.pbf importance.csv")

    segments = set()

    with open(sys.argv[2]) as f:
        reader = csv.reader(f)

        for row in reader:
            segment = (int(row[0]), int(row[1]))
            segments.add(segment)

    handler = Handler(segments)
    handler.apply_file(sys.argv[1])


if __name__ == "__main__":
    main()
