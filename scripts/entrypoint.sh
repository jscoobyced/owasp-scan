#!/bin/sh

python ./zapscan.py -k $ZAPAPIKEY -s "$ZAPSERVERNAME" -p 8080 -u "http://$APPSERVERNAME:$APPPORT" -r report