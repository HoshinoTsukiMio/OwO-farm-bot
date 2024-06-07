import requests

def update_bot():
    print("Updating...")
    update = requests.get(
        "main file link"
    )

    # Save the new version to the local file system
    with open("Main.py", "wb") as f:
        f.write(update.content)
    print("Update complete!")
    #hmm so good
    #perfect

