from app.debugger import debug_challenge

if __name__ == "__main__":
    print("AI Debugging Challenge Simulator")
    buggy_code = input("Paste buggy code below:\n")
    report = debug_challenge(buggy_code)
    print("\nDebug Report:")
    print(report)
