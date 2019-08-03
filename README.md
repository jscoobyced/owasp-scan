# OWASP ZAP scanner for web-applications

This container can run a simple scan for OWASP Top 10 vulnerabilities using [OWASP ZAP](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project).

## How to use

Edit the sample [docker-compose.yml](docker-compose.yml):
- Uncomment one of line 5 **OR** 6 (not both, obviously) and set either your Dockerfile path or your container image name
- Uncomment lines 7 **AND** 8, and on line 8 set your web-application port
- On line 24, change (if needed) the application port to match the port you enabled in step above.  
i.e. if you exposed port 8888, change the `- APPPORT=5000` environment variable to `- APPPORT=8888`  
Do not change the `webapp` server name.

You will find the result of the scan in the created `report.html` in the same directory from which you run this command.

Then you're ready to issue the `docker-compose -f docker-compose.yml up` command.

## Credits

This is highly copied and actualized to recent ZAP version from https://github.com/ritesh/dockerscan/.