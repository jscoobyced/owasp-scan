# OWASP ZAP scanner for web-applications

This container can run a simple scan for OWASP Top 10 vulnerabilities using [OWASP ZAP](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project).

## How to use

Edit the sample [docker-compose.yml](docker-compose.yml):
- Uncomment one of line 4 **OR** 5 (not both, obviously) and set either your Dockerfile path or your container image name
- Uncomment lines 7 **AND** 8, and on line 8 set your web-application port
- On line 19, change (if needed) the URL port to match the port you enabled in step above.  
i.e. if you exposed port 8888, change the `-u "http://webapp:5000"` parameter to `-u "http://webapp:8888"`  
Do not change the `webapp` server name.

You will find the result of the scan in the created `report.html` in the same directory from which you run this command.

Then you're ready to issue the `docker-compose -f docker-compose.yml up` command.

Note this is currently a blocking command. You'll need to open a new Terminal or CMD/Powershell and issue a `docker-compose -f docker-compose.yml down` command in the same directory to stop it. I will eventually improve this to detect the scan is complete and shutdown the containers.

## Credits

This is highly copied and actualized to recent ZAP version from https://github.com/ritesh/dockerscan/.