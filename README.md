# TagCount

A snippet used to count the tags in your blog posts.

## Prerequisite

The tags should be written in the posts' metadata using YAML format. Example:

```yaml
---
title: Some Title
date: 1970/1/1
tags:
	- Tag_1
	- Tag_2
	- Tag_x
---

```

## Usage

There are two ways of using the snippet. The cli method:

```shell
$ python3 Tagcount.py --dir 'Users/Blog/Source/_posts/'
```

This will generate a `wordcloud.txt` in the directory where you run the script.

The coding method:

```python
import tagcount as tgc
file_list = []
file_list = tgc.scan('Users/Blog/Source/_posts/',file_list)
tags = tgc.count(file_list)
tgc.write_as_file(tags, '/Users/enoch/Desktop')
```

Note that the `count()` function returns a dictionary with the keys as tags and values as occurances. Therefore you may utilize this function to directly get the count instead of writing to a wordcloud file.