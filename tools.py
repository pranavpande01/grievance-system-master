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

@tool
def send_email(to, subject, body):
    """
    Sends a plain text email using STARTTLS via Gmail SMTP.

    Args:
        to (str): Recipient's email address.
        subject (str): Subject line of the email.
        body (str): Plain text body content of the email.

    Note:
        This function uses Gmail's SMTP server (smtp.gmail.com:587).
    """


    import smtplib,os
    from email.message import EmailMessage

    user = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASS']

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to
    msg.set_content(body)
    print("sending email...")
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)

@tool
def mail_secratary(subject,body):
    """
    Sends an email to Mr. Pankaj's personal secretary, mrs. neha.
    This function composes and sends an email with the specified subject and message
    to Mr. Pankaj's personal secretary, who knows all his schedules, appointments,  meetings and whereabouts.

    The AI should pass to this function:
    1. Generated subject
    2. Generated body

    """
    #send_email(t"f20212785@pilani.bits-pilani.ac.in",subject,body)
    
