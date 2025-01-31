import requests
import json
import os

def download_quran_json():
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    base_url = "https://raw.githubusercontent.com/semarketir/quranjson/master/source/translation/en"
    combined_data = {"data": {"surahs": []}}
    
    # Download and combine all 114 surahs
    for surah_num in range(1, 115):
        url = f"{base_url}/en_translation_{surah_num}.json"
        print(f"Downloading surah {surah_num}...")
        
        response = requests.get(url)
        if response.status_code == 200:
            surah_data = response.json()
            combined_data["data"]["surahs"].append(surah_data)
        else:
            print(response.text)
            print(f"Failed to download surah {surah_num}")
    
    # Save combined JSON
    output_path = 'data/quran.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=2)
    
    print(f"Combined Quran JSON saved to {output_path}")

if __name__ == "__main__":
    download_quran_json()
