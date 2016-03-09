#!/bin/bash
python ../lib/city_bike_stream.py | python ../lib/monitor_stream.py | python ../lib/delta.py & python ../lib/moving_avg.py & python ../lib/delete_stale_data.py