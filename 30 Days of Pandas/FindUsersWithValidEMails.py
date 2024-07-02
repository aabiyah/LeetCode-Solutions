import pandas as pd
import string

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    allowed_chars = set(string.ascii_lowercase
                            + string.ascii_uppercase
                            + string.digits 
                            + '.' + '_' + '-')

    new_df = pd.DataFrame(columns=['user_id', 'name', 'mail'])

    for index, user in users.iterrows():
        mail = user['mail']

        if '@' in mail:
            split_char = '@'
            index = mail.find(split_char)
            mail_prefix, domain = mail[:index], mail[index:]

            if domain == "@leetcode.com":
                if set(mail_prefix).issubset(allowed_chars) and set(mail_prefix[0]).issubset(string.ascii_lowercase + string.ascii_uppercase):
                    valid_mail_user = pd.DataFrame([{
                                'user_id': user['user_id'],
                                'name': user['name'],
                                'mail': user['mail']
                    }])
                    new_df = pd.concat([new_df, valid_mail_user], ignore_index=True)

    return new_df