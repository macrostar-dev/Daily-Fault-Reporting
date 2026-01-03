import requests

def enviar_mensaje(WEBEX_TOKEN =str,WEBEX_ROOM_ID =str, mensaje=str):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "roomId": WEBEX_ROOM_ID,
        "text": mensaje
    }

    resp = requests.post(url, headers=headers, json=data)

    if resp.status_code == 200:
        print("✅ Mensaje enviado correctamente.")
    else:
        print("❌ Error al enviar mensaje:")
        print(resp.status_code, resp.text)

