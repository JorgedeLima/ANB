# Mailing list (Google Sheet)

Both sign-up forms on the site (Get in Touch page and footer) post to a Google Apps Script web app, which adds a row to a Google Sheet. No paid service and no server.

## One-time setup

Do this in the Google account that should own the list (ideally ANB's, aucklandnewballet@gmail.com).

1. Create a new Google Sheet named **ANB mailing list**.
2. In the Sheet, open **Extensions → Apps Script**.
3. Delete the sample code, paste in all of `apps-script.gs`, and click **Save**.
4. Click **Deploy → New deployment**. Click the gear next to "Select type" and choose **Web app**.
   - Description: `Website sign-ups`
   - Execute as: **Me**
   - Who has access: **Anyone** (the website's visitors aren't signed in to Google; this only lets them add a row, not read the Sheet)
5. Click **Deploy**, then **Authorize access** and allow it. Google warns that the app isn't verified because you wrote it yourself: click **Advanced → Go to (project name)**.
6. Copy the **Web app URL** (ends in `/exec`). Open it in a browser: it should say `ok`.
7. Put the URL in `MAILING_LIST_URL` in `index.html` and publish.

The **Subscribers** tab and its headings appear with the first sign-up.

## Changing the script later

Edit the code, then **Deploy → Manage deployments → (pencil) → Version: New version → Deploy**. This keeps the same URL. A *new deployment* would create a new URL and the site would need updating.

## Sending emails

- Send from the account that owns the Sheet, using a saved Gmail template.
- Put the subscribers in **BCC**, never To or Cc, so people don't see each other's addresses.
- Every email must say who it's from and how to unsubscribe (NZ Unsolicited Electronic Messages Act). For example: "Reply UNSUBSCRIBE and we'll take you off the list."
- When someone unsubscribes, change their **Status** to `unsubscribed` rather than deleting the row, and leave them out of the next send.
- A free Gmail account can send to about 500 recipients a day.
