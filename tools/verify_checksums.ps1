# tools/verify_checksums.ps1 (minimal)
param([string]$Root=".")
Write-Host "Verifying SHA256 under $Root"
Get-ChildItem -Recurse -File $Root | ForEach-Object {
  $h = Get-FileHash $_.FullName -Algorithm SHA256
  "{0}  {1}" -f $h.Hash, $_.FullName
}
