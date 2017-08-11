#!/bin/bash

tshark -l -i enp0s3 -T fields -E separator=" " -e ip.src -e frame.time_epoch -c 15 dst host 10.0.2.15 | python3 sql_common.py
