import re
import urllib.request

def find_emails(text):
    """
    Searches a string and find all valid emails contained in the string

    Example:
        >>> mail = [
        ...     "karl@erik.no",
        ...     "simon@funke.no",
        ...     "funsim@uio.no",
        ...     "karleh@ifi.uio.no",
        ...     "name@server.1o",
        ...     "name@server.o1",
        ...     "name@ser<ver.domin",
        ...     "na&me@domain.com",
        ...     "n~ame@dom_ain.com",
        ...     "name@domain._com",
        ...     "name@domain.c_o.uk"
        ... ]
        >>> for email in find_emails(mail):
        ...     print(email)
        karl@erik.no
        simon@funke.no
        funsim@uio.no
        karleh@ifi.uio.no
        na&me@domain.com
        n~ame@dom_ain.com
        name@domain.c_o.uk
    """
    name = r"[\w\$%&~'\*\+\-/=\?\|\{\}\.\#]+"
    server = r"(?:[\w\$%&~'\*\+\-/=\?\|\{\}\.\#_`]+\.){1,}"
    domain = r"[A-Za-z]\w*[A-Za-z]"
    pattern = name + "@" + server + domain #Pattern of valid email
    matches = []
    if isinstance(text, str):
        matches.append(re.findall(pattern, text))
    elif isinstance(text, list):
        for line in text:
            matches.append(re.findall(pattern, line))
    else:
        raise TypeError("Text must be string or a list of strings")
    return list(sum(filter(None, matches), []))

def find_urls(text):
    r"""
    Finds hyperlinks from html code, including relative links

    Example:
    >>> u = [
    ...     '<a href=\"http://www.mn.uio.no/ifi/personer/vit/karleh/index.html\">'
    ...     'Norwegian<span class=\"offscreen-screenreader\"> version of this page</span></a>',
    ...     'http://www.google.com',
    ...     "<a href=\"http://www.google.com/super_secret/all_the_user_data/\'>Please don't click</a>",
    ...     "<a class=\"vrtx-value\" href=\"mailto:karleh@ifi.uio.no\">karleh@ifi.uio.no</a>"
    ... ]
    >>> print(find_urls(u))
    ['http://www.mn.uio.no/ifi/personer/vit/karleh/index.html']
    """
    matches = [] # List of url matches
    pattern1 = r"<a (?:data-offset=\"\d*\" )?href=(\"|')(?:https?://)(?:www\.)?(?P<url>[\w\.\-~\/\=\?\d\<\>]+)\1.*?</a>" #Pattern for finding urls in html
    pattern2 = r"<a href=(\"|')(?P<url2>[\w\-~]+\.html)\1.*?</a>" #Pattern for finding relative hyperlinks
    if isinstance(text, str):
        for m in re.finditer(pattern1, text, re.S):
            matches.append("http://www." + m.group("url"))
        for m2 in re.finditer(pattern2, text, re.S):
            matches.append("http://www." + m2.group("url2"))

    elif isinstance(text, list):
        for line in text:
            for m in re.finditer(pattern1, line, re.S):
                matches.append("http://www." + m.group("url"))
            for m2 in re.finditer(pattern2, line, re.S):
                matches.append("http://www." + m2.group("url2"))

    else:
        raise TypeError("Text must be string or a list of strings")
    return matches

def all_the_emails(url, depth, all_the_urls = [], all_emails = []):
    """
    Takes the url of a page, fetches the HTML and stores list of emails.
    Then fetches all all urls and calls itself on these urls.
    The depth decides how many times this will happen.
    Depth = 0 will only fetch emails from the HTML of the url we first sent in.

    Example:
    >>> url = "https://lucidtech.io/contact.html"
    >>> print(all_the_emails(url, 1))
    ['august@lucidtech.ai', 'hello@lucidtech.ai', 'staale@lucidtech.ai', 'stig@lucidtech.ai']
    """
    ### Get html code ###
    try:
        f = urllib.request.urlopen(url)

    except IOError: #Avoid broken links
        return
    text = [str(f.read())] #Put html code in list because the sample inputs where in lists

    ### Find emails and urls ###
    urls = find_urls(text)
    emails = find_emails(text)

    ### Make internal urls into full urls ###
    parenturlpattern = r"https?://(?:www\.)?(?P<parenturl>[\w\.\-~]+)/?.*"
    parenturl = re.sub(parenturlpattern, r"\g<parenturl>", url)

    #When depth level is reached, stop searching for new urls, but still add emails
    #from the existing urls
    if depth == 0:
        all_emails.extend(emails) #Storing emails
        #all_the_urls.append(urls)
        # Filter empty strings, remove duplicates, make into list, sort list
        # return sorted(list(set(filter(None, all_emails))))
        return all_the_urls, all_emails

    else:
        for u in urls:
            #No need checking index.html, we already did
            if u == 'http://www.index.html':
                urls.remove(u)
                continue

            ### All urls are stored in all_the_urls. If we find the same url
            ### as used before, this url is skipped
            if u in all_the_urls:
                continue
            regex1 = r".*offset\=\d*"
            regex2 = r".*\.osloskolen\.no"
            m1 = re.match(regex1, u)
            m2 = re.match(regex2, u)
            if m1:
                all_the_urls.append(u) #Appending urls, so we can check if we already searced an url
            if m2:
                all_the_urls.append(u)
            all_emails.extend(emails) #Storing emails
            url = re.sub(r"(?<=www\.)()(?=[\w\.\-~]+\.html)", parenturl + "/", u) #Making sure we have a full url, incase u is .html
            all_the_emails(url, depth - 1, all_the_urls = all_the_urls, all_emails = all_emails)
        return all_the_emails(url, depth - 1, all_the_urls = all_the_urls, all_emails = all_emails)


if __name__ == "__main__":
     #import doctest
     #doctest.testmod()
     urls = ['http://www.oslo.kommune.no/skole-og-utdanning/skoler-og-skoletilhorighet/skoler-i-oslo/?offset=0', 'http://www.oslo.kommune.no/skole-og-utdanning/skoler-og-skoletilhorighet/skoler-i-oslo/?offset=32', 'http://www.oslo.kommune.no/skole-og-utdanning/skoler-og-skoletilhorighet/skoler-i-oslo/?offset=64', 'http://www.oslo.kommune.no/skole-og-utdanning/skoler-og-skoletilhorighet/skoler-i-oslo/?offset=96', 'http://www.oslo.kommune.no/skole-og-utdanning/skoler-og-skoletilhorighet/skoler-i-oslo/?offset=128', 'http://www.oslo.kommune.no/skole-og-utdanning/skoler-og-skoletilhorighet/skoler-i-oslo/?offset=160']
     #url = "https://www.oslo.kommune.no/skole-og-utdanning/skoler-og-skoletilhorighet/skoler-i-oslo/#gref"
     matches = []
     for url in urls:
         f = urllib.request.urlopen(url)
         text = [str(f.read())]
         regex = r"http://www\.\w+\.osloskolen\.no"
         m = re.match(regex, text)
         print(m)
         #matches.append(m)

     print(matches)
     # for i, j in zip(a, b):
     #     print (i, j )
