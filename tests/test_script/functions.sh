ping_command='ping -c 3 -W 5 -q'

check_if_up(){
ip=$1
$ping_command $ip
return $?
}
