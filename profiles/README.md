This is the bike profile where we remove surface tags from influencing routing.
The idea is that we ultimately want to find missing surface tags, therefore surface tags must not influence the routing heuristic.

You can get the bike profile either from upstream or you can copy it from the docker container.
In both cases make sure the version matches to the routing engine version.

Check out the profile at

```
621:    -- compute speed taking into account way type, maxspeed tags, etc.
622:    --WayHandlers.surface,
```

where we comment out surface handling.
