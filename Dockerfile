FROM python:3.13-alpine AS compile-image
RUN apk --no-cache add gcc=14.2.0-r6 musl-dev=1.2.5-r10 git=2.49.1-r0

# Set up virtual environment and path (activate)
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
WORKDIR /usr/src/app
COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.13-alpine AS build-image
COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /usr/src/app
COPY ./app/ .
CMD [ "python", "./app.py" ]