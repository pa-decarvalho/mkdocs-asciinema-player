FROM mcr.microsoft.com/devcontainers/python:3.12

ARG TASK_VERSION=3.45.4
ARG HADOLINT_VERSION=2.12.0

USER root

### Install dependencies ###
# hadolint ignore=DL3008
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

### Task (https://taskfile.dev/)
RUN wget -q -P /tmp https://github.com/go-task/task/releases/download/v$TASK_VERSION/task_linux_amd64.deb && \
    dpkg -i /tmp/task_linux_amd64.deb && \
    rm -f /tmp/task_linux_amd64.deb

### Chrome for SeleniumBase (https://seleniumbase.io/)
RUN apt-get update -y && apt-get upgrade -y && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || apt-get install --no-install-recommends -fy && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    rm google-chrome-stable_current_amd64.deb

### Install Hadolint (https://github.com/hadolint/hadolint)
RUN wget -q -P /tmp https://github.com/hadolint/hadolint/releases/download/v$HADOLINT_VERSION/hadolint-Linux-x86_64 && \
    mv /tmp/hadolint-Linux-x86_64 /usr/local/bin/hadolint && \
    chmod +x /usr/local/bin/hadolint

# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip poetry

USER vscode
