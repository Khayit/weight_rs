from secrets import compare_digest

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from conf import conf


app = FastAPI(title="Weight API")
security = HTTPBasic()


def require_auth(credentials: HTTPBasicCredentials = Depends(security)) -> None:
    valid_login = compare_digest(credentials.username, conf.login or "")
    valid_password = compare_digest(credentials.password, conf.password or "")

    if not (valid_login and valid_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.get("/weight", dependencies=[Depends(require_auth)])
def get_weight() -> dict[str, int | bool]:
    try:
        weight = conf.meter.read_weight(timeout=conf.read_timeout)
    except Exception as e:
        conf.logger.write_log("Error get data from scales", e=e, tb=True)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Can not read weight from scales",
        ) from e

    return {
        "ok": True,
        "weight": weight,
        "stable": weight > conf.minimal_weight,
    }
