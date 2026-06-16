async def common_params(query: str, limit: int):
    return { "query": query, "limit": limit }

async def form_data_params(username: str, password: str):
    return { "username": username, "password": password }