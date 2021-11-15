# Ibrahim Zavala Hernandez
# Julio Gerardo Cazarez Gonzalez
# Pedro Saldaña Vazquez

# --- MODULOS ---
from DownloadImages import Scraping
import DataImages
import argparse

# --- SCRIPT ---
parser = argparse.ArgumentParser()
parser.add_argument('-link', type=str, dest='url', help='url donde se buscaran las imagenes')
params=parser.parse_args()

if __name__ == "__main__":
	scraping = Scraping()
	scraping.scrapingImages(params.url)
	DataImages.printMeta()