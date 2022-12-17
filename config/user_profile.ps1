# OhMyPosh
oh-my-posh init pwsh | Invoke-Expression

# PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView

# Aliases
Set-Alias -Name touch -Value New-Item
Set-Alias -Name vim -Value nvim
Set-Alias -Name 'C:\Program Files\Git\usr\bin\less.exe' -Value less
Set-Alias -Name which -Value where.exe
Set-Alias -Name ll -Value ls
