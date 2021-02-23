# aliases

alias ls "exa --group-directories-first"
alias lsa "exa -la --group-directories-first"
alias tree "exa -T"
alias cat "ccat"
alias gitm "git commit -m"


# funcion para sudo !!
# https://unix.stackexchange.com/questions/235704/fish-sudo-command-not-found
function sudo --description "funcion para sudo !!"
    if test "$argv" = !!
    eval command sudo $history[1]
else
    command sudo $argv
    end
end
