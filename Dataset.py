from bing_image_downloader import downloader

def download_images(query, num_images=10):
    try:
        query_string = query
        downloader.download(query_string, limit=num_images, adult_filter_off=True, force_replace=False)
        print(f"Downloaded {num_images} images for {query}")
    except Exception as e:
        print(f"Error downloading images for {query}: {str(e)}")

def main():
    plants = ["Aizoaceae", "Arecaceae"]
    for plant in plants:
        download_images(plant)

if __name__ == "__main__":
    main()
