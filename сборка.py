import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox

def create_structure(base_path, structure):
    for name, content in structure.items():
        current_path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, content)
        elif isinstance(content, str):
            with open(current_path, "w", encoding="utf-8") as f:
                f.write(content)

def main():
    root = tk.Tk()
    root.withdraw()
    
    # Здесь можно настроить дефолтный формат файлов или стартовую директорию для диалоговых окон
    json_file = filedialog.askopenfilename(
        title="Выберите JSON файл структуры",
        filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
    )
    
    if not json_file:
        return
        
    target_dir = filedialog.askdirectory(
        title="Выберите папку, где создать структуру"
    )
    
    if not target_dir:
        return
        
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        create_structure(target_dir, data)
        messagebox.showinfo("Успех", "Вся структура файлов и папок успешно воссоздана!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при обработке: {e}")

if __name__ == "__main__":
    main()
