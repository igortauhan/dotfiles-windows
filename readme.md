## Dotfiles

### Warning

**Don't use my configs if you don't know what it does!** Use at your own risk.

### Dependencies

- [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3)
- [Scoop](https://scoop.sh/)
- [oh-my-posh](https://ohmyposh.dev/)
- git `winget install Git.Git`
- python `scoop install python`
- neovim `scoop install neovim` (Not required)

### Contains

- Scoop
- Oh-my-posh
  - PSReadLine
- Git config
- IDEA VIM config

### Installation


Add this line in the $PROFILE:

```
. $env:USERPROFILE\.config\powershell\user_profile.ps1
```

And run:

`python3 install.py`
