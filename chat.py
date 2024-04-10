#Framework Installation
#pip install flet

#Steps

# Chat Title
# Button - Start Chat
  # Popup - Welcoming to the Chat
    # Input - Name
    # Button - Sign in (navigation to chat page)

# Chat Page
  # Message - Successful Sign in
  # Input - Enter a Message
  # Button - Send Message

import flet as ft

def main(page):
  title = ft.Text("ABC Chat")

  user_name = ft.TextField(label="Enter your name")

  chat = ft.Column()

  def send_message_on_tunnel(infos):
    chat.controls.append(ft.Text(infos))
    page.update()

  page.pubsub.subscribe(send_message_on_tunnel)

  def send_message(event):
    text_chat_message = f"{user_name.value}: {chat_message.value}" 
    chat.controls.append(ft.Text(text_chat_message))
    page.pubsub.send_all(text_chat_message)
    chat_message.value = ""
    page.update()

  chat_message = ft.TextField(label="Enter a message")

  send_button = ft.ElevatedButton("Send", on_click = send_message)

  def sign_in(event):
    popup.open = False
    page.remove(start_button)
    page.add(chat)
    message_row = ft.Row([chat_message, send_button])
    page.add(message_row)
    success_message = f"{user_name.value} signed in!"
    page.pubsub.send_all(success_message)
    page.update()
    
  popup = ft.AlertDialog(
    open=False, 
    modal=True, 
    title=ft.Text("Welcome to ABC Chat!"),
    content=user_name,
    actions=[ft.ElevatedButton("Sign in", on_click=sign_in)]
    )
  
  def start_chat(event):
    page.dialog = popup
    popup.open = True
    page.update()

  start_button = ft.ElevatedButton("Start Chat", on_click = start_chat)
  
  page.add(title)
  page.add(start_button)
  
#ft.app(main)
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

# deploy 