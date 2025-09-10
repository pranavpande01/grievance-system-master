from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import datetime, subprocess



search_tool=DuckDuckGoSearchRun()

@tool
def delay(seconds: int):
    """
    Delay execution for a specified number of seconds.
    """
    import time
    time.sleep(seconds)
@tool
def date():
    """
    Get the current date and time
    """
    return datetime.datetime.now().isoformat()

@tool
def console(command: str) -> dict:
    """
    Run a console command and return the output and error messages.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10  # Optional: prevent long-hanging processes
        )
        return {
            "command": command,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    except subprocess.TimeoutExpired:
        return {"error": "Command timed out"}
    except Exception as e:
        return {"error": str(e)}
@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}
        
        return {"first_num": first_num, "second_num": second_num, "operation": operation, "result": result}
    except Exception as e:
        return {"error": str(e)}
