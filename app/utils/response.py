def success_response(data=None, message="success"):
    return {"status": "success", "message": message, "data": data}

def error_response(message="error"):
    return {"status": "error", "message": message}
