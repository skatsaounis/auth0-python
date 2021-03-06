from .rest import RestClient


class EmailTemplates(object):

    """Auth0 email templates endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self, id=None):
        url = 'https://%s/api/v2/email-templates' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def create(self, body):
        """Create a new email template.

        Args:
           body (dict): Attributes for the new email template.
           See: https://auth0.com/docs/api/management/v2#!/Email_Templates/
                post_email_templates
        """

        return self.client.post(self._url(), data=body)

    def get(self, template_name):
        """Retrieves an email template by its name.

        Args:
           template_name (str): Name of the email template to get.
              Must be one of: 'verify_email', 'reset_email', 'welcome_email',
              'blocked_account', 'stolen_credentials', 'enrollment_email',
              'change_password', 'password_reset', 'mfa_oob_code'.
              See: https://auth0.com/docs/api/management/v2#!/Email_Templates/
                   get_email_templates_by_templateName
        """

        return self.client.get(self._url(template_name))

    def update(self, template_name, body):
        """Update an existing email template.

        Args:
           template_name (str): Name of the email template to update.
              Must be one of: 'verify_email', 'reset_email', 'welcome_email',
              'blocked_account', 'stolen_credentials', 'enrollment_email',
              'change_password', 'password_reset', 'mfa_oob_code'.

           body (dict): Attributes to update on the email template.
              See: https://auth0.com/docs/api/management/v2#!/Email_Templates/
                   patch_email_templates_by_templateName
        """

        return self.client.patch(self._url(template_name), data=body)
