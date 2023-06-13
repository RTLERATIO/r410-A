docker run --rm -d \
	-p 3306:3306 \
	--env MYSQL_ROOT_PASSWORD=foo \
	-v vol-sql:/var/lib/mysql \
	mysql
