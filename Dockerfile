FROM python:2.7
WORKDIR /opt/owasp
COPY requirements.txt /opt/owasp
RUN pip install -r requirements.txt
RUN rm requirements.txt
COPY scripts /opt/owasp
RUN chmod u+x zapscan.py
RUN chmod u+x entrypoint.sh
ENTRYPOINT [ "/opt/owasp/entrypoint.sh" ]