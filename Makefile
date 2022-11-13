all: dep

dep:
	apt list | grep installed | grep opencv && apt-get -y install opencv

install: all
	mkdir -p /usr/local/sbin/
	cp src/* /usr/local/sbin/
	systemctl enable rc-local
	grep 'facial_recogeniaze.py' /etc/rc.local || echo 'setsid python3 /usr/local/sbin/facial_recogeniaze.py >/tmp/log 2>&1 </dev/null &' >> /etc/rc.local

