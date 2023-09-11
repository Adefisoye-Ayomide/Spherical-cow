cd backups/
timestamp=$(date +"%Y%m%d%H%M%S")
tar -cvzf "${timestamp}.tar.gz" /home/aklima/computation_class/src/
cd ..
cd src/
ls -t | tail -n+4 | xargs rm -rf --

