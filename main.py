import os


for x in os.listdir():
    if x == '.DS_Store':
        continue
    elif x == '.venv':
        continue
    elif x == '.idea':
        continue
    name, exten = os.path.splitext(x)
    full = name+exten

    if exten == '.png':
        print(x)
        os.rename(f'/Users/mohitprathipati/Library/Mobile Documents/com~apple~CloudDocs/Coding /basic practce/fileOrganizer/{full}', f'/Users/mohitprathipati/Library/Mobile Documents/com~apple~CloudDocs/Coding /basic practce/fileOrganizer/images/{full}')
    if exten == '.pdf':
        print(x)
        os.rename(f'/Users/mohitprathipati/Library/Mobile Documents/com~apple~CloudDocs/Coding /basic practce/fileOrganizer/{full}', f'/Users/mohitprathipati/Library/Mobile Documents/com~apple~CloudDocs/Coding /basic practce/fileOrganizer/pdfs/{full}')


