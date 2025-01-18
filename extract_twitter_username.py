# https://twitter.com/richsmedberg

import re

url = input("URL: ").strip()
                                #username = url.replace("https://twitter.com/", "")   #find and replace
                                #username = url.removeprefix("https://twitter.com/")    #remove prefix
                                #username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)   #capture username
# if matches:
#     print(f"Username:", matches.group(3))

# OR..........

if matches := re.search(r"^(https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
                                                # don't need to capture www
    print(f"Username:", matches.group(2))       # changes to 2 because of non-capturing

             ### also look at re.findall