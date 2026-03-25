#!/usr/bin/env python3
"""
Send Flava Pulse newsletter via Gmail SMTP.

Usage:
  python3 send-email.py \
    --from "dan@weapp.se" \
    --password "xxxx xxxx xxxx xxxx" \
    --to "boren@flavaapp.com,skantorp@flavaapp.com" \
    --edition "20260325-01" \
    --output-dir "./output"
"""

import argparse
import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime


def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def send_newsletter(sender, password, recipients, edition, output_dir):
    email_html_path = os.path.join(output_dir, f"flava-pulse-{edition}-email.html")
    pdf_path = os.path.join(output_dir, f"flava-pulse-{edition}.pdf")

    if not os.path.exists(email_html_path):
        print(f"Error: {email_html_path} not found")
        sys.exit(1)

    email_body = load_file(email_html_path)

    msg = MIMEMultipart("mixed")
    msg["From"] = f"Flava Pulse <{sender}>"
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = f"Flava Pulse — {datetime.now().strftime('%-d %B %Y').lower()}"
    msg["X-Priority"] = "3"

    html_part = MIMEText(email_body, "html", "utf-8")
    msg.attach(html_part)

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()
        pdf_attachment = MIMEApplication(pdf_data, _subtype="pdf")
        pdf_attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename=f"flava-pulse-{edition}.pdf",
        )
        msg.attach(pdf_attachment)
        print(f"PDF attached: {pdf_path} ({len(pdf_data) / 1024:.0f} KB)")
    else:
        print(f"Warning: {pdf_path} not found, sending without attachment")

    print(f"Connecting to smtp.gmail.com:465...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipients, msg.as_string())

    print(f"Sent to: {', '.join(recipients)}")
    print(f"From: {sender}")
    print(f"Edition: {edition}")
    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send Flava Pulse newsletter")
    parser.add_argument("--from", dest="sender", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--to", required=True, help="Comma-separated recipients")
    parser.add_argument("--edition", required=True)
    parser.add_argument("--output-dir", default="./output")
    args = parser.parse_args()

    recipients = [r.strip() for r in args.to.split(",")]
    send_newsletter(args.sender, args.password, recipients, args.edition, args.output_dir)
