import traceback

def debug_challenge(code: str) -> str:
    try:
        # Use exec to simulate running buggy code
        exec(code, {})
        return "Code executed without errors."
    except Exception as e:
        # Capture and format error traceback
        return "Error Detected:\n" + traceback.format_exc()
