# aliases

alias ls "exa --group-directories-first"
alias lsa "exa -la --group-directories-first"
alias tree "exa -T"
alias cat "ccat"
alias gitm "git commit -m"
alias texrtm "latexmk -pdf -pvc"

# script para actualizar todo
alias uptall "$HOME/bin/updateall"

# funcion para sudo !!
# https://unix.stackexchange.com/questions/235704/fish-sudo-command-not-found
function sudo --description "funcion para sudo !!"
    if test "$argv" = !!
        eval command sudo $history[1]
    else
        command sudo $argv
    end
end

# funcion para crear pdf desde latex
function texpdf --description "funcion para crear pdf desde .tex sin archivos indeseados"
    if test (count $argv) = 1
        command rubber --pdf $argv
        command rubber --clean $argv
    else
        command echo "necesitas introducir el nombre del archivo"
    end
end
