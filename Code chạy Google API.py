import tkinter as tk
from tkinter import ttk
import requests


class TextTranslatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Text Translator")
        self.create_widgets()

    def create_widgets(self):
        # Label và Entry cho văn bản cần dịch
        label1 = tk.Label(self.root, text="Enter text to translate:")
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry = tk.Entry(self.root, width=58)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        # Chọn ngôn ngữ nguồn
        label2 = tk.Label(self.root, text="Choose source language:")
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.source_lang = ttk.Combobox(self.root, values=["en", "es", "fr", "vi", "ja", "zh"])
        self.source_lang.set("en")
        self.source_lang.grid(row=1, column=1, padx=10, pady=10)

        # Chọn ngôn ngữ đích
        label3 = tk.Label(self.root, text="Choose target language:")
        label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.target_lang = ttk.Combobox(self.root, values=["en", "es", "fr", "vi", "ja", "zh"])
        self.target_lang.set("vi")
        self.target_lang.grid(row=2, column=1, padx=10, pady=10)

        # Nút "Translate"
        translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        translate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Hiển thị kết quả
        self.result_label = tk.Label(self.root, text="Translated text will appear here.", wraplength=400,
                                     justify="left")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_text(self):
        # API Key cho Google Translate API
        api_key = "AIzaSyB1qupyzNgJMrej3hRAnKdaxk0JRqdcF_c"  # Thay YOUR_API_KEY bằng API Key của bạn
        text_to_translate = self.entry.get()
        source_lang = self.source_lang.get()
        target_lang = self.target_lang.get()

        # URL của Google Translate API
        url = f"https://translation.googleapis.com/language/translate/v2"

        # Tham số cho API
        params = {
            'q': text_to_translate,
            'source': source_lang,
            'target': target_lang,
            'key': api_key
        }

        try:
            # Gửi request tới API
            response = requests.post(url, params=params)
            response_data = response.json()

            # Lấy kết quả dịch
            if 'data' in response_data:
                translated_text = response_data['data']['translations'][0]['translatedText']
                self.result_label.config(text=translated_text)
            else:
                self.result_label.config(text="Error: Unable to translate. Check your API key or input.")
        except requests.exceptions.RequestException as e:
            self.result_label.config(text=f"Error: {e}")


# Khởi chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()
