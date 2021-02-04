#!/bin/sh

# Defining the directory with wallpapers
BG_DIR=$HOME/.wallpapers


# Getting current date
TODAY=$(date -I)

# Removing of the old symlink
[ -f "${HOME}"/.config/nitrogen/wallpaper.jpg ] && rm "${HOME}"/.config/nitrogen/wallpaper.jpg 

# Feeding random generator with the date in seconds (UNIX time)
RANDOM=$$$(date +%s)

# Generating list of all wallpapers in the directory
BG_LIST=("${BG_DIR}"/*)

echo "${BG_LIST[1]}"

# Counting total number of files
BG_NUM=$(ls -1 "${BG_DIR}" | wc -l)

# Randomly select some number from the total number of wallpapers
SELECTED_BG=$(( $RANDOM % ${BG_NUM} ))

# Creating new symbolic link to the selected wallpaper with the name "current_bg_image.jpg" 
ln -s "${BG_LIST[$SELECTED_BG]}" "$HOME/.config/nitrogen/wallpaper.jpg" 

