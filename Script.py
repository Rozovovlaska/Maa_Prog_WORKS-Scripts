#!   usr/bin/python3

# Scrip to open  URL 

#input
url=input("Enter the URL:")
# Input URL link into variablф
#url_link = input("Enter the URL link: ")

#  is true  lenght


if len(url)>0 :
    import webbrowser
    #open  URL
    #webbrowser.open  ('https://example.com') & webbrowser.open ('https://github.com')
    webbrowser.open (url)

i=8
def comma_fnc():
    for i in range(10):
        print("Its your  link: ",url)

        if len(url) == 0:
print("Not  Link_!!! ")


    else:
        print("Its  short link!!! ")



# return ii = comma_fnc()

