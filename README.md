# NO-IP DUC
A custom no-ip dynamic update client.

Because the official one is not working and you have to compile it.

## Docker build command
```bash
docker build -t noip-duc:latest .
```

## Environment variables
| Name | Description | Default |
| --- | --- | --- |
| WAIT_TIME | Time to wait between updates | 10 |
| DOMAIN | Domain to update | NONE |


## Mounts layout
| Host | Container | Description |
| --- | --- | --- |
| path-to-config-dir | /app/config | Configuration files |
| path-to-logs-dir | /app/logs | Logs directory |

## Example of `secrets.py` in config directory
```python
# no-ip credentials
username = 'your_username'
password = 'your_password'
```

## Docker run command
```bash
docker run -dit --name no-ip-duc \
    -v /path/to/config:/app/config \
    -v /path/to/logs:/app/logs \
    --network host \
    --restart unless-stopped \
    -e DOMAIN=your.domain.com \
    -e WAIT_TIME=10 \
    noip-duc:latest
```

