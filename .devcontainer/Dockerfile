FROM mcr.microsoft.com/devcontainers/python:3.12

ARG TASK_VERSION=3.41.0

USER root

### Task (https://taskfile.dev/) ###
RUN wget -q -P /tmp https://github.com/go-task/task/releases/download/v$TASK_VERSION/task_linux_amd64.deb && \
    dpkg -i /tmp/task_linux_amd64.deb && \
    rm -f /tmp/task_linux_amd64.deb

### Chrome for SeleniumBase (https://seleniumbase.io/)
RUN apt-get update -y && apt-get upgrade -y && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || apt-get install --no-install-recommends -fy && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    rm google-chrome-stable_current_amd64.deb

RUN pip install --upgrade pip poetry

USER vscode
