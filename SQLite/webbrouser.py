import webbrowser
import sqlite3

# connecting to sqlite and creating
# an actual database
conn = sqlite3.connect("favorites.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS favorites
		(title TEXT, url TEXT)""")


# Created a table named favorites
# (if it didn't already existed).
# Then inserted the headers title
# (which takes text as input)
# and url (which takes text as input)
def get_data():
    """
    Used to extract data from our database
    """

    c.execute('''SELECT * FROM favorites''')
    results = c.fetchall()
    return results


def get_fav(titl):
    """
    Used to extract the favorite website
    """

    c.execute('''SELECT * FROM favorites WHERE title=?''',
              (titl,))
    return c.fetchone()


def add_fav(titl, url):
    """
    Used to add a new favorite website
    """

    c.execute("""INSERT INTO favorites (title, url) VALUES (?, ?)""",
              (titl, url))
    conn.commit()


def remove_fav(titl):
    """
    Used to remove a favorite website from the database
    """

    c.execute('''DELETE FROM favorites WHERE title=?''',
              (titl,))
    conn.commit()


# A loop to listen to commands from the user
while True:
    print()

    # printing each statement like
    # this to keep the code clean
    print("Press v to visit a favorite,", end=" ")
    print("ls for list,", end=" ")
    print("add to add a new item,", end=" ")
    print("rm to delete,", end=" ")
    print("q to quit:", end=" ")

    # taking input command from the user
    response = input("")

    if response.lower() == "v":
        shortcut = input("Enter the shortcut for the website: ")
        record = get_fav(shortcut)

        try:
            # opening the selected website in the browser
            webbrowser.open(record[1])

        except TypeError:
            # if we don't have the shortcut
            # in the database, print this:
            print('This shortcut does not exist in the database')

    elif response.lower() == "ls":
        # printing the items in the database
        print(get_data())

    elif response.lower() == "add":
        # adding a new website to the database
        destination = input(
            "Enter URL for the shortcut (Example -> https://xyz.com): ")

        # adding the shortcut to the above website in
        # the database
        shortcut = input("Enter the shortcut for the URL: ")

        add_fav(shortcut, destination)

    elif response.lower() == "rm":

        # removing an item from the database
        shortcut = input(
            "Enter the shortcut for the URL you want to remove: ")
        remove_fav(shortcut)
        print("Removed Successfully")

    elif response.lower() == "q":
        break

    else:
        print("Enter a valid command")
