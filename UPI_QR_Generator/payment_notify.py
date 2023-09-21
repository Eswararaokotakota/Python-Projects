from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual UPI ID
your_upi_id = "6301189779@ybl"

# Define a callback URL where you'll receive notifications
callback_url = "https://5d09-2401-4900-1c0e-17ae-994b-47e4-1e8-9cb9.ngrok.io"

@app.route('/payment_callback', methods=['POST'])
def payment_callback():
    data = request.json
    if data.get('pa') == your_upi_id and data.get('txnStatus') == 'SUCCESS':
        # Payment received successfully, you can handle notifications here
        # For example, send an email, update a database, or trigger an event
        print("Payment received:", data)
    return jsonify(status='OK')

if __name__ == '__main__':
    from pyngrok import ngrok
    ngrok_url = ngrok.connect(5000)
    print("Public URL for callback:", ngrok_url)
    app.run()
