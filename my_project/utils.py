from fastapi_mail import FastMail


class Mail:

    @staticmethod
    async def send_mail(msg_schema, mail_conf):
        """
        mail send functionality.
        :param msg_schema: msg schema
        :param mail_conf: mail conf
        :return:send the mail
        """
        fm = FastMail(mail_conf)
        await fm.send_message(msg_schema)
