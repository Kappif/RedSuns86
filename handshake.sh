#!/bin/bash
rm -rf t
while true
do
   read packet
   echo $packet >> t
   cnt=`echo $packet | wc -c`
   if [ $cnt == 2 ] #end of message
   then
      key=`cat t | grep "Sec-WebSocket-Key:" | cut -f2 -d " "`
      keylen=`echo -n $key | wc -c`
      keylen=`expr $keylen - 1`
      key2=`echo -n $key | cut -c -$keylen`
      magic="258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
      resp=`echo -n $key2$magic | openssl sha1 -binary | base64`
      echo   -n "HTTP/1.1 101 Switching Protocols"$'\r\n'
      echo   -n "Connection: Upgrade"$'\r\n'
      echo   -n "Upgrade: websocket"$'\r\n'
      echo   -n "Sec-WebSocket-Accept: $resp"$'\r\n\r\n'
      break
   fi
done
