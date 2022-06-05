LINUX_FOLDER="./linux-5.17.6"

# for every config variable
config_no=1
while read var; do
    echo "$config_no"
    echo "CONFIG_NAME::$var"
    config_no=$((config_no+1))
    rg -F $var $LINUX_FOLDER --block-buffered --heading --line-buffered --line-number --with-filename
done <./var_with_config.txt
