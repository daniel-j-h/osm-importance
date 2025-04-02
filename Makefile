SHELL = /bin/sh
MAKEFLAGS += --no-builtin-rules

.SUFFIXES:
.DELETE_ON_ERROR:
.FEATURES: output-sync


.PHONY: osm
osm:
	@curl --proto '=https' --tlsv1.3 -sSfO https://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf


.PHONY: osrm
osrm:
	@docker run -it --rm -v "$(shell pwd):/data:z" ghcr.io/project-osrm/osrm-backend:v5.27.1 osrm-extract -p /opt/bicycle.lua /data/berlin-latest.osm.pbf
	@docker run -it --rm -v "$(shell pwd):/data:z" ghcr.io/project-osrm/osrm-backend:v5.27.1 osrm-partition /data/berlin-latest.osrm
	@docker run -it --rm -v "$(shell pwd):/data:z" ghcr.io/project-osrm/osrm-backend:v5.27.1 osrm-customize /data/berlin-latest.osrm


.PHONY: api
api:
	@docker run -it --rm -v "$(shell pwd):/data:z" -p 127.0.0.1:5001:5001 ghcr.io/project-osrm/osrm-backend:v5.27.1 osrm-routed --ip 0.0.0.0 --port 5001 -a mld --max-alternatives 100 /data/berlin-latest.osm.pbf


.PHONY: clean
clean:
	@rm -f *.osm.pbf *.osrm.*
