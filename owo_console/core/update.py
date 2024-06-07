import requests, os
current_dir = os.getcwd()

# Join the current directory with the filename
flie_data = os.path.join(current_dir, 'core\\main1.py')
print("Updating...")
update = requests.get(
    "https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-farm-bot/Main/owo_console/core/Main.py"
)
with open(flie_data, "wb") as f:
    f.write(update.content)
print("Update complete!")

