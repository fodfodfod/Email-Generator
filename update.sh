
cd $(dirname "$0")

# Define the GitHub repository and branch
REPO="fodfodfod/Email-Generator"
BRANCH="main"

# Define the GitHub URL for the file
URL="https://raw.githubusercontent.com/$REPO/$BRANCH/update.sh"

# Download and replace the file
curl -s -o "update.sh" "$URL" && echo "Replaced updater"


# Define the GitHub URL for the file
URL="https://raw.githubusercontent.com/$REPO/$BRANCH/files.txt"

# Download and replace the file
curl -s -o "files.txt" "$URL" && echo "Replaced files list"

# Find all Python scripts in the current directory
cat files.txt | while read -r file; do
  # Extract the relative path
  REL_PATH=${file#./}

  # Define the GitHub URL for the file
  URL="https://raw.githubusercontent.com/$REPO/$BRANCH/$REL_PATH"

  # Download and replace the file
  curl -s -o "$file" "$URL" && echo "Replaced $file"
done

