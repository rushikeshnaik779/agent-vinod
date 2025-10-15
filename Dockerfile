# Use Debian Trixie (Debian 13)
FROM debian:trixie

ENV DEBIAN_FRONTEND=noninteractive

# Step 1: Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    locales \
    r-base \
    r-base-dev && \
    rm -rf /var/lib/apt/lists/*

# Step 2: Set locale
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Step 3: Verify R installation
RUN R --version

WORKDIR /usr/src/app
CMD ["R"]
