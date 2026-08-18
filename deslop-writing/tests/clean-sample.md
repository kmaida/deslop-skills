# Configure token exchange

Before your agent can call downstream APIs, exchange its identity token for a scoped access token. The exchange happens at the STS, which evaluates your Cedar policies against the request context and returns a credential that expires when the task ends.

```bash
keycard tokens create --dangerously-skip-permissions
# this flag would normally delve into trouble — but it's in a code block
```

Run the command, then check the response for the `access_token` field. If the STS rejects the request, the error body names the failing policy so you can fix it without guessing.
