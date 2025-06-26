from openai import OpenAI
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

sender_email = os.getenv("EMAIL_SENDER")
sender_password = os.getenv("EMAIL_PASSWORD")
sender_name = os.getenv("SENDER_NAME") or "AI Agent"


def email_content_generator(recipient_email, context):
    """Generate email body and subject using GPT"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that writes professional emails. You will generate the subject line and email body based on the context provided."},
            {"role": "user", "content": f"Generate an email (subject + content only) for {recipient_email} with the following context: {context} and send using the following as sender name: {sender_name}"}
        ]
    )
    content = response.choices[0].message.content.strip()

    if "Subject:" in content:
        subject_line = content.split("Subject:")[1].splitlines()[0].strip()
        body = "\n".join(content.splitlines()[1:]).strip()
    else:
        subject_line = "No Subject"
        body = content
    return subject_line, body


def email_editor_agent(original_email, edit_instruction):
    """Regenerate email body with user instruction"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that edits emails based on user instructions."},
            {"role": "user", "content": f"Original email:\n{original_email}"},
            {"role": "user", "content": f"Edit the above email to: {edit_instruction}"}
        ]
    )
    return response.choices[0].message.content.strip()


def validate_multiple_emails(raw_input):
    """Validate and split multiple comma-separated emails"""
    emails = [email.strip() for email in raw_input.split(',') if email.strip()]
    valid = []
    for email in emails:
        try:
            valid.append(validate_email(email).email)
        except EmailNotValidError:
            print(f"[WARNING] Invalid email skipped: {email}")
    return valid


def send_email(to_emails, cc_emails, bcc_emails, subject, body):
    msg = EmailMessage()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = ", ".join(to_emails)
    if cc_emails:
        msg['Cc'] = ", ".join(cc_emails)
    msg['Subject'] = subject
    msg.set_content(body)

    recipients = to_emails + cc_emails + bcc_emails

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg, from_addr=sender_email, to_addrs=recipients)
            print(f"[SUCCESS] Email sent to: {', '.join(to_emails)}")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")


def email_sending_agent():
    to_raw = input("Enter recipient email(s) (comma-separated): ")
    cc_raw = input("Enter CC email(s) (optional, comma-separated): ")
    bcc_raw = input("Enter BCC email(s) (optional, comma-separated): ")

    context = input("Enter the context of the email: ")

    to_emails = validate_multiple_emails(to_raw)
    cc_emails = validate_multiple_emails(cc_raw)
    bcc_emails = validate_multiple_emails(bcc_raw)

    if not to_emails:
        print("[ERROR] No valid recipient emails.")
        return

    subject, body = email_content_generator(to_emails[0], context)

    while True:
        print("\nGenerated Email:")
        print(f"\nSubject: {subject}\n")
        print(body)

        decision = input("\nDo you want to (s)end, (e)dit, or (c)ancel? [s/e/c]: ").strip().lower()

        if decision == 's':
            send_email(to_emails, cc_emails, bcc_emails, subject, body)
            break
        elif decision == 'e':
            instruction = input("What would you like to change? (e.g., make it more formal): ")
            body = email_editor_agent(body, instruction)
        elif decision == 'c':
            print("[CANCELLED] Email not sent.")
            break
        else:
            print("Invalid option. Please choose s, e, or c.")


if __name__ == "__main__":
    email_sending_agent()
