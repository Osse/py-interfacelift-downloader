_(This branch is a slight experiment. Since wget is executed with the -nc
option there is no need to check if the file exists from within Python. only
one wget command is executed with a list of files instead of one wget per file.
This enables the use of --wait and --random-wait. Since this, the subprocess
module has been utilized instead of os.system().)_

Py-Interfacelift-downloader
===========================

This snippets downloads wallapers from Interfacelift according to the
preferences set. To specify which images you want, edit the `urlspec` string.
For now it looks like this:

    urlspec = 'rating/widescreen/1920x1200/'

This will sort the pictures by rating, chooses the widscreen format and further
specifies a resolution of 1920x1200. In general the urlspec looks something
like this:

    urlspec = 'sort/format/resolution'

where

* `sort` can instead be e.g. `date` or `downloads`
* `format` can instead be e.g. `fullscreen`, `hdtv` 
* `resolution` can instead  be e.g. `1280x1024` or `1080p`

Check how the URL changes when you select the options in Interfacelift itself.
You can also download images found by tags or anything else. For example,

    urlspec = 'tags/1426/scene/city_lights/'

is valid.

To specify where to save the images, edit the `directory` string. Please leave
`expanduser('~')` as it is (unless you now what you're doing) and rather edit
the string after the `+` sign. Start the string with `/` and choose the folder
you want.

To specify how many pictures you want, edit the `range()` function. To download
the pictures from the _n_ first pages, change it to read `range(1,n+1)`. This
will download 10 _n_ images.

The script finds the correct URL to the pictures based on the URL of the
preview thumbnail. Note that the matched string will include the random part of
the URL so that you don't have to specify it manually.
