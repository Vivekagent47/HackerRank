def fun(s):
    # return True if s is a valid email, else return False
    try:
        user, url = s.split("@")
        web, ext = url.split(".")
    except ValueError:
        return False
    user = ''.join(i for i in user if i not in "-_")
    return user.isalnum() and web.isalnum() and len(ext) < 4

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)