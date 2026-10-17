/**
 * ANB mailing list: receives sign-ups from the website and adds them to this Sheet.
 *
 * Paste this into Extensions > Apps Script of the subscribers Sheet and deploy it as a
 * web app (steps in tools/mailing-list/README.md). The website posts: email, name
 * (Get in Touch form only), source (contact | footer), page, and a hidden "website"
 * field that only spam bots fill in.
 */

const SHEET_NAME = 'Subscribers';
const HEADERS = ['Signed up', 'Email', 'Name', 'Form', 'Page', 'Status'];

function doPost(e) {
  const p = (e && e.parameter) || {};

  // Spam bots fill in the hidden field; pretend it worked and store nothing.
  if (p.website) return json({ ok: true });

  const email = String(p.email || '').trim().toLowerCase();
  if (email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return json({ ok: false, error: 'invalid' });
  }

  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const sheet = getSheet();
    const last = sheet.getLastRow();
    const existing = last > 1 ? sheet.getRange(2, 2, last - 1, 1).getValues().flat() : [];
    // Already on the list: say yes again, don't add a second row.
    if (existing.indexOf(email) === -1) {
      sheet.appendRow([
        new Date(),
        safe(email),
        safe(String(p.name || '').trim().slice(0, 120)),
        safe(String(p.source || '').slice(0, 20)),
        safe(String(p.page || '').slice(0, 60)),
        'subscribed',
      ]);
    }
  } finally {
    lock.releaseLock();
  }
  return json({ ok: true });
}

// Lets you check the deployment in a browser: opening the /exec URL should say "ok".
function doGet() {
  return ContentService.createTextOutput('ok');
}

function getSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(HEADERS);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

// Stop text from the website being treated as a spreadsheet formula.
function safe(value) {
  return /^[=+\-@]/.test(value) ? "'" + value : value;
}

function json(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
