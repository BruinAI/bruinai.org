# bruinai.org
Our public facing website

<br>

Designed in Webflow \
Deployed with Github Actions, AWS: CodePipeline, S3, Route 53, and Cloudfront \
`release` branch is meant to be a read-only branch

<br>

## Website Update Steps
![image](https://github.com/user-attachments/assets/dbd737ad-c86e-4a23-ab16-20349fe7dc3a)
1. In Design mode, export the website into a .zip file
2. Commit files to repository in main branch
3. Submit PR

### What happens when PR is approved:
1. A Github Action which uses a Github App we created to combat [this problem](https://github.com/orgs/community/discussions/25305#discussioncomment-8256560) runs `urlrewrite.py` and commits the changes to the `release` branch
2. `urlrewrite.py` adds some Javascript code to all `.html` files that automatically changes the URL to display without the `.html` (for example, if you try to visit `/about.html`, the JS code will automatically change it to `/about` to look cleaner to the client)
3. AWS CodePipeline picks up a change in the `release` branch and updates the AWS S3 bucket served with Cloudfront
4. If you need immediate results, you manually must add an cache invalidation to AWS Cloudfront, otherwise you must wait for caches to expire for your changes to take effect
