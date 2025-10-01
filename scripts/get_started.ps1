# scripts/get_started.ps1
$repo = "https://github.com/<you>/see_proto/releases/latest/download"

Write-Host "== SEE quick start =="
Write-Host "1) Download Demo ZIP from: $repo"
Write-Host "2) pip install see_proto --find-links $repo"
Write-Host "3) Unzip Demo_v*.zip and run:  python .\samples\quick_demo.py"
