def find_word(text, find_word):

    split_text = text.split(".")
    lst_senteces = []
    for row in split_text:
        if find_word in row:
            row = ('..' + row[:5] + '..') if len(row) > 5 else row
            lst_senteces.append(row)
    return lst_senteces

print(
    find_word(
        text='''asdhnwhjv 23 as awnndasld. asjdnrasdioihfnawndb pojnnpoh 23 asdknfajasidu1asdhb. aisjdihugealksjdnlgkjhu. asodnne;laksnd.asdddddddawdsmhakjwd 23 alsdknwb.
        awdjnl;aksdhkjhk.awdjnl;aksdhkjhk.awdjnl;aksdhkjhk. awdjnl;aksdhkjhk .23 awljkhbkljdhkjh. awljkhbkljdhkjh. awljkhbkljdhkjhadjkaghdgawdhawd. 23 asdljadjashdas. asdjaosidad.
        aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.23 aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.
        aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.
        aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.aJKhawhdiuawdsdkalksjdkjlk.''',
        
        find_word='23'
        )
    )