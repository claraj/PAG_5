FROM python:3.7.0-alpine

# For generating JUnit-style reports
RUN pip install unittest-xml-reporting==2.2.0

WORKDIR /usr/src/myapp

CMD ["python", "./test_runner.py"]