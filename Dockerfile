FROM python:3.13-alpine AS compile-image
RUN apk --no-cache add gcc musl-dev git

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