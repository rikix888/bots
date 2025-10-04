#!/usr/bin/env python3
"""
Script per ottenere il chat_id di Telegram
Esegui questo script dopo aver scritto /start al bot
"""

import requests
import json

def get_chat_id():
    token = '8496095334:AAF9xgtlI-hUAeTKnDFbybCHw1ds-QR-6zE'
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['ok'] and data['result']:
            print("🔍 Messaggi trovati:")
            for update in data['result']:
                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    user_first_name = update['message']['from'].get('first_name', 'N/A')
                    user_username = update['message']['from'].get('username', 'N/A')
                    message_text = update['message'].get('text', 'N/A')
                    
                    print(f"\n📱 CHAT ID: {chat_id}")
                    print(f"👤 Nome: {user_first_name}")
                    print(f"🔗 Username: @{user_username}")
                    print(f"💬 Messaggio: {message_text}")
                    print("-" * 50)
                    
                    return chat_id
        else:
            print("❌ Nessun messaggio trovato.")
            print("🔔 Per favore:")
            print("1. Apri Telegram")
            print("2. Cerca @PARSIVAL07_bot")
            print("3. Scrivi /start")
            print("4. Riprova questo script")
            return None
            
    except Exception as e:
        print(f"❌ Errore: {e}")
        return None

if __name__ == "__main__":
    chat_id = get_chat_id()
    if chat_id:
        print(f"\n✅ Usa questo chat_id nella configurazione: {chat_id}")