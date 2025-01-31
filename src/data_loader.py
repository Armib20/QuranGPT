import json

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        verses = []
        for surah in data['data']['surahs']:
            surah_name = surah['name']
            surah_index = surah['index']
            
            # Convert verse dict to list of verses with proper metadata
            for verse_key, verse_text in surah['verse'].items():
                # Skip the Bismillah verse (verse_0)
                if verse_key == 'verse_0':
                    continue
                    
                # Extract verse number from key (e.g., 'verse_1' -> '1')
                verse_num = verse_key.split('_')[1]
                
                verses.append({
                    'surah': surah_index,
                    'ayah': verse_num,
                    'text': verse_text,
                    'surah_name': surah_name
                })
        
        return verses