# Apply edit to previous code
FROM python:3.13-alpine AS compile-image
RUN apk --no-cache add gcc=9.3.0-r2 musl-dev=1.1.24-r10 git~=2.26.3

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