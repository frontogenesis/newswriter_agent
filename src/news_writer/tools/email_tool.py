from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import smtplib
from email.mime.text import MIMEText
import os

class EmailToolInput(BaseModel):
    """Input schema for EmailTool."""
    to_email: str = Field(..., description="Email address of the recipient")
    subject: str = Field(..., description="Subject of the email")
    body: str = Field(..., description="Content/body of the email")

class EmailTool(BaseTool):
    name: str = "Email Sender"
    description: str = (
        "A tool to send emails to specified recipients. Requires the following arguments: "
        "to_email (recipient's email address), subject (email subject), and body (email content)."
    )
    args_schema: Type[BaseModel] = EmailToolInput

    def _run(self, to_email: str, subject: str, body: str) -> str:
        try:
            # Get email credentials from environment variables
            smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
            smtp_port = int(os.getenv("SMTP_PORT", "465"))
            sender_email = os.getenv("SENDER_EMAIL")
            sender_password = os.getenv("SENDER_PASSWORD")

            if not all([sender_email, sender_password]):
                return "Error: Email credentials not found in environment variables"

            # Create message
            message = MIMEText(body, "html")
            message["From"] = f"Ray Hawthorne <{sender_email}>"
            message["To"] = to_email
            message["Subject"] = subject

            # Create SMTP session
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(sender_email, sender_password)
                server.send_message(message)

            return f"Email successfully sent to {to_email}"
            
        except Exception as e:
            return f"Failed to send email: {str(e)}" 