# Raspberry Pi systemd service

Create a service file:

```bash
sudo nano /etc/systemd/system/weight_rs.service
```

Example service:

```ini
[Unit]
Description=Weight API
After=network.target

[Service]
WorkingDirectory=/project_path
ExecStart=/project_path/venv/bin/uvicorn main:app --app-dir src --host 0.0.0.0 --port 8000
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Replace `/project_path` with the real project path.

Enable and start:

```bash
sudo systemctl enable weight_rs.service
sudo systemctl start weight_rs.service
```

Useful commands:

```bash
sudo systemctl status weight_rs.service
sudo journalctl -u weight_rs.service
sudo systemctl restart weight_rs.service
sudo systemctl stop weight_rs.service
```
