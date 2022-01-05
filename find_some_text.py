def find_word(text, find_word):
    list_find_text = []

    split_text = text.split(".")
    
    for row in split_text:
        if find_word in row:
            list_find_text.append(('..' + row[:5] + '..') if len(row) > 5 else row)
    return list_find_text

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