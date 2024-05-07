from PIL import ImageGrab
import pytesseract

def monitor_screen(region):
	"""Monitor the specified screen region, extract text from it using OCR and print it"""
	text = ""
	print("started...")
	while True:
		print("detecting...")
		extract_text = extract_text_from_screen(region)
		if extract_text and extract_text != text:
			print(f"Detected text: {extract_text}")

if __name__ == "__main__":
	# define the region of your screen where the text appears
	screen_region = (0, 0, 1920, 1280) # Set the region as Monitor 1 for the starter
	monitor_screen(screen_region)
