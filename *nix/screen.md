altscreen on
term xterm-256color

bindkey "^[OP" focus up
bindkey "^[OQ" focus down

bindkey "^[OR" prev
bindkey "^[OS" next

# mouse tracking allows to switch region focus by clicking
#mousetrack on

# the following two lines give a two-line status, with the current window highlighted
hardstatus alwayslastline
hardstatus string '%{= kG}[%{G}%H%? %1`%?%{g}][%= %{= kw}%-w%{+b yk} %n*%t%?(%u)%? %{-}%+w %=%{g}][%{B}%m/%d %{W}%C%A%{g}]'

# huge scrollback buffer
defscrollback 5000

# no welcome message
startup_message off

split
screen -t s1

focus
screen -t s2

focus

