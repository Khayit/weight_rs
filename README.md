# Weight API

FastAPI service for reading the current weight from scales over a serial port.

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy storage\.env.dist storage\.env
```

Edit `storage/.env`:

```dotenv
LOGIN="any"
PASSWORD="secret"
PORT=/dev/ttyUSB0
READ_TIMEOUT="3"
MINIMAL_WEIGHT=100
```

## Run

```bash
uvicorn main:app --app-dir src --host 0.0.0.0 --port 8000
```

## Get Weight

```bash
curl -u any:secret http://localhost:8000/weight
```

Response:

```json
{
  "ok": true,
  "weight": 1200,
  "stable": true
}
```
