import json

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        verses = []
        for surah in data['data']['surahs']:
            for ayah in surah['ayahs']:
                verses.append({
                    'surah': surah['number'],
                    'ayah': ayah['number'],
                    'text': ayah['text']
                })
        return verses