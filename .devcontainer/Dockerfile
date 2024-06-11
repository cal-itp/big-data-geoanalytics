FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    USER=calitp

RUN useradd --create-home --shell /bin/bash $USER && \
    chown -R $USER /home/$USER

USER $USER
ENV PATH "$PATH:/home/$USER/.local/bin"
WORKDIR /app/mkdocs

EXPOSE 8000

RUN python -m pip install --upgrade pip

COPY . .

RUN pip install -r docs/requirements.txt
RUN pip install pre-commit

# install pre-commit environments in throwaway Git repository
# https://stackoverflow.com/a/68758943
RUN git init . && \
    pre-commit install-hooks && \
    rm -rf .git

CMD ["sleep", "infinity"]
