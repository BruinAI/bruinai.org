# bruinai.org
Our public facing website

<br>

Designed in Webflow \
Hosted with Apache2 with SSL/TLS Certificated provided by LetsEncrypt and Certbot

<br>

## Website Update Steps
![image](https://github.com/user-attachments/assets/dbd737ad-c86e-4a23-ab16-20349fe7dc3a)
1. In Design mode, export the website into a .zip file
2. Push files to repository
3. On the deployment server, pull changes

<br>

## Deployment Notes
### .htaccess
Courtesy of multiple Stack Exchange articles (ChatGPT sucks), the .htaccess file:
* Rewrites `bruinai.org/index.html` to `bruinai.org`
* Removes the `.html` extension from URL's (ex: `/about.html` is rewritten to `/about`
* Hides the `/.git/` directory and this README

<br>

### Apache Configuration File
The current Apache2 config file for the HTTPS deployment is as below:
```
<IfModule mod_ssl.c>
<VirtualHost *:443>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        <Directory /var/www/html>
                Options Indexes FollowSymLinks
                AllowOverride All
                Require all granted
        </Directory>
        ServerName bruinai.org
        SSLCertificateFile /etc/letsencrypt/live/bruinai.org/fullchain.pem
        SSLCertificateKeyFile /etc/letsencrypt/live/bruinai.org/privkey.pem
        Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>
</IfModule>
```
