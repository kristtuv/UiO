alias subl='/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl'
alias d='date'
alias cpua="ps -A -o %cpu ";
alias NASA='telnet horizons.jpl.nasa.gov 6775';
alias fys4460="cd ~/Documents/UiO/V18/FYS4460";
alias inf5860="cd ~/Documents/UiO/V18/INF5860";
alias fys4130="cd ~/Documents/UiO/V18/FYS4130";
alias v18="cd ~/Documents/UiO/V18/";
alias bp="mvim ~/.bash_profile";
alias vrc="mvim ~/.vimrc";
alias h='history'
alias j='jobs -l'

alias cd..='cd ..'
alias .='cd ..'
alias ..='cd ../../'
alias ...='cd ../../../'
alias ....='cd ../../../../'
alias .4='cd ../../../../'
alias .5='cd ../../../../..'

export PATH="/usr/local/bin:$PATH";
export PATH="/Applications/NEURON-7.5/nrn/x86_64/bin:$PATH" #added by NEURON installer
export PATH=$PATH:/Applications/Ovito.app/Contents/MacOS/
export PYTHONPATH="${PYTHONPATH}:/Users/Tuv/Documents/Modules/"
# added by Anaconda2 4.3.0 installer
export PATH="/Users/Tuv/anaconda/bin:$PATH"
LS_COLORS=$LS_COLORS:'di=0;35:';
export LS_COLORS

export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[31;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'
