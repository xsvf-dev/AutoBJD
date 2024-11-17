import pathlib

fever_path = "C:\Program Files\FeverGames\FeverGamesLauncher.exe"
fever_launcher_path = "F:\Fever Games\MC\FeverGamesLauncher\FeverGamesLauncher.exe"

log_file = pathlib.Path('F:\\MCLDownload\\Game\\.minecraft\\logs\\latest.log').expanduser().open('r', errors="replace")