import sys
import json
import string
import random
import urllib.request
import collections


API = string.Template("http://127.0.0.1:5001/route/v1/biking/$locations?overview=false&generate_hints=false&alternatives=$alternatives&annotations=nodes")


def main():
    random.seed(1186293367)

    # hard coded for berlin, we make random west -> east
    # routing requests for now only, please extend this
    n, e, s, w = 52.5543, 13.5663, 52.4326, 13.235956

    counts = collections.Counter()

    for _ in range(100):
         source = w, random.uniform(s, n)
         target = e, random.uniform(s, n)

         locations = f"{source[0]},{source[1]};{target[0]},{target[1]}"

         url = API.substitute(locations=locations, alternatives=10)

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

                 for node in nodes:
                     counts[node] += 1

    for node, count in counts.most_common(100):
        print(f"{node},{count}")


if __name__ == "__main__":
    main()
