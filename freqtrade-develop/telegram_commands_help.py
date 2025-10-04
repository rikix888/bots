"""
🤖 COMANDI TELEGRAM DISPONIBILI PER IL BOT FREQTRADE

Una volta configurato il chat_id, potrai usare questi comandi:

📊 INFORMAZIONI:
/status - Stato attuale del bot e trades aperti
/profit - Profitti totali e statistiche
/balance - Saldo del wallet
/whitelist - Lista delle coppie monitorate
/blacklist - Lista delle coppie escluse
/logs - Ultimi log del bot

📈 TRADING:
/start - Avvia il bot di trading
/stop - Ferma il bot (sicuro)
/forcebuy <pair> - Forza acquisto di una coppia
/forcesell <trade_id> - Forza vendita di un trade
/delete <trade_id> - Cancella un trade

⚙️ CONFIGURAZIONE:
/reload_conf - Ricarica la configurazione
/show_config - Mostra configurazione attuale
/stopbuy - Ferma solo gli acquisti (mantiene vendite)
/help - Lista completa dei comandi

🔔 NOTIFICHE CONFIGURATE:
✅ Entrata in posizione
✅ Uscita da posizione (profit/loss)
✅ Stop loss attivato
✅ ROI raggiunto
✅ Avvisi e errori
✅ Stato del bot

💡 SUGGERIMENTO:
Usa /status per monitorare costantemente il bot
"""

print(__doc__)