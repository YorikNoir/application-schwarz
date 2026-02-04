"""Generate QR code for the GitHub Pages URL."""
import qrcode
import sys

def generate_qr_code(url, output_file="qr-code.png"):
    """Generate a QR code for the given URL."""
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size in boxes
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="#667eea", back_color="white")
    
    # Save the image
    img.save(output_file)
    print(f"QR code generated: {output_file}")
    print(f"URL: {url}")

if __name__ == "__main__":
    # Default URL - replace with your actual GitHub Pages URL
    default_url = "https://DEIN-USERNAME.github.io/application-schwarz/"
    
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = default_url
        print(f"Using default URL: {url}")
        print("To use a custom URL, run: python generate_qr.py YOUR_URL")
        print()
    
    generate_qr_code(url)
