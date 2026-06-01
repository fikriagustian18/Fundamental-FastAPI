async def common_params(query: str = None, limit: int = 10):
    return { "query": query, "limit": limit }

async def form_data_params(username: str = None, password: str = None):
    return { "username": username, "password": password }