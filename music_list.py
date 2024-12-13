from pathlib import Path
from mutagen import File
from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4
import logging


class MusicMetadataExtractor:
    def __init__(self):
        # Set up logging
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
        self.logger = logging.getLogger(__name__)

    def get_metadata_mp3(self, file_path):
        """Extract metadata from MP3 files."""
        try:
            audio = EasyID3(file_path)
            artist = audio.get("artist", ["Unknown Artist"])[0]
            title = audio.get("title", [Path(file_path).stem])[0]
            return artist, title
        except Exception as e:
            self.logger.warning(f"Error reading MP3 metadata from {file_path}: {str(e)}")
            return None, None

    def get_metadata_m4a(self, file_path):
        """Extract metadata from M4A/AAC files."""
        try:
            audio = MP4(file_path)
            artist = audio.get("\xa9ART", ["Unknown Artist"])[0]
            title = audio.get("\xa9nam", [Path(file_path).stem])[0]
            return artist, title
        except Exception as e:
            self.logger.warning(f"Error reading M4A metadata from {file_path}: {str(e)}")
            return None, None

    def get_metadata_flac(self, file_path):
        """Extract metadata from FLAC files."""
        try:
            audio = File(file_path)
            artist = audio.get("artist", ["Unknown Artist"])[0]
            title = audio.get("title", [Path(file_path).stem])[0]
            return artist, title
        except Exception as e:
            self.logger.warning(f"Error reading FLAC metadata from {file_path}: {str(e)}")
            return None, None

    def extract_metadata(self, file_path):
        """Extract metadata based on file extension."""
        extension = file_path.suffix.lower()
        if extension == ".mp3":
            return self.get_metadata_mp3(file_path)
        elif extension in [".m4a", ".aac"]:
            return self.get_metadata_m4a(file_path)
        elif extension == ".flac":
            return self.get_metadata_flac(file_path)
        else:
            self.logger.warning(f"Unsupported file format: {extension}")
            return None, None

    def process_directory(self, directory_path, output_file="music_list.txt"):
        """Process all music files in the directory and save metadata to a file."""
        directory = Path(directory_path)
        if not directory.exists():
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist")

        # List to store all music entries
        music_entries = []
        supported_extensions = {".mp3", ".m4a", ".aac", ".flac"}

        # Process all files
        total_files = 0
        processed_files = 0

        for file_path in directory.rglob("*"):
            if file_path.suffix.lower() in supported_extensions:
                total_files += 1
                artist, title = self.extract_metadata(file_path)

                if artist and title:
                    entry = f"{artist} - {title}"
                    music_entries.append(entry)
                    processed_files += 1
                    self.logger.info(f"Processed: {entry}")

        # Sort entries alphabetically
        music_entries.sort()

        # Write to output file
        with open(output_file, "w", encoding="utf-8") as f:
            for entry in music_entries:
                f.write(f"{entry}\n")

        self.logger.info("\nProcessing complete:")
        self.logger.info(f"Total music files found: {total_files}")
        self.logger.info(f"Successfully processed: {processed_files}")
        self.logger.info(f"Output saved to: {output_file}")


def main():
    print("Music Metadata Extractor")
    print("-----------------------")

    # Get directory path from user
    directory_path = "G:\My Drive\DriveSyncFiles\Music\Eclectic"
    output_file = "music_list.txt"

    # Use default output file name if none provided
    if not output_file:
        output_file = "music_list.txt"

    # Add .txt extension if not provided
    if not output_file.endswith(".txt"):
        output_file += ".txt"

    # Process the files
    extractor = MusicMetadataExtractor()
    try:
        extractor.process_directory(directory_path, output_file)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
