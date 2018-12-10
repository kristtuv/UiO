import re


def parse_nwodkram(text):
    """
    Takes Nwodkram text and substituting to html text
    Example:
    >>> text = "[here](www.google.com) is a hyperlink.%this% *this* \* \%"
    >>> print(parse_nwodkram(text))
    <a href='http://www.google.com'>here</a> is a hyperlink.<b>this</b> <i>this</i> * %
    """
    ### Nwodkram ###
    italic = r"(?<!\\)\*(?P<italicword>[\w\*\s\%\.\?\!\\]+)(?<!\\)\*"#Italic words
    bold =  r"(?<!\\)\%(?P<boldword>[\w\*\s\%\.\?\!\\]+)(?<!\\)\%" #Bold words
    url = r"\[(?P<bracketcontent>[^\[\]]+)\]\((http(?P<s>s)?:\/\/)?(?P<www>www\.)?(?P<url>[\w\.\-~\?\$\|]+[\w\.\-~\/]+)\)"

    slash_italic = r"\\\*" #Finding \*
    slash_bold = r"\\\%" #Finding \%

    wikipedia = r"\[wp\:(?P<wiki>.+)\]" #Wikipedialink
    blockquote = r">>(?P<block>.*)"
    image = r"<(?P<image>https?://(?:www)?.+)>\(w=(?P<width>\d+),h=(?P<height>\d+)\)" #Imagelink

    ### Html replacement###
    italic_repl = r"<i>\g<italicword></i>"
    bold_repl = r"<b>\g<boldword></b>"
    url_repl = "<a href='http\g<s>://\g<www>\g<url>'>\g<bracketcontent></a>"

    slash_bold_repl = "%"
    slash_italic_repl = "*"

    wikipedia_repl = "<a href=\"www.wikipedia.org/wiki/\g<wiki>\">Search Wikipedia for \g<wiki></a>"
    blockquote_repl = r"<blockquote>\g<block></blockquote>"
    image_repl = "<img src=\"\g<image>\" style=\"width:\g<width>px;height:\g<height>px\";>"


    ### Substituting words ###
    matches = re.sub(italic, italic_repl, text, re.S)
    matches = re.sub(bold, bold_repl, matches, re.S)
    matches = re.sub(image, image_repl, matches, re.S)
    matches = re.sub(url, url_repl, matches, re.S)

    matches = re.sub(slash_bold, slash_bold_repl, matches, re.S)
    matches = re.sub(slash_italic, slash_italic_repl, matches, re.S)

    matches = re.sub(wikipedia, wikipedia_repl, matches, re.S)
    matches = re.sub(blockquote, blockquote_repl, matches)

    return matches
if __name__ == "__main__":
    import doctest
    doctest.testmod()
