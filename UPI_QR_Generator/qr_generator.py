import qrcode
from pyngrok import ngrok
ngrok_url = ngrok.connect(5000)
# User-selected UPI amount and UPI ID
amount = "20"  # Replace with the user's selected amount
upi_id = "6301189779@ybl"  # Replace with the recipient's UPI ID

# Create the UPI payment URL
# upi_url = f"upi://pay?pa={upi_id}&pn=Recipient&am={amount}&cu=INR"
upi_url = f"upi://pay?pa={upi_id}&pn=Recipient&am={amount}&cu=INR&tn=Payment%20for%20Your%20Product&tr={ngrok_url}"
# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(upi_url)
qr.make(fit=True)

# Create an image from the QR code data
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_img.save(r"C:\Users\Eswar\Desktop\upi_qr.png")
print("Done")
