import json
import os


class BronzeLoader:

    @staticmethod
    def save_json(data, directory, filename):

        os.makedirs(directory, exist_ok=True)

        file_path = os.path.join(directory, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved -> {file_path}")