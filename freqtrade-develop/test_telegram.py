#!/usr/bin/env python3
"""
Script per testare le notifiche Telegram
"""

import requests
import json

def send_test_message(chat_id):
    token = '8496095334:AAF9xgtlI-hUAeTKnDFbybCHw1ds-QR-6zE'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    
    message = """
🤖 *FREQTRADE BOT ATTIVO*

✅ Bot di trading configurato correttamente
📊 Strategia: Strategy001
💰 Modalità: Dry Run (Test)
🔄 Timeframe: 5m
💵 Stake: 20 USDT per trade
📈 Max trades: 3

🎯 *Coppie monitorate:*
• BTC/USDT • ETH/USDT • BNB/USDT
• ADA/USDT • DOT/USDT • LINK/USDT
• LTC/USDT • XRP/USDT • SOL/USDT

🚀 *Il bot è pronto per iniziare!*
    """
    
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    
    try:
        response = requests.post(url, data=payload)
        result = response.json()
        
        if result['ok']:
            print("✅ Messaggio di test inviato con successo!")
            return True
        else:
            print(f"❌ Errore nell'invio: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Errore: {e}")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Uso: python3 test_telegram.py <chat_id>")
        print("Esempio: python3 test_telegram.py 123456789")
        sys.exit(1)
    
    chat_id = sys.argv[1]
    send_test_message(chat_id)