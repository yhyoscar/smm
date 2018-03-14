# Notes of installing, running, and configuring MySQL server on Ubuntu

1. Installing and configuring MySQL server
    
    Reference: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04
    
    + > sudo apt-get install mysql-server
    + > sudo mysql_secure_installation
    + > sudo mysql_install_db
    + > service mysql status
    + > mysqladmin -p -u root version

2. Change database directory
    + > sudo service mysql stop
    + > mv /var/lib/mysql /mnt/mydata/
    + replace /var/lib/mysql with /mnt/mydata/mysql in
        - > /etc/passwd         (keyword: mysql)
        + /etc/mysql/my.cnf     (keyword: [mysqld] datadir)
        + /etc/apparmor.d/usr.sbin.mysqld   (keyword: /var/lib/mysql; replace it twice)
    + > sudo service mysql start

3. Basic commands
    
    Reference: https://dev.mysql.com/doc/mysql-getting-started/en/

