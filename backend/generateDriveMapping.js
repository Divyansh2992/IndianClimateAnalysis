const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');

// Path to your service account key file
const KEYFILEPATH = path.join(__dirname, 'credentials', 'IndianClimateAnalysis.json');

// Replace with your folder ID (from the Google Drive folder link)
const FOLDER_ID = '1BD1xaNuwYE-aN5wPeQ2NzUWsy9cGl8rc'; // e.g., '1_N-VFFBW1B4zSkqWJ2frkUpQAxg231Hz'

async function listFilesInFolder(folderId) {
  const auth = new google.auth.GoogleAuth({
    keyFile: KEYFILEPATH,
    scopes: ['https://www.googleapis.com/auth/drive.readonly'],
  });
  const drive = google.drive({ version: 'v3', auth });

  let files = [];
  let pageToken = null;
  do {
    const res = await drive.files.list({
      q: `'${folderId}' in parents and trashed = false`,
      fields: 'nextPageToken, files(id, name)',
      pageToken: pageToken,
    });
    files = files.concat(res.data.files);
    pageToken = res.data.nextPageToken;
  } while (pageToken);

  return files;
}

async function main() {
  const files = await listFilesInFolder(FOLDER_ID);
  const mapping = {};
  files.forEach(file => {
    // Remove extension for mapping key (e.g., 'Nagaur.epw' -> 'Nagaur')
    const key = file.name.replace(/\.[^/.]+$/, '');
    mapping[key] = file.id;
  });
  fs.writeFileSync('csvFileIds.json', JSON.stringify(mapping, null, 2));
  console.log('Mapping saved to epwFileIds.json');
}

main().catch(console.error);