Retries the upload. Gives up after 5 tries. Returns the last error.

Previously this used a fixed delay. For now the backoff is linear.
