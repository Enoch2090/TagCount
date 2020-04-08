import Tagcount

file_list = []
file_list = Tagcount.scan(
    '/Users/enoch/Library/Mobile Documents/com~apple~CloudDocs/Blog/enoch2090/source/_posts/', file_list)
tags = Tagcount.count(file_list)
Tagcount.write_as_file(tags, '/Users/enoch/Desktop')
