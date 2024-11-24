import smtpd
import asyncore
from email.parser import Parser
from pyngrok import ngrok
import json
import os

class MySMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print(f"--- メールを受信しました ---")
        print(f"From: {mailfrom}")
        print(f"To: {rcpttos}")
        
        msg = Parser().parsestr(data.decode())
        print(f"件名: {msg.get('Subject')}")
        print(f"本文: {msg.get_payload(decode=True).decode()}")
        
        email_data = {
            "from": mailfrom,
            "to": rcpttos,
            "subject": msg.get('Subject'),
            "body": msg.get_payload(decode=True).decode()
        }
        
        # メールをJSONファイルに保存
        with open("received_email.json", "a", encoding="utf-8") as f:
            json.dump(email_data, f, ensure_ascii=False, indent=4)
            f.write(",\n")  # 複数のメールを保存するため

        return "250 OK"

if __name__ == "__main__":
    # 使用するポート番号
    port = 1225

    # Stop existing tunnels using ngrok API if necessary
    active_tunnels = ngrok.get_tunnels()
    if len(active_tunnels) >= 3:
        print("Too many active tunnels. Disconnecting one...")
        ngrok.disconnect(active_tunnels[0].public_url)  # Disconnect the first tunnel


    # ngrokで公開するURLを取得
    public_url = ngrok.connect(port)
    print(f"公開されたSMTPサーバーのURL: {public_url}")
    
    # SMTPサーバーを起動
    server = MySMTPServer(('localhost', port), None)
    print(server)
    try:
        # 非同期でサーバーを実行
        asyncore.loop()
    except KeyboardInterrupt:
        print("サーバーを停止します。")
