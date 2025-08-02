# file-organizer
File Organizer Project / Ordner-Organizer-Projekt
Project Description / Projektbeschreibung

This project is a file organizer that sorts files into folders based on their file extensions. It also logs every operation performed (such as file processing, folder creation, and file movement) into a CSV file for tracking purposes.
Features:

    Sort files based on their extensions (e.g., .txt, .jpg, .pdf).

    Create folders for each extension type.

    Move the files into the respective folders.

    Log each action in a CSV file for auditing.

Technologies Used / Verwendete Technologien:

    Python: The programming language used.

    CSV module: For creating and updating CSV files.

    os module: For interacting with the operating system (file system management).

    shutil module: For moving files and creating directories.

How to Use / Verwendung

    Clone the repository (or copy the script).

    Run the Python script.

    The script will prompt you to enter the folder path where you want to organize the files.

    The program will:

        Process all files in the specified folder.

        Create a new folder for each unique file extension.

        Move the files into the corresponding folders based on their extensions.

        Log every action in a CSV file (data.csv).

CSV Log Format:

The CSV file will contain logs like:

    Folder path

    File processing steps

    Folder creation steps

    File movement steps

How to Run the Script / Wie man das Skript ausführt

    Ensure you have Python installed (Python 3.6 or later).

    Download or clone the project.

    Open your terminal or command prompt and run the script with:

    python file_organizer.py

    Enter the path of the folder you want to organize when prompted.

Project Details / Projektdetails

The script:

    Processes each file by its extension.

    Creates a folder for each extension (if the folder doesn't already exist).

    Moves files into their respective folders.

    Logs every action (folder creation, file movement, etc.) to a CSV file for auditing purposes.

Future Enhancements / Zukünftige Verbesserungen

    Error Handling: Add more robust error handling for permission issues or file access problems.

    File Name Conflicts: Handle cases where multiple files have the same name in the destination folder.

    Recursive Directory Traversal: Extend the script to support recursive file movement (subdirectories).

    Enhanced Logging: Include timestamps and more detailed logs in the CSV.

Contact / Kontakt

If you have any questions or suggestions, feel free to contact me via [your email or GitHub profile link].
File Organizer Project / Ordner-Organizer-Projekt
Projektbeschreibung

Dieses Projekt ist ein Ordner-Organizer, der Dateien basierend auf ihren Dateierweiterungen in Ordner sortiert. Es protokolliert auch jede ausgeführte Aktion (wie das Verarbeiten von Dateien, das Erstellen von Ordnern und das Verschieben von Dateien) in einer CSV-Datei zur Nachverfolgung.
Funktionen:

    Sortieren von Dateien basierend auf ihren Erweiterungen (z.B. .txt, .jpg, .pdf).

    Erstellen von Ordnern für jede Erweiterung.

    Verschieben der Dateien in die entsprechenden Ordner.

    Protokollieren jeder Aktion in einer CSV-Datei zur Überprüfung.

Verwendete Technologien:

    Python: Die verwendete Programmiersprache.

    CSV-Modul: Zum Erstellen und Aktualisieren von CSV-Dateien.

    os-Modul: Zum Interagieren mit dem Betriebssystem (Dateisystemverwaltung).

    shutil-Modul: Zum Verschieben von Dateien und Erstellen von Ordnern.

Verwendung

    Klonen Sie das Repository (oder kopieren Sie das Skript).

    Führen Sie das Python-Skript aus.

    Das Skript fordert Sie auf, den Ordnerpfad einzugeben, in dem Sie die Dateien organisieren möchten.

    Das Programm wird:

        Alle Dateien im angegebenen Ordner verarbeiten.

        Ein neuen Ordner für jede eindeutige Dateierweiterung erstellen.

        Die Dateien in die entsprechenden Ordner verschieben.

        Jede Aktion in einer CSV-Datei (data.csv) protokollieren.

CSV-Protokollformat:

Die CSV-Datei enthält Protokolle wie:

    Ordnerpfad

    Dateiverarbeitungs-Schritte

    Ordnererstellungs-Schritte

    Dateiverschiebeschritte

Wie man das Skript ausführt

    Stellen Sie sicher, dass Python installiert ist (Python 3.6 oder höher).

    Laden Sie das Projekt herunter oder klonen Sie es.

    Öffnen Sie Ihr Terminal oder die Kommandozeile und führen Sie das Skript mit folgendem Befehl aus:

    python file_organizer.py

    Geben Sie den Ordnerpfad ein, den Sie organisieren möchten, wenn Sie dazu aufgefordert werden.

Projektdetails

Das Skript:

    Verarbeitet jede Datei nach ihrer Erweiterung.

    Erstellt einen Ordner für jede Erweiterung (wenn der Ordner noch nicht existiert).

    Verschiebt die Dateien in die entsprechenden Ordner.

    Protokolliert jede Aktion (Ordnererstellung, Dateiverschiebung usw.) in einer CSV-Datei zur Nachverfolgung.

Zukünftige Verbesserungen

    Fehlerbehandlung: Eine robustere Fehlerbehandlung für Berechtigungsprobleme oder Dateizugriffsprobleme hinzufügen.

    Namenskonflikte bei Dateien: Fälle behandeln, in denen mehrere Dateien denselben Namen im Zielordner haben.

    Rekursive Durchsuchung von Verzeichnissen: Das Skript erweitern, um auch Unterverzeichnisse zu unterstützen.

    Erweitertes Logging: Zeitstempel und detailliertere Protokolle in die CSV-Datei aufnehmen.

