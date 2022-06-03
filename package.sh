#!/bin/bash
target_folder=${1:-/tmp/objdetect}
[ ! -d $target_folder ] && mkdir -p $target_folder

compress_target_dirs="result assets build"

for compress_dir in $compress_target_dirs; do
    echo "Compressing $compress_dir"
    zip -r $target_folder/$compress_dir.zip $compress_dir > /dev/null &
    tar -czf $target_folder/$compress_dir.tar.gz $compress_dir &
    tar -I zstd -cf $target_folder/$compress_dir.zstd.tar.zst $compress_dir &
done

wait