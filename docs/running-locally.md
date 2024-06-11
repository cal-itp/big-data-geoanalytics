# Running locally

Requires [Docker](https://docs.docker.com/get-docker/). The following commands
should be entered and run in a terminal program like `bash`.

## Clone the repository

```bash
git clone https://github.com/cal-itp/mkdocs-template
cd mkdocs-template
```

## Build the image

```bash
docker build -t mkdocs-template -f .devcontainer/Dockerfile .
```

## Run a container

```bash
docker run -p 8000:8000 mkdocs-template
```

The site should be available at <http://localhost:8000>.

## VS Code Devcontainer

This repository comes with a [VS Code Devcontainers](https://code.visualstudio.com/docs/remote/containers) configuration.

Once you clone the repository locally, simply open it within VS Code, which will
prompt you to re-open the repository within the Devcontainer.

Once the Devcontainer is running, bring up the Command Palette and enter:

```console
> Tasks: Run Build Task
```

To build the site and launch a local server. The site is running on <http://localhost> at a randomly assigned port; see the
VS Code `Ports` tab for information.
