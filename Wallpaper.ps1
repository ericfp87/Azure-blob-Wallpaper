$url = "https://bulbeenergia.blob.core.windows.net/datalake-bulbe/RH/wallpaper/fundo-tela-note.png"
$dest = "C:\Wallpaper\fundo-tela-note.png"

$wc = New-Object System.Net.WebClient
$wc.DownloadFile($url, $dest)
