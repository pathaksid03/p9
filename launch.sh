

#!/bin/sh
echo "Server and Client Terminals will now open.."



gnome-terminal -e "bash -c \"python server.py; exec bash\""

gnome-terminal -e "bash -c \"telnet localhost 8888; exec bash\""
gnome-terminal -e "bash -c \"telnet localhost 8888; exec bash\""
