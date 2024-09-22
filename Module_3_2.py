def send_email(message, recipient, *, sender = "univercity.help@gmail.com"):
    message = input("Enter your message to recipient & press Enter button: ")
    recipient = input("Enter recipients e-mail & press Enter button: ")
    if recipient.find('@') == -1 or sender.find('@') == -1 or recipient.endswith(('.com', '.ru', '.net')) == False or sender.endswith(('.com', '.ru', '.net')) == False:
        print(f"Unable to send e-mail from {sender} to {recipient}")
    elif sender == recipient:
        print("Unable to send e-mail to yourself")
    elif sender == "univercity.help@gmail.com":
        print(f"The e-mail has been successfully sent from {sender} to {recipient}")
    elif sender != "univercity.help@gmail.com":
        print(f"Non-standart sender! The e-mail has been successfully sent from {sender} to {recipient}")

choose_sender = input("Enter 'yes' if use default sender or Enter 'no' to use another senders e-mail: ")
if choose_sender == "no":
    send_email("", "", sender = input("Enter new senders e-mail & press Enter button: "))
else:
    send_email("", "",)