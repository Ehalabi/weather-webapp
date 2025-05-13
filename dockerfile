FROM python:3.12-slim AS compile-image

COPY web_app_project/ /app
WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r project_board/requirements.txt

FROM python:3.12-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv
COPY --from=compile-image /app /app

WORKDIR /app/project_board

ENV PATH="/opt/venv/bin:$PATH"
ENV BG_COLOR="#f0f8ff"

EXPOSE 8000

ENTRYPOINT ["python3", "pages.py"]
