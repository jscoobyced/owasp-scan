#!/usr/bin/env python

import time
import sys
import getopt
from zapv2 import ZAPv2


def usage():
    print 'Usage:'
    print sys.argv[0] + \
        ' -k <key> -u <base_url> [-s <server>] [-p <port>] [-r <filename>]'
    print 'Where: '
    print '<key> is the ZAP API key. Required.'
    print '<base_url> is the root URL to crawl. Example: "https://www.example.org:8080". Required.'
    print '<server> is the servername or IP address on which ZAP is running. Optional. Defaults to localhost.'
    print '<port> is the port on which ZAP is running. Optional. Defaults to 8080.'
    print '<filename> is the path of the HTML report to be created. Optional. Defaults to None.'


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "k:u:s:p:r:")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    apikey = None
    url = None
    server = "localhost"
    port = 8080
    report = None
    required = [0, 0]
    for o, a in opts:
        if o == "-k":
            apikey = a
            required[0] = 1
        elif o == "-u":
            url = a
            required[1] = 1
        elif o == "-s":
            server = a
        elif o == "-p":
            port = a
        elif o == "-r":
            report = a.replace(".", "").replace("/", "")
        else:
            assert False, "Unexpected option."
    if required[0] == 0 or required[1] == 0:
        print 'Missing required arguments.'
        usage()
        sys.exit(2)
    runscan(apikey, url, server, port, report)


def runscan(api, target, zap, port, report):
    zap = ZAPv2(apikey=api,
                proxies={'http': 'http://' + zap + ':' + str(port)})

    print 'Accessing target %s' % target
    zap.urlopen(target)
    time.sleep(2)

    print 'Spidering target %s' % target
    scanid = zap.spider.scan(target, subtreeonly=False,
                             recurse=True, apikey=api)
    time.sleep(2)

    while (int(zap.spider.status(scanid)) < 100):
        print 'Spider progress %: ' + zap.spider.status(scanid)
        time.sleep(2)

    print 'Spider completed'

    while (int(zap.pscan.records_to_scan) > 0):
        print ('Records to passive scan : ' + zap.pscan.records_to_scan)
        time.sleep(2)
    print ('Passive scanning complete')

    print ('Scanning target ' + target)
    ascan_id = zap.ascan.scan(target)
    while (int(zap.ascan.status(ascan_id)) < 100):
        print ('Scan progress %: ' + zap.ascan.status(ascan_id))
        time.sleep(5)
    print ('Scan completed')

    print ('Hosts: ' + ', '.join(zap.core.hosts))
    print ('Sites: ' + ', '.join(zap.core.sites))
    print ('URLs: ')
    for url in zap.core.urls():
        print(url)

    print ('Alerts: ')
    for alert in zap.core.alerts():
        print(alert['alert'] + ', risk: ' + alert['risk'])

    if report != None:
        f = open(report + '.html', 'w')
        f.write(zap.core.htmlreport(apikey=api))
        f.close()


if __name__ == "__main__":
    main()
exit()
