#! /bin/bash

source_dir="/home/matthew/computational_physics/src"
backup_dir="/home/matthew/computational_physics/backups"

mkdir -p "$backup_dir"

timestamp=$(date '+%d_%m_%Y_%H_%M_%S')

tar_filename="backup_"$timestamp
tar -zcvf $backup_dir/$tar_filename".tar.gz" $source_dir

find "$backup_dir" -name 'backup_*.tar.gz' -type f | sort -r | tail -n +4| xargs rm -f
