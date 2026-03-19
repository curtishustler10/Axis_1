// Simple Google OAuth2 Authorization URL Generator
// Replace these values with your OAuth credentials from Google Cloud Console

const CLIENT_ID = 'YOUR_CLIENT_ID';
const REDIRECT_URI = 'http://localhost:3000/oauth/callback';
const SCOPES = [
  'https://www.googleapis.com/auth/docs',
  'https://www.googleapis.com/auth/spreadsheets',
  'https://www.googleapis.com/auth/drive.file'
].join(' ');

// Generate authorization URL
const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${encodeURIComponent(CLIENT_ID)}&redirect_uri=${encodeURIComponent(REDIRECT_URI)}&response_type=code&scope=${encodeURIComponent(SCOPES)}&access_type=offline&prompt=consent`;

console.log('Authorization URL:');
console.log(authUrl);
console.log('\n1. Visit the URL above');
console.log('2. Authorize the app');
console.log('3. Copy the authorization code from the redirect URL');
console.log('4. Exchange it for tokens using the token exchange endpoint');
